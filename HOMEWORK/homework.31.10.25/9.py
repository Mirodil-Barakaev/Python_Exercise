class WiFi:
    def connect(self): print("WiFi on")
class Ethernet:
    def connect(self): print("Ethernet on")

for n in [WiFi(), Ethernet()]:
    n.connect()