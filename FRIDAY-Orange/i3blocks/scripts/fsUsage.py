#!/home/rjslater/anaconda3/bin/python
import psutil as p


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Y', suffix)

fsTotal = p.disk_usage('/').total
fsUsed = p.disk_usage('/').used
fsPercent = int(100 * fsUsed / fsTotal)
fsChar = '\uf200' #'\uf233'

print('{} {}%'.format(fsChar, fsPercent))
# print('{} {} / {} {}%'.format(fsChar, sizeof_fmt(fsUsed), sizeof_fmt(fsTotal), fsPercent))
