from parseXMLs import Parser
import time


def getCloseTime():    # 현재시간에서 가장 근접한 예보 시간을 반환하는 함수.
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
    elif '2100' <= now < '0000':
        closeTime = '2100'

    return closeTime


def getSpaceFcstData(tree):             # 동네예보정보에서 하늘상태, 강수상태, 온도, 최저온도, 최고온도 뽑아내는 함수
    items = tree.find('body/items')
    fcstData = []
    for item in items:
        if item.find('fcstDate').text == time.strftime('%Y%m%d', time.localtime()): # fcstDate가 현재 날짜와 같은가?
            if item.find('fcstTime').text == getCloseTime():  # 현재 시간 전의 fcstTime인지 확인한다.
                if item.find('category').text == 'SKY' or item.find('category').text == 'PTY' or item.find('category').text == 'T3H': # category가 SKY, PTY, T3H, TMX, TMN 이면
                    category = item.find('category').text
                    fcstValue = item.find('fcstValue').text
                    fcstData.append({category: fcstValue})       # category와 fcstValue를 dict 형태로 list.append 한다.

            if item.find('category').text == 'TMN' or item.find('category').text == 'TMX':
                category = item.find('category').text
                fcstValue = item.find('fcstValue').text
                fcstData.append({category: fcstValue})           # category와 fcstValue를 dict 형태로 list.append 한다.

    return fcstData


def getUltraViolet(uvTree):                                                  # 자외선지수 뽑아내는 함수
    items = uvTree.find('Body/IndexModel')
    uvData = []
    if items.find('today').text is None:                                     # 오늘 자외선 지수 값이 없으면
        uvDate = items.find('tomorrow').tag
        uvDatum = items.find('tomorrow').text
        uvData.append({uvDate : uvDatum})                                    # 내일 값을 리스트에 넣는다

    else:
        uvDate = items.find('today').tag
        uvDatum = items.find('today').text
        uvData.append({uvDate: uvDatum})

    # print({uvDate : uvDatum})
    return uvData
    pass


tree = Parser().TimeFcstDocument
uv = Parser().UVDoc
lst = getSpaceFcstData(tree) + getUltraViolet(uv)

print(lst)
