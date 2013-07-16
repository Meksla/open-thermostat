##This class creates and manages the current schedule.

import csv
import time

class ScheduleManager:
    
    def getCurrentSetpoint(self):   ##Returns current setpoint
        schedule = self.getCurrentSchedule()
        return schedule[self.getCurrentCounter()]
       
    def changeCurrentSetpoint(self, setpoint):
        t = time.localtime()
        schedule = self.getCurrentSchedule()
        schedule[self.getCurrentCounter()] = setpoint

        weekdayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        if time.strftime('%A', t) in weekdayList:
            f = open('Weekday.csv', 'w')
        else:
            f = open('Weekend.csv', 'w')
                    
        myWriter = csv.writer(f)
        myWriter.writerow(schedule)
        
    def getCurrentCounter(self):

        times = self.getCurrentTimeSchedule()
        t = time.localtime()

        counter = 0

        for x in times:
            startTime = int(x.partition('-')[0])
            endTime = int(x.partition('-')[2])
            currentTime = int(time.strftime('%H', t)) * 100 + int(time.strftime('%M', t))
                
            if startTime < currentTime < endTime:
                return counter
                
            counter += 1

    def getCurrentTimeSchedule(self):   ##Retrieves and returns current time schedule

        f = open('Times.csv', 'r')
        reader = csv.reader(f)
    
        for x in reader:
            schedule = x

        f.close()
        return schedule

    def getCurrentSchedule(self):
        
        t = time.localtime()

        weekdayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

        if time.strftime('%A', t) in weekdayList:
            f = open('Weekday.csv', 'r')
        else:
            f = open('Weekend.csv', 'r')
        
        reader = csv.reader(f)

        for x in reader:
            schedule = x

        f.close()
        return schedule

        

   


        
        

 
 
 
    
        
                
        
            
