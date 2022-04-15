class StringUtility:
  #takes the string as an argument and assigns it to the variable string
  
    def __init__(self, string):
      
        self.s=string
      
#string representation of the object it returns the string 
      
    def __str__(self):
      
       return self.s
#returns the number of vowels in the strings, if there are more than 5 "many" is returned      
    def vowels(self):
        count=0
        j=['a','e','i','o','u','A','E','I','O','U']
      
        for i in self.s:
            if i in j:
                count +=1
        if count >= 5:
            return "many"
        else: return count
 #returns the first and last two characters of the string. If its less than two characters its empty
          
    def bothEnds(self):
        if len(self.s) <= 2: return "" 
        else:return self.s[0:2] + self.s[-2:]
#returns the string with the first character and is replaced with an asterisk
          
    def fixStart(self):
      
        if len(self.s) <= 1:
            return self.s
        else:
            return self.s[0]+ self.s[1:].replace(self.s[0],"*")
#returns the sum of the ASCII values of the characters in the string  
          
    def asciiSum(self):
        sum=0
        for i in self.s:
            sum += ord(i)
        return sum
      
    def cipher(self):
        newString=""
        for j in self.s:
            if j.isalpha():
                if j.islower():
                    if ord(j) + len(self.s)>122:
                        newString += chr(ord(j) + len(self.s)- 26)
                    else:
                        newString += chr(ord(j)+ len(self.s))
                else:
                    if ord(j) + len(self.s) > 90:
                        newString += chr(ord(j)+ len(self.s) - 26)
                    else:
                        newString += chr(ord(j) + len(self.s))
                        newString += chr(ord(j) + len(self.s))
            else:
                newString += j
        return newString 
              
                      
                  
                      