from typing import Set, Iterable, Any
from tcod.context import Context
from tcod.console import Console
from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler

class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.player = player

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            #send event to ev_keydown() and return Action
            action = self.event_handler.dispatch(event)
            #handling no action
            if action is None:
                continue
            #if action is instance of MovementAction, move player
            if isinstance(action, MovementAction):
                self.player.move(dx=action.dx, dy=action.dy)
            elif isinstance(action, EscapeAction):
                raise SystemExit()

    #draws screen, prints entities, presents context, then clears console
    def render(self, console: Console, context: Context) -> None:
        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)

        console.clear()