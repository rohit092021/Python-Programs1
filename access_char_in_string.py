name=input("enter string")
ch=input("enter ch thats frequency u want")
f=0
for i in name:
    if i==ch:
        f+=1
print('frequency of given   no is',f)