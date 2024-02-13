#import stuff no rbm, recreate arrays here
import math
import numpy as np


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

#create translation matrices
def Tx(x):
	return np.array([[1,0,0,x],
				    [0,1,0,0],
				    [0,0,1,0],
				    [0,0,0,1]])
def Ty (y): 
	return np.array([[1,0,0,0],
				  	[0,1,0,y],
				  	[0,0,1,0],
				  	[0,0,0,1]])
def Tz (z):
	return np.array([[1,0,0,0],
				  	[0,1,0,0],
				  	[0,0,1,z],
				  	[0,0,0,1]])


#rotation for x axis and print matrix
def Rx (psi):
	return np.array([[1, 0, 0, 0], 
	                 [0, np.cos(psi), -np.sin(psi), 0],
	            	 [0, np.sin(psi), np.cos(psi), 0], 
	            	 [0, 0, 0, 1]])

#rotation for y axis and print matrix
def Ry (theta):
	return np.array([[np.cos(theta), 0, np.sin(theta), 0], 
	            [0,1,0,0], 
	            [-np.sin(theta), 0, np.cos(theta), 0], 
	            [0,0,0,1]])

#rotation for z axis and print matrix
def Rz (phi):
	return np.array([[np.cos(phi), -np.sin(phi),0,0], 
	            [np.sin(phi), np.cos(phi), 0, 0], 
	            [0,0,1,0], 
	            [0,0,0,1]])

