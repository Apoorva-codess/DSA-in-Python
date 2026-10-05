def union_arrays(nums1,nums2):
    n=len(nums1)
    m=len(nums2)
    i=0
    j=0
    result=[]
    while i<n and j<m:
        if nums1[i]<=nums2[j]:
            if len(result)==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i+=1
        else:
                if len(result)==0 or result[-1]!=nums2[j]:
                    result.append(nums2[j])
                j+=1
    while i<n:
         if len(result)==0 or result[-1]!=nums1[i]:
            result.append(nums1[i])
         i+=1
    while j<m:
         if len(result)==0 or result[-1]!=nums2[j]:
              result.append(nums2[j])
         j+=1
    return result 
nums1=list(map(int,input("Enter the numbers :").split()))
nums2=list(map(int,input("Enter the nos: ").split()))
result=union_arrays(nums1,nums2)
print("The union of the arrays is : ",result)