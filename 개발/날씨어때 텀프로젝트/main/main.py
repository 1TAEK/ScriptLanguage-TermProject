from tkinter import*

class FragmentManager():
    pass

class Main():
    def __init__(self):
        self.__windowWidth = 400
        self.__windowHeight = 600
        self.__backgroundColor = '#%02x%02x%02x' % (224, 255, 255)

        # Init Window
        self.__window = Tk()
        self.__window.title("날씨어떄")
        self.__window.geometry("400x600+100+100")
        self.__window.resizable(False, False)
        self.__window.configure(bg=self.__backgroundColor)

        # Init Scroll
        scrollbar = Scrollbar(self.__window)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.__window)

        # Init Frame
        # Menu Frame 메뉴프레임
        self.menuFrame = Frame(self.__window, bg = self.__backgroundColor);
        # Main Frame 개황프레임
        # TimeToWeather Frame 시간별 날씨 프레임
        # DayToWeather Frame 일별 날씨 프레임
        # AirFresh Frame 공기청정지수 프레임

        # Pack Frame
        # Menu Frame
        menuButtonwidth = 6
        menuButtonheight = 1
        self.menuFrame.pack()
        Button(self.menuFrame, width = menuButtonwidth, height = menuButtonheight, command = self.search).grid(row=0, column = 0)
        Button(self.menuFrame,command = self.bookmark).grid(row=0, column = 1)
        Button(self.menuFrame,command = self.email).grid(row=0, column = 2)
        Button(self.menuFrame,command= self.home).grid(row=0, column = 4)
        Button(self.menuFrame, command = self.refresh).grid(row=0, column = 5)
        Button(self.menuFrame, command = self.location).grid(row=1, column = 2)

    def search(self):
        pass
    def bookmark(self):
        pass
    def email(self):
        pass
    def home(self):
        pass
    def refresh(self):
        pass
    def location(self):
        pass

    def main(self):
        self.__window.mainloop()


Main().main()





