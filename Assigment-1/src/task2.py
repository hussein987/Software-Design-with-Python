import time
import inspect
from contextlib import redirect_stdout
import io


def decorator_2(func):

    def format_mutli_lines(lines):
        non_empty_lines = [line.strip()
                           for line in lines.split('\n') if line.strip() != ""]
        redirected_out = io.StringIO()
        with redirect_stdout(redirected_out):
            print(non_empty_lines[0])
            for line in non_empty_lines[1:]:
                print(f"\t{line}")
        return redirected_out.getvalue()

    def get_args(*args, **kwd_args):
        redirected_out = io.StringIO()
        with redirect_stdout(redirected_out):
            print(f"positional {args}")
            print(f"\t key=worded {kwd_args}")
        return redirected_out.getvalue()

    def call_counter(*args, **kwd_args):
        call_counter.calls += 1

        st = time.time()
        redirected_out = io.StringIO()
        with redirect_stdout(redirected_out):
            res = func(*args, **kwd_args)
        et = time.time()

        print(f"{func.__name__} call {call_counter.calls} executed in {et - st} sec")

        print("Name:   ", func.__name__)
        print("Type:   ", type(func))
        print("Sign:   ", inspect.signature(func))

        print("Args:   ", get_args(*args, **kwd_args))
        print("Doc:   ", format_mutli_lines(func.__doc__))
        print("Source:", format_mutli_lines(
            "".join(inspect.getsourcelines(func)[0])))

        res = str(res) if res is not None else ''
        print("Output:", format_mutli_lines(redirected_out.getvalue() + res))

        print(f"{'=' * 50}\n")

    call_counter.calls = 0
    return call_counter
