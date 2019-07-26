from proj_setup.common_met import *
from proj_modules_elements.wcome_elements import *
from proj_setup.generic_decorators import *


class WelcomeScreen:

    def module_start(self):
        log_report().start_module('WelcomeModule')

    @skip(True)
    def tc_001(self):
        try:
            click_on_web_element(ar_ele)
            click_on_web_element(ad_ele)
            if is_web_element_displayed(del_ele):
                log_report().pass_test(test_case_id(), 'Working as expected', 'T')
            else:
                log_report().fail_test(test_case_id(), 'Working as expected', 'T')
        except Exception as ex:
            log_report().fail_test(test_case_id(), str(ex), 'T')

    def tc_002(self):
        try:
            click_on_web_element(ar_ele)
            click_on_web_element(ad_ele)
            if is_web_element_displayed(del_ele):
                log_report().pass_test(test_case_id(), 'Working as expected', 'T')
            else:
                log_report().fail_test(test_case_id(), 'Working as expected', 'T')
        except Exception as ex:
            log_report().fail_test(test_case_id(), str(ex), 'T')

    def module_end(self):
        return_back()
        log_report().end_module()
