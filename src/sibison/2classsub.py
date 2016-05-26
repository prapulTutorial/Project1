class First(object):
    def __init__(self):
        print "first"

class Second(object):
    def __init__(self):
        print "second"

class subclass(First, Second):
    def __init__(self):
        super(subclass, self).__init__()


s1=sup