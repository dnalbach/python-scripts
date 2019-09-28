import keyboard # must 'pip install keyboard' before using
import time
import state
import curses

last_frame_time = 0
new_time = 0
endless_loop = True

# Initialize game resources
game_state = state.State()

# Begin game
curses.initscr()
curses.savetty()
window = curses.newwin(22, 82, 0, 0)
curses.noecho()
curses.curs_set(0)
window.border()

def end_program():
    global endless_loop
    endless_loop = False
    curses.endwin()
    curses.resetty()

keyboard.add_hotkey("d", lambda: game_state.player.update_position( "x", True),  timeout=0.01)
keyboard.add_hotkey("a", lambda: game_state.player.update_position( "x", False), timeout=0.01)
keyboard.add_hotkey("s", lambda: game_state.player.update_position( "y", True),  timeout=0.01)
keyboard.add_hotkey("w", lambda: game_state.player.update_position( "y", False), timeout=0.01)
keyboard.add_hotkey("esc", end_program)

while endless_loop: 
    new_time = time.time()
    if new_time - last_frame_time > .02 : 
        window.clear()
        # Draw the fruit
        window.move(game_state.fruit.y, game_state.fruit.x)
        window.addstr(game_state.fruit.icon)
        # Draw the player
        window.move(game_state.player.y, game_state.player.x)
        window.addstr(game_state.player.icon)

        last_frame_time = new_time
        window.border()
        window.refresh()
