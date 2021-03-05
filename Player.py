class Player:
    # player IDs are the cardinal direction based on where they are sitting on a card table.
    # N and S are partners, similarly W and E
    player_id = ['N', 'S', 'W', 'E']

    def __init___(self, name, direction, hand, partner):
        self.direction = Player.player_id[direction]
        self.name = name
        self.hand = hand
        self.partner = partner
