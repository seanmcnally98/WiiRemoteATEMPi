import subprocess
import re
import time
import sys

def get_paired_devices():
    output = subprocess.check_output(['bluetoothctl', 'paired-devices'])
    lines = output.decode('utf-8').split('\n')
    devices = []
    for line in lines:
        match = re.search(r'Device\s([0-9A-F:]{17})', line)
        if match:
            devices.append(match.group(1))
    return devices

def is_device_connected(device):
    output = subprocess.check_output(['bluetoothctl', 'info', device])
    output = output.decode('utf-8')
    return 'Connected: yes' in output

# Continually re-check the list of connected devices
while True:
    # Get paired devices
    paired_devices = get_paired_devices()

    # Check if target device is connected
    if '00:17:AB:21:02:E9' in paired_devices and is_device_connected('00:17:AB:21:02:E9'):
        # We did it!
        print("Found The Wii Remote!")
        process = subprocess.Popen(['/bin/bash', '/home/pi/startchataigne.sh'])
        sys.exit(0)
        break

    # Wait for a few seconds before re-checking
    time.sleep(3)

