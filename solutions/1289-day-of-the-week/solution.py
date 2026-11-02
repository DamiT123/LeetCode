class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        time = 0
        days = ["Friday","Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        reg_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leap_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
             
        for i in range(1971, year):
            if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
                time += 366
            else:
                time += 365
            
        for i in range(month - 1):
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                time += leap_months[i]
            else:
                time += reg_months[i]
                
        time += day - 1
        return days[time % 7]
        
        
        
        
            
        
