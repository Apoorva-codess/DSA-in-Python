def Selectionsort(nums):
    n=len(nums)
    for i in range(n):
        max_index=i
        for j in range(i+1,n):
            if(nums[j]>nums[max_index]):
                max_index=j
        nums[i],nums[max_index]=nums[max_index],nums[i]
n=int(input("Enter the size: "))
nums=[]
for i in range(n):
    element=int(input())
    nums.append(element)
print("\nBefore Sorting:")
print(nums)
Selectionsort(nums)
print("\nAfter Sorting:")
print(nums)