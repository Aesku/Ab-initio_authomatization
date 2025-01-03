import numpy as np
from os import path, system, mkdir, system
import shutil

VB = 1

files = ['yambo_gw.in']
xb_values = [50,70,100]
#xc_values = [10,20]
xc_values = [100]

for c in xc_values:
    xc_flag = 'NGsBlkXp = %s Ry'%c
    for b in xb_values:
        with open(files[0], 'r') as f:
             lines = f.readlines()
        lines.append(xc_flag + '\n')
        lines.append('%BndsRnXp\n')
        lines.append('  %s | %s |\n'%(VB,b))
        lines.append('%')
        with open('yambo_Xb%s-%sXc%sRy.in'%(VB,b,c), 'w') as f:
             f.writelines(lines)
exit()
