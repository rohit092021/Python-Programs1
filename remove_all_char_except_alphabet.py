str=input("enter str")
b="" 
for i in str:
    if i.isalpha() or i.isspace():
        b+=i
print(b)