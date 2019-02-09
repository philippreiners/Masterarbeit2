# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 17:41:05 2019

@author: Pille
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt
import datetime




path_plot =  'D:/Uni/Masterarbeit/Plots2/Heimat.pdf'

path_in10 = 'F:/new_match/Africa/2010/Rust_mijn_Ziel__matched_insitu.csv'
path_in13 = 'F:/Extracted_Data/Africa/2013/Variables/Match/Heimat__matched_insitu.csv'

data10 = pd.read_csv(path_in10)
data13 = pd.read_csv(path_in13)

data = data10.append(data13)

count_before = len(data['Jahr'])

data['dif'] = data['lst_mean'] - data['insitu_lst']
data['abs_dif'] = abs(data['lst_mean'] - data['insitu_lst']) 
data = data[data.abs_dif < 10]

data = data[data.lst_uncertainty < 2]
data = data[data.lst_sigma < 1]
data = data[data.quality_flags_L1b == 0]

mad = np.mean(data['abs_dif'])
ad = np.mean(data['dif'])
sigma_error =  np.std(data['dif'])
n = len(data['dif'])
comp = n/count_before
rmse = sqrt(mean_squared_error(data['insitu_lst'], data['lst_mean']))
#data = data[data.quality_flags == 0]
   
margin = np.array(range(75))+255
xticks = np.array(range(8))*10+260
yticks = np.array(range(8))*10+260

fig = plt.figure()

ax = fig.add_subplot(111)
 
ax.plot(data['insitu_lst'], data['lst_mean'], '+', color = 'blue')
ax.plot(margin, margin)
ax.set_xlabel('In-situ LST [K]')
ax.set_ylabel('TIMELINE LST [K]')
ax.set_xlim(255,330)
ax.set_ylim(255,330)
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.set_aspect('equal')
ax.text(260,325, 'AD = '+str(round(ad,2)))
ax.text(260,320, 'n = '+str(n))
ax.text(260,315, 'MAD = '+str(round(mad,2)))
ax.text(260,310, 'Comp = '+str(round(comp,3)))
ax.text(260,305, 'RMSE = '+str(round(rmse,2)))
ax.text(260,300, 'sig_err = '+str(round(sigma_error,2)))
fig.savefig(path_plot)


# Plot Evora

path_plot =  'D:/Uni/Masterarbeit/Plots2/Evora.pdf'

path_in10 = 'F:/Extracted_Data/Europe/2010/Variables/Match/Evora__matched_insitu.csv'


data = pd.read_csv(path_in10)


count_before = len(data['Jahr'])

data['dif'] = data['lst_mean'] - data['insitu_lst']
data['abs_dif'] = abs(data['lst_mean'] - data['insitu_lst']) 
data = data[data.abs_dif < 10]

data = data[data.lst_uncertainty < 2]
data = data[data.lst_sigma < 1]
#data = data[data.quality_flags_L1b == 0]

mad = np.mean(data['abs_dif'])
ad = np.mean(data['dif'])
sigma_error =  np.std(data['dif'])
n = len(data['dif'])
comp = n/count_before
rmse = sqrt(mean_squared_error(data['insitu_lst'], data['lst_mean']))
#data = data[data.quality_flags == 0]
   
margin = np.array(range(75))+255
xticks = np.array(range(8))*10+260
yticks = np.array(range(8))*10+260

fig = plt.figure()

ax = fig.add_subplot(111)
 
ax.plot(data['insitu_lst'], data['lst_mean'], '+', color = 'blue')
ax.plot(margin, margin)
ax.set_xlabel('In-situ LST [K]')
ax.set_ylabel('TIMELINE LST [K]')
ax.set_xlim(255,330)
ax.set_ylim(255,330)
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.set_aspect('equal')
ax.text(260,325, 'AD = '+str(round(ad,2)))
ax.text(260,320, 'n = '+str(n))
ax.text(260,315, 'MAD = '+str(round(mad,2)))
ax.text(260,310, 'Comp = '+str(round(comp,3)))
ax.text(260,305, 'RMSE = '+str(round(rmse,2)))
ax.text(260,300, 'sig_err = '+str(round(sigma_error,2)))
fig.savefig(path_plot)

# Calculate time difference

starttime = np.array(data['starttime'].values)
starttime = starttime.astype('|S10')

start_mins = list()
start_hours = list()

for i in range(len(starttime)):
    timestring = starttime[i]
    start_mins.append(timestring[-4:-2])
    start_hours.append(timestring[-6:-4])


end_mins = np.array(data['insitu_mins'])
end_hours = np.array(data['insitu_hours'])



for i in range(len(starttime)):
    startmin = int(start_mins[i])
    starthour = int(start_hours[i])
    endmin = int(end_mins[i])
    endhour = int(end_hours[i])
    start = datetime.datetime(100, 1, 1, starthour, startmin, 0)
    end = datetime.datetime(100, 1, 1, endhour, endmin, 0)
    time_dif = end - start
    print(start)
    print(end)
    print(time_dif)






