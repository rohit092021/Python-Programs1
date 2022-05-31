a=int(input("enter a number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a>b and b>c:
    print(  a)
elif b>a and a>c:
    print(b)
elif c>a and c>b:
    print(c)
else:
    print("both no are equal")