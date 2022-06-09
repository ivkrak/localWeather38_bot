import calendar
from cProfile import label
from unicodedata import name
import telebot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import time
from scipy import stats

#На вход d-день, m-месяц, y-год (из 4-х чисел)
def Param_For_ID(d, m, y):
    if y!=0 and d!=0 and m!=0:
        date_end = d-1
        mounth_end = m
        year_end = y
        if date_end == 0: 
            mounth_end -= 1
            if mounth_end == 0:
                mounth_end = 12
                year_end -= 1
            day_in_mounth = (calendar.monthrange(year_end, mounth_end))[1]
            date_end = day_in_mounth
        # Ищем id для даты конца, так как месяц может поменятся
        date_start = date_end - 31
        mounth_start = mounth_end
        year_start = year_end
        while date_start <= 0:
            mounth_start -= 1
            if mounth_start == 0:
                mounth_start = 12
                year_start -= 1
            day_in_mounth = (calendar.monthrange(year_start, mounth_start))[1]
            date_start += day_in_mounth
        
        #Превращение в строку
        if date_start < 10:
            Str_date_start = '0' + str(date_start)
        else:
            Str_date_start = date_start

        if date_end < 10:
            Str_date_end = '0' + str(date_end)
        else:
            Str_date_end = date_end
        
        if mounth_start < 10:
            Str_mounth_start = '0' + str(mounth_start)
        else:
            Str_mounth_start = mounth_start

        if mounth_end < 10:
            Str_mounth_end = '0' + str(mounth_end)
        else:
            Str_mounth_end = mounth_end


        #Задаём формат строки 0000-00-00 00:00:00
        StartDate = str(year_start) + '-' + str(Str_mounth_start) + '-' + str(Str_date_start) + ' 00:00:00'
        EndDate = str(year_end) + '-' + str(Str_mounth_end) + '-' + str(Str_date_end) + ' 23:00:00'

        return StartDate, EndDate
    else: 
        StartDate, EndDate = ' ', ' '
    return StartDate, EndDate
    
    
