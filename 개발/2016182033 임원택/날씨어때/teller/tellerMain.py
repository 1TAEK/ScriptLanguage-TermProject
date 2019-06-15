
import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

from teller import noti
from server.parseXMLs import parsed

class Teller:
    def replyAptData(self,user,telleData):
        msg = telleData[0]+'\n'+telleData[1]+'\n'+telleData[2]+'\n'+telleData[3]+'\n'+telleData[4]
        noti.sendMessage(user,msg)
        # if msg:
        #     noti.sendMessage( user, msg )
        # else:
        #     noti.sendMessage( user, '%s 기간에 해당하는 데이터가 없습니다.'%date_param )

    # 사용자 입력을 받아서 메시지의 종류와 사용자 아이디를 확인
    def handle(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        # if content_type != 'text':
        #     noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        #     return

        text = msg['text']
        print (text)
        parsed.update(text)
        self.mOverview.update()

        # 지역명에 따라 지역 데이터 받아오기
        # Text가 지역리스트에 있을때
        self.replyAptData( chat_id,self.mOverview.sendInfo())
        # else:
        #     noti.sendMessage(chat_id, "모르는 명령어입니다.\n명령어를 다시 입력해주세요.\n명령어:지역 + 지역명")

    # 데이터 받아오기
    def __init__(self, overview):
        today = date.today()
        current_month = today.strftime('%Y%m')

        print( '[',today,']received token :', noti.TOKEN )

        bot = telepot.Bot(noti.TOKEN)
        pprint( bot.getMe() )

        bot.message_loop(self.handle)

        print('Listening...')

        self.mOverview = overview
        self.mTelledata = None
