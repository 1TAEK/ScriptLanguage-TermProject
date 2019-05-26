from tkinter import*
from overview import Overview

class FragmentManager():
    pass

class Main():
    def __init__(self):
        self.__mWindowWidth = 400
        self.__mWindowHeight = 600
        self.__mBackgroundColor = '#%02x%02x%02x' % (224, 255, 255)

        # Init Window
        self.__mWindow = Tk()
        self.__mWindow.title("날씨어떄")
        self.__mWindow.geometry("400x600+100+100")
        self.__mWindow.resizable(False, False)
        self.__mWindow.configure(bg=self.__mBackgroundColor)

        # Whole Frame
        self.mWholeFrame = Frame(self.__mWindow,bg=self.__mBackgroundColor)
        self.mWholeFrame.pack()

        # Init Frame
        # Menu, Main Frame
        self.mMenuFrame = Frame(self.mWholeFrame,width = self.__mWindowWidth,height = self.__mWindowHeight*0.9, bg = self.__mBackgroundColor);
        self.mMenuFrame.pack()
        self.mMainFrame = Frame(self.mWholeFrame, bg = self.__mBackgroundColor);
        self.mMainFrame.pack()
        self.mScrollbar = Scrollbar(self.mMainFrame)
        self.mScrollbar.pack(side=RIGHT, fill=Y)

        # Fragment
        frameRate = 0.4
        # Overview Frame 개황프레임
        self.mOverviewFrame = Frame(self.mMainFrame,width = self.__mWindowWidth,height = self.__mWindowHeight*frameRate);
        self.mOverviewFrame.pack()
        self.mOverview = Overview(self.mOverviewFrame)

        # TimeToWeather Frame 시간별 날씨 프레임
        self.mTimeToWeatherFrame = Frame(self.mMainFrame,width = self.__mWindowWidth,height = self.__mWindowHeight*frameRate, bg = "blue")
        self.mTimeToWeatherFrame.pack()
        # DayToWeather Frame 일별 날씨 프레임
        self.mDayToWeatherFrame = Frame(self.mMainFrame,width = self.__mWindowWidth,height = self.__mWindowHeight*frameRate, bg = "green")
        self.mDayToWeatherFrame.pack()
        # AirFresh Frame 공기청정지수 프레임
        self.mAirFreshFrame = Frame(self.mMainFrame,width = self.__mWindowWidth,height = self.__mWindowHeight*frameRate, bg = "yellow")
        self.mAirFreshFrame.pack()

        # Button
        menuButtonwidth = 8
        menuButtonheight = 1
        Button(self.mMenuFrame,text = "검색",width = menuButtonwidth, height = menuButtonheight, command = self.search).grid(row=0, column=0,padx = 4, pady=4)
        Button(self.mMenuFrame,text = "즐겨찾기",width = menuButtonwidth, height = menuButtonheight, command = self.bookmark).grid(row=0, column=1,padx = 4, pady=4)
        Button(self.mMenuFrame,text = "E-Mail",width = menuButtonwidth, height = menuButtonheight, command = self.email).grid(row=0, column=2, padx = 4, pady=4)
        Button(self.mMenuFrame,text = "Home",width = menuButtonwidth, height = menuButtonheight, command= self.home).grid(row=0, column=3, padx = 4, pady=4)
        Button(self.mMenuFrame,text = "갱신",width = menuButtonwidth, height = menuButtonheight, command = self.refresh).grid(row=0, column=4,padx = 4, pady=4)
        Button(self.mMenuFrame,text = "지역",width = menuButtonwidth, height = menuButtonheight, command = self.location).grid(row=1, column=2, pady=10)

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
        self.__mWindow.mainloop()

Main().main()





