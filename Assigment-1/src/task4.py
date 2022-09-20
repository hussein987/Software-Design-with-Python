from task2 import decorator_2
from task3 import decorator_3
from datetime import datetime
import traceback
from contextlib import redirect_stdout
import time
import io
import inspect


class decorator_4(decorator_3):

    def __call__(self, *args, **kwd_args):
        try:
            super().__call__(*args, **kwd_args)
        except Exception:
            dt = datetime.now()
            ts = datetime.timestamp(dt)
            with open("/Users/husseinyounes/University/Python/Software-Design-with-Python/Assigment-1/data_files/error.log", "a") as logf:
                logf.write(f"TimeStamp: {ts}\n")
                logf.write(traceback.format_exc())
                logf.write(f"{'=' * 100}\n")


def decorator_5(func):

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

        redirected_out = io.StringIO()
        st = time.time()
        with redirect_stdout(redirected_out):
            try:
                res = func(*args, **kwd_args)
            except Exception:
                dt = datetime.now()
                ts = datetime.timestamp(dt)
                with open("/Users/husseinyounes/University/Python/Software-Design-with-Python/Assigment-1/data_files/error.log", "a") as logf:
                    logf.write(f"TimeStamp: {ts}\n")
                    logf.write(traceback.format_exc())
                    logf.write(f"{'=' * 100}\n")
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
