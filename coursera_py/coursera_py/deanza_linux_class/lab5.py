# Gregory Tuayev-Deane 
# Description: Create a Clock class that allows the user to set new time values for hours, minutes, and seconds and check whether their inputs are valid.

class Clock:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def print_time(self):
        h = self.hours
        m = self.minutes
        s = self.seconds
        time_str=f"{h:02d}:{m:02d}:{s:02d}"
        print("The current time is: ", time_str)

    def change_time(self, h:int=0, m:int=0, s:int=0):
        try:
            self._validate_time(h=h, m=m, s=s)
            self.hours = h
            self.minutes = m
            self.seconds = s
            print("The time has been changed.")
        except ValueError as ValueErr:
            print(ValueErr)
        self.print_time()

    def _validate_time(self, h:int=0, m:int=0, s:int=0):
        if h>=24 or h<0:
            raise ValueError("Hours value must be integer between 0-23")
        if m>=60 or m<0:
            raise ValueError("Minutes value must be integer between 0-59")
        if s>=60 or s<0:
            raise ValueError("Seconds value must be integer between 0-59")
        
def main():
    myClock = Clock()
    print()
    myClock.print_time()
    myClock.change_time(h=9,m=43,s=59)
    print()
    #test hours exeption
    print()
    myClock.print_time()
    myClock.change_time(h=24,m=43,s=59)
    print()
    #test mins exception
    print()
    myClock.print_time()
    myClock.change_time(h=23,m=60,s=59)
    print()
    #test seconds exception
    print()
    myClock.print_time()
    myClock.change_time(h=23,m=59,s=60)
    print()


if __name__ == "__main__":
    main()