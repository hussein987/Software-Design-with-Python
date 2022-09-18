import time

class decorator_1:

    def __init__(self, func):
      self.func = func
      self.arguments = []
      self.kwd_arguments = {}
      self.call_count = 0

    def __call__(self, *args, **kwd_args):
      self.call_count += 1
      self.arguments = args
      self.kwd_arguments = kwd_args
      st = time.time()
      self.func(*self.arguments, **self.kwd_arguments)
      et = time.time()
      print(f"func call {self.call_count} executed in {et - st} sec")



import time

class decorator_1:

    def __init__(self, func):
      self.func = func
      self.arguments = []
      self.kwd_arguments = {}
      self.call_count = 0

    def __call__(self, *args, **kwd_args):
      self.call_count += 1
      self.arguments = args
      self.kwd_arguments = kwd_args
      st = time.time()
      self.func(*self.arguments, **self.kwd_arguments)
      et = time.time()
      print(f"func call {self.call_count} executed in {et - st} sec")
