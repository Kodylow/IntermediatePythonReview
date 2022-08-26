# Errors and Exceptions
a = -5
if a > 0:
    raise Exception('x should be negative')

assert(a>=0), 'x is not positive'

try:
    a = 5/1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
# else is run if no exception occurred
else:
    print('everything is fine')
# finally does clean up operations
finally:
    print('cleaning up')


# Defining your own errors
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = messageself.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)

