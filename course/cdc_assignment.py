import convert
import course
from course import *
import networkx as nx
import itertools
from professor.professor import *

cdc = convert.cdc
profs = convert.profs
assigned_course = []
El = convert.electives 

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

total_course = cdc + El
# Instead of creating a regular Graph, create a MultiGraph
G = nx.MultiGraph()
G.add_nodes_from(profs, bipartite=0)
G.add_nodes_from(total_course, bipartite=1)
pos_graph = [G]

grouped_courses = {length: list(group) for length, group in itertools.groupby(assigned_course, key=lambda x: len(x.profs))}
for length, courses in grouped_courses.items():
    grouped_courses[length] = sorted(courses, key=lambda x: x.avg, reverse=True)

assigned_course = [course for length, courses in sorted(grouped_courses.items()) for course in courses]

crash_test = ""


for i in range(len(assigned_course)):
    prof = list(assigned_course[i].profs.keys())[0]
    if len(assigned_course[i].profs) == 1:
        if prof.value[0] >= 1:
            for j in range(len(pos_graph)):
                if(not prof.get_assigned(j) and not assigned_course[i].get_assigned(j)):
                    assigned_course[i].set_value(1, j)
                    prof.set_value(assigned_course[i].value[0], j)
                    pos_graph[j].add_edge(prof, assigned_course[i].name)
        elif(isinstance(prof, x1)):
            crash_test = "Can't assign the cdc insufficient number of profs only being taken by" + prof.name 
            
    else:
        if assigned_course[i].value[0] == 1:
            first_assignment = True

            for prof in assigned_course[i].profs:
                for other_prof in assigned_course[i].profs: 
                    if prof != other_prof and prof.value[0] <= 1.5 and prof.value[0] > 0 and other_prof.value[0] > 0 and other_prof.value[0] <= 1.5:
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
                                    pos_graph[m].add_edge(other_prof, assigned_course[i].name)
                        else:
                            G1 = pos_graph[0].copy()
                            edges_to_remove = [(node, course_node) for node, course_node in G1.edges() if course_node == assigned_course[i].name]
                            G1.remove_edges_from(edges_to_remove)
                            G1.add_edge(prof, assigned_course[i].name)
                            G1.add_edge(other_prof, assigned_course[i].name)
                            prof.append_value(0.5)
                            other_prof.append_value(0.5)
                            assigned_course[i].append_value(1)
                            pos_graph.append(G1.copy())
                            for d in range(len(assigned_course)):
                                    for m in assigned_course[d].profs:
                                        if len(prof.value) > len(m.value):
                                            if(m == edges_to_remove[0][0] or m == edges_to_remove[1][0]):
                                                if(len(edges_to_remove) == 1):
                                                    m.append_value(m.value[0]+ 1)
                                                else:
                                                    m.append_value(m.value[0] + 0.5)
                                            else:
                                                m.append_value(m.value[0])
                                    if len(assigned_course[i].value) > len(assigned_course[d].value):
                                        assigned_course[d].append_value(assigned_course[d].value[0])
        elif assigned_course[i].value[0] == 3:
            first_assignment = True
            for prof in assigned_course[i].profs:
                for other_prof in assigned_course[i].profs:
                    for third_prof in assigned_course[i].profs:
                        if prof != other_prof != third_prof and third_prof != prof and prof.value[0] >= 1 and other_prof.value[0] >= 1 and third_prof.value[0] >= 1:
                            if first_assignment:
                                for m in range(len(pos_graph)):
                                    if(not prof.get_assigned(m) and not other_prof.get_assigned(m) and not third_prof.get_assigned(m) and not assigned_course[i].get_assigned(m)):
                                        assigned_course[i].set_value(3, m)
                                        prof.set_value(1, m)
                                        other_prof.set_value(1, m)
                                        third_prof.set_value(1, m)
                                        pos_graph[m].add_edge(prof, assigned_course[i].name)
                                        pos_graph[m].add_edge(other_prof, assigned_course[i].name)
                                        pos_graph[m].add_edge(third_prof, assigned_course[i].name)
                                first_assignment = False
                            else:
                                G1 = pos_graph[0].copy()
                                edges_to_remove = [(node, course_node) for node, course_node in G1.edges() if course_node == assigned_course[i].name]
                                G1.remove_edges_from(edges_to_remove)
                                G1.add_edge(prof, assigned_course[i].name)
                                G1.add_edge(other_prof, assigned_course[i].name)
                                G1.add_edge(third_prof, assigned_course[i].name)
                                prof.append_value(1)
                                other_prof.append_value(1)
                                third_prof.append_value(1)
                                assigned_course[i].append_value(3)
                                pos_graph.append(G1.copy())
                                for d in range(len(assigned_course)):
                                    for m in assigned_course[d].profs:
                                        if len(prof.value) > len(m.value):
                                            m.append_value(m.value[0])
                                    if len(assigned_course[i].value) > len(assigned_course[d].value):
                                        assigned_course[d].append_value(assigned_course[d].value[0])

prof_assignments = []
indices_to_remove = []   

for i in range(len(pos_graph)):
    sum_edges = len(pos_graph[i].edges())
    
    if sum_edges == len(pos_graph[0].edges()):
        prof_assignment = {}
        
        for prof in profs:
            prof_assignment[prof] = []

        for edge in pos_graph[i].edges():
            prof, course_node = edge
            if course_node in cdc and prof in profs:
                prof_assignment[prof].append(course_node)

        prof_assignments.append(prof_assignment)
    else:
        indices_to_remove.append(i)

for index in reversed(indices_to_remove):
    pos_graph.pop(index)
    for assigned_course_instance in assigned_course:
        assigned_course_instance.remove_value(index)
    for prof in profs:
        prof.remove_value(index)


for i in range(len(pos_graph)):
    for node,degree in dict(pos_graph[0].degree).items():
        if isinstance(node, Professor):
            if(isinstance(node, x1) and node.value[i] > 0 and degree == 0):
                node.value[i] = 0
                node.assigned[i] = True
            elif(isinstance(node, x2) and node.value[i] > 0 and degree == 1):
                node.value[i] = 0
                node.assigned[i] = True
            elif(isinstance(node, x3) and node.value[i] > 0 and degree == 2):
                node.value[i] = 0
                node.assigned[i] = True

with open("prof_cdc_assignments_output.txt", "w") as output_file:
    for i, prof_assignment in enumerate(prof_assignments):
        print(f"Graph {i+1} Prof Assignments:", file=output_file)
        for prof in prof_assignment:
            print(prof.name, file=output_file)
            print(prof_assignment[prof], file=output_file)
            print("\n", file=output_file)