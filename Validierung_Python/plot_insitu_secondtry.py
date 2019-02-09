# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 19:45:08 2019

@author: Pille
"""

import plot_functions

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt


station = 'Bondville_IL'
path_extracted = 'F:/new_match/'
path_out =  'D:/Uni/Masterarbeit/Plots2/'


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

data = data[data.lst_uncertainty < 2]
data = data[data.quality_flags_L1b == 0]
data = data[np.isfinite(data['lst_mean'])]

'''
plot by platform -----------------------------------------------------------
'''
data_classified = classify_unique(data, 'platform')
titles = data['platform'].unique()
titles.astype(str)
fig = plt.figure()
plt.subplots_adjust(bottom=5, top=6, left=2, right=3)
fig = plot_lst(fig, titles[0], data_classified[0], 'red', 221)
fig = plot_lst(fig, titles[1], data_classified[1], 'red', 222)
fig = plot_lst(fig, titles[2], data_classified[2], 'red', 223)
fig = plot_lst(fig, titles[3], data_classified[3], 'red', 224)

path_plot = path_out + '/' + station + '_platform.pdf'
fig.savefig(path_plot)

'''
plot by year -----------------------------------------------------------
'''
data_classified = classify_unique(data, 'Jahr')
titles = data['Jahr'].unique()
titles.astype(str)
fig = plt.figure()
plt.subplots_adjust(bottom=5, top=6, left=2, right=3)
fig = plot_lst(fig, titles[0], data_classified[0], 'red', 221)
fig = plot_lst(fig, titles[1], data_classified[1], 'red', 222)
fig = plot_lst(fig, titles[2], data_classified[2], 'red', 223)
fig = plot_lst(fig, titles[3], data_classified[3], 'red', 224)

path_plot = path_out + '/' + station + '_year.pdf'
fig.savefig(path_plot)