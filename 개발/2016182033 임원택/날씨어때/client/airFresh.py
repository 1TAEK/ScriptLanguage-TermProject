from tkinter import *
from tkinter import ttk

from server import forecastAirPollution

class AirFresh:
    def drawLocationName(self,labelList,frame,param, count):
        # 마지막 리스트는 5개이기때문에 outofrange 오류발생
        for i in range(count):
            labelList.append(Label(frame, text = param[i],bg= self.mBackgroundColor, font=self.mFontDate))
            labelList[i].grid(row =0, column = i, padx = 35,pady=20)

    def drawHistogram(self,params,canvas,count):
        maxAP = int(max(params))
        minAP = int(min(params))

        # 그려주기 사이간격은 12
        barW = (self.mWindowWidth-24)/6
        barH = 350
        for i in range(count):
            if int(params[i]) == maxAP:
                canvas.create_rectangle(i*barW+40,barH-(barH -50)*int(params[i])/maxAP,
                                          i*barW+60,barH,tag="picture",fill="red")
            elif int(params[i]) == minAP:
                canvas.create_rectangle(i*barW+40,barH-(barH -50)*int(params[i])/maxAP,
                                          i*barW+60,barH,tag="picture",fill="blue")
            else:
                canvas.create_rectangle(i*barW+40,barH-(barH -50)*int(params[i])/maxAP,
                                          i*barW+60,barH,tag="picture")

            canvas.create_text(i*barW+40+10,barH-(barH -50)*int(params[i])/maxAP -15,text=str(params[i]))

    def inputData(self):
        dicData = self.mParamData.getAPData()
        # 6 6 5
        for i in range(0,6):
            self.mParamDataA.append(dicData[i])
        for i in range(6,12):
            self.mParamDataB.append(dicData[i])
        for i in range(12,17):
            self.mParamDataC.append(dicData[i])


    def __init__(self):
        # Etc
        self.mBackgroundColor = '#%02x%02x%02x' % (224, 255, 255)
        self.mFontDate = font.Font(family = "HoonWhitecatR",size = 7)

        # Window Scroll
        self.mWindow = Tk()
        self.mWindow.title("날씨어떄")
        self.mWindow.geometry("730x530")
        self.mWindow.resizable(False, False)
        self.mWindow.configure(bg=self.mBackgroundColor)
        self.mWindowWidth = 730
        self.mWindowHeight = 530

        # 지역별로 미세먼지, 지역 17개
        self.mParamData = forecastAirPollution.FcstAirPollution()
        self.mParamLocationA = ['서울','부산','대구','인천','광주','대전']
        self.mParamLocationB = ['울산','경기도','강원','충북','충남','전북']
        self.mParamLocationC = ['전남','경북','경남','제주','세종']
        self.mParamDataA = []
        self.mParamDataB = []
        self.mParamDataC = []
        self.mParamAirPolution = self.mParamData.getAPData()

        # InputData
        self.inputData()

        # Notebook
        self.mNotebook = ttk.Notebook(self.mWindow,width = self.mWindowWidth, height = self.mWindowHeight)
        self.mNotebook.pack()

        # LocationA
        self.mFrameA = Frame(self.mWindow, bg=self.mBackgroundColor)
        self.mFrameTextA = Frame(self.mFrameA,bg=self.mBackgroundColor)
        self.mFrameTextA.pack()
        self.mCanvasA = Canvas(self.mFrameA,bg=self.mBackgroundColor)
        self.mCanvasA.pack(fill=BOTH, expand=TRUE)
        # Set Param
        self.mTxtLocationA = []
        self.drawLocationName(self.mTxtLocationA,self.mFrameTextA,self.mParamLocationA,6)
        self.drawHistogram(self.mParamDataA,self.mCanvasA, 6)
        self.mNotebook.add(self.mFrameA,text = "지역 A")

        # LocationB
        self.mFrameB = Frame(self.mWindow, bg=self.mBackgroundColor)
        self.mFrameTextB = Frame(self.mFrameB,bg=self.mBackgroundColor)
        self.mFrameTextB.pack()
        self.mCanvasB = Canvas(self.mFrameB,bg=self.mBackgroundColor)
        self.mCanvasB.pack(fill=BOTH, expand=TRUE)
        # Set Param
        self.mTxtLocationB = []
        self.drawLocationName(self.mTxtLocationB,self.mFrameTextB,self.mParamLocationB,6)
        self.drawHistogram(self.mParamDataB,self.mCanvasB, 6)
        self.mNotebook.add(self.mFrameB,text = "지역 B")

        # LocationC
        self.mFrameC = Frame(self.mWindow, bg=self.mBackgroundColor)
        self.mFrameTextC = Frame(self.mFrameC,bg=self.mBackgroundColor)
        self.mFrameTextC.pack()
        self.mCanvasC = Canvas(self.mFrameC,bg=self.mBackgroundColor)
        self.mCanvasC.pack(fill=BOTH, expand=TRUE)
        # Set Param
        self.mTxtLocationC = []
        self.drawLocationName(self.mTxtLocationC,self.mFrameTextC,self.mParamLocationC,5)
        self.drawHistogram(self.mParamDataC,self.mCanvasC, 5)
        self.mNotebook.add(self.mFrameC,text = "지역 C")


    def update(self):
        pass
