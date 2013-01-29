def nearest_4_neighbors_by_linear_position(grid_width, grid_height, position):
    """
    Returns the nearest 4 neighbors (Von Neumann neighborhood) of a focal
    position in a grid.

    Note: Toroidal grid used, meaning that focal positions on border of grid
    will have neighbors that 'wrap around' to the opposite boundary.
    """
    x, y = convert_linear_ordering_to_coordinate_pair(grid_width, position)
    neighbors = nearest_4_neighbors(grid_width, grid_height, x, y)
    return [convert_coordinate_pair_to_linear_ordering(grid_width, x, y)
            for (x, y) in neighbors]


def nearest_4_neighbors(grid_width, grid_height, x, y):
    return [correct_for_wrapping(grid_width, grid_height, neigh_x, neigh_y)
            for (neigh_x, neigh_y) in nearest_4_without_wrapping(x, y)]


def convert_linear_ordering_to_coordinate_pair(
        grid_width, position):
    """
    Converts a single dimensional position to a 2 dimensional
    coordinate pair
    """
    return (position % grid_width, position / grid_width)


def convert_coordinate_pair_to_linear_ordering(grid_width, x, y):
    """
    Inverse of convert_linear_ordering_to_coordinate_pair
    """
    return x + y * grid_width


def correct_for_wrapping(grid_width, grid_height, x, y):
    """
    Returns a coordinate pair that respects the grid boundaries
    """
    return (x % grid_width, y % grid_height)


def nearest_4_without_wrapping(x, y):
    """
    Returns a list of 4 pairs, denoting the (x, y) coordinates
    of the 4 nearest neighbors.
    """
    return [(x, y - 1),
            (x, y + 1),
            (x - 1, y),
            (x + 1, y)]
