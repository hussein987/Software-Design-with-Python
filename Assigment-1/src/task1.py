import time
from contextlib import redirect_stdout
import io


def decorator_1(func):
    def call_counter(*args, **kwd_args):

        call_counter.calls += 1
        
        st = time.time()
        redirected_out = io.StringIO()
        with redirect_stdout(redirected_out):
            func(*args, **kwd_args)
        et = time.time()

        print(f"func call {call_counter.calls} executed in {et - st} sec")

    call_counter.calls = 0

    return call_counter
