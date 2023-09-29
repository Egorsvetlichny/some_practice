# example1
def func(name):
    def say_hi():
        print(f'Hi, {name}!')

    return say_hi


# example2
def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start

    return step


# example3
def strip_string(strip_chars = ' '):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


if __name__ == '__main__':
    f1 = func('John')
    f2 = func('Python')
    f1()
    f2()
    print()

    c1 = counter(10)
    c2 = counter()
    print(c1(), c2())
    print(c1(), c2())
    print(c1(), c2())
    print()

    string1 = strip_string()
    string2 = strip_string(" !.")
    print(string1('     .....hello python!.....'))
    print(string2('     .....hello python!.....'))