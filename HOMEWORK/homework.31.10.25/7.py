class Runner:
    def run(self): print("Run fast")
class Car:
    def run(self): print("Car runs")

def start(o): o.run()

for x in [Runner(), Car()]:
    start(x)