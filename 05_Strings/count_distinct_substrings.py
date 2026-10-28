def count_distinct_substring(s):
    n=len(s)
    n_set=set()
    for i in range(n):
        string=" "
        for j in range(i,n):
            string+=s[j]
            n_set.add(string)
    return len(n_set)+1
s=input("Enter the string:")
result=count_distinct_substring(s)
print("No. of distinct substring: ",result)

