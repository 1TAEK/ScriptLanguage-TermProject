import urllib.request
import urllib.parse
from xml.dom.minidom import parseString
from xml.etree import ElementTree
import time
# 동네예보 xml은 base_date를 넘겨줘야함.
# 2019.05.17 : 필요한 Open API 파싱 완료.
#              하지만 옵션들 고정적인게 아니라 현재 또는 원하는 date, time 지정해줄 수 있어야 하기 때문에 수정이 필요함.
# 2019.05.22 : 동네예보 파싱시 date, time 해당시간에 맞게(baseTime에 가장 가까운 예보시간부터) 파싱해옴.
#              좌표값 또한 바뀌어야 하므로, 추가작업이 필요함.
# 2019.05.24 : get_baseDateAndTime 함수 수정
# base_date = time.strftime('%Y%m%d', time.localtime())
base_time = time.strftime('%H', time.localtime()) + '00'


def get_baseDateAndTime():          # 동네예보 base_date, base_time 반환하는 함수
    base_date = time.strftime('%Y%m%d', time.localtime())
    base_time = time.strftime('%H', time.localtime()) + '00'
    if '0000' <= base_time < '0300':
        base_date = str(int(base_date) - 1)
        base_time = '2000'
    elif '0300' <= base_time < '0600':
        base_date = str(int(base_date) - 1)
        base_time = '2300'
    elif '0600' <= base_time < '2359':
        base_time = '0200'
    # elif '0900' <= base_time < '1200':
    #     base_time = '0500'
    # elif '1200' <= base_time < '1500':
    #     base_time = '0800'
    # elif '1500' <= base_time < '1800':
    #     base_time = '1100'
    # elif '1800' <= base_time < '2100':
    #     base_time = '1400'
    # elif '2100' <= base_time < '0000':
    #     base_time = '1700'

    return base_date, base_time


def parseFcstPerTime():  # 동네예보조회 xml 파싱
    url = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData'
    serviceKey = 'ServiceKey=8KngOJTE%2Fh%2BjNJwkeXlJsC5d1ShWfQ9YadkSpoLeubDe9cekkO44ShcRAra7hjTk%2BYAzJEui5eYPFVGegxUngw%3D%3D'

    baseDate ,baseTime = get_baseDateAndTime()
    baseDate = 'base_date=' + baseDate
    baseTime = 'base_time=' + baseTime
    nx = 'nx=60'
    ny = 'ny=127'

    params = '?' + serviceKey + '&' + baseDate + '&' + baseTime + '&' + nx + '&' + ny + '&numOfRows=200&pageNo=1'
    request = urllib.request.Request(url + params)

    try:
        resp = urllib.request.urlopen(request)
    except urllib.error.URLError as e:
        print(e.reason)
        print(parseString(e.read().decode('utf-8')).toprettyxml())
    except urllib.error.HTTPError as e:
        print("error code=" + e.code)
        print(parseString(e.read().decode('utf-8')).toprettyxml())
    else:
        xml = resp.read()
        print("XML Document loading complete.")
        dom = parseString(xml)
        # print(dom.toprettyxml())
        tree = ElementTree.fromstring( str(dom.toxml()))
        return tree

def getMiddleLandWeather():     # 중기육상예보 xml (3일~10일 후 예보 정보 구름많음 등..)
    url = 'http://newsky2.kma.go.kr/service/MiddleFrcstInfoService/getMiddleLandWeather'
    queryParams = '?' + 'ServiceKey=8KngOJTE%2Fh%2BjNJwkeXlJsC5d1ShWfQ9YadkSpoLeubDe9cekkO44ShcRAra7hjTk%2BYAzJEui5eYPFVGegxUngw%3D%3D' +\
        '&regId=11B00000&tmFc=201905170600&numOfRows=10&pageNo=1'

    request = urllib.request.Request(url + queryParams)

    try:
        resp = urllib.request.urlopen(request)
    except urllib.error.URLError as e:
        print(e.reason)
        print(parseString(e.read().decode('utf-8')).toprettyxml())
    except urllib.error.HTTPError as e:
        print("error code=" + e.code)
        print(parseString(e.read().decode('utf-8')).toprettyxml())
    else:
        xml = resp.read()
        print("XML Document loading complete.")
        dom = parseString(xml)
        tree = ElementTree.fromstring(str(dom.toxml()))
        return tree


