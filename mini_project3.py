import time  # Used to add delays (sleep) between reminders
from plyer import notification  # Used to send desktop notifications

def water_reminder(interval_minutes):
    # Convert minutes into seconds because time.sleep() works in seconds
    interval_seconds = interval_minutes * 60

    # Inform the user that the reminder has started
    print("Water Drinking Reminder Started")
    print(f"You will get a notification every {interval_minutes} minutes\n")

    # Infinite loop to keep sending reminders
    while True:
        # Wait for the specified interval
        time.sleep(interval_seconds)

        # Send a desktop notification
        notification.notify(
            title="Drink Water",  # Title of the notification
            message="Time to drink water and stay hydrated.",  # Notification message
            timeout=10  # Duration the notification stays on screen (in seconds)
        )

# Start the reminder with a 30-minute interval
water_reminder(5)