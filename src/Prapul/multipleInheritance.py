class SuperClassA:
    def draw(self):
        print "drawing from A"

class SuperClassB:
    def draw(self):
        print "drawing from B"

class ChildAB(SuperClassA,SuperClassB):
    def create(self):
        print "create"

class ChildBA(SuperClassB,SuperClassA):
    def create(self):
        print "create"

c1 = ChildAB ()

c1.draw()

c2 = ChildBA ()

c2.draw()