#import stuff including p2_solve.py
import p2_solve as p2
import math
import numpy as np
 
if __name__ == '__main__':
	#transformation 1 
	T1_x = p2.translation_matrix(2.5,0,0)
	T2_y = p2.translation_matrix(0,-1.5,0)
	t3_z = p2.translation_matrix(0,0,0.5)
