import sys
sys.path.append("..")
from BasicTester import BasicTester

def find(seq):
   ret=set()
   tmp=set()
   for x in range(len(seq)-9):
      tmp_seq=seq[x:x+10]
      if(tmp_seq in tmp):
         ret.add(tmp_seq)
      else:
         tmp.add(tmp_seq)
   
   return list(ret)


tester=BasicTester(find)
tester.test("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",["CCCCCAAAAA","AAAAACCCCC"])
tester.test("AAAAAAAAAAA",["AAAAAAAAAA"])
tester.test("AAAAAAAAAAAAA",["AAAAAAAAAA"])


