#import stuff no rbm, recreate arrays here
import math
import numpy as np

if __name__ == '__main__':
	#test values
	tx = 2	# x trans value
	ty = 3	# y trans value
	tz = 4	# z trans value
	psi = math.pi/2		#x rot value
	theta = math.pi/2	#y rot value
	phi = math.pi/2		#z rot value
	
	#update output format
	np.set_printoptions(precision = 2, suppress= True)
	
	#define 4d vector from example
	v0 = np.array([0,1,1,1]) #start coords
	
	#translation matrices and print each one 
	T = np.array([[1,0,0,tx],
				  [0,1,0,ty],
				  [0,0,1,tz],
				  [0,0,0,1]])
	print("Translation matrix that represents (x,y,z) as (2,3,4) respectively: \n", T)
	
	
	#rotation for x axis and print matrix
	Rx = np.array([[1, 0, 0, 0], 
	               [0, np.cos(psi), -np.sin(psi), 0],
	               [0, np.sin(psi), np.cos(psi), 0], 
	               [0, 0, 0, 1]])
	print("rotation matrix for basic homogenous transformation about x axis:\n ", Rx)
	
	#rotation for y axis and print matrix
	Ry = np.array([[np.cos(theta), 0, np.sin(theta), 0], 
	               [0,1,0,0], 
	               [-np.sin(theta), 0, np.cos(theta), 0], 
	               [0,0,0,1]])
	print("rotation matrix for basic homogenous transformation about x axis:\n ", Ry)
	
	#rotation for z axis and print matrix
	Rz = np.array([[np.cos(phi), -np.sin(phi),0,0], 
	               [np.sin(phi), np.cos(phi), 0, 0], 
	               [0,0,1,0], 
	               [0,0,0,1]])
	print("rotation matrix for basic homogenous transformation about x axis:\n ", Rz)
