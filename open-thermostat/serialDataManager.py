
import threading
import serial
import DataManager

dataManager = DataManager

class SerialDataManager(threading.Thread): #Manager that connects to all Units via Serial Communication

    def __init__(self):

        threading.Thread.__init__(self)
        self.startSerialCOM()

    def run(self):

        while True:
            self.getSerialData()

    def startSerialCOM(self): #Starts Serial Communication between Main Unit and External Units

        COM_PORT = 2
        self.serialCOM = serial.Serial(COM_PORT)
        self.serialCOM.flushInput()

    def getSerialData(self): #Receives any available Serial Data

        self.serialData = self.serialCOM.readline()
        self.processSerialCommand(self.serialData)

    def sendSerialData(self, serialNumber, data): #Sends data to specific unit

        self.serialCOM.write(data)

    def processSerialCommand(self, serialData): #Processes Serial Command received from External Units

        serialData = serialData.strip()
        dataManager.toZoneManager.put(["Serial", serialData])

        print "Received Serial Data From: " + serialNumber + " -- " + data