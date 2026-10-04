def missing_nums(nums,n):
    n=len(nums)
    exp_sum=n*(n+1)//2
    actual_sum=sum(nums)
    return exp_sum-actual_sum

n = int(input("Enter the value of n: "))
nums=list(map(int,input("Enter the nums: ").split()))
result=missing_nums(nums,n)
print("Missing number is :",result)