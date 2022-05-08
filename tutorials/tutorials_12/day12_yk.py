import time


def countdown(start_time, end_time):

    while start_time >= end_time:
        mins, secs = divmod(start_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        start_time -= 1

    print('Fire in the hole!!')


def countup(start_time, end_time):
    while start_time <= end_time:
        mins, secs = divmod(start_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        start_time += 1

    print('Fire in the hole!!')


def choice():
    scount = input("Enter 1 for CountUp Timer and Enter 2 for CountDown Timer: ")
    if scount == '1':
        start_time = int(input("Enter the start time in seconds: "))
        end_time = int(input("Enter the end time in seconds: "))
        countup(start_time, end_time)
    elif scount == '2':
        start_time = int(input("Enter the start time in seconds: "))
        end_time = int(input("Enter the end time in seconds: "))
        countdown(start_time, end_time)
    else:
        print("please enter 1 or 2 only")
        choice()


choice()