# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 10:30:05 2018

@author: Pille
"""

path_in = 'D:/Uni/Masterarbeit/Emissivity_stations/Changed2/'

path_out = 'D:/Uni/Masterarbeit/Emissivity_stations/Changed2/station_emis/'

items = os.listdir(path_in)

newlist = []
for names in items:
    if names.endswith(".txt"):
        newlist.append(names)


firstfile = pd.read_csv(path_in + '/' + newlist[0])
stations = firstfile['Station']




for station in stations:
    output = pd.DataFrame()

    for i in range(len(newlist)):
        data = pd.read_csv(path_in + '/' + newlist[i])
        month = data.loc[data['Station'] == station]
        month['Month'] = i+1
        output = output.append(month)    
    
    output.to_csv(path_out + '/' + station +  '_emi.csv')
    
    
path_in = 'D:/Uni/Masterarbeit/Emissivity_stations/Changed2/station_emis/'

items = os.listdir(path_in)

newlist = []
for names in items:
    if names.endswith(".csv"):
        newlist.append(names)
        
for i in range(len(newlist)):
        data = pd.read_csv(path_in + '/' + newlist[i])
        emi29 = data['[3600x7200] Emis_29 MODIS_MONTHLY_0.05DEG_CMG_LST (8-bit unsigned integer)']
        plt.plot(emi29)