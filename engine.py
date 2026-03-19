from typing import Set, Iterable, Any
from tcod.context import Context
from tcod.console import Console
from entity import Entity
from input_handlers import EventHandler

class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler,
    game_map: GameMap, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            # Send event to ev_keydown() and return Action
            action = self.event_handler.dispatch(event)
            # Handling no action
            if action is None:
                continue
            
            action.perform(self, self.player)

    #draws screen, prints entities, presents context, then clears console
    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)   # Render console from Game Map

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)

        console.clear()