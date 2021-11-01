class CustomMeta(type):
    def __new__(cls, clsname, bases, namespace):
        prefix = 'custom_'
        custom_attr = {}
        for name, val in namespace.items():
            if not name[:2] == '__':
                custom_attr[prefix + name] = val
            else:
                custom_attr[name] = val
        return super(CustomMeta, cls).__new__(cls, clsname, bases, custom_attr)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100
inst = CustomClass()
inst.custom_line()
inst.custom_x