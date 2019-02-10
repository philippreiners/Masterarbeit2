# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 20:11:08 2019

@author: Pille
"""

import plot_functions
import filter_functions

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt

stations = ['Bondville_IL','Boulder_CO','Desert_Rock_NV','Fort_Peck_MT']
titles = ['Bondville','Boulder','Desert Rock','Fort Peck']
fig = plt.figure()
plt.subplots_adjust(bottom=0, top=1, left=0.125, right=0.98)
plot_positions = [221,222,223,224]

for i in range(len(stations)):
    
    station = stations[i]
    path_extracted = 'F:/new_match/'
    
    path_in10 = path_extracted + '/' + '2010/' + station + '__matched_insitu.csv'
    path_in11 = path_extracted + '/' + '2011/' + station + '__matched_insitu.csv'
    path_in12 = path_extracted + '/' + '2012/' + station + '__matched_insitu.csv'
    path_in13 = path_extracted + '/' + '2013/' + station + '__matched_insitu.csv'
    
    data10 = pd.read_csv(path_in10) 
    data11 = pd.read_csv(path_in11) 
    data12 = pd.read_csv(path_in12) 
    data13 = pd.read_csv(path_in13) 
    
    data = data10.append(data13)
    data = data.append(data11)
    data = data.append(data12)

    data = filter_insitu_matches(data)
    fig = plot_lst(fig, titles[i], data, 'black', plot_positions[i])
    

path_plot = 'D:/Uni/Masterarbeit/Plots2/Plot_insitu_stations/insitu_stations_1.pdf'
fig.savefig(path_plot)  

stations = ['Goodwin_Creek_MS','Penn_State_PA','Sioux_Falls_SD']
titles = ['Goodwin Creek','Pennsylvania State University','Sioux Falls']
fig = plt.figure()
plt.subplots_adjust(bottom=0, top=1, left=0.125, right=0.98)
plot_positions = [221,222,223]

for i in range(len(stations)):
    
    station = stations[i]
    path_extracted = 'F:/new_match/'
    
    path_in10 = path_extracted + '/' + '2010/' + station + '__matched_insitu.csv'
    path_in11 = path_extracted + '/' + '2011/' + station + '__matched_insitu.csv'
    path_in12 = path_extracted + '/' + '2012/' + station + '__matched_insitu.csv'
    path_in13 = path_extracted + '/' + '2013/' + station + '__matched_insitu.csv'
    
    data10 = pd.read_csv(path_in10) 
    data11 = pd.read_csv(path_in11) 
    data12 = pd.read_csv(path_in12) 
    data13 = pd.read_csv(path_in13) 
    
    data = data10.append(data13)
    data = data.append(data11)
    data = data.append(data12)

    data = filter_insitu_matches(data)
    fig = plot_lst(fig, titles[i], data, 'black', plot_positions[i])
    
path_in10 = 'F:/new_match/Africa/2010/Rust_mijn_Ziel__matched_insitu.csv'
path_in13 = 'F:/Extracted_Data/Africa/2013/Variables/Match/Heimat__matched_insitu.csv'

data10 = pd.read_csv(path_in10)
data13 = pd.read_csv(path_in13)
data = data10.append(data13)
data = filter_insitu_matches(data)
fig = plot_lst(fig, 'Heimat/Rust mijn Ziel', data, 'black', 224)
path_plot = 'D:/Uni/Masterarbeit/Plots2/Plot_insitu_stations/insitu_stations_2.pdf'
fig.savefig(path_plot)  

