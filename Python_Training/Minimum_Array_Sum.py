
l1=list(map(int,input().split()))
min = 0 
max = 0
sum = 0
for i in l1:
    if max<i:
        max=i
for i in l1:
    if i == max:
        continue
    else:
        if min<i:
            min=i
avg=(min+max)/2
print(avg)
for i in l1:
    if i>avg:
        sum=sum+i
    else:
          continue
print(sum)
  


