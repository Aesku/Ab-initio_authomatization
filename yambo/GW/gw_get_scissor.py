import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

FS = 20
MERGED = True
first_band = 14
PRINT_DATA = True

fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0.15,0.15,0.8,0.8])

data_up = np.loadtxt('data_up.txt')
data_dn = np.loadtxt('data_dn.txt')

ax.scatter(data_up[:,0],data_up[:,1], color='r',label='up')
ax.scatter(data_dn[:,0],data_dn[:,1], color='b',label='dn')
ax.legend(fontsize=FS, loc = 'lower right')
ax.set_xlabel('IP (eV)',fontsize=FS)
ax.set_ylabel('QP (eV)', fontsize=FS)
ax.set_title('GW correction',fontsize=FS)
ax.tick_params(labelsize=FS)
ax.set_xlim(-5,7)
ax.set_ylim(-5,7)
ax.grid(visible=True)

plt.savefig('gw_corr-bands.pdf',format='pdf')
plt.show()

#Calculate linear regression:

# Load data from the file
up_valence = data_up[:8,:]
up_cond = data_up[8:,:]
dn_valence = data_dn[:8,:]
dn_cond = data_dn[8:,:]
names = ['upv','upc','dnv','dnc']
colors = ['r','r','b','b']

for i,data in enumerate([up_valence,up_cond,dn_valence,dn_cond]):
    x = data[:, 0]  # First column (independent variable)
    y = data[:, 1]  # Second column (dependent variable)

# Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Print the regression parameters
    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")
    print(f"R-squared: {r_value**2}")

# Generate regression line
    y_pred = slope * x + intercept

# Plot the data and regression line
    fig = plt.figure(figsize=(7,7))
    ax = fig.add_axes([0.15,0.15,0.8,0.8])
    ax.scatter(x, y, label=names[i], color=colors[i])
    ax.plot(x, y_pred, label='Slope %s'%names[i], color=colors[i])
    ax.text(x[0]+0.2,y_pred[0],f"Slope: {slope}", fontsize=FS)
    ax.set_xlabel('IP (eV)',fontsize=FS)
    ax.set_ylabel('QP (eV)', fontsize=FS)
    ax.set_title('GW correction',fontsize=FS)
    ax.tick_params(labelsize=FS)
    plt.legend()
    plt.savefig('scissor-slope-%s.pdf'%names[i], format = 'pdf')
    plt.show()

exit()
