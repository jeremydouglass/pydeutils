"""pydeutils test sketch"""

import pydeutils as pu

def setup():
    """Set up the sketch."""

    test_pickle()
    test_print_args()
    exit()

class Cucumber(object):
    """A simple class for an object to pickle (save data to disk)."""
    def __init__(self, txt):
        self.txt = txt

def test_pickle():
    """Save, load, and remove pickle data."""

    ## save
    obj = Cucumber("vinegar")
    pu.savePickle('obj.pickle', obj)
    ## load
    obj2 = pu.loadPickle('obj.pickle')
    print obj2.txt
    ## delete save file
    pu.deletePickle('obj.pickle')

def test_print_args():
    """Inspect function calls and objects for debugging."""

    @pu.print_args
    def wardback(one, two):
        """Prints two + one.
           The @pu.print_args decorator causes this function
           to print its name and arguments to the console.
           when called.
        """
        print '...backwards is:', two + one

    wardback('foo', 'bar')

@pu.at_exit
def final_thought():
    """Prints a final thought.
       The @pu.at_exit decorator causes this function
       to be called just before a normal exit occurs -- such as
       calling exit(), or closing the pyde sketch window.
    """
    print "Exiting: That's all, folks!"
