
import socket
import threading
import thread

import DataManager

dataManager = DataManager

enabledZoneList = []

class NetworkManager(threading.Thread): #Manager that connects to all Units via Serial Communication

    def __init__(self):

        self.startNetworkCOM()
        threading.Thread.__init__(self)
        thread.start_new_thread(self.checkQueueData, ())

    def run(self):

        while True:
            clientSocket, address = self.serverSocket.accept()
            print "Connected to Unit at ", address
            thread.start_new_thread(self.processNetworkData, (clientSocket, ))

    def checkQueueData(self):

        if not dataManager.toNetworkManager.empty():
            data = dataManager.toNetworkManager.get()
            self.processQueueData(data)

    def processQueueData(self, data):

        if data == "Zone 1" or "Zone 2" or "Zone 3" or "Zone 4":
            enabledZoneList.append(data)

    def startNetworkCOM(self):

        HOST = ''
        PORT = 50000
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((HOST, PORT))
        self.serverSocket.listen(5)

    def processNetworkData(self, clientSocket):

        SIZE = 1024

        while True:
            data = clientSocket.recv(SIZE)

            if data:
                data = data.strip()

                if data == "GiveZoneData":
                    print "Received Command: " + data
                    print "Sending Data: " + ','.join(dataManager.enabledZones)
                    clientSocket.send(','.join(dataManager.enabledZones) + '\n')
                    continue

                if data == "Refresh":
                    clientSocket.send(','.join(enabledZoneList) + '\n')
                    continue

                if data[0:8] == "[Zone 1]" or "[Zone 2]" or "[Zone 3]" or "[Zone 4]":

                    if not len(enabledZoneList):
                        print "Adding " + data[8:] + " to " + data[1:7]
                        dataManager.toZoneManager.put(("Network", data))
                        print dataManager.toZoneManager
                    continue

        clientSocket.close()