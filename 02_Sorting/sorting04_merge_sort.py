def merge_array(left,right):
    result=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]: #if i value less than j
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    #if i or j are exhausted 
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result
def merge_sort(arr): #splitting the arr 
    if len(arr)<=1: #returns arr
        return arr
    mid=len(arr)//2
    left_arr=arr[:mid] #excluded mid
    right_arr=arr[mid:] #from mid to end
    left=merge_sort(left_arr) #applying merge sort in left arr
    right=merge_sort(right_arr)

    return merge_array(left,right)
n=int(input("Enter the no. of elements :"))
arr=[]
print("Enter the elements:")
for i in range(n):
    value=int(input(f"Element {i+1}:"))
    arr.append(value)
print("Original array:", arr)

sorted_arr = merge_sort(arr)

print("Sorted array:", sorted_arr)