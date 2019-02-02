import os

from flask import Flask, render_template, redirect, url_for
from game_queue.forms import UsernameForm

# Create and configure the app
app = Flask(__name__)

# Update config for the app
app.config.from_mapping(
    SECRET_KEY=os.environ['SECRET_KEY'],
)


# Page routing
@app.route('/', methods=['GET', 'POST'])
def index():
    """The index page.
    """
    form = UsernameForm()
    if form.validate_on_submit():
        return redirect(url_for('queue'))

    return render_template('index.html')


@app.route('/loading')
def loading():
    """The loading page while waiting for queues.
    """
    return render_template('loading.html')


@app.route('/queue')
def queue():
    """The queue page showing all users in queue.
    """
    return render_template('queue.html')


if __name__ == '__main__':
    app.run()
