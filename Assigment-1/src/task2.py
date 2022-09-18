import inspect
from task1 import decorator_1

class decorator_2(decorator_1):

    def __init__(self, func):
        super().__init__(func)
        

    def __call__(self, *args, **kwd_args):
        super().__call__(*args, **kwd_args)

        print(f"Name:\t{self.func.__name__}")
        print(f"Type:\t{type(self.func)}")
        print(f"Sign:\t{inspect.signature(self.func)}")
    
        # print(f"Args:\t{inspect.signature(self.func).bind(*args, **kwd_args).apply_defaults()}")
        print(f"Args:\t{self.__get_args()}")
        print(f"Doc:\t{self.func.__doc__}")
        print(f"Source:\t{''.join(inspect.getsourcelines(self.func)[0])}")

        print(f"Annotation:\t{self.func.__annotations__}")
        print(f"Output:\t")

        def __get_args(self):
            print(f"positional: {self.func.args}")