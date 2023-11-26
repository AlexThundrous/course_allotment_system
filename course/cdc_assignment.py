import convert
import course
from course import *
import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import itertools
from professor.professor import *

cdc = convert.cdc
profs = convert.profs
assigned_course = []

for i in range(len(cdc)):
    profindex = []
    if(cdc[i] == "CS F111"):
        curse = course(cdc[i], 3)
    else:
        curse = course(cdc[i], 1)
    assigned_course.append(curse)
    for j in range(len(profs)):
        if(cdc[i] in profs[j].pref[0]):
            profindex.append([j, profs[j].pref[0].index(cdc[i])])
        elif(cdc[i] in profs[j].pref[2]):
            profindex.append([j, profs[j].pref[2].index(cdc[i])])
    for k in range(len(profindex)):
            assigned_course[i].set_prof(profs[profindex[k][0]], profindex[k][1])


for i in range(len(assigned_course)):
     assigned_course[i].set_avg()

assigned_course.sort(key=lambda x: len(x.profs)) 

G = nx.Graph()
G.add_node(tuple(profs), bipartite=0)
G.add_node(tuple(cdc), bipartite=1)
pos_graph = [G]


grouped_courses = {length: list(group) for length, group in itertools.groupby(assigned_course, key=lambda x: len(x.profs))}

for length, courses in grouped_courses.items():
    grouped_courses[length] = sorted(courses, key=lambda x: x.avg, reverse=True)

assigned_course = [course for length, courses in sorted(grouped_courses.items()) for course in courses]


