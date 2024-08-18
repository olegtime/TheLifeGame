from flask import Flask
from flask import render_template
from game import GameOfLife

app = Flask(__name__)

game_of_life = GameOfLife(25, 25)


@app.route("/")
def index():
    game_of_life.generate_universe()
    return render_template('index.html')


@app.route("/live")
def live():
    if game_of_life.generation > 0:
        game_of_life.form_new_generation()
    game_of_life.generation += 1
    return render_template('live.html', game_of_life=game_of_life)


if __name__ == "__main__":
    app.run(debug=True)


