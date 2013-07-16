
from NetworkManager import NetworkManager
from ZoneManager import ZoneManager
from SerialDataManager import SerialDataManager

class Thermostat():

    def __init__(self):
        
        self.start()

    def start(self):

        networkManager = NetworkManager()
        networkManager.start()

        zoneManager = ZoneManager()
        zoneManager.start()

        serialDataManager = SerialDataManager()
        serialDataManager.start()
    
if __name__ == '__main__':
    thermostat = Thermostat()

    
    

   
        
