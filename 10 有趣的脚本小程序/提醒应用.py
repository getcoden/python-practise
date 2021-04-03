from win10toast import ToastNotifier
import time
toaster = ToastNotifier()
try:
    print("Title of reminder")
    header = input()
    print("Message of reminder")
    text = input()
    print("In how many minutes?")
    time_min = input()
    time_min=float(time_min)
except:
    header = input("Title of reminder\n")
    text = input("Message of remindar\n")
    time_min=float(input("In how many minutes?\n"))
time_min = time_min * 60
print("Setting up reminder..")
time.sleep(2)
print("all set!")
time.sleep(time_min)
toaster.show_toast(f"{header}",
f"{text}",
duration=10,
threaded=True)
while toaster.notification_active(): time.sleep(0.005) 