class CustomMeta(type):
    pass

class CustomClass(metaclass = CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

inst = CustomClass()
inst.custom_x
inst.custom_val
inst.custom_line()

inst.x  # ошибка
inst.val  # ошибка
inst.line() # ошибка


class A: 
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

a = A()
a()