import numpy as np
from os import path, system, mkdir, system
import shutil

VB = 1

files = ['yambo_gw.in']
xb_values = [30,50,100,150,200]

for b in xb_values:
    with open(files[0], 'r') as f:
         lines = f.readlines()
    lines.append('%GbndRnge\n')
    lines.append('  %s | %s |\n'%(VB,b))
    lines.append('%')
    with open('yambo_Gb%s-%s.in'%(VB,b), 'w') as f:
         f.writelines(lines)
exit()
