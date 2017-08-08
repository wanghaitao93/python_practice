# -*- encoding=utf-8 -*-

import sys
import time
import functools

reload(sys)
sys.setdefaultencoding('utf-8')
    
def log(func):
    def wrapper(*args, **kw):
        print 'call %s()' % func.__name__
        return func(*args, **kw)
    return wrapper

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


@log2('excute')
# now = log2('execute')(now)
def now():
    print time.time()

f = now
print f.__name__
f()
print f.__name__
