
# Format

# "Register name : [ register_value, add_value, multiply_value, export ]

# Based on https://www.pichlerluft.at/unterlagen.html?file=files/content/downloads/KNX/08KNXGA350450A_Datenpunkte%20ModKNX%20LG350_450_V2.1.xlsx

pichler_input_registers = {
    "status_heizreg" : [11, 0, 1, True ],        # Ausgang Heizregister (0-100%)
    "status_vhr" : [16, 0, 1, True ],            # Vorheizregister, H2
    "status_bypass" : [20, 0, 1, True ],         # Bypass, H8
    "status_klappen" : [21, 0, 1, True ],        # Aussenluft und Fortluftklappen
    "temp_frischluft" : [30, -1000, 0.1, True],  # Celsius, from out to pichler
    "temp_fortluft" : [31, -1000, 0.1, True],    # Celsius, from pichler to outside
    "temp_abluft" : [32, -1000, 0.1, True],      # Celsius, from room to pichler
    "temp_zuluft" : [33, -1000, 0.1, True],      # Celsius, from room to pichler
    "temp_vhr" : [34, -1000, 0.1, True],         # Celsius, Vorheizregister
    "tacho_zuluft" : [39, 0, 1, True ],          # unknown unit, rpm?
    "tacho_abluft" : [40, 0, 1, True ],          # unknown unit, rpm?
    "volumenstrom_zuluft" : [46, 0, 1, True],    # m^3/s
    "volumenstrom_abluft" : [47, 0, 1, True],    # m^3/s
    "status_betrieb" : [48, 0, 1, True ],        # 0=startup 1=Standby 2=Anlauf 3=Betrieb 4=Nachlauf 5=Standby 6=Testmodus
    }

