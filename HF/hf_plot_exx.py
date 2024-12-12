import matplotlib.pyplot as plt
import numpy as np

cutoffs = [1,2,5,10,20,40,50,60,70,80]
fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0.15,0.15,0.8,0.8])
gaps = []


for c in cutoffs:
    data = np.loadtxt('o-exx%sRy.hf'%c)
    gaps.append(data[1,3]-data[0,3])

ax.plot(cutoffs,gaps,'-o',color = 'k')
ax.set_xlabel('HF cutoff (Ry)',fontsize=14)
ax.set_ylabel('HF gap (eV)', fontsize=14)
ax.set_title('HF convergence',fontsize=14)
ax.tick_params(labelsize=14)

plt.savefig('exx-conv.pdf',format='pdf')
plt.show()
exit()
