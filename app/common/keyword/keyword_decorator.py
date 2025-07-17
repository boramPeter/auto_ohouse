from functools import wraps
def custom_given(step_text):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            locator1 = kwargs.get('locator1')
            action1 = kwargs.get('action1')
            locator2 = kwargs.get('locator2')
            action2 = kwargs.get('action2')
            locator3 = kwargs.get('locator3')
            action3 = kwargs.get('action3')
            locator4 = kwargs.get('locator4')
            action4 = kwargs.get('action4')
            locator5 = kwargs.get('locator5')
            action5 = kwargs.get('action5')
            case_no = kwargs.get('case_no')

            return func(locator1, action1, locator2, action2, locator3, action3, locator4, action4, locator5, action5, case_no)
        return inner
    return wrapper
