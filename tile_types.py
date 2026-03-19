from typing import Tuple

import numpy as np 

# tile graphics structured type compatible with Console.tiles_rgb
# dtype creates data type that numpy can use, behaves similarly to struct in C
graphic_dt = np.dtype(
    [
        ("ch", np,int32),   # Character, translated from int to Unicode
        ("fg", "3B"),   # Foreground color, 3 unsigned bytes, for RGB colors
        ("bg", "3B"),   # Background color, similar to fg
    ]
)

# Tile struct used for statically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # Boolean that describes if player can walk across tile, True = tile can be walked over
        ("transparent", np.bool),   # Boolean that describes if tile blocks FOV, True = doesn't block
        ("dark", graphic_dt),   # Graphics for this when this tile is not in FOV
    ]
)

# Helper function for defining individual tile types
def new_tile(
    *,  # Enforce use of keywords, so parameter order doesn't matter
    walkable: int,
    transparent, int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Returns numpy array of one tile_dt element and returns it"""
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
)