#!/home/rjslater/anaconda3/bin/python
from subprocess import Popen, PIPE

p = Popen(['nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, err = p.communicate(b"input data that is passed to subprocess' stdin")
output = output.decode(encoding='utf-8')

gpuIcon = '\uf108'
gpuUsagePercent = output[output.find('%') + 3:-3]

print('{} {}%'.format(gpuIcon, gpuUsagePercent))
