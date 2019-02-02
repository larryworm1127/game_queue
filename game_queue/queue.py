import random

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

    def remove_player(self, player):
        self.players.remove(player)


    def shuffle_players(self):
        random.shuffle(self.players)
        team1 = self.players[0:4]
        team2 = self.players[5:9]

        return team1, team2
