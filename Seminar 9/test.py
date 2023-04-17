class TypedMeta(type):
    def __call__(cls, *args, **kwargs):
        # логика создания нового объекта
        obj = super().__call__(*args, **kwargs)
        return obj


class MyClass(metaclass=TypedMeta):
    def method_1(self):
        pass

    def method_2(self):
        print("Небольшая проблема")


obj_1 = MyClass()
obj_2 = MyClass()
print(obj_1 is obj_2)  # False
