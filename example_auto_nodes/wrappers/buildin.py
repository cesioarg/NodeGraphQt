import sys


def abs(x):
    return abs(x)


def all(iterable):
    return all(iterable)


def any(iterable):
    return any(iterable)


def ascii(object):
    return ascii(object)


def bin(x):
    return bin(x)


def bool(x):
    return bool(x)


def breakpoint(*args, **kws):
    return breakpoint(*args, **kws)


def bytearray(source, encoding, errors):
    return bytearray(source, encoding, errors)


def bytes(source, encoding, errors):
    return bytes(source, encoding, errors)


def callable(object):
    return callable(object)


def chr(i):
    return chr(i)


def classmethod():
    raise NotImplementedError


def compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1):
    return compile(source, filename, mode, flags, dont_inherit, optimize)


def complex(real, imag):
    return complex(real, imag)


def delattr(object, name):
    return delattr(object, name)


def dict(iterable, **kwarg):
    return dict(iterable, **kwarg)


def dir(object):
    return dir(object)


def divmod(a, b):
    return divmod(a, b)


def enumerate(iterable, start=0):
    return enumerate(iterable, start)


def eval(expression, globals=globals(), locals=locals()):
    return eval(expression, globals, locals)


def exec(object, globals=globals(), locals=locals()):
    return exec(object, globals, locals)


def filter(function, iterable):
    return filter(function, iterable)


def float(x):
    return float(x)


def format(value, format_spec=""):
    return format(value, format_spec)


def frozenset(iterable=None):
    return frozenset(iterable)


def getattr(object, name, default=None):
    return getattr(object, name, default)


def globals():
    return globals()


def hasattr(object, name):
    return hasattr(object, name)

    
def hash(object):
    return hash(object)


def help(object):
    return help(object)


def hex(x):
    return hex(x)


def id(object):
    return id(object)


def input(prompt=''):
    return input(prompt)


def int(x, base=10):
    return int(x, base)


def isinstance(object, classinfo):
    return isinstance(object, classinfo)


def issubclass(clss, classinfo):
    return issubclass(clss, classinfo)


def iter(object):
    return iter(object)


def len(s):
    return len(s)


def list(iterable=[]):
    return list(iterable)


def locals():
    return locals()


def map(function, iterable):
    return map(function, iterable)


def max(iterable):
    return max(iterable)


def memoryview(obj):
    return memoryview(obj)


def min(iterable):
    return min(iterable)


def next(iterator, default=None):
    return next(iterator, default)


def oct(x):
    return oct(x)


def open(file, mode='r', buffering=-1, encoding=None,
         errors=None, newline=None, closefd=True, opener=None):
    return open(file, mode, buffering, encoding,
                errors, newline, closefd, opener)


def ord(c):
    return ord(c)


def pow(base, exp, mod=1):
    return pow(base, exp, mod)


def print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    kwarg['sep'] = sep
    kwarg['end'] = end
    kwarg['file'] = file
    kwarg['flush'] = flush
    return print(*objects, **kwarg)


def property(fget=None, fset=None, fdel=None, doc=None):
    return property(fget, fset, fdel, doc)


def range(start, stop, step=1):
    return range(start, stop, step)


def repr(object):
    return repr(object)


def reversed(seq):
    return reversed(seq)


def round(number, ndigits=0):
    return round(number, ndigits)


def set(iterable):
    return set(iterable)


def setattr(object, name, value):
    return setattr(object, name, value)


def slice(start, stop, step=1):
    return slice(start, stop, step)


def sorted(iterable):
    return sorted(iterable)


def staticmethod():
    raise NotImplementedError


def str(object=''):
    return str(object)


def sum(iterable, start=0):
    return sum(iterable, start)


def super():
    raise NotImplementedError

    
def tuple(iterable):
    return tuple(iterable)


def type(object):
    return type(object)


def vars(object):
    return vars(object)


def zip(*iterables):
    return zip(*iterables)


def __import__(name, globals=None, locals=None, fromlist=(), level=0):
    return __import__(name, globals, locals, fromlist, level)
