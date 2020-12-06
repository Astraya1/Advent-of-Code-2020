def filterer(y):
    
    if y == '':
        return False
    else:
        return True
    
def Part1(x):
    
    lol = open(x).readlines()
    
    for i in range(len(lol)):
        lol[i] = lol[i].rstrip('\n')
        
    count = 0
    
    XD = ['']*len(lol)
    
    for i in lol:
        if i != '':
            XD[count] += i
        else:
            count += 1
            
    XD = list(filter(filterer, XD))
    
    count1 = 0
    
    for x in range(len(XD)):
        XD[x] = ''.join(set(XD[x]))
        count1 += len(XD[x])
    
    return XD, count1

def Part2(x):
    lol = open(x).readlines()
    
    for i in range(len(lol)):
        lol[i] = lol[i].rstrip('\n')
        
    count = 0
    count1 = 0
    XD = ['']*len(lol)
    
    lengths = []
    
    for i in lol:
        if i != '':
            XD[count] += i
            count1 += 1
        else:
            count += 1
            lengths.append(count1)
            count1 = 0
    lengths.append(count1)
            
    XD = list(filter(filterer, XD))
    
    count2 = 0
    
    for i in range(len(XD)):
        XD[i] = list(XD[i])
        my_dict = {k:XD[i].count(k) for k in XD[i]}
        for m in my_dict.values():
            if m == lengths[i]:
                count2 += 1
            
    return count2
    