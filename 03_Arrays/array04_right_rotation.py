def right_rotation(nums):
    n=len(nums)
    temp=nums[n-1]
    for i in range(n-2,-1,-1):
        nums[i+1]=nums[i]
    nums[0]=temp
nums=list(map(int,input("Enter the elements :").split()))
right_rotation(nums)
print("Arrays after right rotation :",nums)