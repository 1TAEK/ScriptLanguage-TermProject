from server.parseXMLs import parsed


class fcstAirPollution:
    def __init__(self):
        self.tree = parsed.getAPFcst()
        pass

    def getAPData(self):
        items = self.tree.find('body/items')
        airPollutionData = []
        airPollutionData.clear()
        # 현재시간에서 가장 가까운 시간을 기준으로 평균 대기질 수치를 가져옴.
        # 총 19 item에서 앞에 두 개를 뺀 항목들이 지역 값임 앞에 두개는 넣지 말아야함.
        flag = True
        for item in items:
            if flag:
                #서울, 부산, 대구, 인천, 광주, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종
                airPollutionData.append(item.find('seoul').text)
                airPollutionData.append(item.find('busan').text)
                airPollutionData.append(item.find('daegu').text)
                airPollutionData.append(item.find('incheon').text)
                airPollutionData.append(item.find('gwangju').text)
                airPollutionData.append(item.find('daejeon').text)
                airPollutionData.append(item.find('ulsan').text)
                airPollutionData.append(item.find('gyeonggi').text)
                airPollutionData.append(item.find('gangwon').text)
                airPollutionData.append(item.find('chungbuk').text)
                airPollutionData.append(item.find('chungnam').text)
                airPollutionData.append(item.find('jeonbuk').text)
                airPollutionData.append(item.find('jeonnam').text)
                airPollutionData.append(item.find('gyeongbuk').text)
                airPollutionData.append(item.find('gyeongnam').text)
                airPollutionData.append(item.find('jeju').text)
                airPollutionData.append(item.find('sejong').text)
                flag = False
        return airPollutionData

fcstAirPollution().getAPData()