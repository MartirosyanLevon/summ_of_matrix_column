from random import randint

a = []

r = int(input('Enter line of column: '))
c = int(input('Enter line of row: '))

for i in range(c):
    b = []
    for j in range(r):
        b.append(randint(0,100))
        #b.append(int(input('Enter a numbre: '))) # so you can input numbre's
    a.append(b) 


for i in a:
    print(i)  

print()


for i in range(r):
    sum = 0
    for j in range(c):
        sum += a[j][i]
    print('sum of ',i + 1,'column = ',sum)    
