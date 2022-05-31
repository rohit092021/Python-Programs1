n=int(input('enter no'))
if n<2:
    print('not prime')
else:
    for i in range(2,n):
        if n%i==0:
            print('Not prime')
            break
    else:
        print('prime')