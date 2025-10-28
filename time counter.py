
import time
t = int(input("Enter seconds: "))
while t:
    mins, secs = divmod(t, 60)

    print(f"{mins:02d}:{secs:02d}", end="\r")
    time.sleep(1)
    t -= 1
print("⏰ Time’s up!")
