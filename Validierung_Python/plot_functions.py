# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 19:43:39 2019

@author: Pille
"""

def classify_unique(data,column_name):
    values = data[column_name].unique()
    return_list = list()
    for i in range(len(values)):
        return_list.append(data[data[column_name]==values[i]])
    return return_list



def classify_by_values(data, column_name, values):
    return_list = list()
    for i in range(len(values)-1):
        int1 = values[i]
        int2 = values[i+1]
        condition = (data[column_name]>=int1) & (data[column_name]<int2)
        return_list.append(data[condition])
    return return_list


def plot_lst(fig, title, data, color, plotnumber):
    data['dif'] = data['lst_mean'] - data['insitu_lst']
    data['abs_dif'] = abs(data['lst_mean'] - data['insitu_lst'])
    
    mad = np.mean(data['abs_dif'])
    md = np.mean(data['dif'])
    sigma_error =  np.std(data['dif'])
    n = len(data['dif'])
    rmse = sqrt(mean_squared_error(data['insitu_lst'], data['lst_mean']))
    
    margin = np.array(range(75))+265
    xticks = np.array(range(8))*10+270
    yticks = np.array(range(8))*10+270
    
    fig.set_figheight(8)
    fig.set_figwidth(8)
    ax = fig.add_subplot(plotnumber)
    ax.plot(data['insitu_lst'], data['lst_mean'], '+', color = color)
    ax.plot(margin, margin)
    ax.set_xlabel('In-situ LST [K]')
    ax.set_ylabel('TIMELINE LST [K]')
    ax.set_xlim(265,340)
    ax.set_ylim(265,340)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.set_aspect('equal')
    ax.text(270,335, 'MAD = '+str(round(mad,2)))
    ax.text(270,330, 'n = '+str(n))
    ax.text(270,325, 'MD = '+str(round(md,2)))
    ax.text(270,320, 'RMSE = '+str(round(rmse,2)))
    ax.text(270,315, 'sig_err = '+str(round(sigma_error,2)))
    ax.set_title(title)
    return fig
    
def overplot_lst(fig, data, color):
    
    ax = fig.add_subplot(111)
    ax.plot(data['insitu_lst'], data['lst_mean'], '+', color = color)
    return fig

