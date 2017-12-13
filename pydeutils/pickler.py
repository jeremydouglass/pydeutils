"""Simple pickling."""

import os
import pickle
from decorators import handle_file

@handle_file('r')
def loadPickle(fref):
    """Load pickle file to panelcode object."""
    try:
        return pickle.load(fref)
    except EnvironmentError as err:
        print(fref + ' not loaded.')
        print(err)
        raise

def deletePickle(fpath):
    """Remove pickle file from disk."""
    if(fpath.endswith('.pickle')):
        try:
            os.remove(fpath)
        except OSError as err:
            print(fpath + ' not removed.')
            print(err)

@handle_file('w')
def savePickle(fref, obj):
    """Save (serialize) panelcode object to a pickle file."""
    try:
        pickle.dump(obj, fref)
    except EnvironmentError as err:
        print(fref + ' not saved.')
        print(err)
        raise
