from math import *



def convert_size(size_bytes, unit="MB"):
   units = {
       "B" : 1,
       "KB": 1024,
       "MB": 1024 ** 2,
       "GB": 1024 ** 3,
   }

   return str(size_bytes/units[unit]) + unit

def display_state(state):
    output = "********STATE********"
    for i in range(0, len(state)):
        if i % 3 == 0:
            output += "\n"
        output += str(state[i]) + " "
    print(output)


moves = {
    'Up': -3,
    'Down': 3,
    'Left': -1,
    'Right': 1,
}


def expand(state, reverse=False):
    expansions = []
    zero_index = state.index(0)
    for move, pos_change in moves.items():
        new_index = zero_index + pos_change

        # Check valid moves to avoid edge wrapping
        if (move == 'Left' and zero_index % 3 == 0) or \
                (move == 'Right' and zero_index % 3 == 2) or \
                not (0 <= new_index < 9):
            continue
        new_state = state[:]
        new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
        # display_state(new_state)
        expansions.append([new_state, move])
    if reverse:
        expansions = reversed(expansions)
    return expansions


initial_state = [1, 2, 5,
                 3, 4, 7,
                 6, 0, 8]


# expand(initial_state)


def manh_dist(current_state, goal_state):
    distance = 0
    for i, tile in enumerate(current_state):
        if tile != 0:
            goal_index = goal_state.index(tile)
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_index, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


def euclidean_dist(current_state, goal_state):
    distance = 0
    for i, tile in enumerate(current_state):
        if tile != 0:
            goal_index = goal_state.index(tile)
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_index, 3)
            distance += sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
    return distance


def get_heuristic(neighbor, goal_state, heuristic):
    if heuristic == 'manhattan':
        h = manh_dist(neighbor, goal_state)
    elif heuristic == 'euclidean':
        h = euclidean_dist(neighbor, goal_state)
    return h
