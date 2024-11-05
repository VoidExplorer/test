from queue import *
from funcs import *
import tracemalloc
import time


def display_state(state):
    output = "********STATE********"
    for i in range(0, len(state)):
        if i % 3 == 0:
            output += "\n"
        output += str(state[i]) + " "
    print(output)


def bfs(initial_state, goal_state):
    tracemalloc.start()
    start_time = time.time()
    queue = Queue()
    queue.put((initial_state, []))
    visited = set()
    expanded_nodes = 0
    max_depth = 0

    moves = {
        'Up': -3,
        'Down': 3,
        'Left': -1,
        'Right': 1
    }

    while not queue.empty():
        state, path = queue.get()
        display_state(state)
        # display_state(state)
        # print(queue.queue)
        if state == goal_state:
            max_ram_usage = convert_size(tracemalloc.get_traced_memory()[1])
            running_time = time.time() - start_time
            cost = len(path)
            print("cost:", cost)
            print("Expanded Nodes count: ", expanded_nodes)
            print("max ram usage:", max_ram_usage)
            print("running time:", running_time)
            print("max depth:", max_depth)
            tracemalloc.stop()
            return path

        zero_index = state.index(0)  # find position of 0
        expanded_nodes += 1
        max_depth = max(max_depth, len(path))

        for neighborNode in expand(state):
            # Add new state to stack if not visited
            neighbor, move = neighborNode[0], neighborNode[1]
            neighbor_tuple = tuple(neighbor)
            if neighbor_tuple not in visited:
                # print("adding: ", neighbor)
                visited.add(neighbor_tuple)
                queue.put((neighbor, path + [move]))

    return "No solution found"


def dfs(initial_state, goal_state):
    tracemalloc.start()
    start_time = time.time()
    stack = LifoQueue()
    stack.put((initial_state, []))  # Store current state and the path to reach it
    visited = set()  # To avoid cycles
    visited.add(tuple(initial_state))
    expanded_nodes = 0
    max_depth = 0

    while not stack.empty():
        state, path = stack.get()
        display_state(state)
        max_depth = max(max_depth, len(path))
        # Check if the current state is the goal state
        if state == goal_state:
            max_ram_usage = convert_size(tracemalloc.get_traced_memory()[1],"GB")
            running_time = time.time() - start_time
            cost = len(path)
            print("cost:", cost)
            print("Expanded Nodes count: ", expanded_nodes)
            print("max ram usage:", max_ram_usage)
            print("running time:", running_time)
            print("max depth:", max_depth)
            tracemalloc.stop()
            return path

        expanded_nodes += 1
        print(expanded_nodes)
        for neighborNode in expand(state, reverse=True):
            # Add new state to stack if not visited
            neighbor, move = neighborNode[0], neighborNode[1]
            neighbor_tuple = tuple(neighbor)
            if neighbor_tuple not in visited:
                # print("adding: ", neighbor)
                visited.add(neighbor_tuple)
                stack.put((neighbor, path + [move]))

    return "No solution found"


def ast(initial_state, goal_state, heuristic):
    tracemalloc.start()
    start_time = time.time()
    q = PriorityQueue()
    q.put((0, initial_state, []))
    expanded_nodes = 0
    max_depth = 0

    visited = set()
    visited.add(tuple(initial_state))
    expanded_nodes = 0

    while not q.empty():
        cost, state, path = q.get()
        display_state(state)
        expanded_nodes += 1
        max_depth = max(max_depth, len(path))
        if state == goal_state:
            max_ram_usage = convert_size(tracemalloc.get_traced_memory()[1])
            running_time = time.time() - start_time
            cost = len(path)
            print("cost:", cost)
            print("Expanded Nodes count: ", expanded_nodes)
            print("max ram usage:", max_ram_usage)
            print("running time:", running_time)
            print("max depth:", max_depth)
            tracemalloc.stop()
            return path

        for neighborNode in expand(state):
            neighbor = neighborNode[0]
            move = neighborNode[1]
            if tuple(neighbor) not in visited:
                h = get_heuristic(neighbor, goal_state, heuristic)
                g = len(path) + 1
                f = h + g
                q.put((f, neighbor, path + [move]))
                visited.add(tuple(neighbor))
    return "No Path found"


initial_state = [1, 2, 5,
                 3, 4, 0,
                 6, 7, 8]
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# display_state(goal_state)
#
# # Run BFS
# solution = bfs(initial_state, goal_state)
# print("BFS Solution path:", solution)

solution = dfs(initial_state, goal_state)
print("DFS Solution path:", solution)

# solution = ast(initial_state, goal_state, "manhattan")
# print("AST Solution path:", solution)

# solution = ast(initial_state, goal_state, "euclidean")
# print("AST Solution path:", solution)
