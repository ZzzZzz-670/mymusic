import math
nums = list(map(float, input().split()))
a = nums[0]
b = nums[1]
c = nums[2]
delta = b * b - 4 * a * c

#无解
if a==0 and b==0 and c!=0:
    print("4")
elif a==0 and b==0 and c==0:
    print("5") 
elif a==0:
    print("6")
    print(f"{(-c/b):.2f}")
elif(delta<0):
    print("3")
elif(delta==0):
    print("2")
    print(f"{(-b/(2*a)):.2f}")
elif(delta>0):
    print("1")
    x = math.sqrt(delta)
    print(f"{((-b-x)/(2*a)):.2f} {((-b+x)/(2*a)):.2f}")
    