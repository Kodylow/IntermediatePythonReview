# Decorators: function that takes another function as an argument, and extends the behavior of the function without modifying it. do_something extended with functionality of mydecorator. functions are first class citizens in python.

# Syntax for decorators
@mydecorator
def do_something():
    pass


import functools

def my_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@my_decorator
def print_name():
    print("Alex")

#print_name = my_decorator(print_name)
print_name()


@my_decorator
def add5(x):
    return x + 5

# res = add5(10)
# print(help(add5))
# print(add5.__name__)


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greet('Alex')


# Nested Decorators

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k,v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, *kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@my_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello('John Doe')



# Class Decorators, good for tracking state

class CountCalls:

    def __init__(self,func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.nu+} times')
        return self.func(*args, **kwargs)
        

cc = CountCalls(None)

@CountCalls
def say_hello():
    print('Hello')