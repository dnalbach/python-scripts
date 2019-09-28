import fruit

class State:
    player = None
    game_characters = { "wall": "@", "player": "*" }
    coordinates = {}
    fruit = fruit.Fruit()