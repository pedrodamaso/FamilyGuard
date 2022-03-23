#!/bin/env python
import threading
from processing import DataProcessing
from notification import create_app, socketio, Notification
from threading import Thread

if __name__ == "__main__":
    Thread(target = DataProcessing(1).run).start()
    Thread(target = Notification(2).run).start()

    #obj1 = DataProcessing(1)
    #obj1.run()

    #obj2 = Notification(2)
    #obj2.run()    