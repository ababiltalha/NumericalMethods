import numpy as np

A=np.array([[25.0, 5.0, 1.0],[64.0, 8.0, 1.0],[144.0, 12.0, 1.0]],dtype=np.float32)
B=np.array([106.8, 177.2,  279.2],dtype=np.float32)
print(A)
print(B)


def gaussianElimination(A,B,d):
    n=len(B)
    R=np.ones((n,1),dtype=np.float32)

    for i in range(0,n):
        for j in range(i+1,n):
            # print(A[j,i]/A[i,i])
            B[j]=(A[j,i]/A[i,i])*B[i]-B[j]
            A[j]=(A[j,i]/A[i,i])*A[i]-A[j]
        if d==True:
            for k in range(0, n):
                for m in range(0, n):
                    print('%0.4f'%A[k,m],end="\t")
                print()
            print()
            for k in range(0, n):
                print('%0.4f'%B[k])
            print()
    for i in range(n-1,-1,-1):
        R[i]=((B[i]-np.dot(A[i],R))+A[i,i])/A[i,i]
    return R

# Akib er code
def gaussianElemination(a,b):
    n =len(b)
    x = np.zeros(n, dtype = float)

    #Elimination step
    for k in range(n-1):
        for i in range (k+1,n):
            if a[i][k] == 0:
                continue
            factor = a[k][k]/a[i][k]
            for j in range(k,n):
                a[i][j] =a[k][j] - a[i][j] * factor
            b[i] = b[k] - b[i] * factor
    #printing the matrix after the elemination
    #BackSubstitution
    #doing the last row
    x[n-1] = b[n-1] / a[n-1][n-1]
    #as the loop is descending the value 
    for i in range(n-2,-1,-1):
        sum_ax = 0
        for j in range(i+1,n):
            sum_ax += a[i][j] * x[j]
        x[i] = (b[i] - sum_ax) / a[i][i]

    #now x has the solution of the system
    # print(x)
    return x


# n=int(input("Enter number of variable:"))
# print("Enter matrix:")
# A=np.zeros((n,n),dtype=np.float32)
# B=np.zeros((n,1),dtype=np.float32)
# for i in range(n):
#     for j in range(n):
#         A[i,j]=float(input())
# # print(A)
# for i in range(n):
#     B[i]=float(input())
# print()
# d=True
# R=gaussianElimination(A,B,d)
# print("Solution column matrix:")
# for i in range(n):
#     print('%0.4f'%R[i,0])
print(gaussianElemination(A,B))