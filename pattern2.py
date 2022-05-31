a=input("enter string:")
ch=ord(a[0])
c=0
for i in range(1+len(a)):
    if(ch==ord(a[i]) or ch==ord(a[i])+32):
        c=c+1
    else:
        print("not")
        break
if(c==len(a)):
    print("YES")