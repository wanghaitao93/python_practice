# -*- encoding=utf-8 -*- 

import sys
import time
import functools

reload(sys)
sys.setdefaultencoding('utf-8')

# print func run time from start to end
def print_run_time(func):
    @functools.wraps(func) 
    def wrapper(*args, **kw):
        pre_time = time.time()
        result = func(*args, **kw)
        print 'time ', time.time() - pre_time
        return result
    return wrapper
    
def fibonacci(n):
    # recursion func  
    if (n < 1):
        return 0
    if (n == 1):
        return 1
    if (n == 2):
        return 2
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_dict(n, my_dict):
    # use dict store calculated f(n) 
    if (n < 1):
        return 0
    if (n == 1):
        return 1
    if (n == 2):
        return 2
    
    if n in my_dict:
        return dict[n]
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)
        dict[n] = value
        return value
    

@profile
@print_run_time
def fibonacci_dynamic_programming(n):
    """
    dynamic programming have three core element, include: 
        optimal substructure
        boundary
        state transition equation
    """
    if (n < 1):
        return 0
    if (n == 1):
        return 1
    if (n == 2):
        return 2
    
    a = 1 
    b = 2
    temp = 0

    for i in xrange(3, n + 1):
        temp = a + b 
        a = b
        b = temp

    return temp
    
print fibonacci_dynamic_programming(1000)
