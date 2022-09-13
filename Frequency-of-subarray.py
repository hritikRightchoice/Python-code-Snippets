n = len(s) #s isthe given substring
dictt = {}
count = {}
fsub = {}
for i in range(n):
    elem = s[i]
    if elem in count:
        count[elem]+=1
    else:
        count[elem] = 1
    fsub[i] = copy.deepcopy(count)
# print(fsub)
for i in range(1,n+1):
    for j in range(0,n-i+1):
        if s[j:j+i-1] not in dictt:
            if j == 0:
                counti = {}
            else:
                counti = fsub[j-1]
            countj = fsub[j+i-1]
            res = {key1: countj[key1] - counti.get(key1, 0)
               for key1 in countj}
            dictt[s[j:j+i-1]] = res
