#!/home/rjslater/anaconda3/bin/python
from subprocess import Popen, PIPE
import os
import signal

if __name__ == '__main__':
    process = Popen(['nmcli', 'radio', 'wifi'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    stdout = stdout.decode('utf-8').strip()

    if 'enabled' in stdout:
        process = Popen(['nmcli', 'radio', 'wifi', 'off'], stdout=PIPE, stderr=PIPE)
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    else:
        process = Popen(['nmcli', 'radio', 'wifi', 'on'], stdout=PIPE, stderr=PIPE)
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
