class clockTime:
    def __init__(self):
        self.hrs = 0
        self.mins = 0
        self.sec = 0
    
    def setHours(self, hrs):
        self.hrs = hrs
    
    def setMinutes(self, mins):
        self.mins = mins
    
    def setSec(self, sec):
        self.sec = sec
    
    def setTime(self, hrs, mins, sec):
        self.setHours(hrs)
        self.setMinutes(mins)
        self.setSec(sec)
    
    def showTime(self):
        clocktime = str(self.hrs + ":" + self.mins + ":" + self.sec)
        return clocktime

ct = clockTime()
x = input("Hours:" )
ct.setHours(x)
y = input("Minutes:" )
ct.setMinutes(y)
z = input("Seconds:" )
ct.setSec(z)

print("The time now is " + ct.showTime())
