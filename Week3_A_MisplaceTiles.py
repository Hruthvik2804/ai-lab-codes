import heapq

# Define the goal state for the puzzle
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

# Helper function to calculate the misplaced tiles heuristic
def misplaced_tiles(state, goal_state):
    """Calculate the number of misplaced tiles."""
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count

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

# A* algorithm using misplaced tiles heuristic
def a_star_misplaced(initial_state):
    """A* algorithm implementation for 8-puzzle problem with misplaced tiles heuristic."""
    open_list = []
    closed_set = set()

    # Initial cost
    g = 0
    f = g + misplaced_tiles(initial_state, goal_state)

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
            new_f = new_g + misplaced_tiles(neighbor, goal_state)
            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [current_state]))

    return None

# Helper function to print a state
def print_state(state):
    for row in state:
        print(row)
    print()

# Initial state
initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]

# Run the A* algorithm with misplaced tiles heuristic
print("Solution using misplaced tiles heuristic:")
solution_misplaced = a_star_misplaced(initial_state)
if solution_misplaced:
    for step in solution_misplaced:
        print_state(step)
else:
    print("No solution found using misplaced tiles heuristic.")

