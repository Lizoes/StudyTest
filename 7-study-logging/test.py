# @Time    : 2021/10/13 22:37
# @Author  : Lizo
# @File    : test.py


class A:
    def __init__(self):
        print("A init")
        self.a = 1

    def fun(self):
        print("fun")

    def __new__(cls, *args, **kwargs):
        print("A new")


class B(A):
    def __init__(self):
        # super().__init__()
        print("B init")
        self.b = 2

    def __new__(cls, *args, **kwargs):
        print("B new")


if __name__ == '__main__':
    b = B()
    # print(b.a)
    b.fun()