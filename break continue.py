i=10
while(i<10):
    print(i)
i=i+1

for i in ("python"):
    print (i)

for i in [1,2,3,4,5]:
    print (i)

for i in range(20,25):
    print (i)

for i in range(30,50,2):
    print(i)
    
for i in range(0,21,2):
    print(i)

a=[1,2,3,4,5,6,7,8,9]
for i in a:
    if i%2==0:
        break
    print (i)

a=[1,2,3,4,5,6,7,8,9]
for i in a:
    if i%2==0:
        continue
    print(i)

a=[1,2,3,4,5,6,7,8,9]
for i in a:
    if(i==4):
        break
    print(i)

a=[1,2,3,4,5,6,7,8,9]
for i in a:
    if(i==4):
        continue
    print(i)

a=int(input("enter a value:"))
b=int(input("enter b value:"))
def add(i,j):
    c=i+j
    return c
print(add(a,b))

for i in "python":
    if (i=='t'):
        break
    print(i)

a="python"    
for i in "python":
    if (i==a[3]):
        break
    print(i)
