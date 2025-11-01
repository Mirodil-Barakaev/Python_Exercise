class WiFi: 
    def connect(self): print("WiFi")
class Ethernet: 
    def connect(self): print("Ethernet")
for o in [WiFi(), Ethernet()]: o.connect()