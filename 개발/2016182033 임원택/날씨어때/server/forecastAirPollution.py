from server.parseXMLs import parsed


class fcstAirPollution:
    def __init__(self):
        self.tree = parsed.getAPFcst()
        pass

