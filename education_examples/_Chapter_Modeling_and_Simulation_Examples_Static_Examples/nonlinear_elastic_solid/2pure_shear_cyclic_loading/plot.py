import numpy as np
import matplotlib.pyplot as plt  
import h5py 

def h52stressStrain(h5in_filename):
	h5in=h5py.File(h5in_filename,"r")
	outputs_all=h5in['/Model/Elements/Gauss_Outputs'][()]
	stress = outputs_all[14 , 1:-1]
	strain = outputs_all[2  , 1:-1]
	return [stress, strain]

# [stress, strain]   = h52stressStrain("DP_1Confine.h5.feioutput")
[stress_load,   strain_load]   = h52stressStrain("DP_1Confine.h5.feioutput")
[stress_unload, strain_unload] = h52stressStrain("DP_2Release.h5.feioutput")
stress  = np.concatenate((stress_load,stress_unload))
strain  = np.concatenate((strain_load,strain_unload))

# [stress_reload, strain_reload] = h52stressStrain("DP_3ReConfine.h5.feioutput")
# stress  = np.concatenate((stress_load,stress_unload,stress_reload))
# strain  = np.concatenate((strain_load,strain_unload,strain_reload))

# plt.plot(strain, stress)
# plt.show()

plt.plot(strain, stress)
plt.xlabel('Strain / (unitless)')
plt.ylabel('Stress / (Pa)')
plt.title('Material Behavior: Stress-Strain')
plt.grid()
plt.box()
plt.savefig('result.pdf', transparent=True, bbox_inches='tight')
plt.show()