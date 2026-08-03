def insertion_sort(nums):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j=j-1
        nums[j+1]=key
n=int(input("Enter the size :"))
nums=[]
print("Enter the elements :")
for i in range(n):
    elements=int(input("Enter elements: "))
    nums.append(elements)
print("Before sorting :")
print(nums)
insertion_sort(nums)
print("After sorting :")
print(nums)