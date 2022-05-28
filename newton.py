def g(x):
    return x**2 - 5*x + 6
def f(x):
    return x**3 - 2400*x**2 - 3*x + 2


def solve(f, x, maxError = 0.001, maxIteration = 50):
    xold = x
    xnew = 0
    error = 100
    iteration = 0
    while error>maxError and iteration < maxIteration:
        xold = x
        del_x = 0.0000001
        del_f = f(x+del_x)-f(x)
        f_prime  = del_f/del_x
    
        xnew = x = x - f(x)/f_prime
        error = abs(1-xold/xnew)*100
        #print(error,"\t", xold, "\t",xnew)
        iteration+=1
        
    return x

print(solve(g,3.4))
print(solve(f,-100))
    
        