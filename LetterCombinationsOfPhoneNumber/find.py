import sys
sys.path.append("..")
from BasicTester import *

def find(digits):
   dict={ "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"   }
   queue=[("",0)]
   ret=[]

   while(len(queue)!=0):
      string,point=queue.pop(0)
      if(len(string)==len(digits)):
         ret.append(string)
      for x in digits[point:]:
         point+=1
         for y in dict[x]:
            tmp=string
            tmp+=y
            queue.append((tmp,point))
   return ret

tester=BasicTester(find)
tester.test("254",["ajg","ajh","aji","akg","akh","aki","alg","alh","ali","bjg","bjh","bji","bkg","bkh","bki","blg","blh","bli","cjg","cjh","cji","ckg","ckh","cki","clg","clh","cli"])
tester.test("2345",["adgj","adgk","adgl","adhj","adhk","adhl","adij","adik","adil","aegj","aegk","aegl","aehj","aehk","aehl","aeij","aeik","aeil","afgj","afgk","afgl","afhj","afhk","afhl","afij","afik","afil","bdgj","bdgk","bdgl","bdhj","bdhk","bdhl","bdij","bdik","bdil","begj","begk","begl","behj","behk","behl","beij","beik","beil","bfgj","bfgk","bfgl","bfhj","bfhk","bfhl","bfij","bfik","bfil","cdgj","cdgk","cdgl","cdhj","cdhk","cdhl","cdij","cdik","cdil","cegj","cegk","cegl","cehj","cehk","cehl","ceij","ceik","ceil","cfgj","cfgk","cfgl","cfhj","cfhk","cfhl","cfij","cfik","cfil"])
tester.test("3",["d","e","f"])
