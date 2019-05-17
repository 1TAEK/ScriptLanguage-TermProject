 # 개황 프레임에서 필요한 xml파일을 파싱하는 모듈
import urllib.request
import urllib.parse
from xml.dom.minidom import parseString
from xml.etree import ElementTree

loopFlag = 1
xmlFD = -1
WeatherDoc = None

def printMenu():
    print("₩nWelcome! Book Manager Program (xml version)")
    print("========Menu==========")
    print("Load xml:  l")
    print("Print temperature list: b")
    print("Print dom to xml: p")
    print("Quit program:   q")
    print("==================")

def launcherFunction(menu):
    global WeatherDoc
    if menu == 'l':
        WeatherDoc = loadXMLfromAPI()
    elif menu == 'b':
        PrintWeatherList(['category','fcstValue'])
    elif menu == 'p':
        PrintDOMtoXML()
    elif menu == 'q':
        Quit()
    else:
        print ("error : unknow menu key")

def loadXMLfromAPI():
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


def PrintDOMtoXML():
    if checkDocument():
        print(WeatherDoc.toprettyxml())
    pass


def Quit():
    global loopFlag
    loopFlag = 0
    pass

def checkDocument():
    global WeatherDoc
    if WeatherDoc == None:
        print("Error : Document is empty")
        return False
    return True


def PrintWeatherList(tags):
    global WeatherDoc
    if not checkDocument():
        return None

    # doc = WeatherDoc.childNodes
    # res = doc[0].childNodes
    # for body in res:
    #     if body.nodeName == "body": # 엘리먼트 중 body를 찾는다.
    #         items = body.firstChild
    #         # item = items.childNode
    # for item in items:
    #             if item.nodeName == "item":
    #                 print("found item!")
    #             print(item.nodeValue)
    doc = WeatherDoc.childNodes
    res = doc[0].childNodes
    print("test")
    body = res[1].childNodes
    items = body[0].childNodes
    for item in items:
        subitem = item.childNodes
        for atom in subitem:
            if atom.nodeName in tags:
                print(atom.firstChild.nodeValue, '\n')

WeatherDoc = loadXMLfromAPI()
PrintWeatherList(['category', 'fcstValue'])
##### run #####
# while(loopFlag > 0):
#     printMenu()
#     menuKey = str(input ('select menu :'))
#     launcherFunction(menuKey)
# else:
#     print("Thank you! Good Bye")