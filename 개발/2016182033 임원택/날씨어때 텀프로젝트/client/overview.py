from tkinter import*
from tkinter import font
from server import overviewS

class Overview:
    def getDate(self):
        pass
    def getWeather(self):
        dicData = self.mParamDataList.getSpaceFcstData()
        ptyCode = 0
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
                self.mParamWeather = PhotoImage(file = "sunny.gif",width = 50, height = 50)
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
        self.mParamDate = "5월 2일 목요일 오전 11:14"
        self.mParamWeather = ""
        self.mParamTemperature = "21도"
        self.mParamHighRowTemp = "22/7"
        self.mParamUVRays = "자외선 21도"
        self.mParamDesc = "따뜻함이 물씬 느껴지는 하루 강한 자외선을 주의하세요"

        self.mParamDataList = overviewS.OverviewS()
        self.getWeather()

        self.mFont = font.Font(family = "08SeoulHangangL_0",size = 30)
        self.mBackgroundColor = '#%02x%02x%02x' % (224, 255, 255)

        # Date
        self.mTxtDate = Label(frame, text = self.mParamDate)
        self.mTxtDate.grid(row = 0, column = 1)

        # Weather & Temperature
        self.mMidFrame = Frame(frame,bg = self.mBackgroundColor)
        self.mMidFrame.grid(row=1,column = 1)
        # Weather Image
        self.mImgWeather = Label(self.mMidFrame,image = self.mParamWeather,bg = self.mBackgroundColor)
        self.mImgWeather.grid(row=0,column = 0)
        # Temperature
        self.mTxtTemperature = Label(self.mMidFrame,text = self.mParamTemperature, font=self.mFont,bg = self.mBackgroundColor)
        self.mTxtTemperature.grid(row=0, column =1)

        # SubTemperature, UV Rays
        self.mBotFrame = Frame(frame)
        self.mBotFrame.grid(row = 2, column=1)
        self.mParamHighRowTemp = Label(self.mBotFrame, text=self.mParamHighRowTemp)
        self.mParamHighRowTemp.grid(row=0, column=0)
        self.mParamUVRays = Label(self.mBotFrame,text = self.mParamUVRays)
        self.mParamUVRays.grid(row = 0, column=1)

        # Text
        self.mTxtDesc = Label(frame,text =  self.mParamDesc)
        self.mTxtDesc.grid(row = 3, column = 1)


    def update(self):
        # Service에서 받아오기
        self.mParamDate = "갱신됨"
        self.mParamWeather = "갱신됨"
        self.mParamTemperature = "갱신됨"
        self.mParamSubTemperature = "갱신됨"
        self.mParamDesc = "갱신됨"

        # Label 적용
        self.mTxtDate.configure(text = self.mParamDate)
        self.mImgWeather.configure(text = self.mParamWeather)
        self.mTxtTemperature.configure(text = self.mParamTemperature)
        self.mImgSubTemperature.configure(text = self.mParamSubTemperature)
        self.mTxtDesc.configure(text = self.mParamDesc)
