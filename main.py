#!/usr/bin/env python3
import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    #receive events and process them
    event_handler = EventHandler()

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)
            root_console.clear() #clear leftover @

            for event in tcod.event.wait():
                #send event to ev_keydown() and return Action
                action = event_handler.dispatch(event)
                #handling no action
                if action is None:
                    continue
                #if action is instance of MovementAction, move @ symbol
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy
                elif isistance(action, EscapeAction):
                    raise SystemExit()

if __name__ == "__main__":
    main()