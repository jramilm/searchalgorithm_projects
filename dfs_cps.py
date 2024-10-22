from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx

def dfs(course, graph, visited, stack, result):
    
    if visited[course] == -1:
        return False
    
    if visited[course] == 1:
        return True
    
    visited[course] = -1
    
    for prereq in graph[course]:
        if not dfs(prereq, graph, visited, stack, result):
            return False
    
    visited[course] = 1
    
    result.append(course)
    return True

def find_course_order(courses, prerequisites):
    graph = defaultdict(list)
    
    for prereq, course in prerequisites:
        graph[course].append(prereq)
    
    visited = {course: 0 for course in courses}  # 0 = unvisited, -1 = visiting, 1 = fully visited
    result = []  
    stack = [] 
    
    for course in courses:
        if visited[course] == 0: 
            if not dfs(course, graph, visited, stack, result):
                return "There is a cycle. Cannot complete the courses."
    
    return result[::-1]

def visualize_graph(graph, courses, title):
    G = nx.DiGraph()
    
    for course, prereqs in graph.items():
        for prereq in prereqs:
            G.add_edge(prereq, course)
    
    try:
        pos = nx.nx_agraph.graphviz_layout(G, prog="dot")  
    except:
        pos = nx.spring_layout(G, seed=49) 
    
    plt.figure(figsize=(12, 8))
    ax = plt.gca()
    ax.set_title(title)

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', arrows=True,
            arrowstyle='-|>', arrowsize=15, edge_color='gray')
    
    plt.show()

# Example courses and prerequisites. Feel free to manipulate this the way you want
courses = ["Math", "Physics", "Programming", "Algorithms", "Databases", 
            "Linear Algebra", "Data Structures", 
           "Operating Systems", "AI", "Machine Learning"]

prerequisites = [
    ("Math", "Physics"), ("Math", "Algorithms"), ("Physics", "Programming"),
    ("Programming", "Databases"), ("Algorithms", "Data Structures"),
    ("Data Structures", "Operating Systems"), ("Operating Systems", "AI"),
    ("AI", "Machine Learning"), ("Linear Algebra", "AI"), ("Linear Algebra", "Machine Learning")
]

graph = defaultdict(list)

course_order = find_course_order(courses, prerequisites)

if isinstance(course_order, str):
    print(course_order)
else:
    print("Topologically sorted course order:", course_order)

    sorted_graph = defaultdict(list)

    for i in range(len(course_order) - 1):
        sorted_graph[course_order[i]].append(course_order[i + 1])
    
    visualize_graph(sorted_graph, course_order, "Topologically Sorted Course Graph")
