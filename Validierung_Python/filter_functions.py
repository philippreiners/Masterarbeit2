# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 19:53:12 2019

@author: Pille
"""

def filter_insitu_matches(data):
    data = data[data.lst_uncertainty < 2]
    data = data[data.quality_flags_L1b == 0]
    data = data[np.isfinite(data['lst_mean'])]
    return data