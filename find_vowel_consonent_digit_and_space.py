st=("name is rohit 3 2 4")
vowel=0
consonent=0
digit=0
space=0
for i in st:
    if i in ('aeiou'):
        vowel+=1
print('vowel=',vowel)

for i in st:
    if i in ' ':
        space+=1
print('space=',space)

for i in st:
    if st[i]>=0 and st[i]<=9:
        digit+=1
print('numbers=',digit)

for i in st:
    if st[i]>='a ' and st[i]<='z':
        consonent+=1
print('consonent=',consonent)