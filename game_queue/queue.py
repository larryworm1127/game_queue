import random


class Game:
    def __init__(self):
        self.queues = []

    def add_queue(self, queue):
        self.queues.append(queue)


class Queue:
    def __init__(self):
        self.players = []
        self.size = 4

    def add_player(self, player):
        if len(self.players) < self.size:
            self.players.append(player)
            return True

        return False

    def remove_player(self, player):
        self.players.remove(player)

    def shuffle_players(self):
        random.shuffle(self.players)
        team1 = self.players[:self.size // 2]
        team2 = self.players[self.size // 2:]

        return team1, team2

    def is_full(self):
        if self.players == 10:
            return True

        return False


def find_queue():
    from game_queue.app import game

    ret_queue = None
    for queue in game.queues:
        if not queue.is_full():
            ret_queue = queue
            break

    if ret_queue is None:
        ret_queue = Queue()
        game.add_queue(ret_queue)

    return ret_queue
