from tkinter import*

class TimeToWeather:
    def drawHistogram(self):
        pass

    def __init__(self,frame):
        # Init 초기값 받아오기
        self.mParamTime = "시간"
        self.mParamWeather = "날씨"
        self.mParamRainAmount = "강수량"
        self.mParamMaxTemperature = "20'"
        self.mParamMinTempereature = "15'"

        # 시간
        mTxtTime = Label(frame, text = self.mParamTime)
        mTxtTime.pack()
        # 날씨
        mImgWeather = Label(frame, text=self.mParamWeather)
        mImgWeather.pack()
        # 강수량
        mTxtRainAmount = Label(frame, text=self.mParamRainAmount)
        mTxtRainAmount.pack()
        # 최고온도, 최저온도 막대그래프
        mHistogramTemperature = self.drawHistogram()

    def update(self):
        pass