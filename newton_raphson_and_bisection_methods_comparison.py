import math
import timeit

print('Shem Nicholas Opiyo')
print('SCT211-0509/2021')

# this code starts with the comparison description of the 
# function to be used in comparing the newton raphson 
# method and bisection method. The section also has a 
# derivative to be used in implementing newton raphson 
# method. The timeit library will be used to measure the 
# runtime of the two methods.

def f(x) :                      #this is the function to be compared.
     return x**4+x**3-2*x**2+x-18
     
def df(x):                      # this is the derivative of the function
    return 4*x**3+3*x**2-4*x+1 
# these are the limits to be used in implementing bisection method,
# and indicating the start of the newton raphson method.      
a = 1
b = 2
tolerance = 1e-6
x0 = a 
max_iterations = 100

# This section implements the bisection method 
start_time = timeit.default_timer()        
for  i in range(max_iterations) :
    c = (a+b)/2

    if abs(f(c))<tolerance:
        print(f"Through the Bisection method, root found at x={c:.6f}")
        break
    elif f(c) * f(a) <0 :
        b= c
    else:
        a = c
bisection_time = timeit.default_timer() - start_time
print(f"BisectionTime : {bisection_time}")

# This section implements the newton raphson method 
start_time = timeit.default_timer()
for  i in range(max_iterations) :
        fx = f(x0)
        dfx = df(x0)
        x1 = x0 - fx/dfx
        if abs( f(x1) ) < tolerance:
            print(f"Through Newton Raphson method, root found at x = {x1:.6f}" )
            break 
        else:
            x0 = x1

newton_time = timeit.default_timer() - start_time
print(f"Newton Raphson Time : {newton_time}" ) 

if newton_time < bisection_time :
    print(f"\n\n Juding from the comparison of the two method's run time, Newton raphson method takes a shorter period than bisection method")
else:
    print("\n\nJudging from the comparison of the two methods's runtime, bisection method takes a shorter period than Newton Raphson method")
