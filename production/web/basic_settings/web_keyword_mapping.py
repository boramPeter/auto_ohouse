# from production.web.basic_settings.keywords import navigate
# from production.web.basic_settings.keywords import verify
from production.web.basic_settings.keywords import *

keyword_map = {
    'step': navigate,
    'result':verify
}

def execute_keyword(page, keyword, *args):
    keyword_map[keyword](page, *args)
