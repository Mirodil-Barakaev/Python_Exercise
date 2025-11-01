class Notification:
    def send(self): print("Send")
class EmailNotification(Notification):
    def send(self): print("Email")
class SMSNotification(Notification):
    def send(self): print("SMS")
for n in [EmailNotification(), SMSNotification()]: n.send()