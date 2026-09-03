def bubbleSort(arr,n):
    if n<=1:
        return
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    bubbleSort(arr,n-1)

n=int(input("Enter no. of elements :"))
arr=list(map(int,input("Enter the elements :").split()))
bubbleSort(arr,n)
print("Sorted array:",arr)