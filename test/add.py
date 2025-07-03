n = int(input())
# nums = int(input().split())
nums = list(map(int, input().split()))
# 
target = int(input())
for i in range(n):
    for j in range(n):
        if ((nums[i]+nums[j]) == target) and i < j:
            print(i,j)