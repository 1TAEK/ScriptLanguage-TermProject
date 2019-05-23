from tkinter import*

from common import time

from server import forecastPerTime

class TimeToWeather:
    def drawHistogram(self):
        pass

    def inputData(self):
        # 시간별로 그 값들 저장
        self.mDataList

    def inputTime(self):
        # 현재시간 받아오기
        # 시간룰에 따라 배열에 넣어주기 3시간주기
        curTime = time.Time().getIntHour()
        curStrTime = ""
        for i in range (8):
            if curTime > 24:
                curTime = curTime - 24
            # string 변환
            if curTime > 12:
                curStrTime = "오후 " + str(curTime - 12)
            else:
                curStrTime = "오전 " + str(curTime)
            # 배열에 넣어주기
            self.mParamTime.append(curStrTime)
            if curTime < 10:
                self.mParamIntTime.append('0'+str(curTime))
            else:
                self.mParamIntTime.append(str(curTime))
            curTime = curTime+3

    def inputWeather(self):
        # 시간에 따른 날씨이미지 넣어주기
        dicData = self.mParamDataList.getFcstPerTime()
        print(dicData)

        # 시간에 따라 8(시간)*4개씩
        # PTY,SKY 값 추출
        ptyCode = []
        skyCode = []
        for i in range (32):
            if dicData[i].get('PTY'):
                ptyCode.append(dicData[i].get('PTY'))
            if dicData[i].get('SKY'):
                skyCode.append(dicData[i].get('SKY'))

        # print (ptyCode)
        # print (skyCode)
        # PTY에 따른 날씨값 저장
        for i in range(8):
            if ptyCode[i] == '0':
                self.mParamWeather.append(skyCode[i])
            else:
                self.mParamWeather.append(ptyCode[i])
        print(self.mParamWeather)

        for i in range(8):
            if self.mParamWeather[i] == '1':
                self.mImgWeather.append()
            elif self.mParamWeather[i] == '3':
                self.mImgWeather.append()
            elif self.mParamWeather[i] == '4':
                self.mImgWeather.append()

    def __init__(self):
        # Init 초기값 받아오기
        self.mParamDataList = forecastPerTime.ForecastPerTime()

        self.mParamTime = []
        self.mParamIntTime = []
        self.mParamWeather = []
        self.mParamRainAmount = []
        self.mParamTemperature = []

        # 배열에넣기------------------------------------------
        # 현재시간으로부터 3시간 주기로 배열에 넣어주기
        self.inputTime()

        # 그리기----------------------------------------------
        self.mBackgroundColor = '#%02x%02x%02x' % (224, 255, 255)
        self.mFontDate = font.Font(family = "08SeoulHangangL_0",size = 10)

        # Window
        self.mWindow = Tk()
        self.mWindow.title("날씨어떄")
        self.mWindow.geometry("730x600")
        self.mWindow.resizable(False, False)
        self.mWindow.configure(bg=self.mBackgroundColor)

        # 시간
        self.mTxtTime = []
        for i in range(8):
            self.mTxtTime.append(Label(self.mWindow, text = self.mParamTime[i],bg= self.mBackgroundColor, font=self.mFontDate))
            self.mTxtTime[i].grid(row =0, column = i, padx = 12,pady=20)
        # 날씨
        self.mImgWeather = []
        self.inputWeather()
        for i in range(8):
            self.mImgWeather.append(Label(self.mWindow, image=self.mParamWeather[i],bg= self.mBackgroundColor))
            mImgWeather[i].grid(row =0, column = i, padx = 10,pady=20)
        # 강수량
        mTxtRainAmount = Label(self.mWindow, text=self.mParamRainAmount)
        mTxtRainAmount.pack(side=LEFT)

        # 기온 막대그래프
        mHistogramTemperature = self.drawHistogram()

    def update(self):
        pass
