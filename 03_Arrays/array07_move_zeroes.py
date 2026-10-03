def move_zeros(nums):
    i=0
    while i<len(nums):
        if nums[i]==0:
            break
        i+=1
    if i==len(nums):
        return 
    j=i+1
    while j<len(nums):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
        j+=1
nums=list(map(int,input("Enter the array elements:").split()))
move_zeros(nums)
print("Array after moving the zeros : ",nums)
