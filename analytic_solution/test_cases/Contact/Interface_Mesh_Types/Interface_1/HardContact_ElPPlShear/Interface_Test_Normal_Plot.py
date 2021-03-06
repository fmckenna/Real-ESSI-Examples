#!/usr/bin/python
import h5py
import matplotlib.pylab as plt
import matplotlib as mpl
import sys
import numpy as np;
import matplotlib;
import math;
from matplotlib.ticker import MaxNLocator

plt.rcParams.update({'font.size': 28})

# set tick width
mpl.rcParams['xtick.major.size'] = 10
mpl.rcParams['xtick.major.width'] = 5
mpl.rcParams['xtick.minor.size'] = 10
mpl.rcParams['xtick.minor.width'] = 5
plt.rcParams['xtick.labelsize']=24

mpl.rcParams['ytick.major.size'] = 10
mpl.rcParams['ytick.major.width'] = 5
mpl.rcParams['ytick.minor.size'] = 10
mpl.rcParams['ytick.minor.width'] = 5
plt.rcParams['ytick.labelsize']=24

###############################################################
## Analytical Solution
###############################################################
# Go over each feioutput and plot each one.  
thefile = "Analytical_Solution_Normal_Stress.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
normal_stress  = -finput["/Model/Elements/Element_Outputs"][9,:];
normal_strain  = -finput["/Model/Elements/Element_Outputs"][6,:];

# Configure the figure filename, according to the input filename.
outfig=thefile.replace("_","-")
outfigname=outfig.replace("h5.feioutput","pdf")

# Plot the figure. Add labels and titles.
plt.figure(figsize=(12,10))

plt.plot(normal_strain*100,normal_stress/1000,'-r',label='Analytical Solution', Linewidth=4, markersize=20)
plt.xlabel(r"Interface Type #")
plt.ylabel(r"Normal Stress $\sigma_n [kPa]$")
plt.hold(True)

###############################################################
## Numerical Solution
###############################################################
# Go over each feioutput and plot each one.  
thefile = "Interface_Surface_Adding_axial_Load.h5.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
normal_stress  = -finput["/Model/Elements/Element_Outputs"][9,:];
normal_strain  = -finput["/Model/Elements/Element_Outputs"][6,:];

# Configure the figure filename, according to the input filename.
outfig=thefile.replace("_","-")
outfigname=outfig.replace("h5.feioutput","pdf")

# Plot the figure. Add labels and titles.
plt.plot(normal_strain*100,normal_stress/1000,'-k',label='Numerical Solution', Linewidth=4, markersize=20)
plt.xlabel(r"Normal Strain [%]")
plt.ylabel(r"Normal Stress $\sigma_n [kPa]$")



#############################################################
# # # axes = plt.gca()
# # # axes.set_xlim([-7,7])
# # # axes.set_ylim([-1,1])
# outfigname  = "Interface_Test_Normal_Stress.pdf";
# plt.axis([0, 5.5, 90, 101])

# legend = plt.legend()
# legend.get_frame().set_linewidth(0.0)
# legend.get_frame().set_facecolor('none')
plt.legend()
plt.savefig(outfigname,  bbox_inches='tight')
# plt.show()