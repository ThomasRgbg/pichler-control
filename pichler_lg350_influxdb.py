#!/usr/bin/env python3

import time
import os
import argparse

from configparser import RawConfigParser

from pichler_lg350 import PichlerLG350 
from influxdb_cli2.influxdb_cli2 import influxdb_cli2

import paho.mqtt.client as paho

def mqtt_on_connect(client, userdata, flags, rc):
    print("pichler_lg350_influxdb.py: MQTT Connection returned result: " + str(rc))
    client.subscribe(client.lueftung_topic + "/luftstufe_set", 1)
    client.subscribe(client.lueftung_topic + "/l1_qmh_set", 1)

# The callback for when a PUBLISH message is received from the server.
def mqtt_on_message(client, userdata, msg):
    print("pichler_lg350_influxdb.py: Got from MQTT: "+msg.topic+": {0}".format(int(msg.payload)) )
    if msg.topic == client.lueftung_topic + "/luftstufe_set":
        if int(msg.payload) > -1 and int(msg.payload) < 4:
            print("pichler_lg350_influxdb.py: set luftstufe because of MQTT msg")
            client.lueftung.luftstufe = int(msg.payload)
    elif msg.topic == client.lueftung_topic + "/l1_qmh_set":
        if int(msg.payload) >= 50 and int(msg.payload) < 190:
            print("pichler_lg350_influxdb.py: set l1_qmh because of MQTT msg")
            client.lueftung.l1_qmh = int(msg.payload)

if __name__ == "__main__":
    config = RawConfigParser(delimiters='=')
    config.read(os.path.dirname(os.path.realpath(__file__)) + '/pichler_lg350.cfg')

    mqtt_topic = config.get('mqtt','topic')

    influxdb = influxdb_cli2(config.get('influxdb','url', raw=True), 
                            token=config.get('influxdb','token'), 
                            org=config.get('influxdb','org'), 
                            bucket=config.get('influxdb','bucket'),
                            debug=False,
                            )

    lg350 = PichlerLG350(config.get('pichler','port'), debug=False)

    mqtt= paho.Client()
    mqtt.on_connect = mqtt_on_connect
    mqtt.on_message = mqtt_on_message
    mqtt.lueftung = lg350
    mqtt.lueftung_topic = config.get('mqtt','topic')
    mqtt.connect(config.get('mqtt','server'),config.getint('mqtt','port'))
    mqtt.loop_start()

    while True:
        results = lg350.get_all_input_registers()

        for name, value in results.items():
            influxdb.write_sensordata("lueftung", name, value)

        influxdb.write_sensordata("lueftung", 'luftstufe', lg350.luftstufe)

        for i in range(6):
            mqtt.publish(mqtt.lueftung_topic + "/luftstufe", lg350.luftstufe)
            time.sleep(20)
