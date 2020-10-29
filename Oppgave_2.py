# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 16:39:32 2020

Besvarelse på del 2 prosjektoppgave i kurset
PY1010 Python-programmering for beregninger, selvvalgt oppgave

Program for å hente inn værvarsel for de neste 48 timer fra to steder,
Sinsen (der jeg bor) og Rørestranda(der jeg har båtplass og seilbåt). 
Programmet beregner max, min, gjennomsnitt
av temp, vind og regn, plotter resultater, skriver til pdf og excel fil.
Til slutt regner programmet en kvalitetsfaktor på været 
og gir meg en anbefaling på hvor jeg bør oppholde meg neste 48 timer.
For at dette skal fungere kreves library for Yr. 
installeres med: pip install yr.libyr 
Har også brukt json library, men det ligger default i Python 
og skal være installert hos de fleste
@author: torkr
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# https://github.com/wckd/python-yr
from yr.libyr import Yr
import json

# henter værvarsel for Sinsen for neste 48 timer, time for time
weather_Sinsen = Yr(location_name='Norway/Oslo/Oslo/Sinsen', forecast_link='forecast_hour_by_hour')

# lager lister som blir brukt til verdier i for-løkken under
tid_lst_Sinsen  = []
temp_lst_Sinsen = []
wind_lst_Sinsen = []
rain_lst_Sinsen = []

# itirerer json telegrammet og legger verdier i lister
for forecast in weather_Sinsen.forecast(str):
        data = json.loads(forecast)
        tid = data['@from']
        tid_lst_Sinsen.append(tid)
        temperature = data['temperature']
        all_temps = temperature['@value']
        temp_lst_Sinsen.append(all_temps)
        wind = data['windSpeed']
        all_wind = wind['@mps']        
        wind_lst_Sinsen.append(all_wind)
        rain = data['precipitation']
        all_rain = rain['@value']        
        rain_lst_Sinsen.append(all_rain)
        
# gjør om liste til array,gjør så om string array til float array          
tid_arr_Sinsen  = np.array(tid_lst_Sinsen)       
temp_arr_Sinsen = np.array(temp_lst_Sinsen)
temp_arr_Sinsen = temp_arr_Sinsen.astype(np.float) 
wind_arr_Sinsen = np.array(wind_lst_Sinsen)
wind_arr_Sinsen = wind_arr_Sinsen.astype(np.float) 
rain_arr_Sinsen = np.array(rain_lst_Sinsen)
rain_arr_Sinsen = rain_arr_Sinsen.astype(np.float) 


# henter værvarsel for Rørestranda for neste 48 timer, time for time
weather_Rørestranda = Yr(location_name='Norway/Vestfold/Horten/Rørestranda', forecast_link='forecast_hour_by_hour')

# lager lister som blir brukt til verdier i for-løkken under
tid_lst_Rørestranda  = []
temp_lst_Rørestranda = []
wind_lst_Rørestranda = []
rain_lst_Rørestranda = []

# itirerer json telegrammet og legger verdier i lister
for forecast in weather_Rørestranda.forecast(str):
        data = json.loads(forecast)
        tid = data['@from']
        tid_lst_Rørestranda.append(tid)
        temperature = data['temperature']
        all_temps = temperature['@value']
        temp_lst_Rørestranda.append(all_temps)
        wind = data['windSpeed']
        all_wind = wind['@mps']        
        wind_lst_Rørestranda.append(all_wind)
        rain = data['precipitation']
        all_rain = rain['@value']        
        rain_lst_Rørestranda.append(all_rain)
        
# gjør om liste til array,gjør så om string array til float array       
tid_arr_Rørestranda  = np.array(tid_lst_Rørestranda)        
temp_arr_Rørestranda = np.array(temp_lst_Rørestranda)
temp_arr_Rørestranda = temp_arr_Rørestranda.astype(np.float)
wind_arr_Rørestranda = np.array(wind_lst_Rørestranda)
wind_arr_Rørestranda = wind_arr_Rørestranda.astype(np.float)
rain_arr_Rørestranda = np.array(rain_lst_Rørestranda)
rain_arr_Rørestranda = rain_arr_Rørestranda.astype(np.float)



# legger arrayene etter hverandre som kolonner
vaer_arr = np.column_stack((tid_arr_Sinsen,temp_arr_Sinsen, temp_arr_Rørestranda, wind_arr_Sinsen, wind_arr_Rørestranda, rain_arr_Sinsen, rain_arr_Rørestranda))
# lager en dataframe med beskrivelse på kolonner
vaer_df = pd.DataFrame(vaer_arr, columns = ['Tid','Sinsen_temp', 'Rørestranda_temp','Sinsen_vind', 'Rørestranda_vind','Sinsen_regn', 'Rørestranda_regn'])
# skriver til excel fil
vaer_df.to_excel("Vaer.xlsx") 

# finner max, min og gjennomsnitt
  #temp
maxtemp_Sinsen         = max(temp_arr_Sinsen)
mintemp_Sinsen         = min(temp_arr_Sinsen)
snitttemp_Sinsen       = np.mean(temp_arr_Sinsen)
maxtemp_Rørestranda    = max(temp_arr_Rørestranda)
mintemp_Rørestranda    = min(temp_arr_Rørestranda)
snitttemp_Rørestranda  = np.mean(temp_arr_Rørestranda)

  #wind
