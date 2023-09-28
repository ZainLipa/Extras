# Program of the Day: Simple Alarm Clock

import time

def set_alarm(hours, minutes):
    # Calculate the alarm time in seconds
    alarm_time = hours * 3600 + minutes * 60

    # Get the current time in seconds since epoch
    current_time = int(time.time())

    # Calculate the time remaining until the alarm
    time_remaining = alarm_time - current_time

    if time_remaining <= 0:
        print("Invalid alarm time. Please set a future time.")
    else:
        print(f"Alarm set for {hours:02}:{minutes:02}.")
        time.sleep(time_remaining)
        print("Time's up! Alarm activated.")

# Example usage: Set the alarm for 7:30 AM
set_alarm(7, 30)
