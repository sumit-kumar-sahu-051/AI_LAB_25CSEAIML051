def bfs(graph, start_code, target_node) :
    visited = []
    queue = [start_code]

    while queue :
        current_node = queue.pop(0)
        if current_node not in visited :
            print(f"Exploring node : {current_node}")
            visited.append(current_node)

            # Check if target node is found

            if current_node == target_node :
                print(f"\nTarget node '{target_node}' found!")
                return visited

            for neighbour in graph.get(current_node, []) :
                if neighbour not in visited and neighbour not in queue :
                    queue.append(neighbour)

    print(f"\nTarget node '{target_node}' not found!")
    return visited


#-----------User input section----------------

print("-------------BFS Graph Traversal with Target Search----------")
print("\n----Build your graph-----")

student_graph = {}

#----------Get the total number of connections------------------

num_edges = int(input("\nHow many edges (connections) does your graph have : "))
print("\nEnter each edge separated by a space (e.g., A B) : ")

for i in range(num_edges):

    # Read the edge and split it into two variables

    u, v = input(f"Edge {i+1} : ").split()

    # Initialize the lists if the nodes don't exist yet

    if u not in student_graph :
        student_graph[u] = []

    if v not in student_graph :
        student_graph[v] = []

    # Add the connection (Undirected graph)

    student_graph[u].append(v)
    student_graph[v].append(u)

# Get the starting point

start = input("\nEnter the starting node for BFS : ")

# Get the target node

target = input("Enter the target node : ")

print(f"\nYour graph dictionary : {student_graph}")
print("\nStarting BFS traversal.......\n")

visited_nodes = bfs(student_graph, start, target)

print("\nVisited Nodes :", visited_nodes)