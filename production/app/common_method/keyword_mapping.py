from production.app.common_method.keywords import Keywords

class KeywordMapping:
    keyword_map = {
        'login': Keywords.email_login,
        'step':Keywords.navigate,
        'result':Keywords.verify,
        'skip':Keywords.scenario_skip,
        'restart': Keywords.restart_app

    }
    def execute_keyword(self, keyword, *args):
        KeywordMapping.keyword_map[keyword](self, *args)
