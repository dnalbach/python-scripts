def build(game_state):
    iy = 0
    while iy < 22 :
        ix = 0
        # This if condition does the top and bottom row walls
        if iy == 0 or iy == 21 :
            while ix < 82 :
                keyname = "x" + str(ix) + "y" + str(iy)
                grid_object = { keyname: { "is_wall": True, "player": False }}
                
                game_state.coordinates.update(grid_object)
                ix += 1
        # This covers the middle rows, where the player could be
        else :
            while ix < 82 :
                keyname = "x" + str(ix) + "y" + str(iy)
                exists = game_state.coordinates.get(keyname)
                if exists :
                    grid_object = game_state.coordinates.get(keyname)
                else :
                    grid_object = { keyname: { "is_wall": False, "player": False }}
                
                # Only the first and last position are wall positions
                if ix == 0 or ix == 81 :
                    grid_object.update({ "is_wall" : True })
                else :
                    if game_state.player.x == ix and game_state.player.y == iy :
                        grid_object.update({ "player" : True })
                    else :
                        grid_object.update({ "player" : False })
                    if game_state.fruit.x == ix and game_state.fruit.y == iy :
                        grid_object.update({ "item": { "name": "fruit", "icon": "+" }})
                    else :
                        grid_object.update({ "item": False })

                game_state.coordinates.update(grid_object)
                ix += 1
        iy += 1
            