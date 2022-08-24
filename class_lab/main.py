from alarm_clock import AlarmClock


print('\nAlarm Clock Tasks')
clock = AlarmClock('9:00am')

print('Current time:', clock.current_time)
clock.set_current_time('11:00am')
clock.set_alarm_time('6:00am')
clock.toggle_alarm_on_or_off()


print('\nCustomer Shopping Cart Tasks')
