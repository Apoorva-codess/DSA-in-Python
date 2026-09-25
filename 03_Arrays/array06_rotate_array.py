def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
def rotate_arrays(nums,k):
    n=len(nums)
    k=k%n
    reverse(nums,n-k,n-1)
    reverse(nums,0,n-k-1)
    reverse(nums,0,n-1)
nums=list(map(int,input("Enter the elements :").split()))
k=int(input("Enter the value of k:"))
rotate_arrays(nums,k)
print("Array after rotation: ",nums)