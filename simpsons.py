import math as math

u= 2000
q= 2100
m0= 140000
g= 9.8
t1= 30
t0= 8

def error(old, new):
    err=100*((abs(new-old))/new)
    return err

def f(t):
    return u*math.log(m0/(m0-q*t))-g*t

def simpsons(a, b, n):
    if n%2!=0:
        return "The number of divisions must be even for Simpson's 1/3rd rule"
    h= (b-a)/n
    sum= f(a)+f(b)
    i=0
    for i in range(n-1):
        if (i+1)%2==0:
            sum+=2*f(a+(i+1)*h)
        else:
            sum+=4*f(a+(i+1)*h)
    sum=sum*(h/3)
    return sum

def simpsonsErrorTable(a, b):
    prevSum=0
    print('Divisions\t','        Calculated Values\t','                Absolute Approximate Relative Error')
    for i in range(5):
        sum=simpsons(a, b, 2*(i+1))
        err=error(prevSum, sum)
        if i==0:
            print(2*(i+1),'               \t','%1.10f'%sum,'                  \t','--------')
        else:
            print(2*(i+1),'               \t','%1.10f'%sum,'                  \t','%3.6f'%err)
        prevSum=sum
        
n= int(input("Enter number of divisions:"))
print(simpsons(t0, t1, n))
simpsonsErrorTable(t0, t1)