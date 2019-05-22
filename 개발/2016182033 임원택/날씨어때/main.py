from tkinter import*

from common import scrollLayout

from client import overview
from client import timeToWeather
from client import dayToWeather
from client import airFresh


class FragmentManager():
    pass

class Main():
    def __init__(self):
        self.mWindowWidth = 400
        self.mWindowHeight = 600
        self.mBackgroundColor = '#%02x%02x%02x' % (224, 255, 255)

        # Init Window
        self.mWindow = Tk()
        self.mWindow.title("날씨어떄")
        self.mWindow.geometry("400x600")
        self.mWindow.resizable(False, False)
        self.mWindow.configure(bg=self.mBackgroundColor)

        # Init Frame
        # Menu, Main Frame
        self.mMenuFrame = Frame(self.mWindow, bg = self.mBackgroundColor)
        self.mMenuFrame.pack()
        self.mScrollLayout = scrollLayout.ScrollLayout(self.mWindow, (0, 0, 400, 2400))
        self.mScrollLayout.pack()
        self.mMainFrame = Frame(self.mScrollLayout.canvas, bg=self.mBackgroundColor)

        # Fragment
        # Overview Frame 개황프레임
        self.mOverviewFrame = Frame(self.mMainFrame,bg=self.mBackgroundColor)
        self.mOverview = overview.Overview(self.mOverviewFrame)
        self.mOverviewFrame.pack(ipady = 10,fill=BOTH)
        # TimeToWeather Frame 시간별 날씨 프레임
        self.mTimeToWeatherFrame = Frame(self.mMainFrame,bg=self.mBackgroundColor)
        self.mTimeToWeather = timeToWeather.TimeToWeather(self.mTimeToWeatherFrame)
        self.mTimeToWeatherFrame.pack(ipady = 10,fill=BOTH)
        # DayToWeather Frame 일별 날씨 프레임
        self.mDayToWeatherFrame = Frame(self.mMainFrame,bg=self.mBackgroundColor)
        self.mDayToWeather = dayToWeather.DayToWeather(self.mDayToWeatherFrame)
        self.mDayToWeatherFrame.pack(ipady = 10,fill=BOTH)
        # AirFresh Frame 공기청정지수 프레임
        self.mAirFreshFrame = Frame(self.mMainFrame,bg=self.mBackgroundColor)
        self.mAirFresh = airFresh.AirFresh(self.mAirFreshFrame)
        self.mAirFreshFrame.pack(ipady = 10,fill=BOTH)

        # Button
        menuButtonwidth = 8
        Button(self.mMenuFrame,text = "검색",width = menuButtonwidth, command = self.search).grid(row=0, column=0,padx = 4, pady=4)
        Button(self.mMenuFrame,text = "즐겨찾기",width = menuButtonwidth, command = self.bookmark).grid(row=0, column=1,padx = 4, pady=4)
        Button(self.mMenuFrame,text = "E-Mail",width = menuButtonwidth, command = self.email).grid(row=0, column=2, padx = 4, pady=4)
        Button(self.mMenuFrame,text = "Home",width = menuButtonwidth, command= self.home).grid(row=0, column=3, padx = 4, pady=4)
        Button(self.mMenuFrame,text = "갱신",width = menuButtonwidth, command = self.refresh).grid(row=0, column=4,padx = 4, pady=4)
        Button(self.mMenuFrame,text = "지역",width = menuButtonwidth, command = self.location).grid(row=1, column=2, pady=10)

        # Add Frame
        self.mScrollLayout.addFrame(self.mMainFrame)

    def search(self):
        pass
    def bookmark(self):
        pass
    def email(self):
        pass
    def home(self):
        pass
    def refresh(self):
        self.mOverview.update()
    def location(self):
        pass

    def main(self):
        self.mWindow.mainloop()

Main().main()





