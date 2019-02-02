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


# Page routing
@app.route('/', methods=['GET', 'POST'])
def index():
    """The index page.
    """
    return render_template('index.html')


@app.route('/loading', methods=['POST', 'GET'])
def loading():
    """The loading page while waiting for queues.
    """
    data = request.form['name']
    curr_queue.add_player(data)
    return redirect(url_for('queue'))


@app.route('/queue', methods=['POST', 'GET'])
def queue():
    """The queue page showing all users in queue.
    """
    return render_template('queue.html', queue=curr_queue)


if __name__ == '__main__':
    app.run()
