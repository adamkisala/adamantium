from flask import Flask, jsonify
from flask import Response
from flask import request
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

import controllers.GameController
from controllers.DatabaseController import DatabaseController
from exception.ExceptionHandler import ExceptionHandler
from factory.GameFactory import *
from model.Dialogue import Dialogue
from serializers.Serializer import DialogueSerializer
from settings.db_settings import Base

app = Flask(__name__)

with app.app_context():
    """@:var GameController"""
    game_controller = None
    db_controller = DatabaseController()

    @app.errorhandler(ExceptionHandler)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response


    @app.route("/", methods=['POST'])
    def receive():
        data = request.json
        if 'dialogueId' not in data:
            raise ExceptionHandler("GAME_ID_NOT_FOUND", 500)
        try:
            start_dialogue(data.get('dialogueId'))
            # TODO return interaction move
            return Response("OK", 200)
        except Exception as err:
            code = err.args[0] if len(err.args) > 1 else 500
            message = err.args[1] if len(err.args) > 1 else err.args[0]
            raise ExceptionHandler(message, code)

    @app.route("/dialogue", methods=['POST', 'GET'])
    def dialogue():
        if request.method == 'GET':
            dialogue_repo = db_controller.session.query(Dialogue).all()
            response = []
            for dg in dialogue_repo:
                response.append(DialogueSerializer().serialize(dg))
            return jsonify(dialogues=response)
        elif request.method == 'POST':
            # TODO save to DB
            pass

    @app.route("/dialogue/<id>", methods=['GET'])
    def check_dialogue(id):
        game = get_game_from_db(id)
        return jsonify(id=game.id, description=game.dialogueDescription)

    def main():
        app.run()


    def start_dialogue(game_id: str):
        game_fac = GameFactory()
        game = get_game_from_db(game_id)
        input_stream = InputStream(game.dialogueDescription)
        game = game_fac.create_game(input_stream)
        global game_controller
        game_controller = controllers.GameController.GameController(game)
        return game_controller.play()


    def get_game_from_db(game_id: str):
        try:
            """@:var Dialogue dg"""
            dg = db_controller.session.query(Dialogue).filter(Dialogue.id == game_id).one()
        except NoResultFound:
            raise NoResultFound('ENTITY_NOT_FOUND', 404)
        except MultipleResultsFound:
            raise MultipleResultsFound('MULTIPLE_ENTITIES_WITH_SAME_ID', 500)
        return dg


    if __name__ == '__main__':
        main()
