import re
def ifre(s):
    pattern = r'^[a-zA-Z0-9_]+@([a-zA-Z]+\.[a-zA-Z]+)+$'
    return re.match(pattern,s)
    
s = input()
if ifre(s):
    print('True')
else:
    print('False')