import requests
import json


def run():
    r = requests.get('http://127.0.0.1:5000/game/new')
    game = json.loads(r.text)

    game_over = False
    while not game_over:
        r = requests.get('http://127.0.0.1:5000/game/{}/level/new'.format(game['id']))
        level = json.loads(r.text)
        guess = input("Give me a word that starts with {}: ".format(level['letter']))
        r = requests.get('http://127.0.0.1:5000/game/{}/level/{}/{}'.format(game['id'], level['letter'], guess))
        answer = json.loads(r.text)
        if answer['Winner!!!']:
            print("YOU'RE THE BEST")
            game_over = True
        elif answer['Right!']:
            print("NICE! Your Score is {}".format(answer['score']))
        else:
            print("GAME OVER\nYour Score was {}".format(answer['score']))
            game_over = True


def multirun():
    r = requests.get('http://127.0.0.1:5000/multigame/new')
    game = json.loads(r.text)

    game_over = False
    while not game_over:
        r = requests.get('http://127.0.0.1:5000/multigame/level/new')
        level = json.loads(r.text)
        guess = input("Give me a word that starts with {}: ".format(level['letter']))
        r = requests.get('http://127.0.0.1:5000/multigamegame/level/{}/{}'.format(level['letter'], guess))
        answer = json.loads(r.text)
        if answer['Winner!!!']:
            print("YOU'RE THE BEST")
            game_over = True
        elif answer['Right!']:
            print("NICE! Your Score is {}".format(answer['score']))
        else:
            print("GAME OVER\nYour Score was {}".format(answer['score']))
            game_over = True


if __name__ == '__main__':
    run()
