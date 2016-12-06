#can't figure out how to properly feed md5 hasher in Haskell, so here goes python
import md5
#part one
input_str = "ffykfhsq"
index = 0
res_string = ""

def getMD5(input_str,index):  
    return md5.new(input_str+str(index)).hexdigest()

while(len(res_string)<8):
    if getMD5(input_str,index)[:5] == "0"*5: res_string += getMD5(input_str,index)[5]
    index+=1

index = 0
res_string2=list('-'*8)
while('-' in res_string2):
    cand = getMD5(input_str,index)
    try:
        if cand[:5] == "0"*5 and int(cand[5])<8 and res_string2[int(cand[5])] == '-':
            res_string2[int(cand[5])] = cand[6]
    except ValueError: pass
    index += 1
        
print res_string, "".join(res_string2)

