def Bubblesort(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]

n=int(input("Enter the size :"))
nums=[]
print("Enter the numbers: ")
for i in range(n):
    element=int(input())
    nums.append(element)
print("Before sorting :")
print(nums)
Bubblesort(nums)
print("After sorting :")
print(nums)
        