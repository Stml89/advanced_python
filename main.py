class MetaClass(type):

    def __init__(cls, name, bases, class_dict):
        type.__init__(cls, name, bases, class_dict)
        accessors = {}
        prefixes = ["get_", "set_", "del_"]
        for k in class_dict.keys():
            for i in range(len(prefixes)):
                if k.startswith(prefixes[i]):
                    v = getattr(cls, k)
                    accessors.setdefault(k[4:], [None, None, None])[i] = v
        for name, (getter, setter, deler) in accessors.items():
            setattr(cls, name, property(getter, setter, deler, ""))


class MyClass(metaclass=MetaClass):
    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value


ex = MyClass()
ex.x = 255
print(ex.x)
ex.y = 100
print(ex.y)
