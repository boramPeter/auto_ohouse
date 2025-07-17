import locale


class NumberFormatter:
    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')

    def add_commas_to_number(self, number):
        number = int(number)
        formatted_number = locale.format_string("%d", number, grouping=True)
        return formatted_number
