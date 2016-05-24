from rajesh.classes.class1 import Student
import datetime


s1=Student('Sibison','20','address')
print dir(s1)
print '1-->  ',s1.__doc__
# print '2-->  ',s1.__init__()
s2= s1.__class__()
print type(s2)
print '3-->  ',s2
print '4-->  ',s1.__module__
print s1.__dict__