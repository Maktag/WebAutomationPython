from proj_exe.run_seq import test_list
from proj_modules_scripts import wcome_script
from proj_modules_scripts import cbox_script
from proj_setup import base_setup


test_modules = [base_setup.Base(),
                wcome_script.WelcomeScreen(),
                cbox_script.CheckboxScreen(),
                base_setup.Clear()
                ]


def start_execution():
    test_list(test_modules)


if __name__ == '__main__':
    start_execution()
