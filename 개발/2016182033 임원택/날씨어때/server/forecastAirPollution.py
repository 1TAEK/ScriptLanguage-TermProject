from server.parseXMLs import parsed

class FcstAirPollution:
    def __init__(self):
        self.tree = parsed.getAPFcst()
        pass

    def getAPData(self):
        items = self.tree.find('body/items')
        airPollutionData = []
        airPollutionData.clear()
        # ����ð����� ���� ����� �ð��� �������� ��� ����� ��ġ�� ������.
        # �� 19 item���� �տ� �� ���� �� �׸���� ���� ���� �տ� �ΰ��� ���� ���ƾ���.
        flag = True
        for item in items:
            if flag:
                #����, �λ�, �뱸, ��õ, ����, ���, ���, ����, ���, �泲, ����, ����, ���, �泲, ����, ����
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
