import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import mpltex
import sys
import os


os.environ["PATH"] += os.pathsep + "C:\Program Files\MiKTeX 2.9\miktex\bin"
print(os.getenv("PATH"))
cwd=os.getcwd()
print(cwd)
name=sys.argv[1]
#name=input('filename-\n')
strain,px,py,pz=np.genfromtxt(name,delimiter=' ',unpack=True,skip_header=1)


@mpltex.aps_decorator
def my_plot(name):
    fig, ax = plt.subplots(1)
    linestyles = mpltex.linestyle_generator(markers=[])
    #ax.plot(t, t, label='$t$', **next(linestyles))
    ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.05))
    ax.plot(strain, pz,linewidth=1, **next(linestyles),label="Pz")
    ax.plot(strain, py,linewidth=1, **next(linestyles),label="Py")
    ax.plot(strain, px,linewidth=1, **next(linestyles),label="Px")


    ax.set_xlabel('Strain')
    ax.set_ylabel('Stress')
    ax.legend(loc='best', ncol=2)
    plt.grid()
    fig.tight_layout(pad=0.1)
    fig.savefig("plot"+name[:-4])


my_plot(name)




