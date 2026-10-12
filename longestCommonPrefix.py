def longestCommonPrefix(strs: list[str]):

    #Traverse the list
    #Check each character at the begining
    #if begining char does not match no prefix
    #if matches add to longestPrefix
    if len(strs) ==1:
        return strs[0]
    else:
        longest = ""
        same = False 
        for index in range(len(strs[0])):
            for nextIndex in range(1, len(strs)):
                print("index is:", index, "nextindex is:", len(strs[nextIndex]))
                if(index < len(strs[nextIndex])):
                    if(strs[0][index]== strs[nextIndex][index]):
                        same = True
                    else:
                        same = False
                        break
                else:
                    same = False
                    break
            if same:
                longest += strs[0][index]
            else:
                same = False 
                break
        
    return longest

                    
    
str1 = ["flower","flow","flight"]
str2 = ["ab","a"]
print(longestCommonPrefix(str1))

