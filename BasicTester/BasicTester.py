class BasicTester():
    function=None
    counter=0
    def __init__(self,func=None):
        self.function=func
    def test(self,query,actualValue):
        if(self.function==None):
            assert False,"Error : declare function first!"
        else:
            value=self.function(query)
            if(value==actualValue):
                self.counter+=1
                print("Test {} Passed !".format(self.counter))
            else:
                self.counter+=1
                assert False,"Problem in Test {} ::: Actual Value : {} Got : {} ".format(self.counter,actualValue,value)