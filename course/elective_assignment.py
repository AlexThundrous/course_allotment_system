import convert
import course
import cdc_assignment
from course import *
import networkx as nx
import matplotlib.pyplot as plts
import itertools
from cdc_assignment import pos_graph
from professor.professor import *

elective = convert.electives
profs = cdc_assignment.profs
assigned_course = []
total_course = cdc_assignment.total_course
assigned_course_cdc = cdc_assignment.assigned_course

for i in range(len(elective)):
    profindex = []
    curse = course(elective[i], 1)
    assigned_course.append(curse)

    for j in range(len(profs)):
        if(elective[i] in profs[j].pref[1]):
            profindex.append([j, profs[j].pref[1].index(elective[i])])
        if(elective[i] in profs[j].pref[3]):
            profindex.append([j, profs[j].pref[3].index(elective[i])])
    for k in range(len(profindex)):
        assigned_course[i].set_prof(profs[profindex[k][0]], profindex[k][1])

grouped_courses = {length: list(group) for length, group in itertools.groupby(assigned_course, key=lambda x: len(x.profs))}
for length, courses in grouped_courses.items():
    grouped_courses[length] = sorted(courses, key=lambda x: x.avg, reverse=True)

assigned_course = [course for length, courses in sorted(grouped_courses.items()) for course in courses]

for i in range(len(assigned_course)):
    for d in range(len(assigned_course_cdc[0].value)):
        assigned_course[i].append_value(assigned_course[i].value[0])

for i in range(len(assigned_course)):
    for prof in assigned_course[i].profs:
        for other_prof in assigned_course[i].profs: 
            if prof != other_prof and prof.value[0] <= 1.5 and prof.value[0] > 0 and other_prof.value[0] <= 1.5 and other_prof.value[0] > 0:
                for m in range(len(pos_graph)):
                    if(not prof.get_assigned(m) and not other_prof.get_assigned(m) and not assigned_course[i].get_assigned(m)):
                        assigned_course[i].set_value(1,m)
                        prof.set_value(0.5, m)
                        other_prof.set_value(0.5, m)
                        pos_graph[m].add_edge(prof, assigned_course[i].name)
                        pos_graph[m].add_edge(other_prof, assigned_course[i].name)
                    elif(not prof.get_assigned(m) and (isinstance(prof, x2) or isinstance(prof, x3)) and not assigned_course[i].get_assigned(m)):
                        assigned_course[i].set_value(1,m)
                        prof.set_value(1, m)
                        pos_graph[m].add_edge(prof, assigned_course[i].name)
                    elif(not other_prof.get_assigned(m) and (isinstance(other_prof, x2) or isinstance(other_prof, x3)) and not assigned_course[i].get_assigned(m)):
                        assigned_course[i].set_value(1,m)
                        other_prof.set_value(1, m)
                        pos_graph[m].add_edge(other_prof, assigned_course[i].name)
                        

print(len(pos_graph))
for i in range(len(pos_graph)):
    sum = 0
    for edge in pos_graph[i].edges():
        sum += 1
    if(sum >=33):
        print("new possibility")
        for edge in pos_graph[i].edges():
            prof, course_node = edge
            if course_node in total_course and prof in profs:
                print(course_node, prof.name)