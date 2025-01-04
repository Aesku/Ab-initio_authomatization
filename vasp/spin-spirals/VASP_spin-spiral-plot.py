from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib import colorbar,colors

eV2meV = 1000

def plot_vectors(v1,v2,M,K):
    print(v1)
    plt.quiver(0,0,v1[0],v1[1],color='k',scale=40)
    plt.quiver(0,0,(v1+v2)[0],(v1+v2)[1],color='k',scale=40)
    plt.quiver(0,0,(-v1)[0],(-v1)[1],color='k',scale=40)
    plt.quiver(0,0,(-v2)[0],(-v2)[1],color='k',scale=40)
    plt.quiver(0,0,(-v1-v2)[0],(-v1-v2)[1],color='k',scale=40)
    plt.quiver(0,0,v2[0],v2[1],color='k',scale=40)
    plt.quiver(0,0,M[0],M[1],color='r',scale=40,label='M')
    plt.quiver(0,0,K[0],K[1],color='g',scale=40,label='K')
    plt.legend()
    plt.show()
    exit()


def get_colors(w, cmap = 'rainbow'):
    #cmap = matplotlib.cm.get_cmap('rainbow')
    cmap = get_cmap(cmap)
    c_array = []
    for j in w:
        c_array.append(cmap(j*1.0/max(w)))
        #c_array.append(cmap(1.0*(j+1.0)/nfiles))
    return c_array

def calculate_distances(N, cell = 'hex', plot_cell = False, **kwargs):
    if cell == 'hex':
       #Lattice vectors
       b1 = (2.0*np.pi)/(np.sqrt(3)) * (np.sqrt(3)*np.array([1,0]) - np.array([0,1]))
       b2 = (4.0*np.pi)/(np.sqrt(3)) * np.array([0,1])
       G = np.array([0,0])
       M = b1 + 0.5 * b2
       K = b1 + b2
       dgx, dmk, dkg = np.linalg.norm(M - G) / N[0], np.linalg.norm(K - M) / N[1], np.linalg.norm(G - K) / N[2]
   #    dgx, dmk, dkg = np.linalg.norm(M - G), np.linalg.norm(K - M), np.linalg.norm(G - K)
       print(dgx, dmk, dkg)
   
       if plot_cell: plot_vectors(b1,b2,M,K)

       #Creating the distanced array
       x_array = [0.0]
       x0 = x_array[-1]
       for n in np.arange(1,N[0]+1):
           x_array.append(x0+n*dgx)
       x0 = x_array[-1]
       for n in np.arange(1,N[1]+1):
           x_array.append(x0+n*dmk)
       x0 = x_array[-1]
       for n in np.arange(1,N[2]+1):
           x_array.append(x0+n*dkg)
       return x_array
    if cell == 'cubic':
       a = kwargs.pop('a',1)
       b = kwargs.pop('b',1)
       c = kwargs.pop('c',1)
       #Lattice vectors
       b1 = ((2.0*np.pi)/a)*np.array([1,0])
       b2 = ((2.0*np.pi)/b)*np.array([1,0])
       G = np.array([0,0])
       X = b1
       S = b1 + b2
       Y = b2
       dgx, dxs, dsy,dyg = np.linalg.norm(X - G) / N[0], np.linalg.norm(S - X) / N[1], np.linalg.norm(Y - S) / N[2], np.linalg.norm(G - Y) / N[2]

       #Creating the distanced array
       x_array = [0.0]
       x0 = x_array[-1]
       for n in np.arange(1,N[0]+1):
           x_array.append(x0+n*dgx)
       x0 = x_array[-1]
       for n in np.arange(1,N[1]+1):
           x_array.append(x0+n*dxs)
       x0 = x_array[-1]
       for n in np.arange(1,N[2]+1):
           x_array.append(x0+n*dsy)
       x0 = x_array[-1]
       for n in np.arange(1,N[3]+1):
           x_array.append(x0+n*dyg)
       return x_array
   
def normalization(energies):
    return energies[0]
    #return min(energies)

def plot_interpolation(ax, x, y, N = 50, color = 'k', lw = 2,iwantdata=False):
    energies = []
    for e in y:
        energies.append(e - normalization(y))
    f = interp1d(x,energies,kind='quadratic')
    new_x = np.linspace(0,x[-1],N)
    new_y = f(new_x)
    ax.plot(new_x,new_y,color=color,lw = lw)
    if iwantdata == True: return np.vstack((new_x, new_y)).T

def custom_ax(ax,x_array,N, cell = 'hex', label = True):
    if cell == 'hex':
       a,b,c,d = x_array[0],x_array[N[0]],x_array[N[0]+N[1]],x_array[-1]
       if label: ax.set_xticks([a,b,c,d],[r'$\Gamma$','M','K',r'$\Gamma$'])
       ax.axvline(a,color='k')
       ax.axvline(b,color='k')
       ax.axvline(c,color='k')
       ax.axvline(d,color='k')
    if cell == 'cubic':
       a,b,c,d,e = x_array[0],x_array[N[0]],x_array[N[0]+N[1]],x_array[N[0]+N[1]+N[2]],x_array[-1]
       if label: ax.set_xticks([a,b,c,d,e],[r'$\Gamma$','X','S','Y',r'$\Gamma$'])
       ax.axvline(a,color='k')
       ax.axvline(b,color='k')
       ax.axvline(c,color='k')
       ax.axvline(d,color='k')
       ax.axvline(e,color='k')

fig = plt.figure(figsize = (7,7))
ax = fig.add_axes([0.15,0.1,0.8,0.8])

CELL = 'hex'
file = 'dispersion.txt'
data = np.loadtxt(file)
N = [15,5,10]
x_array = calculate_distances(N,cell = CELL, a = 3.508, b = 4.763)
np.savetxt('x_array_distanced.txt',x_array)
ax.plot(x_array,eV2meV*(data[:,3]-normalization(data[:,3])),'-o', markersize=6, color = 'k')
#datafile = plot_interpolation(ax, x_array, data[:,3]*eV2meV,N = 100,iwantdata=True)
#np.savetxt('crsbr2-gbt.txt',datafile)
#np.savetxt('crsbr2-gbt_points.txt',np.vstack((x_array,eV2meV*(data[:,3]-normalization(data[:,3])))).T)
custom_ax(ax,x_array,N,cell=CELL,label = True)

ax.set_ylabel('meV', fontsize=15)
ax.tick_params(labelsize=14)

#ax.set_ylim(-30,100)

plt.savefig('nibr2_gBt_LDA.pdf', format = 'pdf')
plt.show()
