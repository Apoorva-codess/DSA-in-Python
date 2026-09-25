def left_rotation(nums):
    n=len(nums)
    temp=nums[0]
    for i in range(0,n-1):
        nums[i]=nums[i+1]
    nums[n-1]=temp
nums=list(map(int,input("Enter the elements : ").split()))
left_rotation(nums)
print("Array after left rotation :",nums )