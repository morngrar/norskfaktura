
from gi.repository import GObject

def new(signal, widget):
    """Convenience wrapper around the GObject signal emitter"""
    GObject.signal_new(
        signal, 
        widget, 
        GObject.SIGNAL_RUN_LAST, 
        GObject.TYPE_PYOBJECT, 
        (GObject.TYPE_PYOBJECT,)
    )