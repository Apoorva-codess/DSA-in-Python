n=int(input("Enter no. of rows :"))
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    for j in range(i,n-1):
        print(" ",end=' ')
    for j in range(i,n-1):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print()
for i in range(n-2,-1,-1):
    for i in range(i+1):
        print("*",end=' ')
    for j in range(i,n-1):
        print(" ",end=' ')
    for j in range(i,n-1):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print()
