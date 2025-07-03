'''
p = input().split()
h = 0
for i in range(1,len(p)+1):#1-n
    total = 0
    for index_ in p:
        if int(index_) >= i:
            total += 1
    if total >= i :
        h = i

print(h)
'''

'''
计数排序法:h一定传进小于n
构建一个n长度的数组
引用为i的篇数为arr[i]
最后得到
'''
def hIndex(citations):
    n = len(citations)
    count = [0] * (n + 1)  # count[i]表示引用次数≥i的论文数
    for c in citations:
        if c >= n:
            count[n] += 1
        else:
            count[c] += 1
    total = 0
    for i in range(n, -1, -1):
        total += count[i]
        if total >= i:
            return i
    return 0

