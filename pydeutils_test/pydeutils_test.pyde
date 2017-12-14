"""pydeutils test sketch"""

import pydeutils as pu

def setup():
    """Set up the sketch."""

    test_pickle()
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
