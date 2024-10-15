def depth_limited_search(node, goal, depth):
    if depth == 0 and node == goal:
        return node  # Goal found
    if depth > 0:
        for neighbor in get_neighbors(node):
            result = depth_limited_search(neighbor, goal, depth - 1)
            if result is not None:
                return result
    return None 
def iterative_deepening_search(start, goal, max_depth):
    for depth in range(max_depth):
        print(f"Searching at depth: {depth}")
        result = depth_limited_search(start, goal, depth)
        if result is not None:
            return result  
    return None  


def get_neighbors(node):
    neighbors = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': [],
        'F': [],
        'G': []
    }
    return neighbors.get(node, [])

start_node = 'A'  # Start node
goal_node = 'G'   # Goal node
max_depth = 3     # Maximum depth to search
result = iterative_deepening_search(start_node, goal_node, max_depth)

if result:
    print(f"Goal {goal_node} found!")
else:
    print(f"Goal {goal_node} not found within depth limit.")
