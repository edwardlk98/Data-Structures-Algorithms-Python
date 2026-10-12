def isValid(s:str):
    if(len(s))%2 !=0:
        return False
    else:
        i = 0
        ls = []
        while i < len(s):
            if(s[i]=="(" or s[i]=="{" or s[i]=="["):
                ls.append(s[i])
            else:
                 if(len(ls)==0):
                    return False          
            if(s[i]==")"):
                lastBracket = ls.pop()
                print("lastBracket" + lastBracket)
                if(lastBracket!="("):
                    return False                 
            elif(s[i]=="}"):
                lastBracket = ls.pop()
                print("lastBracket" + lastBracket)
                if(lastBracket!="{"):
                    return False
            elif(s[i]=="]"):
                lastBracket = ls.pop()
                print("lastBracket" + lastBracket)
                if(lastBracket!="["):
                    return False                    
            i+=1
        print(len(ls))
        if(len(ls)==0):
            return True
        else:
            return False
    
            
s = "([])"
print(isValid(s))