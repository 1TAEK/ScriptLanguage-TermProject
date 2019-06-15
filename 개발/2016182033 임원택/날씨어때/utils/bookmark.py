from tkinter import *
from tkinter import font
from tkinter import messagebox

from server.parseXMLs import parsed

import spam

class Bookmark:
    def __init__(self,bookmarkList):
        # Etc
        self.mBackgroundColor = '#%02x%02x%02x' % (224, 255, 255)
        self.mFontDate = font.Font(family = "08SeoulHangangL_0",size = 10)

        # Window
        self.mWindow = Tk()
        self.mWindow.title("날씨어떄")
        self.mWindow.geometry("280x230")
        self.mWindow.resizable(False, False)
        self.mWindow.configure(bg=self.mBackgroundColor)
        self.mWindowWidth = 280
        self.mWindowHeight = 230

        self.mScrollbar = Scrollbar(self.mWindow)
        self.mScrollbar.pack(sid=RIGHT, fill=Y)

        self.mListBox = Listbox(self.mWindow, selectmode = 'extended', yscrollcommand = self.mScrollbar.set)
        for i in range(len(bookmarkList)):
            self.mListBox.insert(i,bookmarkList[i])

        self.mListBox.pack(fill=BOTH, expand = TRUE)
        self.mScrollbar.config(command=self.mListBox.yview)

        # 선택버튼
        Button(self.mWindow,text="지역 선택 완료",command=self.pick).pack(fill=BOTH, expand = TRUE)


    def pick(self):
        if self.mListBox.get(self.mListBox.curselection()):
            parsed.update(self.mListBox.get(self.mListBox.curselection()))
        else:
            messagebox.showinfo("오류","지역을 선택해주세요.")


