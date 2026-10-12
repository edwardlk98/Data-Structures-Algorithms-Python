def longestPalindrome(s:str):
    longPal = []

    if(len(s)==1):
        return s
    else:
        longest = ""
        for i in range(len(s)):           
            left = i
            right = i
            while(left >= 0 and right < len(s)):
                if(s[left]==s[right]):
                    left -= 1
                    right +=1
                    tempstr = s[left+1:right]                   
                else:
                    break
                if(len(tempstr)> len(longest)):
                    longest = tempstr  
            left = i
            right = i+1
            while(left >= 0 and right < len(s)):
                if(s[left]==s[right]):
                    left -= 1
                    right +=1
                    tempstr = s[left+1:right]                   
                else:
                    break
                if(len(tempstr)> len(longest)):
                    longest = tempstr  
        return longest
                        


print(longestPalindrome("aa"))
print(longestPalindrome("aba"))
print(longestPalindrome("abc"))
print(longestPalindrome("a"))
print(longestPalindrome("abba"))
