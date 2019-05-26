from tkinter import*

from common import time
from server import forecastPerTime


class TimeToWeather:
    def drawHistogram(self):
        self.mCanvas.delete("picture")
        histogram = []
        # 날씨값 받아오기
        dicData = self.mParamDataList.getFcstPerTime()
        for i in range (32):
            if dicData[i].get('T3H'):
                histogram.append(int(dicData[i].get('T3H')))
        # 빈도수 최대값을 구함
        maxTemp = int(max(histogram))
        # 그려주기 사이간격은 12
        barW = (self.mWindowWidth-24)/8
        barH = 350
        for i in range(8):
            self.mCanvas.create_rectangle(i*barW+40,barH-(barH -50)*histogram[i]/maxTemp,
                                          i*barW+60,barH,tag="picture")
            self.mCanvas.create_text(i*barW+40+10,barH-(barH -50)*histogram[i]/maxTemp -15,text=str(histogram[i]))

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

        # 시간에 따라 8(시간)*4개씩
        # PTY,SKY 값 추출
        ptyCode = []
        skyCode = []
        for i in range (32):
            if dicData[i].get('PTY'):
                ptyCode.append(dicData[i].get('PTY'))
            if dicData[i].get('SKY'):
                skyCode.append(dicData[i].get('SKY'))

        # PTY에 따른 날씨값 저장
        isCheckPTY = []
        for i in range(8):
            if ptyCode[i] == '0':
                self.mParamWeather.append(skyCode[i])
                isCheckPTY.append(False)
            else:
                self.mParamWeather.append(ptyCode[i])
                isCheckPTY.append(True)

        for i in range(8):
            # True :PTY ON(PTY) / False: PTY OFF(SKY)
            # SKY : 맑음(1), 구름많음(3), 흐림(4)
            # PTY : 없음(0), 비(1), 비/눈(2), 눈(3), 소나기(4)
            if isCheckPTY[i]:
                if self.mParamWeather[i] == '1':
                    # self.mImgWeather.append(PhotoImage(file = "sunny.gif",width = 20, height = 20))
                    self.mImgWeather.append("비")
                elif self.mParamWeather[i] == '2':
                    # self.mImgWeather.append(PhotoImage(file = "sunny.gif",width = 20, height = 20))
                    self.mImgWeather.append("비/눈")
                elif self.mParamWeather[i] == '3':
                    # self.mImgWeather.append(PhotoImage(file = "sunny.gif",width = 20, height = 20))
                    self.mImgWeather.append("눈")
                elif self.mParamWeather[i] == '4':
                    # self.mImgWeather.append(PhotoImage(file = "sunny.gif",width = 20, height = 20))
                    self.mImgWeather.append("소나기")
            else:
                if self.mParamWeather[i] == '1':
                    # self.mImgWeather.append(PhotoImage(file = "sunny.gif",width = 20, height = 20))
                    self.mImgWeather.append("맑음")
                elif self.mParamWeather[i] == '2':
                    # self.mImgWeather.append(PhotoImage(file = "sunny.gif",width = 20, height = 20))
                    self.mImgWeather.append("구름조금")
                elif self.mParamWeather[i] == '3':
                    # self.mImgWeather.append(PhotoImage(file = "sunny.gif",width = 20, height = 20))
                    self.mImgWeather.append("구름많음")
                elif self.mParamWeather[i] == '4':
                    # self.mImgWeather.append(PhotoImage(file = "sunny.gif",width = 20, height = 20))
                    self.mImgWeather.append("흐림")

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
        self.mWindow.geometry("730x500")
        self.mWindow.resizable(False, False)
        self.mWindow.configure(bg=self.mBackgroundColor)
        self.mWindowWidth = 730
        self.mWindowHeight = 500

        # 시간
        self.mFrame = Frame(self.mWindow, bg=self.mBackgroundColor)
        self.mFrame.pack()
        self.mTxtTime = []
        for i in range(8):
            self.mTxtTime.append(Label(self.mFrame, text = self.mParamTime[i],bg= self.mBackgroundColor, font=self.mFontDate))
            self.mTxtTime[i].grid(row =0, column = i, padx = 12,pady=20)
        # 날씨
        self.mImgWeather = []
        self.mLabelWeather = []
        self.inputWeather()

        for i in range(8):
            self.mLabelWeather.append(Label(self.mFrame,text=self.mImgWeather[i],bg= self.mBackgroundColor))
            self.mLabelWeather[i].grid(row =1, column = i, padx = 10,pady=20)
        # 강수량
        # mTxtRainAmount = Label(self.mWindow, text=self.mParamRainAmount)
        # mTxtRainAmount.pack(side=LEFT)

        # 기온 막대그래프
        self.mCanvas = Canvas(self.mWindow,bg = self.mBackgroundColor)
        self.mCanvas.pack(fill=BOTH,expand=True)
        self.drawHistogram()

    def update(self):
        pass