for i in range(len(assigned_course)):
    prof = list(assigned_course[i].profs.keys())[0]
    if len(assigned_course[i].profs) == 1:
        if prof.value[0] <= 1:
            for j in range(len(pos_graph)):
                if(not prof.get_assigned(j) and not assigned_course[i].get_assigned(j)):
                    assigned_course[i].set_value(prof.value[0], j)
                    prof.set_value(assigned_course[i].value[0], j)
                    pos_graph[j].add_edge(prof, assigned_course[i].name)
        elif prof.value[0] == 1.5:
            for j in range(len(pos_graph)):
                if(not prof.get_assigned(j) and not assigned_course[i].get_assigned(j)):
                    assigned_course[i].set_value(1,j)
                    prof.set_value(assigned_course[i].value[0], j)
                    pos_graph[j].add_edge(prof, assigned_course[i].name)
    else:
        if assigned_course[i].value[0] == 1:
            first_assignment = True
            for prof in assigned_course[i].profs:
                for other_prof in assigned_course[i].profs:
                    if prof != other_prof and prof.value[0] <= 1.5 and other_prof.value[0] <= 1.5:
                        if first_assignment:
                            first_assignment = False
                            for m in range(len(pos_graph)):
                                if(not prof.get_assigned(m) and not other_prof.get_assigned(m) and not assigned_course[i].get_assigned(m)):
                                    assigned_course[i].set_value(1, m)
                                    prof.set_value(0.5, m)
                                    other_prof.set_value(0.5, m)
                                    pos_graph[m].add_edge(prof, assigned_course[i].name)
                                    pos_graph[m].add_edge(other_prof, assigned_course[i].name)
                                elif(not prof.get_assigned(m) and (isinstance(prof, x2) or isinstance(prof, x3))):
                                    assigned_course[i].set_value(1, m)
                                    prof.set_value(1, m)
                                    pos_graph[m].add_edge(prof, assigned_course[i].name)
                                elif(not other_prof.get_assigned(m) and (isinstance(other_prof, x2) or isinstance(other_prof, x3))):
                                    assigned_course[i].set_value(1, m)
                                    other_prof.set_value(1, m)
                                    pos_graph[m].add_edge(prof, assigned_course[i].name)
                        else:
                            G1 = pos_graph[0].copy()
                            edges_to_remove = [(node, course_node) for node, course_node in G1.edges() if course_node not in cdc]
                            G1.remove_edges_from(edges_to_remove)
                            G2 = G1.copy()
                            if(isinstance(prof, x2) or isinstance(prof, x3)):
                                 G2.add_edge(prof, assigned_course[i].name)
                                 prof.append_value(1)
                                 assigned_course[i].append_value(1)
                                 pos_graph.append(G2)
                                 for d in range(len(assigned_course)):
                                    for m in assigned_course[d].profs:
                                        if len(prof.value) > len(m.value):
                                            m.append_value(m.value[0])
                                    if len(assigned_course[i].value) > len(assigned_course[d].value):
                                        assigned_course[d].append_value(assigned_course[d].value[0])
                            elif(isinstance(other_prof, x2) or isinstance(other_prof, x3)):
                                 G2.add_edge(other_prof, assigned_course[i].name)
                                 other_prof.append_value(1)
                                 assigned_course[i].append_value(1)
                                 pos_graph.append(G2)
                                 for d in range(len(assigned_course)):
                                    for m in assigned_course[d].profs:
                                        if len(other_prof.value) > len(m.value):
                                            m.append_value(m.value[0])
                                    if len(assigned_course[i].value) > len(assigned_course[d].value):
                                        assigned_course[d].append_value(assigned_course[d].value[0])
                            G1.add_edge(prof, assigned_course[i].name)
                            G1.add_edge(other_prof, assigned_course[i].name)
                            prof.append_value(0.5)
                            other_prof.append_value(0.5)
                            assigned_course[i].append_value(1)
                            pos_graph.append(G1)
                            for d in range(len(assigned_course)):
                                    for m in assigned_course[d].profs:
                                        if len(prof.value) > len(m.value):
                                            m.append_value(m.value[0])
                                    if len(assigned_course[i].value) > len(assigned_course[d].value):
                                        assigned_course[d].append_value(assigned_course[d].value[0])

        elif assigned_course[i].value[0] == 3:
            first_assignment = True
            for prof in assigned_course[i].profs:
                for other_prof in assigned_course[i].profs:
                    for third_prof in assigned_course[i].profs:
                        if prof != other_prof != third_prof and prof.value[0] >= 1 and other_prof.value[0] >= 1 and third_prof.value[0] >= 1:
                            if first_assignment:
                                for m in range(len(pos_graph)):
                                    if(not prof.get_assigned(m) and not other_prof.get_assigned(m) and not assigned_course[i].get_assigned(m)):
                                        assigned_course[i].set_value(3, m)
                                        prof.set_value(1, m)
                                        other_prof.set_value(1, m)
                                        third_prof.set_value(1,m)
                                        pos_graph[m].add_edge(prof, assigned_course[i].name)
                                        pos_graph[m].add_edge(other_prof, assigned_course[i].name)
                                        pos_graph[m].add_edge(third_prof, assigned_course[i].name)
                                first_assignment = False
                            else:
                                G1 = pos_graph[0].copy()
                                edges_to_remove = [(node, course_node) for node, course_node in G1.edges() if course_node not in cdc]
                                G1.remove_edges_from(edges_to_remove)
                                G1.add_edge(prof, assigned_course[i].name)
                                prof.append_value(1)
                                other_prof.append_value(1)
                                third_prof.append_value(1)
                                assigned_course[i].append_value(3)
                                for d in range(len(assigned_course)):
                                    for m in assigned_course[d].profs:
                                        if len(prof.value) > len(m.value):
                                            m.append_value(m.value[0])
                                    if len(assigned_course[i].value) > len(assigned_course[d].value):
                                        assigned_course[d].append_value(assigned_course[d].value[0])
print("done")
# Printing the e dges
'''
print(len(pos_graph))
for i in range(len(pos_graph)):
    print("new possibility")
    for edge in pos_graph[i].edges():
        prof, course_node = edge
        if course_node in cdc and prof in profs:
            print(course_node, prof.name)
'''