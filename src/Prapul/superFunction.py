class Parent:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class Child(Parent,object):

    def __init__(self, a, b, c, d, e):
        super(Child, self).__init__(a, b, c)

        self.d = d
        self.e = e

c1 = Child(1, 2, 3, 4, 5)

print c1.a, " ", c1.b, " ", c1.c, " ", c1.d, " ", c1.e

