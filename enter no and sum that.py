# enter no eg 1234 and print 1+2+3+4=10
total =0
num=(input("enter no"))
for i in range(0,len(num)):
    total+=int(num[i])
print(total)
