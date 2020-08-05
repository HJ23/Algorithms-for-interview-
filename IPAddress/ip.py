import sys
sys.path.append("..")
from BasicTester import BasicTester


def validIP(IP: str) -> str:
   ip4=set(["1","2","4","3","5","6","7","8","9","0"])
   ip6=set(["1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F"])
   tmp=IP.split(".")
   if(len(tmp)==1):
      IP=IP.split(":")
      if(len(IP)!=8):
         return "Neither"
      for x in IP:
         if(len(x)>4 or x==""):
            return "Neither"
         for y in x:
            if(not str(y).upper() in ip6):
               return "Neither"
      return "IPv6"

   if(len(tmp)>1):
      IP=IP.split(".")
      if(len(IP)!=4):
         return "Neither"
      for x in IP:
         if(len(x)>3 or x==""):
            return "Neither"
         for y in x:
            if(not str(y) in ip4):
               return "Neither"
         if(int(x)>255 or (x[0]=="0" and len(x)!=1)):
            return "Neither"
      return "IPv4"

   return "Neither"


testme=BasicTester(validIP)
testme.test("192.0.0.1","IPv4")
testme.test("172.16.254.1","IPv4")
testme.test("172.16.254.01","Neither")
testme.test("256.256.256.256","Neither")
testme.test("2001:0db8:85a3:0:0:8A2E:0370:7334","IPv6")
