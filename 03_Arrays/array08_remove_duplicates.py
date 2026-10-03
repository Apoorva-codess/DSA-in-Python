def remove_duplicates(nums):
    n=len(nums)
    if n==1:
        return 1
    i=0
    j=i+1
    while j<n:
        if nums[j]!=nums[i]:
            i=i+1
            nums[i],nums[j]=nums[j],nums[i]
        j=j+1
    return i+1
nums=list(map(int,input("Enter the numbers :").split()))
nums.sort()
k=remove_duplicates(nums)
print("No. of unqiue elements :",k)
print("Array after removing the duplicates :",nums[:k])
