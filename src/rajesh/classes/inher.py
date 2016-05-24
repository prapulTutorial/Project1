
class SuperSuperClass():
    def funct1(self):
        print "super super funct1"

class SuperClass(SuperSuperClass):
    def funct2(self):
        print "super funct1"

class SubClass(SuperClass):
    # def funct1(self):
    #     print "sub funct1"
    def funct2(self):
        print "sub funct2"


s1 = SuperClass()
s1.funct1()
s2 = SubClass()
s2.funct1()
s2.funct2()


def funct2(self):
    print "super funct1"

funct2(s2)








