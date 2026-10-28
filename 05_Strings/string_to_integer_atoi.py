def string_to_integer_atoi(s):
    INT_MIN=-(2**31)
    INT_MAX=(2**31)-1
    i=0
    n=len(s)
    while i<n and s[i]==" ":
        i+=1
    sign=1
    if i<n and s[i]=="-":
        sign=-1
        i+=1
    elif i<n and s[i]=="+":
        i+=1
    result=0
    while i<n and "0"<=s[i]<="9":
        digit=ord(s[i])-ord("0")
        result=result*10+digit
        if sign*result<INT_MIN:
            return INT_MIN
        if sign*result>INT_MAX:
            return INT_MAX
        i+=1
    return sign*result
s = input("Enter a string: ")

result = string_to_integer_atoi(s)
print("Integer value:", result)
