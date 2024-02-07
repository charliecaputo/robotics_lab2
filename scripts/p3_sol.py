#import stuff including p2_solve.py
import p2_sol as p2
import math
import numpy as np
 
if __name__ == '__main__':

	#define the fixed vector/ origin
	v0 = np.array([[1,0,0,0],
					[0,1,0,0],
					[0,0,1,0],
					[0,0,0,1]])
					
	current_pos = np.array([[1,0,0,0],
					 		[0,1,0,0],
							[0,0,1,0],
							[0,0,0,1]])
	
	#transformation 1
	H_1 = np.dot(p2.Tx(2.5), np.dot(p2.Tz(0.5), p2.Ty(-1.5)))
	result_1 = current_pos = np.dot(H_1, current_pos)
	print("Transformation 1: \n", result_1)
	
	#transformation 2
	H_2 = np.dot(p2.Tz(0.5), np.dot(p2.Tx(2.5), p2.Ty(-1.5)))
	result_2 = np.dot(H_2, current_pos) #ask if i should dot by H_1 since its current and not fixed
	print("Transformation 2: \n", result_2)
	
	#transformation 3 this is the same as one because there is no rotation
	H_3 = np.dot(p2.Tx(2.5), np.dot(p2.Tz(0.5), p2.Ty(-1.5))) 
	print("Transformation 3: \n", H_3)
	
	#transformation 4 same as two because there is no rotation and both are starting at origin
	H_4 = np.dot(p2.Tz(0.5), np.dot(p2.Tx(2.5), p2.Ty(-1.5)))
	print("Transformation 3: \n", H_4)
	
	#Transformation 5
	H_5 = np.dot(p2.Rx(np.pi/2), np.dot(p2.Tx(3), np.dot(p2.Tz(-3), p2.Rz(-np.pi/2))))
	result_5 = np.dot(H_5, current_pos)
	print("transformation 5: \n", result_5)
	
	
