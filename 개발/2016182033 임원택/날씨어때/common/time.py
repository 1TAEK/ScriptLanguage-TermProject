from datetime import datetime

class Time:
    def __init__(self):
        self.mTimeNow = datetime.now()
        self.mTimeTotal = ""
        self.mTimeWeekDay = ""
        self.mTimeHour = ""
        self.mTimeMin = ""

        self.setWeekend()
        self.setHour()
        self.setDay()

    def getIntHour(self):
        return self.mTimeNow.hour

    # 오후 오전 표시
    def setHour(self):
        if self.mTimeNow.hour > 12:
            self.mTimeHour = "오후 " + str(self.mTimeNow.hour - 12)
        else:
            self.mTimeHour = "오전 " + str(self.mTimeNow.hour)
    def getHour(self):
        self.setHour()
        return self.mTimeHour

    def setWeekend(self):
        week = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
        self.mTimeWeekDay = week[self.mTimeNow.weekday()]
    def getWeekend(self):
        self.setWeekend()
        return self.mTimeWeekDay

    def setDay(self):
        self.setWeekend()
        self.setHour()
        self.mTimeTotal = str(self.mTimeNow.month)+"월 "+str(self.mTimeNow.day) + "일 " + self.mTimeWeekDay + " "+ self.mTimeHour+":"+ str(self.mTimeNow.minute)
    def getDay(self):
        self.setDay()
        return self.mTimeTotal
