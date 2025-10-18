import time
def for_input():
    while True:
        try:
            time_str = input("Enter time in h:m:s format: ")
            h, m, s = map(int, time_str.split(':'))
            print(f"Hours: {h}, Minutes: {m}, Seconds: {s}")
            if h < 0 or m < 0 or s < 0:
                raise  ValueError
        except ValueError:
            print("Invalid input: all parts must be numbers.")
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
