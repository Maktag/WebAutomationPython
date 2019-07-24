import sys
import datetime


def time_def(start_time, end_time):
    """This will return difference of two date objects"""
    return str(end_time-start_time).split('.')[0]+' hours'


def singleton(cls):
    """This is a singleton class"""
    instance = [None]

    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]
    return wrapper


def suit(func):
    def suit_log(*args, **kwargs):
        print('Platform -- Python' + str(sys.version_info[0]) + '.' + str(sys.version_info[1]))
        print('============================= Test Suit Starts ==============================')
        start_at = datetime.datetime.now()
        func(*args, **kwargs)
        end_at = datetime.datetime.now()
        print('===================== Test Suit Ended in '+time_def(start_at, end_at)+' ======================')
    return suit_log
