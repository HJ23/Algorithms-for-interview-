
import sys
import time

class argumentPack():
    def __init__(self):
        pass

class TestFailedException(Exception):
    def __init__(self,message):
        self.message=message
    def show(self):
        print(self.message)

def timer(func):
   start=time.time()
   def run(inp):
      return func(inp)
   print(f"Execution time : {time.time()-start} sec.")
   return run


class BasicTester():
    function=None
    counter=0
    def __init__(self,func=None):
        self.function=func
    def test(self,packet,actualValue):
        if(self.function==None):
            print("*Test method argument error")
            sys.exit(0)
        else:
            @timer
            value=self.function(packet)
            self.counter+=1
            try:
                if(value==actualValue):
                    print("Test {a} Passed !  elapsed time : {b} sec".format(a=self.counter,b=(stop_t-start_t)))
                else:
                    raise TestFailedException("*Test Failed : Test number : "+str(self.counter)+ "\nActual Value : "+str(actualValue)+" Got : "+str(value))
            except TestFailedException as exp:
                exp.show()
