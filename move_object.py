from os import system
import time
import keyboard
import random

system('clear')

x = 1
y = 1
wall_character = "@"
player_character = "*"
fruit_x = 0
fruit_y = 0
coordinate_dictionary = {}

def set_player_start():
    coordinate_dictionary[keyname] = { "is_wall": True }

def build_arena(player_x, player_y):
    global coordinate_dictionary
    iy = 0
    while iy < 22 :
        ix = 0
        # This if condition does the top and bottom row walls
        if iy == 0 or iy == 21 :
            while ix < 82 :
                keyname = "x" + str(ix) + "y" + str(iy)
                grid_object = { keyname: { "is_wall": True, "player": False }}
                coordinate_dictionary.update(grid_object)
                ix += 1
        # This covers the middle rows, where the player could be
        else :
            while ix < 82 :
                keyname = "x" + str(ix) + "y" + str(iy)
                exists = coordinate_dictionary.get(keyname)
                if exists :
                    grid_object = coordinate_dictionary.get(keyname)
                else :
                    grid_object = { keyname: { "is_wall": False, "player": False }}
                
                # Only the first and last position are wall positions
                if ix == 0 or ix == 81 :
                    grid_object.update({ "is_wall" : True })
                else :
                    if player_x == ix and player_y == iy :
                        grid_object.update({ "player" : True })
                    else :
                        grid_object.update({ "player" : False })
                    if fruit_x == ix and fruit_y == iy :
                        grid_object.update({ "item": { "name": "fruit", "icon": "+" }})
                    else :
                        grid_object.update({ "item": False })

                coordinate_dictionary.update(grid_object)
                ix += 1
        iy += 1
            

print "Press the arrow keys to move\n"

def draw_screen():
    global coordinate_dictionary
    iy = 0
    while  iy < 22 :
        row = [""] * 82
        ix = 0
        while ix < 82 :
            keyname = "x" + str(ix) + "y" + str(iy)
            current_position = coordinate_dictionary.get(keyname)           
            if current_position.get("is_wall") == True :
                row[ix] = wall_character
            elif current_position.get("player") == True :
                row[ix] = player_character
            elif current_position.get("item") :
                row[ix] = current_position.get("item").get("icon")
            else :
                row[ix] = " "
            ix += 1
        print "".join(row)
        iy += 1

def spawn_item():
    global fruit_x
    global fruit_y
    fruit_x = random.randint(1, 80)
    fruit_y = random.randint(1, 20)

def update_player_position(direction, addition):
    global x
    global y
    system('clear')
    if addition :
        if direction == "x" and x < 80 :
            x += 1
        if direction == "y" and y < 20 :
            y += 1
    else :
        if direction == "x" and x > 1 :
            x -= 1
        if direction == "y" and y > 1 :
            y -= 1

    
    keyname = "x" + str(x) + "y" + str(y)
    key_value = coordinate_dictionary.get(keyname)
    key_value["player"] = True
    coordinate_dictionary[keyname] = key_value
    
    print "x = ", x, ", y = ", y

    
    build_arena(x, y)
    draw_screen()

build_arena(1, 1)
spawn_item()

keyboard.add_hotkey("d", lambda: update_player_position("x", True))
keyboard.add_hotkey("a", lambda: update_player_position("x", False))
keyboard.add_hotkey("s", lambda: update_player_position("y", True))
keyboard.add_hotkey("w", lambda: update_player_position("y", False))

keyboard.wait()

