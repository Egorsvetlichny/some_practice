def func_decorator(func):
    def wrapper(*args, **kwargs):
        print('do wome work before function')
        res = func(*args, **kwargs)
        print('do wome work after function')
        return res
    return wrapper

@func_decorator
def some_func(text, tag):
    s = f'text = {text}, tag = {tag}'
    return s


if __name__ == '__main__':
    # some_func = func_decorator(some_func) -- декоратор без синтаксического сахара @func_decorator
    print(some_func('Python forever!', '<h1>'))