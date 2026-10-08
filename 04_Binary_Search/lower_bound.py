def lower_bound(nums,target):
    n=len(nums)
    low=0
    high=n-1
    lb=0
    while low<=high:
        mid=low+high//2
        if nums[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return lb
nums=list(map(int,input("Enter the nos:").split()))
target=int(input("Enter the target:"))
result=lower_bound(nums,target)
if result<len(nums):
    print("lower bound is :",result)
else:
    ("No element is greater than or equal to target")