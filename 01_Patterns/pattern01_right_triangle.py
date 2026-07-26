# Pattern 01: Right Triangle Star Patterncd 
for i in range(1,5):
    for j in range(1,5):
        if j<=i:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()