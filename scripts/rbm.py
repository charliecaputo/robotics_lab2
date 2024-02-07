# Here we write some functions that help us analayze the motions of a rigid body

# import the required modules
import math
import numpy as np

def rot_2d(theta):
	"""
	Receives an input in radians and
	returns a 2D rotation matrix
	R = [cos(theta) -sin(theta)
	     sin(theta)  cos(theta)]
	"""
	rot = np.array([[math.cos(theta), -math.sin(theta)],
					[math.sin(theta), math.cos(theta)]])
	return rot

# use lecture slides for the mathematical equations 
def rot_x(theta):
	rot = np.array([[1.0,  0.0, 0.0],
				    [0.0, math.cos(theta), -math.sin(theta)],
					[0.0, math.sin(theta), math.cos(theta)]])
	return rot
	
def rot_y(theta):
	rot = np.array([[math.cos(theta),  0.0, math.sin(theta)],
				    [0.0, 1.0, 0.0],
					[-math.sin(theta), 0.0, math.cos(theta)]])
	return rot
	
def rot_z(theta):
	rot = np.array([[math.cos(theta),  -math.sin(theta), 0.0],
					[math.sin(theta),   math.cos(theta), 0.0],
				    [0.0, 0.0, 1.0]])
	return rot
	
def vec(x,y,z):
#	Define a vector as an numpy and transpose it to a column vector.
	vec = np.array([[x, y, z]]).T 
	return vec
