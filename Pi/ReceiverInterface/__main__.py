#!/usr/bin/env python3
"""
Description:    top-level executable for the GPS display interface
Creation Date:  07/04/22
"""

# import dependencies
import configparser

if __name__ == "__main__":
    # 0. read our config info
    displayConfig = configparser.ConfigParser()
    displayConfig.read("./DisplayConfig.ini")

    # 1. check message queue is up (queue info from conf)
    # 2. wait for an active display (pin info from conf)
    # 3. start display driver
