import threading

import DataManager

dataManager = DataManager()

class LearningAlgorithm(threading.Thread): #Learns and outputs the target temperature for each setpoint time

    def __init__(self):

        threading.Thread.__init__(self)

    #def run(self):

        #while True:
