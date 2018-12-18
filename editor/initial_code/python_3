def checkio(grid):
    # your code here
    return grid


if __name__ == '__main__':
    def checker(function, input_grid):
        input_copy = [row[:] for row in input_grid]
        result = function(input_copy)
        # Check the result...
        class Error(Exception): pass
        try:
            # 1) Check all types.
            if not (isinstance(result, (tuple, list)) and \
                    all(isinstance(row, (tuple, list)) for row in result) and \
                    all(isinstance(s, str) for row in result for s in row)):
                raise Error("The result must be a list/tuple "
                            "of lists/tuples of strings.")
            # 2) Check all sizes.
            nb_rows, nb_cols = len(input_grid), len(input_grid[0])
            if not (len(result) == nb_rows and \
                    all(len(row) == nb_cols for row in result)):
                raise Error("The result must have the same size as input data.")
            # 3) Check all tile types.
            types = {'.' : ('N', 'W', 'S', 'E'),
                     '--': ('NS', 'EW'),
                     '_|': ('NW', 'SW', 'EN', 'ES'),
                     'T' : ('ENW', 'ENS', 'ESW', 'NSW')}
            types = {dirs: tile_type for tile_type, sorted_dirs in types.items()
                                     for dirs in sorted_dirs}
            tile_type = lambda tile: types.get(''.join(sorted(tile)), None)
            for i in range(nb_rows):
                for j in range(nb_cols):
                    if tile_type(result[i][j]) != tile_type(input_grid[i][j]):
                        raise Error("You can only rotate the tiles, not change"
                                    f" them like you did at {(i, j)}.")
            # 4) Check if there is no closed loop / cycle.
            MOVES = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
            OPPOSITE = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}
            visited = {(i, j): False for i in range(nb_rows)
                                     for j in range(nb_cols)}
            def cycle_existence(new, old = None):
                """ Recursively search if there is a closed loop / cycle. """
                visited[old] = True
                i, j = new
                for nwse in result[i][j]:
                    di, dj = MOVES[nwse]
                    x, y = neighbor = i + di, j + dj
                    if not (0 <= x < nb_rows and 0 <= y < nb_cols):
                        raise Error(f"Tile {new} should not point outward.")
                    if OPPOSITE[nwse] not in result[x][y]:
                        raise Error(f"The tile {new} point to {neighbor}: "
                                    "it should be reciprocal.")
                    if visited[neighbor]:
                        if neighbor != old:
                            return True # closed loop / cycle found.
                    elif cycle_existence(neighbor, new): # Visit the neighbor.
                        return True
                visited[new] = True
            start = 0, 0
            if cycle_existence(start):
                raise Error("There must be no closed loop.")
            # 5) We should have visited all cells if it's entirely connected.
            if not all(visited.values()):
                miss = sum(not v for v in visited.values())
                raise Error(f"The result must be entirely connected. {miss} "
                            f"tiles are not connected to the tile at {start}.")
        except Error as error:
            print(error.args[0]) # error message
            return False
        return True

    GRIDS = (('3x3', [['NW' , 'S'  , 'W' ],
                      ['WSE', 'NWE', 'SE'],
                      ['N'  , 'NW' , 'E' ]]),

             ('6x3', [['W' , 'NW' , 'E'  ],
                      ['NS', 'WE' , 'S'  ],
                      ['WE', 'SE' , 'NWE'],
                      ['NE', 'NSE', 'SE' ],
                      ['WS', 'NSE', 'WS' ],
                      ['SE', 'W'  , 'E'  ]]),

             ('5x5', [['NW' , 'S'  , 'N'  , 'E'  , 'SE'],
                      ['NS' , 'W'  , 'NWE', 'NWE', 'SE'],
                      ['WSE', 'NSE', 'NWE', 'W'  , 'E' ],
                      ['WE' , 'WS' , 'WSE', 'SE' , 'WE'],
                      ['W'  , 'NE' , 'N'  , 'NW' , 'WS']]))

    for dim, grid in GRIDS:
        assert checker(checkio, grid), f'You failed with the grid {dim}.'

    print('The local tests are done. Click on "Check" for more real tests.')
