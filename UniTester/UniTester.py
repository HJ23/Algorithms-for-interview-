import time


def timer(function):
   def run(*args,**kwargs):
      start=time.time()
      result=function(*args,**kwargs)
      print(f"Elapsed time : {time.time()-start} seconds")
      return result
   return run


def unitest(target=None):
   def compare(function):
      def run(*args,**kwargs):
         predicted=function(*args,**kwargs)
         return predicted==target
      return run
   return compare

