import urllib.request
import urllib.parse
from xml.dom.minidom import parseString

# 동네예보 xml은 base_date를 넘겨줘야함.



def getForecastSpaceData():     # 동네예보조회 xml 파싱
    url = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData'
    queryParams = '?' + 'ServiceKey=8KngOJTE%2Fh%2BjNJwkeXlJsC5d1ShWfQ9YadkSpoLeubDe9cekkO44ShcRAra7hjTk%2BYAzJEui5eYPFVGegxUngw%3D%3D' +\
        '&base_date=20190517&base_time=0200&nx=60&ny=127&numOfRows=300' \
        '&pageNo=1'

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
        # print(dom.toprettyxml())
        return dom


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
        print(dom.toprettyxml())
        return dom

# TownDocument = getForecastSpaceData()       # 동네예보 xml DOM객체에 저장
# DaysWeatherDoc = getMiddleLandWeather()     # 중기예보 xml DOM객체에 저장
DaysTemperatureDoc = getMiddleTemperature()   # 중기기온 xml DOM객체에 저장