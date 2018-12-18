"""
CheckiOReferee is a base referee for checking you code.
    arguments:
        tests -- the dict contains tests in the specific structure.
            You can find an example in tests.py.
        cover_code -- is a wrapper for the user function and additional operations before give data
            in the user function. You can use some predefined codes from checkio.referee.cover_codes
        checker -- is replacement for the default checking of an user function result. If given, then
            instead simple "==" will be using the checker function which return tuple with result
            (false or true) and some additional info (some message).
            You can use some predefined codes from checkio.referee.checkers
        add_allowed_modules -- additional module which will be allowed for your task.
        add_close_builtins -- some closed builtin words, as example, if you want, you can close "eval"
        remove_allowed_modules -- close standard library modules, as example "math"
checkio.referee.checkers
    checkers.float_comparison -- Checking function fabric for check result with float numbers.
        Syntax: checkers.float_comparison(digits) -- where "digits" is a quantity of significant
            digits after coma.
checkio.referee.cover_codes
    cover_codes.unwrap_args -- Your "input" from test can be given as a list. if you want unwrap this
        before user function calling, then using this function. For example: if your test's input
        is [2, 2] and you use this cover_code, then user function will be called as checkio(2, 2)
    cover_codes.unwrap_kwargs -- the same as unwrap_kwargs, but unwrap dict.
"""

from checkio import api
from checkio.signals import ON_CONNECT
from checkio.referees.io import CheckiOReferee
#from checkio.referees import cover_codes
#from checkio.referees import checkers

from tests import TESTS

def checker(input_grid, result):
    """
        Check if the result is similar to the input_grid
        and is an entirely connected network.
    """
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
        return False, error.args[0] # error message
    return True, "Great!"


api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests = TESTS,
        checker = checker,
        function_name = {
            "python": "checkio",
            "js": "checkio"
        }
        ).on_ready
    )
