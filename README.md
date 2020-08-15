# mpltex_plot
a simple script to plot publication-ready plots using mpltex

This is a script to plot LAMMPS dumpfiles  of uniaxial tension test with strain,px,py,pz outputs seperated with comma as delimiter.
The file name have to be passed as an argument in the command line while calling the script.The output will be in eps format.


For example,to plot a file named silver500.txt the comand should be:
python mpltexplot.py silver500.txt
