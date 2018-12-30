'''
SearchSpace class
Represents a 2D map using Cartesian coordinates for implementing search algorithms, with a start and finish coordinates
'''


class SearchSpace:
    # TODO: Debate whether coordinates should be (Y, X) to match search space
    # States of a given search map
    # Coordinates are (X, Y)
    current_state = [None, None]
    initial_state = [None, None]
    end_state = [None, None]

    # Search space for the function.  Coordinates are non-negative, with (0,0) top left
    # First index is y coordinate, second is x
    search_space = []

    # Path cost for moving in a given direction.  Order is up, down, left, right
    path_cost = [0, 0, 0, 0]

    # Constructor
    # TODO: Make start and finish coordinates default to None and assign random values based off search space
    def __init__(self, input_map, input_path_cost, start_x, start_y, finish_x, finish_y):
        self.search_space = self.search_space.deepcopy(input_map)
        self.initial_state = [start_x, start_y]
        self.end_state = [finish_x, finish_y]
        self.path_cost = input_path_cost

    # Actions on a 2D map search space
    # Search implementations should have a check for valid actions based on current state
    def move_up(self):
        if self.current_state[1] - self.path_cost[0] < 0:
            self.current_state[1] = 0
        else:
            self.current_state[1] = self.current_state[1] - self.path_cost[0]

    def move_down(self):
        if self.current_state[1] + self.path_cost[1] > len(self.search_space):
            self.current_state[1] = len(self.search_space)
        else:
            self.current_state[1] = self.current_state[1] + self.path_cost[1]

    def move_left(self):
        if self.current_state[0] - self.path_cost[2] < 0:
            self.current_state[0] = 0
        else:
            self.current_state[0] = self.current_state[0] - self.path_cost[2]

    def move_right(self):
        if self.current_state[0] + self.path_cost[3] > len(self.search_space[self.current_state[1]]):
            self.current_state[0] = len(self.search_space[self.current_state[1]])
        else:
            self.current_state[0] = self.current_state[1] + self.path_cost[3]

    # Goal test to see if a given goal has been accomplished
    def goal_test(self):
        if self.initial_state[0] == self.end_state[0] and self.initial_state[1] == self.end_state[1]:
            return True
        else:
            return False


if __name__ == "__main__":
    print("Hello World!")
