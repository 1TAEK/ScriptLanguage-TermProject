from tkinter import*
from tkinter import font
from datetime import datetime

from server import overviewS
from common import time

class Overview:
    def getWeather(self):
        dicData = self.mParamDataList.getSpaceFcstData()
        ptyCode =0
        weatherCode = 0

        print(dicData)

        # Check PTY
        for i in range (dicData.__len__()):
            if dicData[i].get('PTY'):
                ptyCode = dicData[i].get('PTY')

        # Get Weather
        if ptyCode == '0':
            for i in range (dicData.__len__()):
                if dicData[i].get('SKY'):
                    weatherCode = dicData[i].get('SKY')
                    isCheckPTY = False
        else:
            weatherCode = ptyCode
            isCheckPTY = TRUE

        if isCheckPTY == False:
            # 1:맑음 3:구름많음 4:흐림
            if weatherCode == '1':
                self.mParamWeather = PhotoImage(file = "sunny.gif",width = 100, height = 100)
            elif weatherCode == '3' or weatherCode == '2':
                self.mParamWeather = PhotoImage(file="cloudy.gif",width = 100, height = 100)
            elif weatherCode == '4':
                self.mParamWeather = PhotoImage(file = "overcast.gif")
        else:
            # 1:비 2:비/눈 3:눈 4:소나기
            if weatherCode == '1':
                self.mParamWeather = PhotoImage(file = "rain.gif")
            elif weatherCode =='2':
                self.mParamWeather = PhotoImage(file = "rain&snow.gif")
            elif weatherCode == '3':
                self.mParamWeather = PhotoImage (file = "snow.gif")
            elif weatherCode =='4':
                self.mParamWeather = PhotoImage(file = "shower.gif")

    def getTemparture(self):
        pass

    def __init__(self,frame):
        # Param
        self.mParamDate = time.Time().mTimeTotal
        self.mParamWeather = ""
        self.mParamTemperature = "21도"
        self.mParamHighRowTemp = "22/7"
        self.mParamUVRays = "자외선 21도"
        self.mParamDesc = "따뜻함이 물씬 느껴지는 하루\n강한 자외선을 주의하세요"

        # self.mParamDataList = overviewS.OverviewS()
        # self.getWeather()
        # test
        self.mParamWeather = PhotoImage(file = "sunny.gif",width = 100, height = 100)


        # Font, BackgroundColor
        self.mFontDate = font.Font(family = "08SeoulHangangL_0",size = 10)
        self.mFontTemp = font.Font(family = "08SeoulHangangL_0",size = 30)
        self.mFontSubTemp = font.Font(family = "08SeoulHangangL_0",size = 12)
        self.mFontText = font.Font(family = "08SeoulHangangL_0",size = 12)
        self.mBackgroundColor = '#%02x%02x%02x' % (224, 255, 255)

        # Date
        self.mTxtDate = Label(frame, text = self.mParamDate,font=self.mFontDate,bg = self.mBackgroundColor,fg="blue")
        self.mTxtDate.pack(anchor = CENTER)

        # Weather & Temperature
        self.mMidFrame = Frame(frame,bg = self.mBackgroundColor)
        self.mMidFrame.pack(anchor = CENTER)
        # Weather Image
        self.mImgWeather = Label(self.mMidFrame,image = self.mParamWeather,bg = self.mBackgroundColor)
        self.mImgWeather.grid(row=0,column = 0)
        # Temperature
        self.mTxtTemperature = Label(self.mMidFrame,text = self.mParamTemperature, font=self.mFontTemp,bg = self.mBackgroundColor,fg="blue")
        self.mTxtTemperature.grid(row=0, column =1)

        # SubTemperature, UV Rays
        self.mBotFrame = Frame(frame,bg = self.mBackgroundColor)
        self.mBotFrame.pack(pady = 5,anchor = CENTER)
        self.mTxtHighRowTemp = Label(self.mBotFrame, text=self.mParamHighRowTemp, font=self.mFontSubTemp,bg = self.mBackgroundColor,fg="blue")
        self.mTxtHighRowTemp.grid(row=0, column=0)
        self.mTxtUVRays = Label(self.mBotFrame,text = self.mParamUVRays, font=self.mFontSubTemp,bg = self.mBackgroundColor,fg="blue")
        self.mTxtUVRays.grid(row = 0, column=1)

        # Text
        self.mTxtDesc = Label(frame,text =  self.mParamDesc, font=self.mFontText,bg = self.mBackgroundColor,fg="blue")
        self.mTxtDesc.pack(anchor = CENTER)

    def update(self):
        # Service에서 받아오기
        self.mParamDate = time.Time().getDay()
        self.mParamWeather = PhotoImage(file = "sunny.gif",width = 100, height = 100)
        self.mParamTemperature = "갱신됨"
        self.mParamHighRowTemp = "갱신됨"
        self.mParamUVRays = "갱신됨"
        self.mParamDesc = "갱신됨"

        # Label 적용
        self.mTxtDate.configure(text = self.mParamDate)
        self.mImgWeather.configure(image = self.mParamWeather)
        self.mTxtTemperature.configure(text = self.mParamTemperature)
        self.mTxtHighRowTemp.configure(text = self.mParamHighRowTemp)
        self.mTxtUVRays.configure(text = self.mParamUVRays)
        self.mTxtDesc.configure(text = self.mParamDesc)
