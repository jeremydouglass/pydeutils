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
