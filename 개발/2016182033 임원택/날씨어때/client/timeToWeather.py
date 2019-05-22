from tkinter import*

from common import time
from common import scrollLayout

class TimeToWeather:
    def drawHistogram(self):
        pass

    def inputTime(self):
        # 현재시간 받아오기
        # 시간룰에 따라 배열에 넣어주기 3시간주기
        curTime = time.Time().getIntHour()
        curStrTime = ""
        for i in range (7):
            curTime = curTime+3
            if curTime > 24:
                curTime = curTime - 24
            # string 변환
            if curTime > 12:
                curStrTime = "오후 " + str(curTime - 12)
            else:
                curStrTime = "오전 " + str(curTime)
            # 배열에 넣어주기
            self.mParamTime.append(curStrTime)

    def __init__(self,frame):
        # Init 초기값 받아오기
        self.mParamTime = []
        self.mParamWeather = ['123']
        self.mParamRainAmount = ['123']
        self.mParamTemperature = ['123']
        # 배열에넣기------------------------------------------
        # 현재시간으로부터 3시간 주기로 배열에 넣어주기
        self.inputTime()


        # 그리기----------------------------------------------
        self.mBackgroundColor = '#%02x%02x%02x' % (224, 255, 255)
        self.mScrollLayout = scrollLayout.ScrollLayout(frame,(0, 0, 400, 2400))
        self.mScrollLayout.pack()
        self.mScrollLayout.horizonMode()

        self.mFrame = Frame(self.mScrollLayout.canvas, bg=self.mBackgroundColor)
        # 시간
        mTxtTime = Label(self.mFrame, text = self.mParamTime)
        mTxtTime.pack()
        # 날씨
        mImgWeather = Label(self.mFrame, text=self.mParamWeather)
        mImgWeather.pack()
        # 강수량
        mTxtRainAmount = Label(self.mFrame, text=self.mParamRainAmount)
        mTxtRainAmount.pack()
        # 기온 막대그래프
        mHistogramTemperature = self.drawHistogram()
        self.mScrollLayout.addFrame(self.mFrame)

    def update(self):
        pass
