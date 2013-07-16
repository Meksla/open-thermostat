
class Zone(): #Manages Zones and External Units connected to each Zone

    def __init__(self, zoneName): #Retrieves from CSV file any previous zone setup

        self.zoneName = zoneName

        self.sensorUnits = {}
        self.motorizedRegisterUnits = {}
        self.externalActuatorUnits = {}

    def addUnit(self, type, serialNumber):

        if type == "SU":
            self.sensorUnits[serialNumber] = "0.00"
        elif type == "EAU":
            self.externalActuatorUnits[serialNumber] = "OFF"
        elif type == "MRU":
            self.motorizedRegisterUnits[serialNumber] = "OFF"

    def removeUnit(self, type, serialNumber):

        if type == "SU":
            del self.sensorUnits[serialNumber]
        elif type == "EAU":
            del self.externalActuatorUnits[serialNumber]
        elif type == "MRU":
            del self.motorizedRegisterUnits[serialNumber]

    def checkListIfUnitExists(self, type, serialNumber):

        if type == "SU":
            for sensorUnit in self.sensorUnits:
                if sensorUnit == serialNumber:
                    return True
        elif type == "EAU":
            for externalActuatorUnit in self.externalActuatorUnits:
                if externalActuatorUnit == serialNumber:
                    return True
        elif type == "MRU":
            for motorizedRegisterUnit in self.motorizedRegisterUnits:
                if motorizedRegisterUnit == serialNumber:
                    return True
        return False

    def getZoneTemperature(self):
        for sensorUnit in self.sensorUnits:
            total += self.sensorUnits[sensorUnit] 
        return total / len(self.sensorUnits)



   


        
        

 
 
 
    
        
                
        
            
