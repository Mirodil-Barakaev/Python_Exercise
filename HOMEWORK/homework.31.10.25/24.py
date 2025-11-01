class Loggable:
    def log(self): print("log")
class Database:
    def connect(self): print("db")
class LoggableDatabase(Loggable, Database): pass
a = LoggableDatabase()
a.log(); a.connect()