from flask import Flask, jsonify
import random
import copy

app = Flask(__name__)

solutionset = {}
solutionset['A'] = set()
solutionset['A'].add("Apple")
solutionset['A'].add("Apron")
solutionset['A'].add("Account")
solutionset['B'] = set()
solutionset['B'].add("Bananna")
solutionset['B'].add("Blanket")
solutionset['B'].add("Bake")
solutionset['C'] = set()
solutionset['C'].add("Cake")
solutionset['C'].add("Cell")
solutionset['C'].add("Camara")

alphabet = ['A', 'B',
            'C']  # , 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
# 'V', 'W', 'X', 'Y', 'Z']

gstate = {}


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
    if word in gstate[gameid]['solutionset'][levelid]:
        gstate[gameid]['solutionset'][levelid].remove(word)
        if len(gstate[gameid]['solutionset'][levelid]) == 0:
            del gstate[gameid]['solutionset'][levelid]
            if len(gstate[gameid]['solutionset']):
                results['Winner!!!'] = True
        results['Right!'] = True
        gstate[gameid]['score'] +=1
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
