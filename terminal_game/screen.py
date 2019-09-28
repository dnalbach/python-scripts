from os import system

class Screen:
    def draw(self, game_state):
        global system
        system("clear")
        print "Press the WASD keys to move\n"
        print "x = ", game_state.player.x, ", y = ", game_state.player.y

        iy = 0
        while  iy < 22 :
            row = [""] * 82
            ix = 0
            while ix < 82 :
                keyname = "x" + str(ix) + "y" + str(iy)
                current_position = game_state.coordinates.get(keyname)           
                if current_position.get("is_wall") == True :
                    row[ix] = game_state.game_characters.get("wall")
                elif current_position.get("player") == True :
                    row[ix] = game_state.game_characters.get("player")
                elif current_position.get("item") :
                    row[ix] = current_position.get("item").get("icon")
                else :
                    row[ix] = " "
                ix += 1
            print "".join(row)
            iy += 1