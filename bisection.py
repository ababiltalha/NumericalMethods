import matplotlib.pyplot as plt
import numpy as num

def f(x):
    return x**3-2400*(x**2)-3*x+2

x = num.linspace(0,1,10000)
y = f(x)
plt.plot(x,y)
plt.grid()

def error(old, new):
    err=100*((abs(new-old))/new)
    return err

def bisection(xl, xu, eps, n):
    xmold=0
    i=1
    if f(xu)*f(xl) > 0:
        print("Range does not include solution.") 
    while i <= n:
        #print(i)
        xm=(xu+xl)/2
        #print(xm)
        if f(xm)*f(xl)<0:
            xu=xm
        elif f(xm)*f(xl)>0:
            xl=xm
        if i>1:
            #print(error(xmold,xm))
            if error(xmold,xm) < eps:
                break
        #print(i,xm,error(xmold,xm))
        xmold=xm
        i=i+1
    return xm   
            
def bisectiontabular(xl, xu, eps, n):
    xmold=0
    i=1
    if f(xu)*f(xl) > 0:
        print("Range does not include solution.") 
    print('Iteration(i)\t','    Estimated Root(xm)\t','                Aboslute Relative Approximate Error(ea)')
    while i <= n:
        xm=(xu+xl)/2
        if f(xm)*f(xl)<0:
            xu=xm
        elif f(xm)*f(xl)>0:
            xl=xm
        ea=error(xmold,xm)
        if i==1:
            print(i,'               \t','%1.10f'%xm,'                  \t','---------')
        else:
            print(i,'               \t','%1.10f'%xm,'                  \t','%3.6f'%ea)
        xmold=xm
        i=i+1
    return xm  

print("\n")
print("The value of x that satisfies the equation is", bisection(0.0,1.0,0.5,20),"\n")
print("The table of estimated values of x with respective errors in percentage is as follows\n")
bisectiontabular(0,1,0.5,20)
plt.show()