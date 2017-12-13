"""A collection of utility decorators.
"""

####################
## @handle_file
####################

class handle_file(object):
    """
    Wrap a function which takes a file or a str as it's first argument.
    If a str is provided, replace the first argument of the wrapped function
    with a file handle, and close the file afterwards.
    
    leemendelowitz.github.io/blog/decorating-python-file-functions.html
    
    Example:
    
    @wrap_file_function('w')
    def write_hi(f):
        f.write('hi!\n')
    
    # This will write to already open file handle.
    f = open('f1.txt', 'w')
    write_hi(f)
    f.close()
    
    # This opens f2.txt with mode 'w', writes, and closes the file.
    write_hi('f2.txt')
    """
    
    def __init__(self, *args):
        self.modes = args if args else ('r',)
    
    def __call__(self, func):
        
        def wrapped(*args, **kwargs):
            
            close = [] # Files that should be closed
            files = [] # File handles that should be passed to func
            num_files = len(self.modes)
            
            try:
                for i, mode in enumerate(self.modes):
                    fp = args[i]
                    if isinstance(fp, str):
                        fp = open(fp, mode)
                        close.append(fp)
                    files.append(fp)
                # Replace the files in args when calling func
                args = files + list(args[num_files:])
                # Make function call and return value
                return func(*args, **kwargs)
            finally:
                for fp in close:
                        fp.close()
        return wrapped

####################
## simple_decorator
####################

def simple_decorator(decorator):
    """Meta-decorate: make decorator functions well-behaved.
    Apply @simple_decorator to a decorator in order to
    preserve the function docstring and attributes of the
    functions that it decorates.
    
    The decorator must be simple: it must expect a function
    and return a function (no descriptors), and it must not
    modify function attributes or docstring.
    
    wiki.python.org/moin/PythonDecoratorLibrary
    #Creating_Well-Behaved_Decorators_.2F_.22Decorator_decorator.22
    """
    
    def new_decorator(f):
        g = decorator(f)
        g.__name__ = f.__name__
        g.__doc__ = f.__doc__
        g.__dict__.update(f.__dict__)
        return g
    
    # Make @simple_decorator itself a well-behaved decorator.
    new_decorator.__name__ = decorator.__name__
    new_decorator.__doc__ = decorator.__doc__
    new_decorator.__dict__.update(decorator.__dict__)
    return new_decorator

####################
## @disable / @enable
####################

@simple_decorator
def disable(func):
    """Do nothing rather than execute the provided function."""
    def empty_func(*args,**kargs):
        pass
    return empty_func

@simple_decorator
def enable(func):
    """Pass through with no changes."""
    return func

## Sample use:
#
#    GLOBAL_ENABLE_FLAG = True
#
#    state = enabled if GLOBAL_ENABLE_FLAG else disabled
#
#    @state
#    def special_function_foo():
#        print "function was enabled"
