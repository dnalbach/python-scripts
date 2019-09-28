from os import system
import keyboard # must 'pip install keyboard' before using
import time
import random
import arena
import player
import screen
import state

last_frame_time = 0
new_time = 0

def update_frame(game_state, screen):
    keyname = "x" + str(game_state.player.x) + "y" + str(game_state.player.y)
    key_value = game_state.coordinates.get(keyname)
    key_value["player"] = True
    game_state.coordinates[keyname] = key_value
       
    arena.build(game_state)
    screen.draw(game_state)

# Initialize game resources
screen = screen.Screen()
player = player.Player()
game_state = state.State()
game_state.player = player

# Begin game
system('clear')
arena.build(game_state)
screen.draw(game_state)

keyboard.add_hotkey("d", lambda: game_state.player.update_position( "x", True),  timeout=0.01)
keyboard.add_hotkey("a", lambda: game_state.player.update_position( "x", False), timeout=0.01)
keyboard.add_hotkey("s", lambda: game_state.player.update_position( "y", True),  timeout=0.01)
keyboard.add_hotkey("w", lambda: game_state.player.update_position( "y", False), timeout=0.01)

while True: 
    new_time = time.time()
    if new_time - last_frame_time > .02 : 
        update_frame(game_state, screen)
        last_frame_time = new_time
