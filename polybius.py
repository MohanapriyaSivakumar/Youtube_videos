def polybius(text):
    lst = [['A','B','C','D','E'],['F','G','H','I','K'],['L', 'M', 'N', 'O', 'P'],['Q','R', 'S','T','U'],['V','W', 'X','Y', 'Z']]
    text=text.split()
    ans=[]
    for i in text:
        if i.isdigit():
            ans.append(digit_tostring(i,lst))
        else:
            ans.append(string_todigit(i,lst))
    print(' '.join(ans))

def digit_tostring(dig,lst):
    dig=[dig[i:i+2] for i in range(0,len(dig),2)]
    string=''
    for i in dig:
        y,x=int(i[0])-1,int(i[1])-1
        string+=lst[y][x].lower()
    return string

def string_todigit(string,lst):
    string=string.upper()
    digit=''
    for i in string:
        if i=='J':
            digit+='24'
        else:
            for x in range(len(lst)):
                if i in lst[x]:
                    digit+=str(x+1)+str(lst[x].index(i)+1)
    return digit

polybius("do or die")
            

    
    
    
