n=int(input("Enter the size:"))
nums=list(map(int,input("Enter the elements :").split()))
largest=float("-inf")
s_largest=float("-inf")
for i in range(n):
    if nums[i]>largest:
        s_largest=largest
        largest=nums[i]
    elif nums[i]>s_largest and nums[i]!=largest:
        s_largest=nums[i]
print("Largest element :",largest)
print("Second largest element : ",s_largest)