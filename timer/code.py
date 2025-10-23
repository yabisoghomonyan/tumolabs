import time
def for_input():
    while True:
        try:
            time_str = input("Enter time in h:m:s format: ")
            parts = time_str.split(':')
            if len(parts) != 3:
                raise ValueError("You must enter exactly 3 numbers separated by colons.")
            h, m, s = map(int, parts)
            if h < 0 or m < 0 or s < 0:
                raise ValueError("All parts must be positive numbers.")
            if m >= 60 or s >= 60:
                raise ValueError("Minutes and seconds must be less than 60.")
        except ValueError as e:
            print(f"Invalid input: {e}")
        else:
            break
    return h,m,s
def timer(h,m,s):
    hour=h
    minute=m
    second=s
    sec=hour*3600+minute*60+second
    while sec!=0:
        print(f"{hour:02d}:{minute:02d}:{second:02d}")
        time.sleep(1)
        sec-=1
        hour=sec//3600
        second=sec%60
        minute=(sec%3600)//60
    print(f"{hour:02d}:{minute:02d}:{second:02d}")
    print("Time is up")
h,m,s=for_input()
timer(h,m,s)
