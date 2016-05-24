
class Student:
    """
    this is student class
    """

    name = ''
    dob = ''
    addess = ''

    def __init__(self,name='common',dob='common',address='common'):
        """"
        hi
        """
        self.name = name
        self.dob = dob
        self.addess = address

    def getAge(self):
        return 'age'

    def __str__(self):
        return 'Name : ' + self.name + '\nDob : ' + str(self.dob)+'\nAddress :  '+self.addess

    def __del__(self):
        print 'Hi'

s1=Student('Sibison','20','address')
print dir(s1)
print '1-->  ',s1.__doc__
# print '2-->  ',s1.__init__()
s2= s1.__class__()
print type(s2)
print '3-->  ',s2
print '4-->  ',s1.__module__
print s1.__dict__





def say():
    return 'hi'

k=say
print type(k)



k