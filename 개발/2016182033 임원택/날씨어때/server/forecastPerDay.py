from server.parseXMLs import parsed


class ForecastPerDay:
    def __init__(self):
        self.fcstTree, self.tempTree = parsed.getDaysFcst()


