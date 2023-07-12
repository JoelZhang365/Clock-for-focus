import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        time_left = end_time - time.time()
        print(f"\rTime left: {int(time_left)} seconds", end="")
        time.sleep(1)
    print("\nTime's up! Take a break.")

focus_timer(25*60) # 25 minutes
