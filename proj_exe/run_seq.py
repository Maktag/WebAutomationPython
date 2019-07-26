from proj_setup.generic_decorators import suit
from termcolor import colored


@suit
def test_list(test_modules):
    prefixes = '_'
    for test_mod in test_modules:
        list = test_mod.__dir__()
        for word in list[:]:
            if word.startswith(prefixes):
                list.remove(word)
        print(colored('\n---------- '+str(test_mod.__dir__).split(' ', 8)[4]+' ----------\n', 'blue'))
        for method in list:
            print(colored('==> Executing::', 'green'), method)
            getattr(test_mod, method)()  # call