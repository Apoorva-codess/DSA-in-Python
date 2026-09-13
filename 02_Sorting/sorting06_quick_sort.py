def partition(nums,low,high):
    pivot=nums[low]
    i=low
    j=high

    while i<j:
        while(nums[i]<=pivot and i<=high-1):
            i=i+1
        while(nums[j]>pivot and j>=low+1):
            j=j-1
    if i<j:
        nums[i],nums[j]=nums[j],nums[i]
    nums[low],nums[j]=nums[j],nums[low]

    return j

def quicksort(nums,low,high):
    if low<high:
        p_index=partition(nums,low,high)
        quicksort(nums,low,p_index-1)
        quicksort(nums,p_index+1,high)
n=int(input("Enter no. of elements :"))
nums=list(map(int,input("Enter the elements :  ").split()))
quicksort(nums,0,n-1)
print("Sorted array :",nums)
