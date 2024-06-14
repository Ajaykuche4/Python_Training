# str=input()
# count=0
# c=0
# for i in str:
#     if i == 'H' or 'h':
#         count=count+2
#         if count==6:
#             print('Game end')
#     elif i=='T' or 't':
#         count=count-1
#         c=c+1
#         if c == 3:
#             print('Game end')
#             exit(0)
# print(count)
s=input()
hc=0
tc=0
score=0
for i in s:
    if i == 'H' or 'h':
        tc=0
        hc +=1
        score +=2
        if hc==3:
            break
    else:
        hc=0
        tc += 1
        score -= 1
        if tc == 3 :
            break
print(score)