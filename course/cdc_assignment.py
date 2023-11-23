import convert
import course
from course import *
import networkx as nx
from networkx.algorithms import bipartite

cdc = convert.cdc
profs = convert.profs
assigned_course = []

for i in range(len(cdc)):
    max = 0
    profindex = []
    if(cdc[i] == "CS F111"):
        curse = course(cdc[i], 3)
    else:
        curse = course(cdc[i], 1)
    assigned_course.append(curse)
    for j in range(len(profs)):
        if(cdc[i] in profs[j].pref[0]):
            if(profs[j].pref[0].index(cdc[i]) >= max):
                max = profs[j].pref[0].index(cdc[i])
                l = [j, max]              
                profindex.append(l)
        elif(cdc[i] in profs[j].pref[2]):
             if(profs[j].pref[2].index(cdc[i]) >= max):
                max = profs[j].pref[2].index(cdc[i])
                l = [j, max]
                profindex.append(l)
    for k in range(len(profindex)):
        if(max == profindex[k][1]):
                assigned_course[i].set_prof(profs[profindex[k][0]])

assigned_course.sort(key=lambda x: len(x.profs))
G = nx.Graph()
G.add_node(tuple(profs), bipartite=0)
G.add_node(tuple(cdc), bipartite=1)
pos_graph = [G]
for i in range(len(assigned_course)):
    if len(assigned_course[i].profs) == 1:
        if(assigned_course[i].profs[0].value <= 1 and assigned_course[i].profs[0].get_assigned() == False and assigned_course[i].get_assigned() == False):
             assigned_course[i].set_value(assigned_course[i].profs[0].value)
             assigned_course[i].profs[0].set_value(assigned_course[i].value)
             for i in range(len(pos_graph)):
                 pos_graph[i].add_edge(assigned_course[i].profs[0], assigned_course[i].name)
        elif(assigned_course[i].profs[0].value == 1.5 and assigned_course[i].profs[0].get_assigned() == False and assigned_course[i].get_assigned() == False):
            assigned_course[i].set_value(1)
            assigned_course[i].profs[0].set_value(assigned_course[i].value)
            for i in range(len(pos_graph)):
                 pos_graph[i].add_edge(assigned_course[i].profs[0], assigned_course[i].name)
    else:
        if(assigned_course[i].value == 1):
            first_assignment = True
            for j in range(0, len(assigned_course[i].profs)):
                for k in range(j+1, len(assigned_course[i].profs)):
                    if(assigned_course[i].profs[j].value <= 1 and assigned_course[i].profs[k].value <= 1 and assigned_course[i].profs[j].get_assigned() == False and assigned_course[i].profs[k].get_assigned() == False and assigned_course[i].get_assigned() == False):
                        assigned_course[i].set_value(1)
                        assigned_course[i].profs[j].set_value(0.5)
                        assigned_course[i].profs[k].set_value(0.5)
                        if first_assignment:
                            for m in range(len(pos_graph)):
                                pos_graph[m].add_edge(assigned_course[i].profs[j], assigned_course[i].name)
                                pos_graph[m].add_edge(assigned_course[i].profs[k], assigned_course[i].name)
                                first_assignment = False
                        else:
                            G1 = G 
                            G1.add_edge(assigned_course[i].profs[j], assigned_course[i].name)
                            pos_graph.append(G1)
        elif(assigned_course[i].value == 3):
            first_assignment = True
            for j in range(0, len(assigned_course[i].profs)):
                for k in range(j+1, len(assigned_course[i].profs)):
                    for l in range(k+1, len(assigned_course[i].profs)):
                        if(assigned_course[i].profs[j].value >= 1 and assigned_course[i].profs[k].value >= 1 and assigned_course[i].profs[l].value >= 1 and assigned_course[i].profs[j].get_assigned() == False and assigned_course[i].profs[k].get_assigned() == False and assigned_course[i].profs[l].get_assigned() == False and assigned_course[i].get_assigned() == False):
                            assigned_course[i].set_value(3)
                            assigned_course[i].profs[j].set_value(1)
                            assigned_course[i].profs[k].set_value(1)
                            assigned_course[i].profs[l].set_value(1)
                            if first_assignment:
                                for m in range(len(pos_graph)):
                                    pos_graph[m].add_edge(assigned_course[i].profs[j], assigned_course[i].name)
                                    pos_graph[m].add_edge(assigned_course[i].profs[k], assigned_course[i].name)
                                    pos_graph[m].add_edge(assigned_course[i].profs[l], assigned_course[i].name)
                                first_assignment = False    
                            else:
                                G1 = G 
                                G1.add_edge(assigned_course[i].profs[j], assigned_course[i].name)
                                pos_graph.append(G1)
        else:
            first_assignment = True
            for j in range(0, len(assigned_course[i].profs)):
                if(assigned_course[i].profs[j].get_assigned() == False and assigned_course[i].get_assigned() == False):
                    assigned_course[i].set_value(0.5)
                    assigned_course[i].profs[j].set_value(0.5)
                    if first_assignment:
                        for m in range(len(pos_graph)):
                            pos_graph[m].add_edge(assigned_course[i].profs[j], assigned_course[i].name)
                    else:
                         G1 = G 
                         G1.add_edge(assigned_course[i].profs[j], assigned_course[i].name)
                         pos_graph.append(G1)
