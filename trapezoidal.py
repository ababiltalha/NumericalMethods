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

def trapezoidalRule(a, b, n):
    h= (b-a)/n
    sum= f(a)+f(b)
    for i in range(n-1):
        sum+=2*f(a+(i+1)*h)
    sum=sum*(h/2)
    return sum

def trapezoidalRuleErrorTable(a, b):
    prevSum=0
    print('Divisions\t','        Calculated Values\t','                Absolute Approximate Relative Error')
    for i in range(5):
        sum=trapezoidalRule(a, b, i+1)
        err=error(prevSum, sum)
        if i==0:
            print(i+1,'               \t','%1.10f'%sum,'                  \t','--------')
        else:
            print(i+1,'               \t','%1.10f'%sum,'                  \t','%3.6f'%err)
        prevSum=sum
        
n= int(input("Enter number of divisions:"))
print(trapezoidalRule(t0, t1, n))
trapezoidalRuleErrorTable(t0, t1)