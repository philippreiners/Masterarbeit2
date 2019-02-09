# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:06:08 2018

@author: rein_pl
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt



path_extracted = 'F:/new_match/'
path_out =  'D:/Uni/Masterarbeit/Plots2/'

path_in10 = path_extracted + '/' + '2010/'
path_in11 = path_extracted + '/' + '2011/'
path_in12 = path_extracted + '/' + '2012/'
path_in13 = path_extracted + '/' + '2013/'



items = os.listdir(path_in13)


newlist = []
for names in items:
    if names.endswith(".csv"):
        newlist.append(names)

all_stations = pd.DataFrame()
all_stations_before = pd.DataFrame()

for filename in newlist:
    
    station_name = filename[:-4]
    print(station_name)
    station_name = station_name.replace('_matched_insitu', '')
    path_plot = path_out + '/' +  station_name + '.pdf'

    data10 = pd.read_csv(path_in10 + '/' + filename)
    data11 = pd.read_csv(path_in11 + '/' + filename)
    data12 = pd.read_csv(path_in12 + '/' + filename)
    data13 = pd.read_csv(path_in13 + '/' + filename)
    
    data = data10.append(data13)
    data = data.append(data11)
    data = data.append(data12)
    
    count_before = len(data['Jahr'])
    data_before = data
    all_stations_before = all_stations_before.append(data_before)
    data['dif'] = data['lst_mean'] - data['insitu_lst']
    data['abs_dif'] = abs(data['lst_mean'] - data['insitu_lst']) 
    data = data[data.abs_dif < 10]
    
    data = data[data.lst_uncertainty < 2]
    #data = data[data.lst_sigma < 10]
    data = data[data.quality_flags_L1b == 0]
    data['Other_error'] = data.lst_uncertainty - data.lst_sigma
    data = data[data.Other_error < 0.5]
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
    ax.plot(data_before['insitu_lst'], data_before['lst'], '+', color = 'red')
    ax.plot(data['insitu_lst'], data['lst_mean'], '+', color = 'black')
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
    

    all_stations = all_stations.append(data)

count_before = len(all_stations_before['Jahr'])
mad = np.mean(all_stations['abs_dif'])
ad = np.mean(all_stations['dif'])
sigma_error =  np.std(all_stations['dif'])
n = len(all_stations['dif'])
comp = n/count_before
rmse = sqrt(mean_squared_error(all_stations['insitu_lst'], all_stations['lst_mean']))   
path_plot = path_out + '/' + 'all_stations.pdf'

fig = plt.figure()

ax = fig.add_subplot(111)
ax.plot(all_stations_before['insitu_lst'], all_stations_before['lst'], '+', color = 'red')
ax.plot(all_stations['insitu_lst'], all_stations['lst_mean'], '+', color = 'black')
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
  

def classify_unique(data,column_name):
    values = data[column_name].unique()
    return_list = list()
    for i in range(len(values)):
        return_list.append(data[data[column_name]==values[i]])
    return return_list


def plot_classified_lst(classified, path_plot):
    
    data = classified[0]
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

 




