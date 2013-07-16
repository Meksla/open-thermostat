
from Zone import Zone

import DataManager
import threading

dataManager = DataManager

class ZoneManager(threading.Thread): #Manages Zones and External Units connected to each Zone

    def __init__(self):

        threading.Thread.__init__(self)
        self.enabledZoneObjects = []

    def run(self):

        while True:
            self.checkQueueForData()

    def checkQueueForData(self):

        if not dataManager.toZoneManager.empty():
            data = dataManager.toZoneManager.get()
            self.processQueueData(data)

    def processQueueData(self, data):

        source = data[0]
        data = data[1]

        if source == "Serial":
            serialNumber = data[data.find("[") + 1:data.find("]")]
            serialData = data[data.find("(") + 1:data.find(")")]
            self.addCurrentDataToUnit(serialNumber, serialData)
        elif source == "Network":
            print "Received Network Data: " + data + '\n'
            zoneName = data[data.find("{") + 1:data.find("}")]
            type = data[data.find("[") + 1:data.find("]")]
            serialNumber = data[data.find("(") + 1:data.find(")")]
            self.addRemoveZoneUnits(zoneName, type, serialNumber)

    def addCurrentDataToUnit(self, serialNumber, serialData):

        if not len(self.enabledZoneObjects):
            for zone in self.enabledZoneObjects:

                if not zone.sensorUnits.keys().count(serialNumber):
                    zone.sensorUnits[serialNumber] = serialData
                elif not zone.externalActuatorUnits.keys().count(serialNumber):
                    zone.externalActuatorUnits[serialNumber] = serialData
                elif not zone.motorizedRegisterUnits.keys().count(serialNumber):
                    zone.motorizedRegisterUnits[serialNumber] = serialData


    def addRemoveZoneUnits(self, zoneName, type, serialNumber):

        if self.isZoneEnabled(zoneName):
            print zoneName + " is Enabled" + '\n'
            self.addUnitToZone(zoneName, type, serialNumber)
        else:
            if type == "SNU":
                print "Enabling " + zoneName + '\n'
                self.enableZone(zoneName, type, serialNumber)

    def addUnitToZone(self, zoneName, type, serialNumber):

        print "Adding " + type + serialNumber + " to " + zoneName + "\n"
        for zone in self.enabledZoneObjects:
            if zone.zoneName == zoneName:
                zone.addUnit(type, serialNumber)
                break

    def removeUnitFromZone(self, zoneName, type, serialNumber):

        print "Removing " + type + serialNumber + " from " + zoneName
        for zone in self.enabledZoneObjects:
            if zone.zoneName == zoneName:
                zone.removeUnit(type, serialNumber)
                break

    def enableZone(self, zoneName, type, sensorUnitSerialNumber):
        dataManager.enabledZones.append(zoneName)
        self.addUnitToZone(zoneName, type, sensorUnitSerialNumber)

        zone = Zone(zoneName)
        self.enabledZoneObjects.append(zone)

    def isZoneEnabled(self, zoneName):

        if not len(self.enabledZoneObjects):
            for zone in self.enabledZoneObjects:
                if zone.zoneName == zoneName:
                    return True

        return False

    def getZoneName(self, serialNumber):

        if not len(self.enabledZoneObjects):
            for zone in self.enabledZoneObjects:

                for sensorUnit in zone.sensorUnits:
                    if sensorUnit == serialNumber:
                        return zone
                for externalActuatorUnit in zone.externalActuatorUnits:
                    if externalActuatorUnit == serialNumber:
                        return zone
                for motorizedRegisterUnit in zone.motorizedRegisterUnits:
                    if motorizedRegisterUnit == serialNumber:
                        return zone
        return ""




