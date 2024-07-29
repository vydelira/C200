from timeit import default_timer as timer
import numpy as np

def fibRecursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibRecursive(n-1) + fibRecursive(n-2)

for n in range(1, 81):
    start = timer()
    print("f({0}) = {1} took {2} seconds.".format(n, fibRecursive(n), timer() - start))

def fibForLoop(n):
    a = np.array(range(n+1), int)
    a[0] = 0
    a[1] = 1
    for i in range(2, n+1):
        a[i] = a[i-1] + a[i-2]
    return a[n]

for n in range(1, 40):
    start = timer()
    print("f({0}) = {1} took {2} seconds.".format(n, fibForLoop(n), timer() - start))

'''
How long doesfib(10), fib(20), fib(40), fib(80)take you?Test this by changing the 
range value in the timing loop for your recursive Fibonacci.How are the numbers (roughly) 
changing for every next Fibonnaci number?
fib(10) took 4.1482490112627044e-05 seconds.
fib(20) took 0.003678684329369261 seconds.
fib(40) took 61.19946320802485 seconds.
fib(80) takes too long to load, I don't have enough patience to wait.
The numbers increase and decrease for the first few fibonacci numbers, then after the 32nd they keep increasing
and run-time slows down.


Compare your time with the while-loop implemention. When do you observe a significant difference in run-time?
The run-time for the for-loop is a lot faster than the recursive, the runtime for fib(40) took about 1 minutes, and it took
the for-loop 5 seconds.
'''