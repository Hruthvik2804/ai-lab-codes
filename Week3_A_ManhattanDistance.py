import heapq

# Define the goal state for the puzzle
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

# Helper function to calculate the Manhattan distance heuristic
def manhattan_distance(state, goal_state):
    """Calculate the Manhattan distance heuristic."""
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                # Get current tile number (1-8)
                value = state[i][j]
                # Find its goal position in the goal state
                goal_x, goal_y = divmod(value, 3)
                # Calculate Manhattan distance
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def is_goal(state):
    """Check if the current state is the goal state."""
    return state == goal_state

def get_neighbors(state):
    """Generate neighbors for a given state."""
    neighbors = []
    # Find the position of the empty space (0)
    x, y = [(ix, iy) for ix, row in enumerate(state) for iy, i in enumerate(row) if i == 0][0]
    # Possible moves: up, down, left, right
    moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    for move_x, move_y in moves:
        if 0 <= move_x < 3 and 0 <= move_y < 3:
            # Create a copy of the current state and swap the empty space
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[move_x][move_y] = new_state[move_x][move_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# A* algorithm using Manhattan distance heuristic
def a_star_manhattan(initial_state):
    """A* algorithm implementation for 8-puzzle problem with Manhattan distance heuristic."""
    open_list = []
    closed_set = set()

    # Initial cost
    g = 0
    f = g + manhattan_distance(initial_state, goal_state)

    # Add the initial state to the open list
    heapq.heappush(open_list, (f, g, initial_state, []))

    while open_list:
        f, g, current_state, path = heapq.heappop(open_list)

        if is_goal(current_state):
            return path + [current_state]

        closed_set.add(tuple(map(tuple, current_state)))

        for neighbor in get_neighbors(current_state):
            if tuple(map(tuple, neighbor)) in closed_set:
                continue

            new_g = g + 1
            new_f = new_g + manhattan_distance(neighbor, goal_state)
            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [current_state]))

    return None

# Helper function to print a state
def print_state(state):
    for row in state:
        print(row)
    print()

# Initial state
initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]

# Run the A* algorithm with Manhattan distance heuristic
print("Solution using Manhattan distance heuristic:")
solution_manhattan = a_star_manhattan(initial_state)
if solution_manhattan:
    for step in solution_manhattan:
        print_state(step)
else:
    print("No solution found using Manhattan distance heuristic.")

