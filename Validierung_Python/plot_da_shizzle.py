# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:22:47 2018

@author: Pille
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np






def plot_da_shizzle(data, appendix):    
    
    mon_days = [0,31,59,90,120,151,181,212,243,273,304,334]
    mon_names = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    
    plt.xlim(-10,370)
    plt.ylim(260,320)
    plt.xticks(mon_days, mon_names)
    plt.xlabel('Month')
    plt.ylabel('TIMELINE LST(red) / in situ LST(blue) [K]')
    plt.plot(data['Pixel_Time'], data['lst'], '+', color = 'red')
    plt.plot(data['insitu_times'], data['insitu_lst'], '+', color = 'blue')
    plt.tight_layout()
    plt.savefig(path_plot + '/' + station_name +  '_' + appendix + '.png')
    plt.clf()
     
    
    x = data['lst'] - data['insitu_lst']
    x = np.array(x)   
    if (len(x)>4):
        plt.ylabel('TIMELINE LST - in situ LST [K]')
        plt.ylim(-7.5,7.5)
        plt.boxplot(x)
        plt.savefig(path_plot + '/' + station_name + '_boxplot_' + appendix + '.png')
        plt.clf()
    
    mad = np.mean(abs(x))
    std_mad = np.std(abs(x))
    count = len(x)
    
    out_file = path_plot + '/' + station_name +  '_' + 'statistics_' + appendix + '.csv'
    file_out = open(out_file, 'w')
    
    file_out.write('MAD: ' + str(mad) + '\n')
    file_out.write('Count: ' + str(count) + '\n')
    file_out.write('Std_MAD: ' + str(std_mad))
    file_out.close()
 
    


path_in = 'D:/Masterarbeit/Final_Data/USA/2010/Variables_LST/Even_new_than_even_newer/Match/'


    



items = os.listdir(path_in)


newlist = []
for names in items:
    if names.endswith(".csv"):
        newlist.append(names)

all_stations = pd.DataFrame()



path_out = 'D:/Uni/Masterarbeit/Match/Result_Plots/'
if not os.path.exists(path_out):
    os.makedirs(path_out)

for filename in newlist:
    
    station_name = filename[:-4]
    print(station_name)
    station_name = station_name.replace('_matched_insitu', '')
    path_plot = path_out + '/' +  station_name + '/' 
    
    if not os.path.exists(path_plot):
        os.makedirs(path_plot)
        
    data = pd.read_csv(path_in + '/' + filename)
    all_stations = all_stations.append(data)
    plot_da_shizzle(data, 'unfiltered')

  
    data_new = data[data.quality_flags == 0]
    plot_da_shizzle(data_new, 'quality_flags')
    
    data_new = data[data.lst_uncertainty <= 1]
  
    data_new = data
    data_new['lst'] = data_new['lst_mean']
    data_new = data_new[data_new.lst_mean.notnull()]
    plot_da_shizzle(data_new, 'lst_mean')
    data_new = data_new[data_new.lst_sigma < 1]
    plot_da_shizzle(data_new, 'lst_sigma')
    


station_name = 'All_stations'

path_plot = path_out + '/' +  station_name + '/' 

if not os.path.exists(path_plot):
    os.makedirs(path_plot)
    
data = all_stations
plot_da_shizzle(data, 'unfiltered')

  
data_new = data[data.quality_flags == 0]
plot_da_shizzle(data_new, 'quality_flags')

data_new = data[data.lst_uncertainty <= 1]
  
data_new = data
data_new['lst'] = data_new['lst_mean']
data_new = data_new[data_new.lst_mean.notnull()]
plot_da_shizzle(data_new, 'lst_mean')
data_new = data_new[data_new.lst_sigma < 1]
plot_da_shizzle(data_new, 'lst_sigma')
    
    
    




