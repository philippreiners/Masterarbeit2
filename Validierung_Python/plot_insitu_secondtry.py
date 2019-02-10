# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 19:45:08 2019

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

stations = ['Bondville_IL','Boulder_CO','Desert_Rock_NV','Fort_Peck_MT',
            'Goodwin_Creek_MS','Penn_State_PA','Sioux_Falls_SD']
for station in stations:
    

    path_extracted = 'F:/new_match/'
    path_out =  'D:/Uni/Masterarbeit/Plots2/' + station + '/'
    
    if not os.path.exists(path_out):
        os.makedirs(path_out)
    
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
  
    '''
    plot by platform -----------------------------------------------------------
    '''
    data_classified = classify_unique(data, 'platform')
    titles = data['platform'].unique()
    titles.astype(str)
    fig = plt.figure()
    plt.subplots_adjust(bottom=0, top=1, left=0.125, right=0.95)
    
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
    plt.subplots_adjust(bottom=0, top=1, left=0.125, right=0.95)
    fig = plot_lst(fig, titles[0], data_classified[0], 'red', 221)
    fig = plot_lst(fig, titles[1], data_classified[1], 'red', 222)
    fig = plot_lst(fig, titles[2], data_classified[2], 'red', 223)
    fig = plot_lst(fig, titles[3], data_classified[3], 'red', 224)
    
    path_plot = path_out + '/' + station + '_year.pdf'
    fig.savefig(path_plot)
    
    '''
    plot by TCWV -----------------------------------------------------------
    '''
    tcwv_classes = np.array([0,5,15,25,35,45,55,65,75])
    data_classified = classify_by_values(data, 'tcwv', tcwv_classes)
    titles = tcwv_classes.astype(str)
    fig = plt.figure()
    plt.subplots_adjust(bottom=0, top=1, left=0.125, right=0.95)
    plot_positions = [221,222,223,224]
    for i in range(4):
        title = titles[i]+'-'+titles[i+1]
        if not data_classified[i].empty:
            fig = plot_lst(fig, title, data_classified[i], 'red', plot_positions[i])
     
    path_plot = path_out + '/' + station + '_tcwv_1.pdf'
    fig.savefig(path_plot)    
        
    for i in range(4,8):
        title = titles[i]+'-'+titles[i+1]
        if not data_classified[i].empty:
            fig = plot_lst(fig, title, data_classified[i], 'red', plot_positions[i-4])

    path_plot = path_out + '/' + station + '_tcwv_2.pdf'
    fig.savefig(path_plot)


    '''
    plot by view angle--------------------------------------------------------
    '''
    
    va_classes = np.array([0,10,30,50,70])
    data_classified = classify_by_values(data, 'sat_zenith', va_classes)
    titles = va_classes.astype(str)
    fig = plt.figure()
    plt.subplots_adjust(bottom=0, top=1, left=0.125, right=0.95)
    plot_positions = [221,222,223,224]
    for i in range(4):
        title = titles[i]+'-'+titles[i+1]
        if not data_classified[i].empty:
            fig = plot_lst(fig, title, data_classified[i], 'red', plot_positions[i])
     
    path_plot = path_out + '/' + station + '_va.pdf'
    fig.savefig(path_plot)    
    
    
    '''
    plot by LST--------------------------------------------------------
    '''
    
    lst_classes = np.array([270,285,300,315,330])
    data_classified = classify_by_values(data, 'lst_mean', lst_classes)
    titles = lst_classes.astype(str)
    fig = plt.figure()
    plt.subplots_adjust(bottom=0, top=1, left=0.125, right=0.95)
    plot_positions = [221,222,223,224]
    for i in range(4):
        title = titles[i]+'-'+titles[i+1]
        if not data_classified[i].empty:
            fig = plot_lst(fig, title, data_classified[i], 'red', plot_positions[i])
     
    path_plot = path_out + '/' + station + '_lst.pdf'
    fig.savefig(path_plot) 
    
      
    '''
    plot by LST--------------------------------------------------------
    '''
    
    sz_classes = np.array([0,30,50,70,90])
    data_classified = classify_by_values(data, 'sun_zenith', sz_classes)
    titles = sz_classes.astype(str)
    fig = plt.figure()
    plt.subplots_adjust(bottom=0, top=1, left=0.125, right=0.95)
    plot_positions = [221,222,223,224]
    for i in range(4):
        title = titles[i]+'-'+titles[i+1]
        if not data_classified[i].empty:
            fig = plot_lst(fig, title, data_classified[i], 'red', plot_positions[i])
     
    path_plot = path_out + '/' + station + '_sz.pdf'
    fig.savefig(path_plot)  
    
    
    
    
    
    
        

   