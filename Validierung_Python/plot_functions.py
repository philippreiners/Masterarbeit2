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


def plot_lst(fig, title, data, color, plotnumber):
    data['dif'] = data['lst_mean'] - data['insitu_lst']
    data['abs_dif'] = abs(data['lst_mean'] - data['insitu_lst'])
    
    mad = np.mean(data['abs_dif'])
    md = np.mean(data['dif'])
    sigma_error =  np.std(data['dif'])
    n = len(data['dif'])
    rmse = sqrt(mean_squared_error(data['insitu_lst'], data['lst_mean']))
    
    fig.set_figheight(7.5)
    fig.set_figwidth(7.5)
    ax = fig.add_subplot(plotnumber)
    ax.plot(data['insitu_lst'], data['lst_mean'], '+', color = color)
    ax.plot(margin, margin)
    ax.set_xlabel('In-situ LST [K]')
    ax.set_ylabel('TIMELINE LST [K]')
    ax.set_xlim(255,330)
    ax.set_ylim(255,330)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.set_aspect('equal')
    ax.text(260,325, 'MAD = '+str(round(mad,2)))
    ax.text(260,320, 'n = '+str(n))
    ax.text(260,315, 'MD = '+str(round(md,2)))
    ax.text(260,310, 'RMSE = '+str(round(rmse,2)))
    ax.text(260,305, 'sig_err = '+str(round(sigma_error,2)))
    ax.set_title(title)
    return fig
    
def overplot_lst(fig, data, color):
    
    ax = fig.add_subplot(111)
    ax.plot(data['insitu_lst'], data['lst_mean'], '+', color = color)
    return fig

