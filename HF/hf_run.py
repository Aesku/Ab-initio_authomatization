"""
run multiple inputs with python
"""
from os import path, system, mkdir, system, remove
import shutil

values = [10,20,30,40,50,60,70,80,90,100]
#values = [1,2,5,10,20,50]
JOB = 'exx'
#JOB = 'randG'

if JOB == 'exx': LABEL = 'Ry'
if JOB == 'randG': LABEL = 'RL'

def create_run_file(v):
    new_run_name = "run-%s%s.sh" %(JOB,v)
    print('creating run file %s' %new_run_name)
    open(new_run_name, 'w')
    return new_run_name

def writing_run_file(v):
    model = 'run.sh'
    run_name = "run-%s%s.sh" %(JOB,v)
    shutil.copyfile(model,run_name)

def modifying_run_file(name, v):
    f = open(name, 'rt')
    data = f.read()
    data = data.replace('JOB', JOB + '%s%s'%(v,LABEL))
    f.close()
    f = open(name, 'wt')
    f.write(data)
    f.close()

def run_jobs(v):
    print('running job for job %s' %v)
    system('sbatch run-%s%s.sh' %(JOB,v))

#Creating all run.sh files
for v in values:
    run_file = create_run_file(v)
    writing_run_file(v)
    modifying_run_file(run_file, v)
    #Running 
#    run_jobs(v)