maxwind_Sinsen         = max(wind_arr_Sinsen)
minwind_Sinsen         = min(wind_arr_Sinsen)
snittwind_Sinsen       = np.mean(wind_arr_Sinsen)
maxwind_Rørestranda    = max(wind_arr_Rørestranda)
minwind_Rørestranda    = min(wind_arr_Rørestranda)
snittwind_Rørestranda  = np.mean(wind_arr_Rørestranda)

  #rain
maxrain_Sinsen         = max(rain_arr_Sinsen)
minrain_Sinsen         = min(rain_arr_Sinsen)
snittrain_Sinsen       = np.mean(rain_arr_Sinsen)
maxrain_Rørestranda    = max(rain_arr_Rørestranda)
minrain_Rørestranda    = min(rain_arr_Rørestranda)
snittrain_Rørestranda  = np.mean(rain_arr_Rørestranda)
print ('')
print ('______________________________________________________') 
print ('')
print('Gjennomsnittlig temp, vind og regn på Sinsen neste 48 timer er:')
print('%.2f'% snitttemp_Sinsen,'°C',',', '%.2f'% snittwind_Sinsen,'m/s', ',','%.2f'%snittrain_Sinsen,'mm')

print('Gjennomsnittlig temp, vind og regn på Rørestranda neste 48 timer er:')
print('%.2f'% snitttemp_Rørestranda,'°C',',', '%.2f'% snittwind_Rørestranda,'m/s', ',','%.2f'%snittrain_Rørestranda,'mm')
print ('')
print ('______________________________________________________') 
print ('')
 
# finner max, min for Sinsen + Rørestranda  
maxtemp = float(max(maxtemp_Sinsen, maxtemp_Rørestranda))
mintemp = float(min(mintemp_Sinsen, mintemp_Rørestranda)) 

if   maxtemp_Sinsen > maxtemp_Rørestranda:
    print('Maxtemp neste 48 timer er:', maxtemp, '°C','og er på Sinsen')
elif maxtemp_Sinsen < maxtemp_Rørestranda:
    print('Maxtemp neste 48 timer er:', maxtemp, '°C','og er på Rørestranda')
elif maxtemp_Sinsen == maxtemp_Rørestranda: 
    print('Maxtemp neste 48 timer er:', maxtemp, '°C','og det er samme temp på Sinsen og Rørestranda')

if   mintemp_Sinsen < mintemp_Rørestranda:
    print('Mintemp neste 48 timer er:', mintemp, '°C','og er på Sinsen')
elif mintemp_Sinsen > mintemp_Rørestranda:
    print('Mintemp neste 48 timer er:', mintemp, '°C','og er på Rørestranda')
elif mintemp_Sinsen == mintemp_Rørestranda: 
    print('Mintemp neste 48 timer er:', mintemp, '°C','og det er samme temp på Sinsen og Rørestranda')

maxwind = float(max(maxwind_Sinsen, maxwind_Rørestranda))
minwind = float(min(minwind_Sinsen, minwind_Rørestranda)) 

if   maxwind_Sinsen > maxwind_Rørestranda:
    print('Maxvind neste 48 timer er:', maxwind, 'm/s','og er på Sinsen')
elif maxwind_Sinsen < maxwind_Rørestranda:
    print('Maxvind neste 48 timer er:', maxwind, 'm/s','og er på Rørestranda')
elif maxwind_Sinsen == maxwind_Rørestranda: 
    print('Maxvind neste 48 timer er:', maxwind, 'm/s','og det er samme vindstyrke på  Sinsen og Rørestranda')

if   minwind_Sinsen < minwind_Rørestranda:
    print('Minvind neste 48 timer er:', minwind, 'm/s','og er på Sinsen')
elif minwind_Sinsen > minwind_Rørestranda:
    print('Minvind neste 48 timer er:', minwind, 'm/s','og er på Rørestranda')
elif minwind_Sinsen == minwind_Rørestranda: 
    print('Minvind neste 48 timer er:', minwind, 'm/s','og det er samme vindstyrke på  Sinsen og Rørestranda')

maxrain = float(max(maxrain_Sinsen, maxrain_Rørestranda))
minrain = float(min(minrain_Sinsen, minrain_Rørestranda))    

if   maxrain_Sinsen > maxrain_Rørestranda:
    print('Maxregn neste 48 timer er:', maxrain, 'mm','og er på Sinsen')
elif maxrain_Sinsen < maxrain_Rørestranda:
    print('Maxregn neste 48 timer er:', maxrain, 'mm','og er på Rørestranda')
elif maxrain_Sinsen == maxrain_Rørestranda: 
    print('Maxregn neste 48 timer er:', maxrain, 'mm','og det er det samme  på Sinsen og Rørestranda')

if   minrain_Sinsen < minrain_Rørestranda:
    print('Minregn neste 48 timer er:', minrain, 'mm','og er på Sinsen')
