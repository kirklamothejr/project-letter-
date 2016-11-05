from flask import Flask,jsonify
import random

app = Flask(__name__)


@app.route('/game/new')
def newgame():
    game={}
    game['id']=str(random.randint(0, 10000000))
    return jsonify(game)


if __name__ == '__main__':
    app.run(debug=True)
