n=int(input("enter no"))
# i=2
# while i<n:
for i in range(2,n):
    if(n%i==0):
        print("not prime")
        break
    # i=i+1
    else:
        print("prime")