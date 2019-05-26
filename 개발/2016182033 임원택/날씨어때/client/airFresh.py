from tkinter import *

from server import forecastAirPollution
from common import scrollLayout

class AirFresh:
    def drawLocationA(self):

        print (self.mParamLocationA)
        for i in range(6):
            self.mTxtLocationA.append(Label(self.mFrame, text = self.mParamLocationA[i],bg= self.mBackgroundColor, font=self.mFontDate))
            self.mTxtLocationA[i].grid(row =0, column = i, padx = 18,pady=20)

    def drawLocationB(self):
        pass
    def drawLocationC(self):
        pass

    def __init__(self):
        # Etc
        self.mBackgroundColor = '#%02x%02x%02x' % (224, 255, 255)
        self.mFontDate = font.Font(family = "08SeoulHangangL_0",size = 7)

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
        self.mParamAirPolution = self.mParamData.getAPData()

        # Scroll Frame
        self.mScrollLayout = scrollLayout.ScrollLayout(self.mWindow,(0, 0, self.mWindowWidth, self.mWindowHeight*4),'red')
        self.mScrollLayout.pack()
        self.mFrame = Frame(self.mScrollLayout, bg=self.mBackgroundColor)


        # Input Data
        # LocationA
        self.mTxtLocationA = []
        self.drawLocationA()

        # AirPolution
        # Location A
        # for i in range(6):
        #     self.mTxtDay.append(Label(self.mFrame, text = self.mParamAirPolution[i],bg= self.mBackgroundColor, font=self.mFontDate))
        #     self.mTxtDay[i].grid(row =0, column = i, padx = 18,pady=20)
        # # Location B
        # for i in range(6,12):
        #     self.mTxtDay.append(Label(self.mFrame, text = self.mParamAirPolution[i],bg= self.mBackgroundColor, font=self.mFontDate))
        #     self.mTxtDay[i].grid(row =0, column = i, padx = 18,pady=20)
        # # Location C
        # for i in range(12,17):
        #     self.mTxtDay.append(Label(self.mFrame, text = self.mParamAirPolution[i],bg= self.mBackgroundColor, font=self.mFontDate))
        #     self.mTxtDay[i].grid(row =0, column = i, padx = 18,pady=20)

        # Add Frame
        self.mScrollLayout.addFrame(self.mFrame)


    def update(self):
        pass
