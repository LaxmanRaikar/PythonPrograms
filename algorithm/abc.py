class a:
    def a1(self):
        print("a")
class b(a):
    def b1(self):
        print("b")
class c(a,b):
    def c1(self):
        print("c")
class d(b,c):
    def d1(self):
        print("d")
v=d()
v.b1()