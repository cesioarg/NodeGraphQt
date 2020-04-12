import sys


def _abs(x):
    return abs(x)


def _all(iterable):
    return all(iterable)


def _any(iterable):
    return any(iterable)


def _ascii(object):
    return ascii(object)


def _bin(x):
    return bin(x)


def _bool(x):
    return bool(x)


def _breakpoint(*args, **kws):
    return breakpoint(*args, **kws)


def _bytearray(source, encoding, errors):
    return bytearray(source, encoding, errors)


def _bytes(source, encoding, errors):
    return bytes(source, encoding, errors)


def _callable(object):
    return callable(object)


def _chr(i):
    return chr(i)


def _classmethod():
    raise NotImplementedError


def _compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1):
    return compile(source, filename, mode, flags, dont_inherit, optimize)


def _complex(real, imag):
    return complex(real, imag)


def _delattr(object, name):
    return delattr(object, name)


def _dict(iterable, **kwarg):
    return dict(iterable, **kwarg)


def _dir(object):
    return dir(object)


def _divmod(a, b):
    return divmod(a, b)


def _enumerate(iterable, start=0):
    return enumerate(iterable, start)


def _eval(expression, globals=globals(), locals=locals()):
    return eval(expression, globals, locals)


def _exec(object, globals=globals(), locals=locals()):
    return exec(object, globals, locals)


def _filter(function, iterable):
    return filter(function, iterable)


def _float(x):
    return float(x)


def _format(value, format_spec=""):
    return format(value, format_spec)


def _frozenset(iterable=None):
    return frozenset(iterable)


def _getattr(object, name, default=None):
    return getattr(object, name, default)


def _globals():
    return globals()


def _hasattr(object, name):
    return hasattr(object, name)

    
def _hash(object):
    return hash(object)


def _help(object):
    return help(object)


def _hex(x):
    return hex(x)


def _id(object):
    return id(object)


def _input(prompt=''):
    return input(prompt)


def _int(x, base=10):
    return int(x, base)


def _isinstance(object, classinfo):
    return isinstance(object, classinfo)


def _issubclass(clss, classinfo):
    return issubclass(clss, classinfo)


def _iter(object):
    return iter(object)


def _len(s):
    return len(s)


def _list(iterable=[]):
    return list(iterable)


def _locals():
    return locals()


def _map(function, iterable):
    return map(function, iterable)


def _max(iterable):
    return max(iterable)


def _memoryview(obj):
    return memoryview(obj)


def _min(iterable):
    return min(iterable)


def _next(iterator, default=None):
    return next(iterator, default)


def _oct(x):
    return oct(x)


def _open(file, mode='r', buffering=-1, encoding=None,
          errors=None, newline=None, closefd=True, opener=None):
    return open(file, mode, buffering, encoding,
                errors, newline, closefd, opener)


def _ord(c):
    return ord(c)


def _pow(base, exp, mod=1):
    return pow(base, exp, mod)


def _print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    kwarg['sep'] = sep
    kwarg['end'] = end
    kwarg['file'] = file
    kwarg['flush'] = flush
    return print(*objects, **kwarg)


def _property(fget=None, fset=None, fdel=None, doc=None):
    return property(fget, fset, fdel, doc)


def _range(start, stop, step=1):
    return range(start, stop, step)


def _repr(object):
    return repr(object)


def _reversed(seq):
    return reversed(seq)


def _round(number, ndigits=0):
    return round(number, ndigits)


def _set(iterable):
    return set(iterable)


def _setattr(object, name, value):
    return setattr(object, name, value)


def _slice(start, stop, step=1):
    return slice(start, stop, step)


def _sorted(iterable):
    return sorted(iterable)


def _staticmethod():
    raise NotImplementedError


def _str(object=''):
    return str(object)


def _sum(iterable, start=0):
    return sum(iterable, start)


def _super():
    raise NotImplementedError

    
def _tuple(iterable):
    return tuple(iterable)


def _type(object):
    return type(object)


def _vars(object):
    return vars(object)


def _zip(*iterables):
    return zip(*iterables)


def _import(name, globals=None, locals=None, fromlist=(), level=0):
    return __import__(name, globals, locals, fromlist, level)
