from server import parseXMLs

class ForecastPerTime:
    def __init__(self):
        self.tree = parseXMLs.Parser().TimeFcstDocument
        # print(self.getFcstPerTime())

    def getFcstPerTime(self):             # 동네예보정보에서 하늘상태, 강수상태와 확률, 온도, 예보시간을 추출하는 함수
        items = self.tree.find('body/items')
        fcstData = []
        cnt = 0
        for item in items:
            if item.find('category').text == 'SKY' or item.find('category').text == 'PTY' or item.find('category').text == 'T3H' or item.find('category').text == 'POP': # category가 SKY, PTY, T3H, POP 이면
                category = item.find('category').text
                fcstValue = item.find('fcstValue').text
                fcstTime = item.find('fcstTime').text
                if cnt <= 3:
                    cnt += 1
                fcstData.append({category: fcstValue})       # category와 fcstValue를 dict 형태로 list.append 한다.
        return fcstData