def getMiddleTemperature():         # 중기기온조회 xml
    url = 'http://newsky2.kma.go.kr/service/MiddleFrcstInfoService/getMiddleTemperature'
    queryParams = '?' + 'ServiceKey=8KngOJTE%2Fh%2BjNJwkeXlJsC5d1ShWfQ9YadkSpoLeubDe9cekkO44ShcRAra7hjTk%2BYAzJEui5eYPFVGegxUngw%3D%3D' + \
                  '&regId=11B10101&tmFc=201905170600'

    request = urllib.request.Request(url + queryParams)

    try:
        resp = urllib.request.urlopen(request)
    except urllib.error.URLError as e:
        print(e.reason)
        print(parseString(e.read().decode('utf-8')).toprettyxml())
    except urllib.error.HTTPError as e:
        print("error code=" + e.code)
        print(parseString(e.read().decode('utf-8')).toprettyxml())
    else:
        xml = resp.read()
        print("XML Document loading complete.")
        dom = parseString(xml)
        tree = ElementTree.fromstring(str(dom.toxml()))
        return tree

def getUltrvLifeList():        # 체감온도 xml
    url = 'http://newsky2.kma.go.kr/iros/RetrieveLifeIndexService3/getUltrvLifeList'

    ServiceKey = 'ServiceKey=8KngOJTE%2Fh%2BjNJwkeXlJsC5d1ShWfQ9YadkSpoLeubDe9cekkO44ShcRAra7hjTk%2BYAzJEui5eYPFVGegxUngw%3D%3D'
    areaNo = 1100000000
    areaNo = 'areaNo=' + str(areaNo)
    now = 'time='+ time.strftime('%Y%m%d%H', time.localtime())
    params = '?' + ServiceKey + '&' + areaNo + '&' + now
    request = urllib.request.Request(url + params)

    try:
        resp = urllib.request.urlopen(request)
    except urllib.error.URLError as e:
        print(e.reason)
        print(parseString(e.read().decode('utf-8')).toprettyxml())
    except urllib.error.HTTPError as e:
        print("error code=" + e.code)
        print(parseString(e.read().decode('utf-8')).toprettyxml())
    else:
        xml = resp.read()
        print("XML Document loading complete.")
        dom = parseString(xml)
        # print(dom.toprettyxml())
        tree = ElementTree.fromstring(str(dom.toxml()))
        return tree


def CityAirPollution():                 # 시,도별 대기오염지수 xml
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst'
    queryParams = '?' + 'ServiceKey=8KngOJTE%2Fh%2BjNJwkeXlJsC5d1ShWfQ9YadkSpoLeubDe9cekkO44ShcRAra7hjTk%2BYAzJEui5eYPFVGegxUngw%3D%3D' + \
                  '&numOfRow=10&pageNo=1&itemCode=PM10&dataGubun=DAILY&searchCondition=WEEK'

    request = urllib.request.Request(url + queryParams)

    try:
        resp = urllib.request.urlopen(request)
    except urllib.error.URLError as e:
        print(e.reason)
        print(parseString(e.read().decode('utf-8')).toprettyxml())
    except urllib.error.HTTPError as e:
        print("error code=" + e.code)
        print(parseString(e.read().decode('utf-8')).toprettyxml())
    else:
        xml = resp.read()
        print("XML Document loading complete.")
        dom = parseString(xml)
        return dom


class Parser:
    def __init__(self):
        self.TimeFcstDocument = parseFcstPerTime()
        self.DaysWeatherDoc = getMiddleLandWeather()
        self.DaysTemperatureDoc = getMiddleTemperature()
        self.UVDoc = getUltrvLifeList()
        self.APDoc = CityAirPollution()

    def update(self):
        self.TimeFcstDocument = parseFcstPerTime()
        self.DaysWeatherDoc = getMiddleLandWeather()
        self.DaysTemperatureDoc = getMiddleTemperature()
        self.UVDoc = getUltrvLifeList()
        self.APDoc = CityAirPollution()

    def getTimeFcst(self):
        return self.TimeFcstDocument

    def getDaysFcst(self):
        return self.DaysWeatherDoc, self.DaysTemperatureDoc

    def getUVFcst(self):
        return self.UVDoc

    def getAPFcst(self):
        return self.APDoc

parsed = Parser()