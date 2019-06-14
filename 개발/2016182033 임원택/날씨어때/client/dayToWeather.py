from tkinter import *

from datetime import datetime

from server import forecastPerDay


class DayToWeather:
    def inputDay(self):
        week = int(datetime.now().weekday())
        weekStr = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
        # 요일마다 번호를 지정해주고
        # 7 보다 커질시 0으로 초기화후 7번 반복문
        for i in range(8):
            if week > 6:
                week = 0
                i -=1
            else:
                self.mParamDay.append(weekStr[week])
                week +=1

    def inputWeather(self):
        # 시간에 따른 날씨이미지 넣어주기
        self.mParamWeather = self.mParamDataList.getFcst()

    def drawHistogram(self):
        self.mCanvas.delete("picture")
        histogram = []
        # 날씨값 받아오기
        dicData = self.mParamDataList.getTemp()
        # 최저 최고 기온 나누기
        maxTempList = []
        minTempList = []

        for i in range (7):
            maxTempList.append(int(dicData[i][0]))
            minTempList.append(int(dicData[i][1]))

        maxTemp = int(max(maxTempList))
        minTemp = int(max(minTempList))

        # 빈도수 최대값을 구함
        # 그려주기 사이간격은 12
        barW = (self.mWindowWidth-10)/7
        barH = 750
        for i in range(7):
            self.mCanvas.create_rectangle(i*barW+45,barH-(barH -50)*maxTempList[i]/maxTemp,
                                          i*barW+65,barH - (50*minTempList[i]/minTemp)*9,
                                          tag="picture")
            # 최고온도
            self.mCanvas.create_text(i*barW+45+10,barH-(barH -50)*maxTempList[i]/maxTemp -15,text=str(maxTempList[i]))
            # 최저온도 h문제
            self.mCanvas.create_text(i*barW+45+10,barH-(50*minTempList[i]/minTemp)*9 +15,text=str(minTempList[i]))

    def __init__(self):
        # Etc
        self.mBackgroundColor = '#%02x%02x%02x' % (224, 255, 255)
        self.mFontDate = font.Font(family = "08SeoulHangangL_0",size = 10)

        # Window
        self.mWindow = Tk()
        self.mWindow.title("날씨어떄")
        self.mWindow.geometry("730x530")
        self.mWindow.resizable(False, False)
        self.mWindow.configure(bg=self.mBackgroundColor)
        self.mWindowWidth = 730
        self.mWindowHeight = 530

        # Init 초기값
        self.mParamDataList = forecastPerDay.ForecastPerDay()
        self.mParamDay = []
        self.mParamWeather = []
        self.mParamHighTemp = []
        self.mParamRowTemp = []

        # 요일
        self.mFrame = Frame(self.mWindow, bg=self.mBackgroundColor)
        self.mFrame.pack()

        self.inputDay()
        self.mTxtDay = []
        for i in range(7):
            self.mTxtDay.append(Label(self.mFrame, text = self.mParamDay[i],bg= self.mBackgroundColor, font=self.mFontDate))
            self.mTxtDay[i].grid(row =0, column = i, padx = 18,pady=20)
        # 날씨
        self.inputWeather()
        self.mImgWeather = []
        for i in range(7):
            self.mImgWeather.append(Label(self.mFrame, text = self.mParamWeather[i],bg= self.mBackgroundColor))
            self.mImgWeather[i].grid(row =1, column = i, padx = 18,pady=20)
        # 최고 최저기온 막대그래프
        self.mCanvas = Canvas(self.mWindow,bg = self.mBackgroundColor)
        self.mCanvas.pack(fill=BOTH,expand=True)
        self.drawHistogram()

    def update(self):
        pass
