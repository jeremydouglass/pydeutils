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
