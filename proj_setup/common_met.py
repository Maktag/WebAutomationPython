from proj_setup.base_setup import Base
import inspect


def click_on_web_element(css_selector):
    try:
        return Base().browser_inst().find_element_by_css_selector(css_selector).click()
    except Exception:
        raise Exception('Element is not appearing on the screen.')


def is_web_element_displayed(css_selector):
    try:
        return Base().browser_inst().find_element_by_css_selector(css_selector).is_displayed()
    except Exception:
        return False


def is_web_element_selected(css_selector):
    try:
        return Base().browser_inst().find_element_by_css_selector(css_selector).is_selected()
    except Exception:
        return False


def clear_text_of_web_element(css_selector):
    try:
        return Base().browser_inst().find_element_by_css_selector(css_selector).clear()
    except Exception:
        raise Exception('Element is not appearing on the screen.')


def is_web_element_enabled(css_selector):
    try:
        return Base().browser_inst().find_element_by_css_selector(css_selector).is_enabled()
    except Exception:
        raise Exception('Element is not appearing on the screen.')


def save_screen_shot(version, module_name, tc_id):
    Base().browser_inst().get_screenshot_as_file('../test_report/' + version + '/' + module_name.replace(' ', '')
                                               + '/' + tc_id + '.png')


def return_back():
    Base().browser_inst().back()


def test_case_id():
    return inspect.stack()[1][3]


def log_report():
    return Base().report_inst()
