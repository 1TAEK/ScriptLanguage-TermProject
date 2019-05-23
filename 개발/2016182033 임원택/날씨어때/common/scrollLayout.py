from tkinter import*

class ScrollLayout():
    def __init__(self,window, scrollregion_, background_ = '#%02x%02x%02x' % (224, 255, 255)):
        self.window = window
        self.canvas = Canvas(window, scrollregion=scrollregion_, bg=background_)

        # Scroll
        self.scrollbar = Scrollbar(self.canvas, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)

    # SubFrame 추가
    def addFrame(self, frame):
        # window 위에 하나가 덮여쓰임
        self.canvas.create_window((200,10),width = 300,height = 300,window = frame, anchor = N)

    # 가로 스크롤 지정
    def horizonMode(self):
        self.scrollbar.pack(side=BOTTOM,fill=X)
        self.scrollbar.config(orient = HORIZONTAL, command = self.canvas.xview)
        self.canvas.config(xscrollcommand=self.scrollbar.set)
        pass

    def pack(self, fill_ = BOTH, expand_ = True):
        self.canvas.pack(fill=fill_, expand=expand_)





