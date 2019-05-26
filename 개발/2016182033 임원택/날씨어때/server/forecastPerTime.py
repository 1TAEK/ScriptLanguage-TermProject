from server.parseXMLs import parsed
import time


class ForecastPerTime:
    def __init__(self):
        self.tree = parsed.TimeFcstDocument

    def getCloseTime(self):  # 현재시간에서 가장 근접한 예보 시간을 반환하는 함수.
        now = time.strftime('%H', time.localtime()) + '00'
        if '0000' <= now < '0300':
            closeTime = '0000'
        elif '0300' <= now < '0600':
            closeTime = '0300'
        elif '0600' <= now < '0900':
            closeTime = '0600'
        elif '0900' <= now < '1200':
            closeTime = '0900'
        elif '1200' <= now < '1500':
            closeTime = '1200'
        elif '1500' <= now < '1800':
            closeTime = '1500'
        elif '1800' <= now < '2100':
            closeTime = '1800'
        elif '2100' <= now <= '2359':
            closeTime = '2100'

        return closeTime

    def getFcstPerTime(self):             # 동네예보정보에서 하늘상태, 강수상태와 확률, 온도, 예보시간을 추출하는 함수
        items = self.tree.find('body/items')
        fcstData = []
        isFind = False
        closeTime = self.getCloseTime()
        for item in items:
            if item.find('fcstTime').text == closeTime:
                isFind = True
            if isFind:
                if item.find('category').text == 'SKY' or item.find('category').text == 'PTY' or item.find(
                        'category').text \
                        == 'T3H' or item.find('category').text == 'POP':  # category가 SKY, PTY, T3H, POP 이면
                    category = item.find('category').text
                    fcstValue = item.find('fcstValue').text
                    fcstData.append({category: fcstValue})  # category와 fcstValue를 dict 형태로 list.append 한다.
        return fcstData
