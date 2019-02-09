# -*- coding: utf-8 -*-
"""
Created on Fri Dec 07 17:20:18 2018

@author: rein_pl
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


path_modis_val = 'M:/Masterarbeit_PhilippReiners/USA/2012/Variables/MODIS_Validation_Files/'


items = os.listdir(path_modis_val)


newlist = []
for names in items:
    if names.endswith(".csv"):
        newlist.append(names)
        

i=0
numbers = np.array(range(12))*5
while i<len(numbers)-1:

    

    weelist = newlist[numbers[i]:numbers[i+1]]
    i=i+1
    print(len(newlist))
    
    data_list = list()
    xticks = list()
    MADs = list()
    Ns = list()
    fig, ax = plt.subplots()
    
    for filename in weelist:
        data = pd.read_csv(path_modis_val + '/' + filename)
        dif = data['lst'] - data['Modis_LST']
        data_list.append(np.array(dif))
        
        adif = abs(data['lst'] - data['Modis_LST'])
        mad = np.mean(adif)
        MADs.append(mad)
        
        n = len(dif)
        Ns.append(n)
        
        xticks.append(filename[25:33])
    
    ax.set_ylim(-30,30)
    ax.boxplot(data_list)
    ax.plot([0,0,0,0,0,0,0,0])
    plt.xticks([1,2,3,4,5],xticks)
    ax.set_xlabel('Month Day Hour Minute')
    ax.set_ylabel('TIMELINE LST - MODIS LST [K]')
    ax.text(0.75,25, 'n = '+str(Ns[0]),fontsize=8)
    ax.text(0.75,-25, 'MAD = '+str(round(MADs[0],2)),fontsize=8)
    ax.text(1.75,25, 'n = '+str(Ns[1]),fontsize=8)
    ax.text(1.75,-25, 'MAD = '+str(round(MADs[1],2)),fontsize=8)
    ax.text(2.75,25, 'n = '+str(Ns[2]),fontsize=8)
    ax.text(2.75,-25, 'MAD = '+str(round(MADs[2],2)),fontsize=8)
    ax.text(3.75,25, 'n = '+str(Ns[3]),fontsize=8)
    ax.text(3.75,-25, 'MAD = '+str(round(MADs[3],2)),fontsize=8)
    ax.text(4.75,25, 'n = '+str(Ns[4]),fontsize=8)
    ax.text(4.75,-25, 'MAD = '+str(round(MADs[4],2)),fontsize=8)
    plt.show()
    fig.savefig('D:/Test/MODIS_Plot_' + str(i) + '.pdf')










    
