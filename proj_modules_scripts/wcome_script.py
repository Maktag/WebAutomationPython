from proj_setup.common_met import *
from proj_modules_elements.wcome_elements import *


class WelcomeScreen:

    def start_module(self):
        log_report().start_module('WelcomeModule')

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

    def end_module(self):
        return_back()
        log_report().end_module()
