#!/usr/bin/env python3

import serial
from datetime import datetime
import pynmea2

port = "/dev/ttyS0"
conn = serial.Serial(port, baudrate=9600, timeout=5)

while 1:
    try:
        incoming_rx = conn.readline().decode("utf-8")
        if '$GPRMC' in incoming_rx:
            rx_parsed = pynmea2.parse(incoming_rx)
            print("{} -- (Lat,Long) = ({},{})".format(datetime.now().strftime("%H:%M:%S"),
                                                    rx_parsed.latitude, rx_parsed.longitude))
    except serial.SerialException as e:
        print('Device error: {}'.format(e))
        break
    except pynmea2.ParseError as e:
        print('Parse error: {}'.format(e))
        continue
    except UnicodeDecodeError as e:
        print('Couldnt convert bytestring to string for some reason: {}'.format(e))
        continue
