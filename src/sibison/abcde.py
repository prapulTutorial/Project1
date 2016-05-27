class A(object):
    def __init__(self, a, b, c):
        self.A=a
        self.B=b
        self.C=c
        class B(A,object):
            def __init__(self, a, b, c, d, e):
                super(B,self).__init__(a, b, c)
                self.D=d
                self.E=e
f=B(1,2,3,4,5)
