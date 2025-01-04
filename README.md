# pichler-control
Control of a Picher LG350 unit via Python and Modbus

!!!!!! Warning !!!!!!!! 
* Use on your own risk, this is no approved accessory!
* Connecting the Modbus RTU means opening the device, which potentially exposes also some live wires (230V) in close proximity!
* Running the ventilation system with modified parameters could not just void the device warranty. But in case you are not an expert, you might also risk all kind of humidity problems in your house, creating mildew etc.
!!!!!! Warning !!!!!!!! 

This is basically a contination of https://github.com/ThomasRgbg/esp8266-pichler, where now the scripts here run directly on a Raspberry PI and a RS485 converter connected to /dev/ttyUSB*

Controlling the Pichler LG350 is realtively straight forward. But I'm not sure how much they like if I disclose the whole register list. Therefore please ask via your own support contacts for the register list. I got a Excel list, but some of the parameters need some addtional calculation (offset/scaling), this is background of the param1/2 in the list. 

I'm using all of this just to read some parameters like temperatures or switch off/on the device. Please do not mess with other parameters without appropriate training. 

pichler_lg350.py is the core implementation of a control module. While pichler_lg350_influx.db is using this to write periodically data into a influxdb or get commands via mqtt
