from datetime import datetime
import functools
import time
import timeit


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        value = func(*args, **kwargs)
        return value

    return wrapper_do_twice


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"{func.__name__!r} nomli funksiyasi {run_time:.4f} sekundda tugadi.")
        return value

    return wrapper_timer


def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(i) for i in args]
        kwargs_repr = [f"{k} = {v!r})" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Murojaat qilinyapti {func.__name__!r} funksiyasiga parametrlar: {signature}")
        value = func(*args, **kwargs)
        return f"{func.__name__!r} qaytaryapti - {value}"

    return wrapper_debug


def slow_down(func):
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down


