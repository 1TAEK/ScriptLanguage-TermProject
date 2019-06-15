from tkinter import*
from tkinter import messagebox
import spam

from common import scrollLayout

from client import overview
from client import timeToWeather
from client import dayToWeather
from client import airFresh

from utils import email
from utils import search
from utils import bookmark

from server.parseXMLs import parsed

from teller import tellerMain

class FragmentManager():
    pass

class Main():
    def __init__(self):
        self.mWindowWidth = 400
        self.mWindowHeight = 400
        self.mBackgroundColor = '#%02x%02x%02x' % (224, 255, 255)
        self.mSearch = None

        # Init Window
        self.mWindow = Tk()
        self.mWindow.title("날씨어떄")
        self.mWindow.geometry("400x400")
        self.mWindow.resizable(False, False)
        self.mWindow.configure(bg=self.mBackgroundColor)

        # Init Frame
        # Menu, Main Frame
        self.mMenuFrame = Frame(self.mWindow, bg = self.mBackgroundColor)
        self.mMenuFrame.pack(pady = 5)
        self.mMainFrame = Frame(self.mWindow, bg=self.mBackgroundColor)
        self.mMainFrame.pack()

        # Fragment
        # Overview Frame 개황프레임
        self.mOverviewFrame = Frame(self.mMainFrame,bg=self.mBackgroundColor)
        self.mOverview = overview.Overview(self.mOverviewFrame)
        self.mOverviewFrame.pack()
        # Fragment Button
        Button(self.mMainFrame,width = 12, height = 6,text="시간별 날씨", relief = "solid",bg = "yellow", command = self.TTW).pack(padx = 10,pady = 25, side = LEFT)
        Button(self.mMainFrame,width = 12, height = 6,text="일별 날씨", relief = "solid",bg = "yellow", command = self.DTW).pack(padx = 10,pady = 25,side=LEFT)
        Button(self.mMainFrame,width = 12, height = 6,text="공기청정지수", relief = "solid",bg = "yellow", command = self.AF).pack(padx = 10,pady = 25,side=LEFT)

        # Button
        menuButtonwidth = 8
        Button(self.mMenuFrame,text = "검색",width = menuButtonwidth, command = self.search).grid(row=0, column=0,padx = 4, pady=4)
        Button(self.mMenuFrame,text = "즐겨찾기",width = menuButtonwidth, command = self.bookmark).grid(row=0, column=1,padx = 4, pady=4)
        Button(self.mMenuFrame,text = "E-Mail",width = menuButtonwidth, command = self.email).grid(row=0, column=2, padx = 4, pady=4)
        Button(self.mMenuFrame,text = "Home",width = menuButtonwidth, command= self.home).grid(row=0, column=3, padx = 4, pady=4)
        Button(self.mMenuFrame,text = "갱신",width = menuButtonwidth, command = self.refresh).grid(row=0, column=4,padx = 4, pady=4)


        # Scroll 관련 주석
        # self.mScrollLayout = scrollLayout.ScrollLayout(self.mWindow, (0, 0, 400, 2400))
        # self.mScrollLayout.pack()
        # self.mScrollLayout.addFrame(self.mMainFrame)

        # telegram
        self.mTeller = tellerMain.Teller(self.mOverview)

    def TTW(self):
        # TimeToWeather Frame 시간별 날씨 프레임
        self.mTimeToWeather = timeToWeather.TimeToWeather()
    def DTW(self):
        # DayToWeather Frame 일별 날씨 프레임
        self.mDayToWeather = dayToWeather.DayToWeather()
    def AF(self):
        # AirFresh Frame 공기청정지수 프레임
        self.mAirFresh = airFresh.AirFresh()

    def search(self):
        self.mSearch = search.Search(parsed.areaObj.getAreaList())

    def bookmark(self):
        if self.mSearch:
            if self.mSearch.getBookmark():
                self.mBookmark = bookmark.Bookmark(self.mSearch.getBookmark())
            else:
                messagebox.showinfo("오류","저장된 북마크가 없습니다.")
        else:
            messagebox.showinfo("오류","저장된 북마크가 없습니다.")

    def email(self):
        email.Email(self.mOverview.sendInfo())
    def home(self):
        pass
    def refresh(self):
        self.mOverview.update()

    def main(self):
        self.mWindow.mainloop()

Main().main()





