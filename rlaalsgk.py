
"""

for i in range(100):
    if (i%10)/3==1or (i%10)/3==2or(i%10)/3==3:
        print("*")
    else:
        print(i)
"""

'''

for i in range(100):
    condition = (i % 10) % 3 == 0 and (i%10)//3 != 0
    condition2 = (i // 10) % 3 == 0 and (i//10)//3 != 0
    if condition:
        if condition2:
            print("**")
        else:
            print("*")
    elif condition2:
        if condition:
            print("**")
        else:
            print("*")
    else:
        print(i)
'''

'''

for i in range(10):

    if i==5:
        continue
    print(i)
'''

"""
for a in range(2,10):
    for i in range(1,10):
        print("{}*{}={}".format(a,i,(a*i)))
"""
a = int(input())

flag= 0 # 0 is prime, 1 is not prime


for i in range(2, a):
    if a % i == 0:
        flag=1
        break

if flag==0:
    print("prime")
else:
    print("not prime")










