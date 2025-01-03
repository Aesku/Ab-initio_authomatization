"""
run multiple inputs with python
"""
from os import path, system, mkdir, system, remove
import shutil

VB = 1

xb_values = [200]
#xc_values = [10,]
xc_values = [70]

def create_run_file(JOB):
    new_run_name = "run-%s.sh" %JOB
    print('creating run file %s' %new_run_name)
    open(new_run_name, 'w')
    return new_run_name

def writing_run_file(JOB):
    model = 'run.sh'
    run_name = "run-%s.sh" %JOB
    shutil.copyfile(model,run_name)

def modifying_run_file(name, JOB):
    f = open(name, 'rt')
    data = f.read()
    data = data.replace('JOB', JOB)
    f.close()
    f = open(name, 'wt')
    f.write(data)
    f.close()

def run_jobs(JOB):
    print('running job for job %s' %JOB)
    system('sbatch run-%s.sh' %JOB)

#Creating all run.sh files
for b in xb_values:
    for c in xc_values:
        JOB = 'Xb%s-%sXc%sRy'%(VB,b,c)
        run_file = create_run_file(JOB)
        writing_run_file(JOB)
        modifying_run_file(run_file, JOB)
    #Running
        run_jobs(JOB)
