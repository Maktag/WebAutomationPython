from proj_setup.generic_decorators import suit


@suit
def test_list(test_modules):

    prefixes = '_'
    for test_mod in test_modules:
        list = test_mod.__dir__()
        for word in list[:]:
            if word.startswith(prefixes):
                list.remove(word)
        # print(list)
        for method in list:
            getattr(test_mod, method)()  # call
