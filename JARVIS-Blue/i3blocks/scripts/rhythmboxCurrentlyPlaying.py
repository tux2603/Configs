#!/home/rjslater/anaconda3/bin/python
import subprocess

cmd = "rhythmbox-client --print-playing --no-start"
ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = ps.communicate()[0].decode('utf-8').strip()

if len(output) > 5:
    print('\uf144 {}'.format(output)[:60])
