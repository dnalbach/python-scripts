class Player:
    x = 1
    y = 1

    def update_position(self, direction, addition):
        if addition :
            if direction == "x" and self.x < 80 :
                self.x += 1
            if direction == "y" and self.y < 20 :
                self.y += 1
        else :
            if direction == "x" and self.x > 1 :
                self.x -= 1
            if direction == "y" and self.y > 1 :
                self.y -= 1