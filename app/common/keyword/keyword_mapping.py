from app.common.keyword.keywords import Keywords, HighLevelKeywords

class KeywordMapping:

    keyword_map = {
        'restart': HighLevelKeywords.app_restart,
        'login': HighLevelKeywords.email_login,
        'logout': HighLevelKeywords.email_logout,
        'search':HighLevelKeywords.search,
        'step':Keywords.navigate,
        'result':Keywords.verify,
        'skip':Keywords.scenario_skip
    }
    def execute_keyword(self, keyword, re_text=None, *args):
        KeywordMapping.keyword_map[keyword](self, *args, re_text=re_text)
