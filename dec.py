import time

def infowrap(f):
    def info(n):
        return f.__name__ + ", " + str(n)
    return info

def timewrap(f):
    start = time.time()
    def timer(n):
        f(n)
        return time.time() - start
    return timer
    
@timewrap
def fib(n):
    if n == 0:
        return 0
    if n <= 2 :
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

print(fib(100))
