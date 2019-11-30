# Complexity  O(n) amortized

text="Red rum, sir, is MurdeR"

def isAlphaNumeric(s):
    return s.isalnum()
    
def run(text):
    i=0
    j=len(text)-1
    while(j>i):
        if((isAlphaNumeric(text[i]) and isAlphaNumeric(text[j]))):
            if((text[i].lower()==text[j].lower())):
                i+=1
                j-=1
            else:
                return False
        else:
            if(not isAlphaNumeric(text[i])):
                i+=1
            if(not isAlphaNumeric(text[j])):
                j-=1
    return True

print(run(text))


            
            
            


