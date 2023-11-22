import csv
import sys
from os.path import abspath, dirname
parent_dir = abspath(dirname(dirname(__file__)))
sys.path.append(parent_dir)
from professor.professor import *


data = []
with open('course_pref.csv', mode='r') as file:
   csvFile = csv.reader(file)
   for lines in csvFile:
      data.append(lines)
profs = []
cdc = []
electives = []
for i  in range(1, len(data)):
   pref = []
   ug_cdc = []
   hd_cdc = []
   ug_electives = []
   hd_electives = []
   course = ""
   for j in data[i][1]:
      if(j == ';'):
        ug_cdc.append(course)
        if course not in cdc:          
            cdc.append(course)
        course = ""
        continue
      course += j
   for j in data[i][3]:
      if(j == ';'):
        hd_cdc.append(course)
        if course not in cdc:          
            cdc.append(course)
        course = ""
        continue
      course += j
   for j in data[i][2]:
      if(j == ';'):
        ug_electives.append(course)
        if course not in cdc:          
            electives.append(course)
        course = ""
        continue
      course += j
   for j in data[i][4]:
      if(j == ';'):
        ug_electives.append(course)
        if course not in cdc:          
            electives.append(course)
        course = ""
        continue
      course += j
   if(data[i][5] == 'x1'):
      pref.append(ug_cdc) 
      pref.append(ug_electives)
      pref.append(hd_cdc)
      pref.append(hd_electives)
      prof = x1(data[i][0], pref)
      profs.append(prof)
   elif(data[i][5] == 'x2'):
      pref.append(ug_cdc) 
      pref.append(ug_electives)
      pref.append(hd_cdc)
      pref.append(hd_electives)
      prof = x2(data[i][0], pref)
      profs.append(prof)
   else:
      pref.append(ug_cdc) 
      pref.append(ug_electives)
      pref.append(hd_cdc)
      pref.append(hd_electives)
      prof = x3(data[i][0], pref)
      profs.append(prof)  

for i in range(len(profs)):
   print(profs[i].name, profs[i].pref)  

      
