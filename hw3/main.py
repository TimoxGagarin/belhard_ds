# tasks 3, 9
class Car:
    i = 0
    def __init__(self, brand, year):
        Car.i += 1
        self.brand = brand
        self.year = year

    @staticmethod
    def count() -> int:
        return Car.i


# task 13
class A:

    def __init__(self, a):
        self.a = a

    def foo1(self):
        print(f'foo1 {self.a}')

class B:
    def __init__(self, b):
        self.b = b

    def foo2(self):
        print(f'foo2 {self.b}')

class C(A, B):
    def __init__(self, a, b):
        A.__init__(self, a)
        B.__init__(self, b)

    def foo1(self):
        A.foo1(self)

    def foo2(self):
        B.foo2(self)


if __name__ == "__main__":
    car1 = Car("Porsche", 1942)
    print(Car.count())
    car2 = Car("Porsche", 1942)
    print(Car.count())
    car3 = Car("Porsche", 1942)
    print(Car.count())

    ac = A(1)
    bc = B(2)
    cc = C(3, 4)

    ac.foo1()
    bc.foo2()
    cc.foo1()
    cc.foo2()
