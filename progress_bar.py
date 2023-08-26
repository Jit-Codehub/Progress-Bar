import sys
from termcolor import cprint
import colorama
from colorama import Fore
colorama.init() # Windows need this

HIGHER_GREEN = Fore.LIGHTGREEN_EX
BOLD_ONLY = ['bold']


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='#'):
    if total != 0:
        percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        cprint(''.join([ HIGHER_GREEN, '%s' % ('\r{} |{}| {}% {}'.format(prefix, bar, percent, suffix)) ]), attrs=BOLD_ONLY, end='' )
        sys.stdout.flush()

a = 15000
for i in range(a):

    printProgressBar(i, a-1, prefix='[...] Downloading:'
                , suffix='Complete', length=100)