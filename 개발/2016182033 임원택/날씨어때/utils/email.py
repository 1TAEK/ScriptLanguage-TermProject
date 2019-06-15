from tkinter import *
from tkinter import ttk

import mimetypes
import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email():
    def sendEmail(self):
        # global host,port
        host = "smtp.gmail.com"
        port = "587"
        html = ""
        title = str(self.titleEntry.get())
        senderAddr = str(self.senderEntry.get())
        recipientAddr = str(self.recipientEntry.get())
        passwd = str(self.passwdEntry.get())
        msgtext = "None"
        # 메세지 안에 담을 내용 생성
        html = self.makeInfo()
        msg = MIMEMultipart('alternative')

        #set Message
        msg['Subject'] = title
        msg['From'] = senderAddr
        msg['To'] = recipientAddr

        msgPart = MIMEText(msgtext, 'plain')
        bookPart = MIMEText(html, 'html', _charset='UTF-8')

        # 메시지에 생성한 MIME 문서를 첨부합니다.
        msg.attach(msgPart)
        msg.attach(bookPart)

        print("connect smtp server ... ")
        s = smtplib.SMTP(host,port)
        #s.set_debuglevel(1)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(senderAddr,passwd)
        s.sendmail(senderAddr , [recipientAddr], msg.as_string())
        s.close()
        print("Mail sending complete!!")

    def makeInfo(self):
        dataStr = self.mParamSendData[0]+'\n'+self.mParamSendData[1]+'\n'+self.mParamSendData[2]+'\n'+self.mParamSendData[3]+'\n'+self.mParamSendData[4]
        return dataStr

    def __init__(self,sendData):
        self.mParamSendData = sendData

        # Etc
        self.mBackgroundColor = '#%02x%02x%02x' % (224, 255, 255)
        self.mFontDate = font.Font(family = "HoonWhitecatR",size = 7)

         # Window Scroll
        self.mWindow = Tk()
        self.mWindow.title("날씨어떄")
        self.mWindow.geometry("280x230")
        self.mWindow.resizable(False, False)
        self.mWindow.configure(bg=self.mBackgroundColor)
        self.mWindowWidth = 280
        self.mWindowHeight = 230

        # 해당지역 오늘 날씨 받아오고 리스트로 기록
        # label title sender recipient passwd
        Label(self.mWindow, text="타이틀").grid(row=0,column =0,sticky="W",padx = 15)
        Label(self.mWindow, text="보내는사람ID").grid(row=1,column =0,sticky="W",padx = 15,pady = 20)
        Label(self.mWindow, text="받는사람ID").grid(row=2,column =0,sticky="W",padx = 15,pady = 20)
        Label(self.mWindow, text="비밀번호").grid(row=3,column =0,sticky="W",padx = 15,pady = 20)
        # Entry
        self.titleEntry = Entry(self.mWindow,justify= LEFT)
        self.senderEntry = Entry(self.mWindow,justify= LEFT)
        self.recipientEntry = Entry(self.mWindow,justify= LEFT)
        self.passwdEntry = Entry(self.mWindow,justify= LEFT)
        self.titleEntry.grid(row=0,column = 1,padx = 15)
        self.senderEntry.grid(row=1,column = 1,padx = 15, pady = 20)
        self.recipientEntry.grid(row=2,column = 1,padx = 15, pady = 20)
        self.passwdEntry.grid(row=3,column = 1,padx = 15, pady = 20)

        # button
        Button(self.mWindow,text="보내기",command=self.sendEmail).grid(row=4, column = 1)
