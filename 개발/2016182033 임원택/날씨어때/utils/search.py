from tkinter import *
from tkinter import font
from tkinter import messagebox

from server.parseXMLs import parsed

import spam

# 검색 즐겨찾기 c++연동

class Search:
    def __init__(self,locationData):
        # Etc
        self.mBackgroundColor = '#%02x%02x%02x' % (224, 255, 255)
        self.mFontDate = font.Font(family = "08SeoulHangangL_0",size = 10)

        # 지역데이터 트리 받아오기
        self.mLocationData = list(locationData)
        self.mLocationData.sort()
        self.mBookmarkList = []
        self.mBookmarkListIndex = 0

        # Window
        self.mWindow = Tk()
        self.mWindow.title("날씨어떄")
        self.mWindow.geometry("730x530")
        self.mWindow.resizable(False, False)
        self.mWindow.configure(bg=self.mBackgroundColor)
        self.mWindowWidth = 730
        self.mWindowHeight = 530

        # Frame
        self.mMainFrame = Frame(self.mWindow,bg=self.mBackgroundColor)
        self.mBookmarkFrame = Frame(self.mWindow,bg=self.mBackgroundColor)
        self.mListFrame = Frame(self.mWindow,bg=self.mBackgroundColor)
        self.mMainFrame.grid(row=0,column=0)
        self.mListFrame.grid(row=1,column=0)
        self.mBookmarkFrame.grid(row=1, column = 1)
        Button(self.mWindow,width = 20, text = "확인",command = self.finalConfirm).grid(row=2,column=1,pady=20)

        #즐겨찾기 라벨, 즐겨찾기 삭제버튼
        self.mSubFrame = Frame(self.mWindow,bg=self.mBackgroundColor)
        self.mSubFrame.grid(row=0,column=1)
        Button(self.mSubFrame,text="추가",command=self.addBookmark).grid(row=1,column=0,padx=5)
        Button(self.mSubFrame,text = "삭제",command=self.deleteBookmark).grid(row=1,column=1,padx=5)
        # 즐겨찾기 리스트
        self.mBookmarkBox = Listbox(self.mBookmarkFrame, width=25, height=25, selectmode = 'extended')
        self.mBookmarkBox.pack(fill=BOTH,expand=TRUE,padx=20)

        # 그리기(UI)
        # 검색 엔트리, 검색버튼, 즐겨찾기 버튼
        self.mSearchEntry = Entry(self.mMainFrame)
        self.mSearchButton = Button(self.mMainFrame,text="검색", command= self.searchKeyword)
        self.mSearchEntry.grid(row=0, column=0, padx = 20, pady = 20)
        self.mSearchButton.grid(row=0, column=1, padx=5, pady=20)

       # 스크롤
        self.mScrollbar = Scrollbar(self.mListFrame)
        self.mScrollbar.pack(sid=RIGHT, fill=Y)

        # 지역목록 리스트
        self.mListBox = Listbox(self.mListFrame,width = 70, height = 25, selectmode = 'extended', yscrollcommand = self.mScrollbar.set)
        for i in range(len(self.mLocationData)):
            self.mListBox.insert(i,self.mLocationData[i])

        self.mListBox.pack(fill=BOTH, expand = TRUE)
        self.mScrollbar.config(command=self.mListBox.yview)

    def searchKeyword(self):
        # list에서 데이터를 찾고 listbox를 갱신해준다.
        if self.mSearchEntry.get() in self.mLocationData:
            messagebox.showinfo("성공","지역을 찾았습니다!")
        else:
            messagebox.showinfo("오류","찾는 지역이 리스트에 없습니다.\n다시 입력해주세요.")

    def addBookmark(self):
        if self.mSearchEntry.get() in self.mLocationData:
            if self.mSearchEntry.get() in self.mBookmarkList:
                messagebox.showinfo("오류","이미 북마크에 존재합니다.")
                print("already in list")
            else:
                self.mBookmarkList.append(self.mSearchEntry.get())
                self.mBookmarkBox.insert(self.mBookmarkListIndex,self.mSearchEntry.get())
                self.mBookmarkListIndex +=1
                messagebox.showinfo("성공","북마크에 추가되었습니다.")
                print(self.mSearchEntry.get())
        else:
            messagebox.showinfo("오류","추가할 지역이 리스트에\n존재하지 않습니다.")
            print("Is not Exist")

    def deleteBookmark(self):
        if self.mBookmarkBox.get(self.mBookmarkBox.curselection()) in self.mBookmarkList:
            # 선택한 곳의 인덱스값을 찾고 삭제하라
            self.mBookmarkList.remove(self.mBookmarkBox.get(self.mBookmarkBox.curselection()))
            self.mBookmarkBox.delete(0,self.mBookmarkListIndex)
            self.mBookmarkListIndex = 0
            for i in range(len(self.mBookmarkList)):
                self.mBookmarkBox.insert(self.mBookmarkListIndex,self.mBookmarkList[i])
                self.mBookmarkListIndex+=1
            # print(self.mBookmarkList)

    def finalConfirm(self):
        if self.mSearchEntry.get() in self.mLocationData:
            parsed.update(self.mSearchEntry.get())
            messagebox.showinfo("성공","지역이 설정완료되었습니다.\n갱신버튼을 눌러주세요.")
        else:
            messagebox.showinfo("오류","찾는 지역이 리스트에 없습니다.\n다시 입력해주세요.")

    def getBookmark(self):
        return self.mBookmarkList
