'''
Discord: deity#0001
'''
class Maps:

    d = None

    def __init__(self, d):
        self.d = d
    
    def getMapValueFromKey(self, key):
        if not self.d == None:
            if not key in self.d.keys():
                return None
            else:
                return self.d[key]
        else: return None

    def setMapValue(self, key, val):
        if not self.d == None:
            self.d[key] = val

    def getMapKeyFromValue(self, value):
        for key, val in self.d.items():
            if val == value:
                return key

    def getMapLength(self):
        if not self.d == None:
            return int(len(self.d.keys()))
        else: return None

    def getMap(self):
        return self.d
    
    def setMap(self, d):
        self.d = d

    def printMapValue(self, key):
        if not self.d == None:
            if key in self.d.keys():
                print("Key has value: {}.".format(self.d[key]))
            else: print("Key doesn't exist!")
        else: print("Map is None")
