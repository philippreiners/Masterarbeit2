# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 13:38:36 2019

@author: Pille
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt


path_in = 'F:/From_TIMELINE_Validation/SURFRAD_files/'
path_plot = 'D:/Uni/Masterarbeit/Plots2/'
station = "Bondville_IL"
years = ["2010","2011","2012","2013"]

data = pd.DataFrame()
i = 0
xticks = list()
for year in years:
    path_data = path_in + '/' + 'SURFRAD_'+ station + "_" + year + '.csv'
    year_data = pd.read_csv(path_data)
    year_data['pixel_times'] = year_data['pixel_times'] + 365*i
    xticks.append(365*i)
    i = i + 1
    data = data.append(year_data, ignore_index = True)


data_filtered = data[data['qual_dw_infrared']==0]
data_filtered = data_filtered[data['qual_uw_ir']==0]



fig = plt.figure()
ax = fig.add_subplot(111)
 
ax.plot(data['pixel_times'],data['station_lst'], '+', color = 'red')
ax.plot(data_filtered['pixel_times'],data_filtered['station_lst'], '+', color = 'black')

ax.set_xlabel('Year')
ax.set_ylabel('SURFARAD LST [K]')
ax.set_xlim(-50,i*365+50)
ax.set_ylim(240,340)
ticks = ax.get_xticks
ax.set_xticks(xticks)
ax.set_xticklabels(years)
fig.savefig(path_plot + '/' + 'SURFRAD_' + station + '.png')
