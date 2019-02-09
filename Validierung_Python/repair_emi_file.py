# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""






def repair_file(path_in, file, path_out):
    
    in_file = path_in + '/' + file
    lines = []
    for line in open(in_file):
        lines.append(line.rstrip('\n'))
    
    
    lines[1] = lines[1].replace('grassland, savannas', 'grassland savannas')
    lines[3] = lines[3].replace('needleleaved, evergreen', 'needleleaved evergreen')
    lines[7] = lines[7].replace('grassland, savannas', 'grassland savannas')
    
    out_file = path_out + '/' + file
    file_out = open(out_file, 'w')
    for i in range(len(lines)-1):
        file_out.write(lines[i] + '\n')
    
    file_out.close()


path_in = 'D:/Uni/Masterarbeit/Emissivity_stations/'
path_out = path_in + '/Changed2/'

items = os.listdir(path_in)

newlist = []
for names in items:
    if names.endswith(".txt"):
        newlist.append(names)



for i in range(len(newlist)):
    print(newlist[i])
    repair_file(path_in, newlist[i], path_out)