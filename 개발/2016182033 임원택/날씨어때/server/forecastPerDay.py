from server.parseXMLs import parsed


class ForecastPerDay:
    def __init__(self):
        self.fcstTree, self.tempTree = parsed.getDaysFcst()

    def getFcst(self):
        item = self.fcstTree.find('body/items/item')
        fcstData = []
        for i in range(3, 11):
            if i < 8:
                wfAm = item.find('wf' + str(i) + 'Am').text
                wfPm = item.find('wf' + str(i) + 'Am').text
            else:   # 8일~10일후 예보는 오전/오후로 안나눠져있음. 같은 값으로 채움.
                wfAm = item.find('wf' + str(i)).text
                wfPm = item.find('wf' + str(i)).text
            fcstData.append((wfAm, wfPm))

        print(fcstData)
        return fcstData

    def getTemp(self):
        pass

ForecastPerDay().getFcst()