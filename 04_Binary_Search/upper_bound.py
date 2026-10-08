def upper_bound(nums,target):
    n=len(nums)
    low=0
    high=n-1
    ub=n
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            ub=mid
            high=mid-1
        else:
            low=mid+1
    return ub
nums=list(map(int,input("Enter the nos: ").split()))
target=int(input("Enter the target:"))
result=upper_bound(nums,target)
print("Upper bound index :",result)
if result<len(nums):
    print("Upper bound value :",nums[result])
else:
    print("No element is greater than target ")