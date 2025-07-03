# 枚举
# 定义判断回文子串
def check(s):
    l = len(s)
    i = 0
    while i<l:
        if s[i]!=s[-i-1]:
            return False
        i+=1
    return True

# 枚举所有的子串
# 0<=i<len i<j<len 如果j-i>max (0) max = s[i:j+1]

s = input()
i = 0
max_ = ""
while i < len(s):
    j = i
    while j <len(s):
        tmp = s[i:j+1]
        if check(tmp) and len(tmp) >len(max_) :
            max_ = tmp
        j+=1
    i+=1
            
print(max_)