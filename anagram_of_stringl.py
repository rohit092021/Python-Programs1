a=input('enter 1st string')
print(sorted(a))
b=input('enter 2nd string')
print(sorted(b))
if sorted(a)==sorted(b):
    print('anagram')
else:
    print('Not anagram')