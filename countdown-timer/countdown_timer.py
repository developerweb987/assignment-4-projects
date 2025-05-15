import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("⏰ Time's up!")

def main():
    print("🕒 Countdown Timer")
    try:
        total_time = int(input("Enter the time in seconds: "))
        countdown_timer(total_time)
    except ValueError:
        print("Please enter a valid number.")

# Run the timer
if __name__ == "__main__":
    main()
