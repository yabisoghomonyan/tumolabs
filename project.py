import time
hour=int(input("enter the hour: "))
minute=int(input("enter the minute: "))
second=int(input("enter the second: "))
def timer(hour,minute,second):
    sec=hour*3600+minute*60+second
    while sec!=0:
        print(f"{hour:02d}:{minute:02d}:{second:02d}")
        time.sleep(1)
        sec-=1
        hour=sec//3600
        second=sec%60
        minute=(sec%3600)//60
    print(f"{hour:02d}:{minute:02d}:{second:02d}")

timer(hour,minute,second)