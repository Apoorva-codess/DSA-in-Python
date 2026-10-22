def max_depth(s):
    max_dep=0
    curr_dep=0
    for ch in s:
        if ch=="(":
            curr_dep+=1
            max_dep=max(max_dep,curr_dep)
        elif ch==")":
            curr_dep-=1
    return max_dep
s=input("Enter the string :")
result=max_depth(s)
print("Maximum nesting depth : ", result)