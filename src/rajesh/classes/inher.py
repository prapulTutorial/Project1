class SuperClass():
    def funct(self):
        print "super funct"

    def funct2(self):
        print "super funct1"

class SubClass(SuperClass):
    def funct(self):
        print "super funct"
        print "sub funct"


    def funct1(self):
        print "sub funct1"
    def funct2(self):
        print "sub funct2"


s1 = SuperClass()
s1.funct()
s2 = SubClass()
s2.funct()







