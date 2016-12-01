import sys,re
re_d = re.compile(r'((\d)\2*)')

def replace(match_obj):
    s = match_obj.group(1)
    return str(len(s)) + s[0]

s = sys.argv[1]
for i in range(50):
    s = re_d.sub(replace,s)
    print len(s)
print len(s)
