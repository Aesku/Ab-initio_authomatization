import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0.15,0.15,0.8,0.8])

VB = 50
cutoffs = [1,5,10,20]
cbands = [60,70,80,90]
for cb in cbands:
    gaps = []
    for cut in cutoffs:
        job = 'o-Xb%s-%sXc%sRy.qp'%(VB,cb,cut)
        data = np.loadtxt(job)
        gaps.append((data[1,3]+data[1,2]) - (data[0,3]+data[0,2]))
        print(cb,cut,gaps)
    ax.plot(cutoffs,gaps,'-o', label = 'Bands: %s-%s'%(VB,cb))

ax.legend(fontsize=13)
ax.set_xlabel('GW cutoff (Ry)',fontsize=14)
ax.set_ylabel('GW gap (eV)', fontsize=14)
ax.set_title('GW convergence | bands and cutoff',fontsize=14)
ax.tick_params(labelsize=14)

plt.savefig('conv-gw.pdf',format='pdf')
plt.show()
exit()
