dp =[True]*(R+1)
dp[0] = False
dp[1] = False

for i in range(2,R+1):
    for j in range(2*i,R+1,i):
        dp[j] = False
nop = 0
for i in range(L,R+1):
    if dp[i]:
        nop+=1
