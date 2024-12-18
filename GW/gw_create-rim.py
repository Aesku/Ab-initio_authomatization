import numpy as np
from os import path, system, mkdir, system
import shutil

files = ['yambo_gw.in']
#values = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
values = [1,2,5,10,20,50]
#JOB = 'exx'
JOB = 'randG'

for v in values:
#    flag = 'EXXRLvcs = %s Ry'%v
    flag = 'RandGvec = %s RL'%v
    with open(files[0], 'r') as f:
             lines = f.readlines()
    lines.append(flag + '\n')
    #lines.insert(-1,flag + '\n')
    #with open('yambo_hf_%s%sRy.in'%(JOB,v), 'w') as f:
    with open('yambo_%s%sRL.in'%(JOB,v), 'w') as f:
         f.writelines(lines)
exit()
