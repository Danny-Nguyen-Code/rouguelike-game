from typing import Optional #denotes something that can be set to type:None
import tcod.event #only need event from tcod

from actions import Action, EscapeAction, MovementAction

#subclsas of EventDispatch, allows to send an event its proper method based on type of event
class EventHandler(tcod.event.EventDispatch[Action]):
    #quit program when 'X' is pressed in window
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    #method receives key press events and returns either Action subclass or None if no valid key pressed
    def ev_keydown(self, event: tcod.event.Keydown) -> Optional[Action]:
        #var holds subclass of Action, if no key pressed -> None
        action: Optional[Action] = None
        #holds actual key press w/o modifiers
        key = event.sym
        #if/else for key pressed
        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key ==tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        return action
