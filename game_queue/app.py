import os

from flask import Flask, render_template, redirect, url_for, request
from game_queue.queue import Game, find_queue

# Create and configure the app
app = Flask(__name__)

# Update config for the app
app.config.from_mapping(
    SECRET_KEY=os.environ['SECRET_KEY'],
)

# Create game instance
game = Game()
curr_queue = None
teams = []


# Page routing
@app.route('/', methods=['GET', 'POST'])
def index():
    """The index page.
    """
    return render_template('index.html')


@app.route('/loading', methods=['POST', 'GET'])
def loading():
    """The loading page for processing queues.
    """
    global curr_queue, teams
    data = request.form['name']
    new_queue = find_queue()
    if new_queue is not curr_queue:
        teams = []
    curr_queue = new_queue

    add = curr_queue.add_player(data)
    if curr_queue.is_full():
        return redirect(url_for('processing'))
    else:
        return redirect(url_for('queue'))


@app.route('/processing', methods=['POST', 'GET'])
def processing():
    """The processing page for loading pages.
    """
    global teams
    teams = curr_queue.shuffle_players()
    return redirect(url_for('queue'))


@app.route('/queue', methods=['POST', 'GET'])
def queue():
    """The queue page showing all users in queue.
    """
    return render_template('queue.html', queue=curr_queue, teams=teams)


if __name__ == '__main__':
    app.run()
