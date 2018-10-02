#include the Numpy library
import numpy as np

#define the main() function
def main():

	i = 0					#declare an integer i
	x = 119.0				#declare a float x with val 119
	
	for i in range(120):	#loop i from 0 to 119, inclusive
		if((i%2)==0):		#if i is even
			x += 3.0		#add 3 to x; (x=x+3)
		else:				#if i is odd
			x -= 5.0		#subtract 5 from x; (x=x-5)
			
	s = "%3.2e" % x			#make a string containing x with
							#sci. notation(e) w/ 2 decimal places(.2)
							
	print(s)				#print s to the screen
	
#now the rest of the program continues
if __name__ == "__main__":	#if the main() function exists, run it
	main()