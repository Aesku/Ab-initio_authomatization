USAGE

1. VASP_restart-all.py
This cleans the directory. 
The directory must have a POSCAR, POTCAR, KPOINTS and INCAR

2. VASP_set_q.py
This creates a set of qs in a path and runs with slurm the calculations

3. VASP_spin-spiral-plot.py
Plot the spin spiral
3.1. grep E0 q*/*slurm > dispersion.txt
3.2. Edit by hand dispersion.txt so that the vectors/energies are in the
  desired order (Still not implemented this authomatic)
3.3. python VASP_spin-spiral-plot.py to visualize
