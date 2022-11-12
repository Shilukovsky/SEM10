import datetime
import time
from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        wraps docs
        :param args:
        :param kwargs:
        :return:
        """
        log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
        log_msg += f'функция: {func.__name__}\t'
        log_msg += f"параметры: {', '.join(map(str, args))}\t"
        res = func(*args, **kwargs)
        log_msg += f'результат: {res}\n'
        with open('log_file.log', 'a', encoding='utf-8') as fp:
            fp.write(log_msg)
        return res

    return wrapper


def log_func(log_lvl=0):
    def logger2(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
            if log_lvl >= 1:
                log_msg += f'функция: {func.__name__}\t'
                if log_lvl == 2:
                    log_msg += f"параметры: {', '.join(map(str, args))}\t"
            res = func(*args, **kwargs)
            log_msg += f'результат: {res}\n'
            with open('log_file.log', 'a', encoding='utf-8') as fp:
                fp.write(log_msg)
            return res

        return wrapper

    return logger2


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        res = func(*args, **kwargs)
        finish = time.time_ns()
        print(finish - start)
        return res

    return wrapper


def cacher(func):
    cach = {}

    @wraps(func)
    def wrapper(*args):
        key = args
        if key not in cach:
            cach[key] = func(*args)
        # print(cach)
        return cach[key]

    return wrapper


@timer
def cube(x, y, z):
    return x * y * z


@timer
@cacher
def seq(n):
    result = []
    for i in range(n):
        res = (1 + i) ** i
        result.append(res)
    return result


def main():
    seq(10)
