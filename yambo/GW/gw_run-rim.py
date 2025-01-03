"""
run multiple inputs with python
"""
from os import path, system, mkdir, system, remove
import shutil

#values = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
values = [1,2,5,10,20,50]
#JOB = 'exx'
JOB = 'randG'

def create_run_file(v):
    new_run_name = "run-%s%s.sh" %(JOB,v)
    print('creating run file %s' %new_run_name)
    open(new_run_name, 'w')
    return new_run_name

def writing_run_file(run_name):
    model = 'run.sh'
    shutil.copyfile(model,run_name)

def modifying_run_file(name, v):
    f = open(name, 'rt')
    data = f.read()
    data = data.replace('JOB', JOB + '%s'%v + 'RL')
    f.close()
    f = open(name, 'wt')
    f.write(data)
    f.close()

def run_jobs(JOB):
    print('running job for %s' %JOB)
    system('sbatch %s' %JOB)

#Creating all run.sh files
for v in values:
    run_file = create_run_file(v)
    writing_run_file(run_file)
    modifying_run_file(run_file, v)
    #Running 
    run_jobs(run_file)
