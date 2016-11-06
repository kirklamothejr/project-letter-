from flask import Flask, jsonify,render_template, url_for
import random
import copy
import pickle

app = Flask(__name__)

fin = open('output.txt', "rb")
solutionset = pickle.load(fin)
fin.close()

gstate = {}


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/game/new')
def newgame():
    game = {}
    game['id'] = str(random.randint(0, 10000000))
    game['score']=0
    gstate[game['id']] = copy.copy(game)
    gstate[game['id']]['solutionset'] = copy.deepcopy(solutionset)
    return jsonify(game)


@app.route('/game/<gameid>/level/new')
def newlevel(gameid):
    level = {}
    remainings = list(gstate[gameid]['solutionset'].keys())
    level['letter'] = random.choice(remainings)
    return jsonify(level)


@app.route('/game/<gameid>/level/<levelid>/<word>')
def levelguess(gameid, levelid, word):
    results = {'Winner!!!': False}
    word = word.lower()
    if word in gstate[gameid]['solutionset'][levelid]:
        results['Right!'] = True
        gstate[gameid]['score'] +=1
        results['score']=gstate[gameid]['score']
        gstate[gameid]['solutionset'][levelid].remove(word)
        if len(gstate[gameid]['solutionset'][levelid]) == 0:
            del gstate[gameid]['solutionset'][levelid]
            if len(gstate[gameid]['solutionset']):
                results['Winner!!!'] = True
    else:
        results['Right!'] = False
        if len(gstate[gameid]['solutionset'][levelid]) < 5:
            results['missed_choices'] = list[gstate[gameid]['solutionset'][levelid]]
        else:
            results['missed_choices'] = random.sample(gstate[gameid]['solutionset'][levelid],5)
    results['score'] = gstate[gameid]['score']
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
