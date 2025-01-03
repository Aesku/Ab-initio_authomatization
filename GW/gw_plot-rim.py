import matplotlib.pyplot as plt
import numpy as np

"""
def get_colors(nfiles,colormap='rainbow'):
    cmap = matplotlib.cm.get_cmap(colormap)
    colors = []
    for j in range(nfiles):
        colors.append(cmap( 1.0*(j+1.0)/nfiles ) )
    return colors
"""

cutoffs = [1,2,5,10,20,50]
fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0.15,0.15,0.8,0.8])
gaps = []


for c in cutoffs:
    data = np.loadtxt('o-randG%sRL.qp'%c)
    gaps.append((data[1,3]+data[1,2]) - (data[0,3]+data[0,2]))

ax.plot(cutoffs,gaps,'-o',color = 'k')
ax.set_xlabel('RIM cutoff (RL)',fontsize=14)
ax.set_ylabel('GW gap (eV)', fontsize=14)
#ax.set_title('GW convergence',fontsize=14)
ax.tick_params(labelsize=14)

plt.savefig('gw_conv_rim.pdf',format='pdf')
plt.show()
exit()
