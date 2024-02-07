#import necessary stuff including rbm.py
import rbm
import math
import numpy as np

if __name__ == '__main__':
	##test values
	psi = math.pi/2     ## x rot variable
	theta = math.pi/2   ## y rot variable
	phi = math.pi/2  	## z rot variable
	
	#update output format
	np.set_printoptions(precision = 2, suppress= True)
	
	#define 3d vector
	v0 =rbm.vec(0,1,1)
	
	#rotation on x axis
	Rx= rbm.rot_x(psi)
	
	#then y axis
	Ry = rbm.rot_y(theta)
	
	#and z axis
	Rz = rbm.rot_z(phi)
	
	#calc total rotaional matrix
	R_total = np.matmul(Rz, np.matmul(Ry,Rx))
	
	#calculate results
	v_rot_tot = np.dot(R_total, v0)
	
	#show results
	print("The transfomred vector after troation is: \n", v_rot_tot)
