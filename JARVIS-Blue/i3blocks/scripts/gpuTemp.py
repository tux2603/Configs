#!/home/rjslater/anaconda3/bin/python
from subprocess import Popen, PIPE

p = Popen(['nvidia-smi', '--query-gpu=temperature.gpu', '--format=csv'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, err = p.communicate(b"input data that is passed to subprocess' stdin")
output = output.decode(encoding='utf-8')

print(output[output.find('\n') + 1:-1] + '\u00B0C')
