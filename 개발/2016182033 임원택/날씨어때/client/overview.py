from tkinter import*
from tkinter import font
from datetime import datetime

from server import overviewS
from common import time

import spam

from server.parseXMLs import parsed


class Overview:
    def setWeather(self):
        dicData = self.mParamDataList.getSpaceFcstData()
        ptyCode =0
        weatherCode = 0

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
            isCheckPTY = True

        if isCheckPTY == False:
            # 1:맑음 3:구름많음 4:흐림
            if weatherCode == '1':
                self.mParamWeather = PhotoImage(file = "sunny.png",width = 100, height = 100)
            elif weatherCode == '3' or weatherCode == '2':
                self.mParamWeather = PhotoImage(file="smallcloud.png",width = 100, height = 100)
            elif weatherCode == '4':
                self.mParamWeather = PhotoImage(file = "cloudy.png")
        else:
            # 1:비 2:비/눈 3:눈 4:소나기
            if weatherCode == '1':
                self.mParamWeather = PhotoImage(file = "rainy.png")
            elif weatherCode =='2':
                self.mParamWeather = PhotoImage(file = "rain&snow.png")
            elif weatherCode == '3':
                self.mParamWeather = PhotoImage (file = "snowy.png")
            elif weatherCode =='4':
                self.mParamWeather = PhotoImage(file = "shower.png")

    def setTemparture(self):
        dicData = self.mParamDataList.getSpaceFcstData()
        for i in range (dicData.__len__()):
            if dicData[i].get('T3H'):
                self.mParamTemperature = str(dicData[i].get('T3H'))+'도'

    def setHighRowTemp(self):
        dicData = self.mParamDataList.getSpaceFcstData()
        highTemp = 0
        rowTemp = 0
        for i in range (dicData.__len__()):
            if dicData[i].get('TMN'):
                highTemp = str(dicData[i].get('TMN'))
            if dicData[i].get('TMX'):
                rowTemp = str(dicData[i].get('TMX'))
        self.mParamHighRowTemp = highTemp+"/"+rowTemp

    def setUVRays(self):
        dicData = self.mParamDataList.getUltraViolet()
        self.mParamUVRays = "자외선지수:" + dicData[0]

    def setDesc(self):
        temp = int(self.mParamTemperature.strip('도'))
        uv = int(self.mParamUVRays.strip('자외선지수:'))

        # 날씨상태체크
        if temp < 4:
            self.mParamDesc = "매우 추운 오늘 롱패딩이 필수입니다\n"
        elif temp >=4 and temp <16:
            self.mParamDesc = "쌀쌀한 기온, 트랜치코트가 필요해요!\n"
        elif temp >=16 and temp <21:
            self.mParamDesc = "데이트하기 딱 좋은 따뜻한 날씨 연애합시다\n"
        elif temp >=21and temp <27:
            self.mParamDesc = "더운 날씨엔 반팔 반바지 착용해요\n"
        elif temp >=27:
            self.mParamDesc = "매우 더운 날씨, 불쾌지수 증가!\n"

        # 자외선체크
        if uv < 3:
            self.mParamDesc += "썬크림 따위는 필요없습니다."
        elif uv >= 3 and uv < 5:
            self.mParamDesc += "낮은 자외선으로 문제없습니다."
        elif uv >=5 and uv < 9:
            self.mParamDesc += "약간의 자외선을 조심하세요!"
        elif uv >=9 and uv < 12:
            self.mParamDesc += "썬글라스는 사치이고 썬크림만 발라주세요!"
        elif uv >=12:
            self.mParamDesc += "썬글라스, 썬크림이 필수입니다!"

    def __init__(self,frame):
        # Param
        self.mCurlocation = parsed.getKey()
        self.mParamDate = time.Time().mTimeTotal
        self.mParamWeather = ""
        self.mParamTemperature = ""
        self.mParamHighRowTemp = ""
        self.mParamUVRays = ""
        self.mParamDesc = "따뜻함이 물씬 느껴지는 하루\n강한 자외선을 주의하세요"

        # 데이터 불러오기
        self.mParamDataList = overviewS.OverviewS()
        self.setWeather()
        self.setTemparture()
        self.setHighRowTemp()
        self.setUVRays()
        self.setDesc()

        # test
        # self.mParamWeather = PhotoImage(file = "sunny.gif",width = 100, height = 100)

        # Font, BackgroundColor
        self.mFontLocation = font.Font(family = "08SeoulHangangL_0",size = 20)
        self.mFontDate = font.Font(family = "08SeoulHangangL_0",size = 10)
        self.mFontTemp = font.Font(family = "08SeoulHangangL_0",size = 30)
        self.mFontSubTemp = font.Font(family = "08SeoulHangangL_0",size = 12)
        self.mFontText = font.Font(family = "08SeoulHangangL_0",size = 12)
        self.mBackgroundColor = '#%02x%02x%02x' % (224, 255, 255)

        # Location
        self.mTxtLocation = Label(frame, text = self.mCurlocation,font=self.mFontLocation,bg = self.mBackgroundColor,fg="green")
        self.mTxtLocation.pack(pady = 15)

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
        self.mParamWeather = PhotoImage(file = "sunny.png",width = 100, height = 100)
        self.mParamTemperature = "갱신됨"
        self.mParamHighRowTemp = "갱신됨"
        self.mParamUVRays = "갱신됨"
        self.mParamDesc = "갱신됨"

        self.mParamDataList = overviewS.OverviewS()
        self.setWeather()
        self.setTemparture()
        self.setHighRowTemp()
        self.setUVRays()
        self.setDesc()
        self.mCurlocation = parsed.getKey()

        # Label 적용
        self.mTxtLocation.configure(text = self.mCurlocation)
        self.mTxtDate.configure(text = self.mParamDate)
        self.mImgWeather.configure(image = self.mParamWeather)
        self.mTxtTemperature.configure(text = self.mParamTemperature)
        self.mTxtHighRowTemp.configure(text = self.mParamHighRowTemp)
        self.mTxtUVRays.configure(text = self.mParamUVRays)
        self.mTxtDesc.configure(text = self.mParamDesc)

    def sendInfo(self):
        list = []
        list.append(self.mParamDate)
        list.append(self.mParamTemperature)
        list.append(self.mParamHighRowTemp)
        list.append(self.mParamUVRays)
        list.append(self.mParamDesc)

        return list
