n=int(input("Enter no. of elements "))
nums=list(map(int,input("Enter the elements : ").split()))
largest=nums[0]
for i in range(n):
    largest=max(largest,nums[i])
print("largest number is :",largest)