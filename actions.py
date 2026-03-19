from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

#Each subclass needs to implement its own version of perform method
class Action:
    def perform(self, engine: Engine, entity: Entity) -> None:
        """Perform action with objects needed for scope
        'engine' is the scope this action is being performed in
        'entity' is the object performing the action
        This method must not be overridden by Action subclasses
        """
        raise NotImplementedError()

# Raise SystemExit()
class EscapeAction(Action):
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()

# Check if move is in bounds and to a walkable tile, if either is true, then
# we return without double checking 
class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()
        self.dx = dx
        self.dy = dy

    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return # Destination is out of bounds
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return # Destination is blocked by tile
        
        entity.move(self.dx, self.dy)