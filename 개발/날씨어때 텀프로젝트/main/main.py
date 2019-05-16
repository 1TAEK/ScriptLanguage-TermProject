from tkinter import*
from overview import Overview

class FragmentManager():
    pass

class Main():
    def __init__(self, **kw):
        self.__windowWidth = 400
        self.__windowHeight = 600
        self.__backgroundColor = '#%02x%02x%02x' % (224, 255, 255)

        # Init Window
        self.__window = Tk()
        self.__window.title("날씨어떄")
        self.__window.geometry("400x600+100+100")
        self.__window.resizable(False, False)
        self.__window.configure(bg=self.__backgroundColor)

        # Whole Frame
        self.wholeFrame = Frame(self.__window,bg=self.__backgroundColor)
        self.wholeFrame.pack()

        # Init Frame
        # Menu, Main Frame
        self.menuFrame = Frame(self.wholeFrame,width = self.__windowWidth,height = self.__windowHeight*0.9, bg = self.__backgroundColor);
        self.menuFrame.pack()
        self.mainFrame = Frame(self.wholeFrame, bg = self.__backgroundColor);
        self.mainFrame.pack()
        self.scrollbar = Scrollbar(self.mainFrame)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Fragment
        # Overview Frame 개황프레임
        self.overviewFrame = Frame(self.mainFrame,width = self.__windowWidth,height = self.__windowHeight*0.4);
        self.overviewFrame.pack()
        self.overview = Overview(self.overviewFrame)


        # TimeToWeather Frame 시간별 날씨 프레임
        self.TimeToWeatherFrame = Frame(self.mainFrame,width = self.__windowWidth,height = self.__windowHeight*0.4, bg = "blue")
        self.TimeToWeatherFrame.pack()
        # DayToWeather Frame 일별 날씨 프레임
        self.DayToWeatherFrame = Frame(self.mainFrame,width = self.__windowWidth,height = self.__windowHeight*0.4, bg = "green")
        self.DayToWeatherFrame.pack()
        # AirFresh Frame 공기청정지수 프레임
        self.AirFreshFrame = Frame(self.mainFrame,width = self.__windowWidth,height = self.__windowHeight*0.4, bg = "yellow")
        self.AirFreshFrame.pack()

        # Button
        menuButtonwidth = 8
        menuButtonheight = 1
        Button(self.menuFrame,text = "검색",width = menuButtonwidth, height = menuButtonheight, command = self.search).grid(row=0, column=0,padx = 4, pady=4)
        Button(self.menuFrame,text = "즐겨찾기",width = menuButtonwidth, height = menuButtonheight, command = self.bookmark).grid(row=0, column=1,padx = 4, pady=4)
        Button(self.menuFrame,text = "E-Mail",width = menuButtonwidth, height = menuButtonheight, command = self.email).grid(row=0, column=2, padx = 4, pady=4)
        Button(self.menuFrame,text = "Home",width = menuButtonwidth, height = menuButtonheight, command= self.home).grid(row=0, column=3, padx = 4, pady=4)
        Button(self.menuFrame,text = "갱신",width = menuButtonwidth, height = menuButtonheight, command = self.refresh).grid(row=0, column=4,padx = 4, pady=4)
        Button(self.menuFrame,text = "지역",width = menuButtonwidth, height = menuButtonheight, command = self.location).grid(row=1, column=2, pady=10)

    def search(self):
        pass
    def bookmark(self):
        pass
    def email(self):
        pass
    def home(self):
        pass
    def refresh(self):
        self.overview.update()
    def location(self):
        pass

    def main(self):
        self.__window.mainloop()

Main().main()