elif minrain_Sinsen > minrain_Rørestranda:
    print('Minregn neste 48 timer er:', minrain, 'mm','og er på Rørestranda')
elif minrain_Sinsen == minrain_Rørestranda: 
    print('Minregn neste 48 timer er:', minrain, 'mm','og det er det samme på Sinsen og Rørestranda')

    
# lager et array for x-verdier for å plotte med      
x_plot = np.linspace(1,48, 48)

# plotter temp
plt.figure(1)
plt.plot(x_plot,temp_arr_Sinsen,'r.-')
plt.plot(x_plot,temp_arr_Rørestranda,'b.-')
plt.xlabel('Timer fremover', fontsize = 16)
plt.ylabel('Temp', fontsize = 16)
plt.legend(('Sinsen', 'Rørestranda'), loc='best', fontsize = 10)
plt.savefig("plot_1.pdf")

# forbereder for å plotte gjennomsnittvind
arrwind = np.ones([48])
meanwSinsen      = arrwind * snittwind_Sinsen 
meanwRørestranda = arrwind * snittwind_Rørestranda 

# plotter vind
plt.figure(2)
plt.plot(x_plot,wind_arr_Sinsen,'r.-')
plt.plot(x_plot,wind_arr_Rørestranda,'b.-')
plt.plot(x_plot, meanwSinsen,'r',dashes=[2, 5])
plt.plot(x_plot, meanwRørestranda,'b', dashes=[2, 5])
plt.xlabel('Timer fremover', fontsize = 16)
plt.ylabel('Vind m/s', fontsize = 16)
plt.legend(('Sinsen', 'Rørestranda'), loc='best', fontsize = 10)
plt.savefig("plot_2.pdf")

# plotter regn
plt.figure(3)
plt.plot(x_plot,rain_arr_Sinsen,'r.-')
plt.plot(x_plot,rain_arr_Rørestranda,'b.-')
plt.xlabel('Timer fremover', fontsize = 16)
plt.ylabel('Regn mm', fontsize = 16)
plt.legend(('Sinsen', 'Rørestranda'), loc='best', fontsize = 10)
plt.savefig("plot_3.pdf")


# lager en funksjon for kvalitetsfaktor Q av wind 
def Q_wind (max_w, min_w, mean_w):
    Q = 0
    if max_w <= 2  and mean_w < 1:# vindstille eller for lite wind
        Q = 0
    if min_w > 1  and mean_w > 2:# litt wind  
        Q = 0.3
    if (2 < mean_w < 8) and max_w < 12:# fine seilforhold
        Q = 1.0
    if (2 < mean_w < 8) and (12<max_w < 20):# greie seilforhold
        Q = 0.8
    if max_w > 20 and mean_w >= 9:# friske seilforhold
        Q = 0.6
    if mean_w > 18 or  max_w > 22:# uvær!!
       Q = 0
    return Q
   
QwSinsen      = Q_wind(maxwind_Sinsen, minwind_Sinsen, snittwind_Sinsen)
QwRørestranda = Q_wind(maxwind_Rørestranda, minwind_Rørestranda, snittwind_Rørestranda)
    

# lager en funksjon for kvalitetsfaktor Q for temp         
# en funksjon på -2x^2+80x vil skjære x aksen ved 0 og 40
# ufyselig varmt og kaldt og gi maks = 800 ved 20 degC, 
# deler på 800 for å få en faktor på maks 1  
def Q_temp (mean_temp):
    Q = ((-2*mean_temp**2) + (80*mean_temp))/800
    if  Q < 0 or Q > 40:
        Q = 0
    return Q  

QtSinsen      = Q_temp(snitttemp_Sinsen) 
QtRørestranda = Q_temp(snitttemp_Rørestranda)   

# Lett regn: Minst 0.1 mm/t
# Regn: 0.5-1 mm/t
# Kraftig regn: Alt over 1 mm/t   
# lager en funksjon for kvalitetsfaktor Q for regn
def Q_rain (mean_rain):
    Q = -2 * mean_rain 
    if Q < -1:
        Q = -1
    return Q
    
QrSinsen      = Q_rain(snittrain_Sinsen) 
QrRørestranda = Q_rain(snittrain_Rørestranda) 

QtotalSinsen = QwSinsen + QtSinsen + QrSinsen  
QtotalRørestranda = QwRørestranda + QtRørestranda + QrRørestranda 

# forbereder for kakediagram
labels = 'Sinsen', 'Rørestranda'
sizes = [QtotalSinsen, QtotalRørestranda] 

plt.figure(4)
plt.pie(sizes, labels = labels, autopct = '%1.1f%%', startangle=-90)
plt.title('Kvalitetsfaktor')
 
print ('*************************************************') 
if  QtotalSinsen > QtotalRørestranda: 
    print ('Neste 48 timer er Sinsen beste sted å oppholde seg!')  
elif QtotalSinsen < QtotalRørestranda:  
    print ('Neste 48 timer er Rørestranda beste sted å oppholde seg!')    
elif QtotalSinsen == QtotalRørestranda:  
    print ('Neste 48 timer er Sinsen & Rørestranda like!') 
print ('*************************************************')     
    