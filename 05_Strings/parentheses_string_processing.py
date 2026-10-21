def process_string(s):
    result=""
    count=0
    for ch in s:
        if ch=="(":
            count+=1
            if count>1:
                result+=ch
        else:
            count-=1
            if count>0:
                result+=ch
    return result
s=input("Enter a parenthesis string :")
result=process_string(s)
print("Result:",result)
