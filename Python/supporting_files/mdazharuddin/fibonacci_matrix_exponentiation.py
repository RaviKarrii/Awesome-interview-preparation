# Helper function that multiplies  
# 2 matrices F and M of size 2*2,  
# and puts the multiplication 
# result back to F[][]  
  
# Helper function that calculates  
# F[][] raise to the power n and  
# puts the result in F[][] 
# Note that this function is  
# designed only for fib() and  
# won't work as general 
# power function  
def fib(n): 
	
	F = [[1, 1], 
		[1, 0]] 
	if (n == 0): 
		return 0
	power(F, n - 1) 
		
	return F[0][0] 
	
def multiply(F, M): 
	
	x = (F[0][0] * M[0][0] +
		F[0][1] * M[1][0]) 
	y = (F[0][0] * M[0][1] +
		F[0][1] * M[1][1]) 
	z = (F[1][0] * M[0][0] +
		F[1][1] * M[1][0]) 
	w = (F[1][0] * M[0][1] +
		F[1][1] * M[1][1]) 
	
	F[0][0] = x 
	F[0][1] = y 
	F[1][0] = z 
	F[1][1] = w 

def power(F, n): 

	if( n == 0 or n == 1): 
		return; 
	M = [[1, 1], 
		[1, 0]]; 
		
	power(F, n // 2) 
	multiply(F, F) 
		
	if (n % 2 != 0): 
		multiply(F, M) 
	
# Driver Code 
if __name__ == "__main__": 
	n = int(input("Enter n: "))
	print(fib(n)) 
