from flask import Flask, render_template, redirect, url_for

from .forms import UsernameForm

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = UsernameForm()
    if form.validate_on_submit():
        return redirect(url_for('queue'))

    return render_template('index.html')


@app.route('/queue')
def queue():
    return 'queue'


if __name__ == '__main__':
    app.run()
