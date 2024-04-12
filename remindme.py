import time
from plyer import notification
print("Welcome to Remind Me")
def drink_water_reminder(interval, num_reminders):
    prompt = input("Enter your reminder (for eg. 'Drink Water'): ")
    for _ in range(num_reminders):
        notification.notify(
            title="Remind Me",
            message= prompt,
            app_icon=None,
            timeout=10
        )
        time.sleep(interval * 60)

def main():
    interval = int(input("Enter the interval between reminders (in minutes): "))
    num_reminders = int(input("Enter the number of reminders you want: "))
    drink_water_reminder(interval, num_reminders)

if __name__ == "__main__":
    main()

    
