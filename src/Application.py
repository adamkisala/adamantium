import logging
import logging.config

from controllers.LoggingController import LoggingController
from exception.ExceptionHandler import ExceptionHandler
from helpers.Constants import *
from factory.GameFactory import *
import controllers.GameController
import sys
from flask import Flask, Response, jsonify

app = Flask(__name__)
game_controller = None


@app.errorhandler(ExceptionHandler)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/", methods=['POST'])
def receive():
    if game_controller is None:
        raise ExceptionHandler("GAME_INSTANCE_NOT_RUNNING", 500)
    try:
        game_controller.play()
    except Exception as err:
        raise ExceptionHandler(err.args[0], 500)


def main(argv):
    if len(sys.argv) > 0:
        # logger.basicConfig(filename='data.log', filemode='w', level=logging.DEBUG)
        file = FileStream(argv[1])
        game_fac = GameFactory()
        game = game_fac.create_game(file)
        global game_controller
        game_controller = controllers.GameController.GameController(game)
        # game_controller.play()
        app.run()
    else:
        print(NO_GAME_DESCRIPTION)


if __name__ == '__main__':
    main(sys.argv)
