# pydeutils

Python utilities for Processing.py (Python mode) sketches. 
## Use

1. Download this repository
2. Copy the pydeutils folder into a Processing.py sketch folder
3. At the sketch file, add:  
   `import pydeutils as pu`

## Why "pyde"?

Utilities for Processing `.pyde` files.

[Processing.py](py.processing.org) sketches use the `.pyde` file extension because they are written in Python -- hence ".py" -- but run in the PDE (Processing Development Environment) -- hence ".pde" -- combined, this is ".pyde".

Unlike the default [Processing](https://processing.org/) `.pde` sketches, which are Java, `.pyde` sketches run Python-on-Java via [Jython](http://www.jython.org/) platform in order to access the [Processing(Java) API](https://processing.org/reference/). Processing.py sketches run on Python 2.7 only, and may only use pure Python (no compiled / CPython) libraries due to the limitations of Jython.

## What's in it?

This is a barebones utilities library that I wrote while learning Processing.py -- it was a work in progress that I never finished. It currently contains some tricks to make certain things easier: primarily file handling and pickling.

After you install and then import it with `import pydeutils as pu`

### decorators -- add with @ above a function definition:

@pu.at_exit -- causes a function to be called just before a normal exit occurs -- such as calling exit(), or - closing the pyde sketch window.
@pu.disable -- Do nothing rather than execute the provided function.
@pu.enable -- Marked as not0-disabled (pass-through)
@pu.handle_file -- for a function which takes a file or a str as it's first argument, if a str is provided, replace the first argument of the wrapped function with a file handle, and close the file after the function returns.
@pu.print_args -- Print arguments passed to a function before calling it.

### functions:

pu.exists() -- shortcut for os.path.exists(), lets you check for a file or folder.
pu.loadPickle, pu.deletePickle, pu.savePickle -- enable you to serialize Python 2 objects to disk and then load them again. This makes it easy to run an arbitrarily complex sketch, save the whole state, and resume on load.
