import convert
import course
from course import *

cdc = convert.cdc
profs = convert.profs
assigned_course = []

for i in range(len(cdc)):
    max = 0
    profindex = []
    for j in range(len(profs)):
        if(cdc[i] in profs[j].pref[0]):
            if(profs[j].pref[0].index(cdc[i]) >= max):
                max = profs[j].pref[0].index(cdc[i])
                l = [j, max]
                profindex.append(l)
    for k in range(len(profindex)):
        if(max == profindex[k][1]):
            if(cdc[i] == "CS F111"):
                 curse = course(cdc[i], profs[profindex[k][0]], 3)
            else:
                 curse = course(cdc[i], profs[profindex[k][0]], 1)
            assigned_course.append(curse) 
            continue
     
for i in range(len(cdc)):
    max = 0
    profindex = []
    for j in range(len(profs)):
        if(cdc[i] in profs[j].pref[2]):
            if(profs[j].pref[2].index(cdc[i]) >= max):
                max = profs[j].pref[2].index(cdc[i])
                l = [j, max]
                profindex.append(l)
    for k in range(len(profindex)):
        if(max == profindex[k][1]):
            curse = course(cdc[i], profs[profindex[k][0]], 1)
            assigned_course.append(curse) 
            continue

            