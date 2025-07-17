from datetime import datetime, timedelta

class TimeProvider:
    def get_today_mmdd(self):
        current_date = datetime.now()

        formatted_date = current_date.strftime("%m-%d")

        return formatted_date

    def get_current_time(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%H:%M")

        return formatted_time

    def sub_one_minute_to_current_time(self):
        current_time = datetime.now()
        new_time = current_time + timedelta(minutes=-1)
        formatted_time = new_time.strftime("%H:%M")

        return formatted_time
