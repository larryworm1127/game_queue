class Game:

    def __init__(self):
        self.queues = []

    def add_queue(self, queue):
        self.queues.append(queue)


class Queue:

    def __init__(self):
        self.players = []
        self.size = 10

    def add_player(self, player):

        if self.players > self.size:
            self.players.append(player)
            return True

        return False

    def get_players(self):
        return self.players

    def remove_player(self, player):
        self.players.remove(player)
        