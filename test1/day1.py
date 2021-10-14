lst = set([i for i in range(1,10001)])
notSelf = set()
sum = 0

for i in lst:
    for j in str(i):
        sum += int(j)
    if sum+i in lst:
        notSelf.add(sum+i)
    sum = 0

for k in sorted(lst - notSelf):
    print(k)
