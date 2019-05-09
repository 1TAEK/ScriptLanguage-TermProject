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
        text = Text(self.__window, width=40, height=10, wrap=WORD, yscrollcommand=scrollbar.set)
        text.pack()
        scrollbar.config(command=text.yview)

    def main(self):
        self.__window.mainloop()


Main().main()





