class Player:
    directions = ['N', 'S', 'W', 'E']

    def __init___(self, name, direction, hand):
        self.direction = Player.directions[direction]
        self.name = name