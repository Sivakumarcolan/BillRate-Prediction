from datetime import datetime
import time
import json

def convert_date_to_year(date,id):
    # date = datetime.datetime.strptime(date,'%Y-%m-%d')
    month = date.month
    year = date.year
    month = date.month
    week = date.isocalendar()[1]
    day = date.timetuple().tm_yday
    if month<4:
        quarter = 1
    elif month < 7:
        quarter = 2
    elif month < 10:
        quarter = 3
    else:
        quarter = 4

    if id == 1:
        return year , None
    elif id == 2:
        return year , quarter
    elif id == 3:
        return year , month
    elif id==4:
        return year , week
    else:
        return year , day

def convert_time_to_shift(fromTime,toTime):
    # fromTime = fromTime.fda
    # toTime = datetime.datetime.strftime(toTime,'%H:%M:%S')
    fromTime = datetime.combine(datetime.now(), fromTime)
    toTime = datetime.combine(datetime.now(), toTime)
    workingTime = toTime - fromTime
    # print()
    if workingTime.total_seconds() > 720:
        shiftType = 4
    else:
        if fromTime.hour > 5 & fromTime.hour <14:
            shiftType = 1
        elif fromTime.hour > 13 & fromTime.hour <21:
            shiftType = 2
        else:
            shiftType = 3
    return workingTime.total_seconds()/3600 , shiftType
# print(convert_time_to_shift('10:30','22:00'))
# print(convert_date_to_year('10/24/2024'))

def modify_dropdown_val(dict):
    data = {}
    for key , vals in dict.items():
        temp = []
        for val in vals:
            temp.append({'value':val,'label':val})
        data[key] = temp
    return data

