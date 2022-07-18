## Source for bootstrapped Neo-6M bootstrapped FPGA module

A pre-built Neo-6M GPS module will be used to test some of the peripheral functionality and evaluate NMEA message formatting to build FPGA interface components later.

Docs: https://www.u-blox.com/en/product/neo-6-series

Setup:
1. in /boot/config.txt => enable_uart=1, force_turbo=1, dtparam=spi=on, dtoverlay=pi3-disable-bt
2. in boot/cmd_line.txt => plymouth.ignore-serial-consoles
3. sudo raspi-config => disable serial login, enable serial hardware
4. sudosystemctl stop serial-getty@ttyAMA0.service
5. sudosystemctl disable serial-getty@ttyAMA0.service
6. enable UART hardware permissions => add user to dialout group, give read access (to prevent needing sudo to see the port)
