n,m = [int(x) for x in input().split()]
key_value = {}
for _ in range(n):
    k, v = input().split()
    key_value[k] = v
for _ in range(m):
    l = input().split()
    key = l[1]
    if l[0]=='Q':
        #if key_value[key]:
        #    print(key_value[key])
        #else:
        #    print('None')
        # 使用 get 方法简化查询逻辑
        print(key_value.get(key, 'None'))
    elif l[0]=='A':
        key_value[key]=l[2]
    elif l[0]=='D':
        if key in key_value:
            del key_value[key]
    
sorted_keys=sorted(key_value.keys())
for key in sorted_keys:
    print(f"{key} {key_value[key]}")
    
