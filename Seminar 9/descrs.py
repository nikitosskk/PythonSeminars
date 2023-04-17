class Descriptor:
    def __init__(self):
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        self._value = value


class MyClass1:
    x = Descriptor()


class MyClass2:
    y = Descriptor()


obj1 = MyClass1()
obj1.x = 10
print(obj1.x)  # 10
obj2 = MyClass2()
obj2.y = "Hello"
print(obj2.y)  # "Hello"
