'''
def findArea(r):
   PI = 3.142
   return PI * (r*r);
# Driver method
print("Area is %.6f" % findArea(5));
'''
'''
start = 11
end = 25

for i in range(start, end+1): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i)
'''


'''
num = 407

if num > 1:
   
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       

else:
   print(num,"is not a prime number")
'''

'''
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
print(Fibonacci(9))
'''
'''
import math 
  
# A utility function that returns true if x is perfect square 
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  
# Returns true if n is a Fibinacci Number, else false 
def isFibonacci(n): 
   
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
     

for i in range(1,11): 
     if (isFibonacci(i) == True): 
         print (i,"is a Fibonacci Number")
     else: 
         print (i,"is a not Fibonacci Number")
'''

'''
def findPosition(k, n): 
    f1 = 0
    f2 = 1
    i =2;  
    while i!=0: 
        f3 = f1 + f2; 
        f1 = f2; 
        f2 = f3; 
  
        if f2%k == 0: 
            return n*i 
  
        i+=1
          
    return 
  
n = 5; 
k = 4; 
  
print("Position of n\'th multiple of k in"
                "Fibonacci Seires is", findPosition(k,n));
''' 

'''
c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))
'''


'''
def squaresum(n) : 

	 
	sm = 0
	for i in range(1, n+1) : 
		sm = sm + (i * i) 
	
	return sm 


n = 4
print(squaresum(n)) 

'''

'''

def sumOfSeries(n): 
	sum = 0
	for i in range(1, n+1): 
		sum +=i*i*i 
		
	return sum



n = 5
print(sumOfSeries(n)) 


'''











 