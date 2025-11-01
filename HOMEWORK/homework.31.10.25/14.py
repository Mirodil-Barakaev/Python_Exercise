class Email:
    def send(self): print("Email")
class SMS:
    def send(self): print("SMS")

def notify_all(lst):
    for n in lst: n.send()

notify_all([Email(), SMS()])