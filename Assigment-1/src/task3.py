import time
import inspect
from contextlib import redirect_stdout
import io


class call_count_decorator:

    execution_times = []

    def __init__(self, func):
        self.func = func
        self.arguments = []
        self.kwd_arguments = {}
        self.call_count = 0
        self.out_file = "/Users/husseinyounes/University/Python/Software-Design-with-Python/Assigment-1/data_files/output.txt"

    def __call__(self, *args, **kwd_args):
        self.call_count += 1
        self.arguments = args
        self.kwd_arguments = kwd_args
        st = time.time()
        self.redirected_out = io.StringIO()
        with redirect_stdout(self.redirected_out):
            self.res = self.func(*args, **kwd_args)
        et = time.time()
        exexution_time = et - st
        with open(self.out_file, 'a') as f:
            call_count_decorator.execution_times.append(
                (self.func.__name__, exexution_time))
            f.write(
                f"func call {self.call_count} executed in {exexution_time} sec\n")


class decorator_3(call_count_decorator):

    def __init__(self, func):
        super().__init__(func)

    def __call__(self, *args, **kwd_args):
        super().__call__(*args, **kwd_args)

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

        with open(self.out_file, 'a') as f:

            f.write(f"Name:    {self.func.__name__}\n")
            f.write(f"Type:    {type(self.func)}\n")
            f.write(f"Sign:    {inspect.signature(self.func)}\n")

            f.write(f"Args:    {get_args(*args, **kwd_args)}\n")
            f.write(f"Doc:    {format_mutli_lines(self.func.__doc__)}\n")
            f.write(
                f"Source: {format_mutli_lines(''.join(inspect.getsourcelines(self.func)[0]))}\n")

            res = str(self.res) if self.res is not None else ''
            f.write(
                f"Output: {format_mutli_lines(self.redirected_out.getvalue() + res)}\n")

            f.write(f"{'=' * 100}\n")

    @classmethod
    def rank_speed(cls):
        l = sorted(cls.execution_times, key=lambda x: x[1])
        sep = f"{' ' * 4} | {' ' * 4}"
        print(f"PROGRAM {sep} RANK {sep} TIME ELAPSED")
        for i in range(len(l)):
            val_1 = l[i][0]
            val_2 = i + 1
            val_3 = l[i][1]
            ind_1 = 20 - len(l[i][0])
            ind_2 = 10
            print(f"{val_1} {ind_1 * ' '} {val_2} {ind_2 * ' '} {val_3}")
