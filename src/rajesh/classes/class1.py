
class Student:
    name = ''
    dob = ''
    addess = ''

    def __init__(self,name='common',dob='common',address='common'):
        self.name = name
        self.dob = dob
        self.addess = address


    def getAge(self):
        return 'age'

    def __str__(self):
        return 'Name : ' + self.name + '\nDob : ' + str(self.dob)+'\nAddress :  '+self.addess



