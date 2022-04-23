import threading
import time
import sys

class SecondCounter(threading.Thread):
    '''
    create a thread object that will do the counting in the background
    default interval is 1/1 of a second
    '''