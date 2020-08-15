import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from pylab import cm
mpl.rcParams['font.family'] =  'Times New Roman'
plt.rcParams['font.size'] = 18
plt.rcParams['axes.linewidth'] = 2

colors = cm.get_cmap('tab10', 3)

cwd=os.getcwd()
print(cwd)
name=sys.argv[1]
file="plot"+name[:-4]+".png"
print("plot"+name[:-4])
strain,px,py,pz=np.genfromtxt(name,delimiter=' ',unpack=True,skip_header=1)

fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.9,0.9])
ax.xaxis.set_tick_params(which='major', size=10, width=2, direction='in', top='on')
ax.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in', top='on')
ax.yaxis.set_tick_params(which='major', size=10, width=2, direction='in', right='on')
ax.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in', right='on')

ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.01))
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.005))
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(0.1))
ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.05))
ax.set_xlabel('Strain', labelpad=10)
ax.set_ylabel('Stress', labelpad=10)
ax.legend(loc='best', ncol=2)
ax.set_xlim(0, 0.2)

ax.plot(strain,pz,label="Pz", linewidth=2, color=colors(0))
ax.plot(strain,py,label="Py", linewidth=2, color=colors(1))
ax.plot(strain,px,label="Px", linewidth=2, color=colors(2))

#ax.set_ylim(-0.2, 2.2)
plt.savefig(file, dpi=300, transparent=False, bbox_inches='tight')
plt.grid()
plt.show()