a=input('enter str')
x=0
b=''
for i in a:
    if a.index(i)==x:
        b+=i
    x+=1
print(b)