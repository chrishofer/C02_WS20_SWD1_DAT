class A:
    def m(self):
        print("m von A")


class B(A):
    def m(self):
        print("m von B")
        #A.m(self)
        super().m()


class C(A):
    def m(self):
        print("m von C")
        #A.m(self)
        super().m()


class D(B, C):
    def m(self):
        print("m von D")
        super().m()
        #B.m(self)
        #C.m(self)


if __name__ == '__main__':
    obj = D()
    obj.m()