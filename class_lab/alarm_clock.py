class AlarmClock:
    def __init__(self, current_time):
        self.current_time = current_time
        self.is_on = False
        self.alarm_time = ''

    def set_current_time(self, time):
        self.current_time = time
        print(f'The current time has been set to {self.current_time}')

    def set_alarm_time(self, time):
        self.alarm_time = time
        print(f'The alarm time has been set to {self.alarm_time}')

    def toggle_alarm_on_or_off(self):
        self.is_on = not self.is_on
        print(f'The alarm is {"ON" if self.is_on else "OFF"}')
