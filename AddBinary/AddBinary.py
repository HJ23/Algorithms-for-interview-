# Complexity O(max(m,n)) -> m,n are lenght of given strings

def sumBinary(a,b):
    sum=int(a)+int(b)
    result=""
    reminder=0
    while(sum!=0):
        temp=(sum%10+reminder)%2
        reminder=0
        if(temp==0 and (sum%10==2 or sum%10==1 )):
            result="0"+result
            reminder=1
        elif(temp==1 and (sum%10==2 )):
            result="1"+result 
            reminder=1
        elif(temp==1 ):
            result="1"+result 
        elif(temp==0):
            result="0"+result   
        sum=(sum-sum%10)/10
    result="1"+result if(reminder==1) else result  
    return result
#Tests
assert sumBinary("11","11")=="110"
assert sumBinary("1","11")=="100"
assert sumBinary("111","111")=="1110"
assert sumBinary("101","1")=="110"
assert sumBinary("101","101")=="1010"
assert sumBinary("11","00")=="11"