#!/bin/bash                  
#SBATCH --job-name=LDAexc
##SBATCH --nodelist=compute06
#SBATCH --exclude=compute01
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=12
#SBATCH --mem=10G
#modules
module load yambo/intel-libs
module load yambo/gpl/5.2-single-omp

export OMP_NUM_THREADS=12

srun --mpi=pmi2 yambo -I ../ -F yambo_hf_JOBRL.in -J JOBRL
