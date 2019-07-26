import sys
import datetime
from termcolor import colored, cprint


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
        print(colored('Platform -- Python' + str(sys.version_info[0]) + '.' + str(sys.version_info[1]), 'blue'))
        cprint('============================= Test Suit Starts ==============================', 'blue', 'on_grey')
        start_at = datetime.datetime.now()
        func(*args, **kwargs)
        end_at = datetime.datetime.now()
        cprint('===================== Test Suit Ended in '+time_def(start_at, end_at)+' ======================', 'blue', 'on_grey')
    return suit_log


def skip(flag):
    def test(func):
        def test_suit(*args, **kwargs):
            if flag:
                print(colored(' -> Skipped\n', 'yellow'))
            else:
                func(*args, **kwargs)
        return test_suit
    return test
