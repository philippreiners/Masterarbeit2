# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 18:30:36 2018

@author: Pille
"""

from osgeo import gdal,ogr
import struct
import pandas as pd
import os



def extract_emissivity(hdf_file, feat):
    station = feat.GetField(0)
    hdf_ds = gdal.Open(hdf_file, gdal.GA_ReadOnly)
    emi29 = gdal.Open(hdf_ds.GetSubDatasets()[13][0], gdal.GA_ReadOnly)
    emi31 = gdal.Open(hdf_ds.GetSubDatasets()[14][0], gdal.GA_ReadOnly)
    emi32 = gdal.Open(hdf_ds.GetSubDatasets()[15][0], gdal.GA_ReadOnly)
    val29 = extract_value(emi29, feat)
    val31 = extract_value(emi31, feat)
    val32 = extract_value(emi32, feat)
    data = {'Station': station, 'Emi29':val29[0], 'Emi31':val31[0], 'Emi32':val32[0]}
    return(data)

        

def extract_value(band, feat):

    
    gt=band.GetGeoTransform()
    rb=band.GetRasterBand(1)
    
    geom = feat.GetGeometryRef()
    mx,my=geom.GetX(), geom.GetY()  #coord in map units

    #Convert from map to pixel coordinates.
    #Only works for geotransforms with no rotation.
    px = int((mx - gt[0]) / gt[1]) #x pixel
    py = int((my - gt[3]) / gt[5]) #y pixel

    intval=rb.ReadAsArray(px,py,1,1)
    intval = intval[0] * 0.002 + 0.49
    return(intval)






shp_filename = 'D:/Masterarbeit/Final_Data/USA/Insitu_Data/Shapefile/insitu_stations_usa.shp'

path_in = 'D:/Masterarbeit/Final_Data/USA/2012/MODIS_emissivity/'
path_out = 'D:/Masterarbeit/Final_Data/USA/Emi_SURFRAD/2012/'

items = os.listdir(path_in)

hdf_files = []
for names in items:
    if names.endswith(".hdf"):
        hdf_files.append(names)

ds=ogr.Open(shp_filename)
lyr=ds.GetLayer()
    
for feat in lyr:
    dataframe = pd.DataFrame(columns=['Station', 'Emi29', 'Emi31', 'Emi32', 'Timecode'])
    station = feat.GetField(0)
    for hdf_file in hdf_files:
        timecode = hdf_file[9:16]
        hdf_file = path_in + '/' + hdf_file
        data = extract_emissivity(hdf_file, feat)
        data['Timecode'] = timecode
        dataframe = dataframe.append(data, ignore_index=True)
    
    dataframe['Month'] = dataframe.index +1
    dataframe.to_csv(path_out + '/' + station +  '_2010_emi.csv')
    


    

    