from datetime import *
import calendar
import time


def get_users_input():
    usersDate = input("Give a date with this format -> HH/MM/EEEE: ")
    return usersDate

"""
/**
* Takes user's input and calculates the
* time difference between input and current
* date
*/@ return: Returns the time difference
"""
def get_users_input_and_calculate_time_difference(usersDate):
    systemsTime = datetime.now().strftime("%X")#Get system's time

    a = datetime.strptime(usersDate + " " + systemsTime, '%d/%m/%Y %H:%M:%S')#Converts date and time into a string
    b = datetime.now()#Get current date

    a = time.mktime(a.timetuple())#The mktime function returns a floating point number, for compatibility with time()
    b = time.mktime(b.timetuple())

    return b-a

def calculate_day_difference(time):
    days = time/86400
    print("Day difference: %d" %(days))
    return days

def calculate_hour_difference(days):
    hours = days * 24
    print("Hour difference: %d" %hours)
    return hours

def calculte_minutes_difference(hours):
    minutes = hours * 60
    print("Minute difference: %d" %minutes)
    return minutes

def calculate_seconds_difference(minutes):
    seconds = minutes * 60
    print("Second difference: %d" %seconds)
    return seconds

def calculate_the_numbers_of_a_month(monthAndYear):
    lista = monthAndYear.split('/')
    monthsWithThirtyOneDays = ['01', '03', '05', '07', '08', '10', '12']
    monthsWithThirtyDays = ['04', '06', '09', '11']
    month = lista[1]
    year = lista[2]
    if(month in monthsWithThirtyOneDays):
        print("The month has 31 days")
    if(month in monthsWithThirtyDays):
        print("The month has 30 days")
    if(month == '02'):
        if(int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0)):
            print("The month has 29 days")
        else:
            print("The month has 28 days")

def display_a_calendar(monthAndYear):
    lista = monthAndYear.split('/')
    c = calendar.TextCalendar(calendar.SUNDAY)
    str = c.formatmonth(int(lista[2]), int(lista[1]))
    print("For the date you entered this month has:", str)



def main():
        flag = 'yes'
        while(flag.casefold() == 'yes'):
            usersInput = get_users_input()
            timeDifference = get_users_input_and_calculate_time_difference(usersInput)
            days = calculate_day_difference(timeDifference)
            hours = calculate_hour_difference(days)
            minutes = calculte_minutes_difference(hours)
            seconds = calculate_seconds_difference(minutes)
            calculate_the_numbers_of_a_month(usersInput)
            display_a_calendar(usersInput)
            flag = input("Type 'yes' if you want to continue or anything else to stop: ")
        print("Terminating the program")

main()
