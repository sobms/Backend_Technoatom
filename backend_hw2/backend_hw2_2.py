class CustomMeta(type): 
    def __call__(cls):
        prefix = 'custom_'
        new_obj = super(CustomMeta, cls).__call__() #call new + init
        for attr in dir(new_obj):
            if not attr.startswith("__"):
                new_obj.__setattr__(prefix + attr, getattr(new_obj, attr))
                if attr in cls.__dict__: 
                    delattr(cls, attr)
                else:                    
                    delattr(new_obj, attr)
        return new_obj
    


class CustomClass(metaclass=CustomMeta):
    x = 50
    def __init__(self, val=99):
        self.val = val
    def line(self):
        return 100
if __name__ == '__main__':
    inst = CustomClass()
    print(inst.custom_line())
    print(inst.custom_x)
    print(inst.custom_val)