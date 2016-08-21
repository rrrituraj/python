# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 12:29:14 2016

@author: RITURAJ
"""

"""
The class Clock is used to simulate a clock.
"""
class Clock():
    
    def __init__(self , hours , minutes , seconds):
        """
        The paramaters hours, minutes and seconds have to be
        integers and must satisfy the following equations:
        0 <= h < 24
        0 <= m < 60
        0 <= s < 60
        """
        self.Set_Clock(hours , minutes , seconds)
    
    def Set_Clock(self , hours , minutes , seconds):
        """
        The paramaters hours, minutes and seconds have to be
        integers and must satisfy the following equations:
        0 <= h < 24
        0 <= m < 60
        0 <= s < 60
        """
        if type(hours) == int and 0 <= hours and hours < 24:
            self._hours = hours
        else:
            raise TypeError("Hours have to be integers between 0 and 23!")
        if type(minutes) == int and 0 <= minutes and minutes < 60:
            self.__minutes = minutes
        else:
            raise TypeError("minutes have to be integers between 0 and 60!")
        if type(seconds) == int and 0 <= seconds and seconds < 60:
            self.__seconds = seconds
        else:
            raise TypeError("seconds have to be integers between 0 and 60!")
            
    def __str__(self):
            return "{0:02d}:{1:02d}:{2:02d}".format(self._hours,
                                                    self.__minutes,
                                                    self.__seconds) 
    def tick(self):
        '''
        This method lets the clock "tick", this means that the
        internal time will be advanced by one second.
        '''
        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                if self._hours == 23:
                    self._hours = 0
                else:
                    self._hours += 1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1
            
"""
The class Calendar implements a calendar.
"""

class Calendar(object):
    months = (31,28,31,30,31,30,31,31,30,31,30,31)
    date_style = "British"
    
    @staticmethod
    def leapyear(year):
        """
        The method leapyear returns True if the parameter year
        is a leap year, False otherwise
        """
        if year % 4 == 0:
            if year % 100 == 0:
                # divisible by 4 and by 100
                if year % 400 == 0:
                    leapyear = True
                else:
                    leapyear = False
            else:
                # divisible by 4 but not by 100
                leapyear = True
        else:
            # not divisible by 4
            leapyear = False
        return leapyear
    
    def __init__(self , d , m , y):
        self.Set_Calendar(d , m , y)
    
    def Set_Calendar(self , d , m , y):
        if type(d) == int and type(m) == int and type(y) == int:
            self.__days = d
            self.__months = m
            self.__years = y
        else:
            raise TypeError("d, m, y have to be integers!")
            
    def __str__(self):
        if Calendar.date_style == "British":
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__days,
                                                   self.__months,
                                                   self.__years)
        else:
            # assuming American style
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__months,
                                                   self.__days,
                                                   self.__years)
                                                  
    def advance(self):
        """
        This method advances to the next date.
        """
        max_days = Calendar.months[self.__months-1]
        if self.__months == 2 and Calendar.leapyear(self.__years):
            max_days += 1
        if self.__days == max_days:
            self.__days= 1
            if self.__months == 12:
                self.__months = 1
                self.__years += 1
            else:
                self.__months += 1
        else:
            self.__days += 1
                             
"""
Modul, which implements the class CalendarClock.
"""
class CalendarClock(Clock , Calendar):
    """
    The class CalendarClock implements a clock with integrated
    calendar. It's a case of multiple inheritance, as it inherits
    both from Clock and Calendar
    """
    
    def __init__(self,day, month, year, hours, minutes, seconds):
        Clock.__init__(self,hours, minutes, seconds)
        Calendar.__init__(self,day, month, year)
    
    def tick(self):
        """
        advance the clock by one second
        """
        previous_hour = self._hours
        Clock.tick(self)
        if (self._hours < previous_hour):
            self.advance()
            
    def __str__(self):
        return Calendar.__str__(self)+',' + Clock.__str__(self)
    
if __name__ == "__main__":
    x = CalendarClock(31,12,2013,23,59,58)
    print("One tick from ",x, end=" ")
    x.tick()
    print("to ", x)
    
    x = CalendarClock(28,2,1900,23,59,59)
    print("One tick from ",x, end=" ")
    x.tick()
    print("to ", x)
    