from tkinter import*

class Overview:
    def __init__(self,frame):
        self.mParamDate = "5월 2일 목요일 오전 11:14"
        self.mParamWeather = "맑음"
        self.mParamTemperature = "21도"
        self.mParamSubTemperature = "체감온도 21도"
        self.mParamDesc = "따뜻함이 물씬 느껴지는 하루 강한 자외선을 주의하세요"

        # Date
        self.mTxtDate = Label(frame, text = self.mParamDate)
        self.mTxtDate.pack()
        # Weather Image
        self.mImgWeather = Label(frame,text = self.mParamWeather)
        self.mImgWeather.pack()
        # Temperature
        self.mTxtTemperature = Label(frame,text = self.mParamTemperature)
        self.mTxtTemperature.pack()
        # SubTemperature
        self.mImgSubTemperature = Label(frame,text = self.mParamSubTemperature)
        self.mImgSubTemperature.pack()
        # Text
        self.mTxtDesc = Label(frame,text =  self.mParamDesc)
        self.mTxtDesc.pack()


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
