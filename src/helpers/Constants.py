import os

NO_GAME_DESCRIPTION = "Please provide game description"
COLON = ":"
OPEN_BRACE = "{"
CLOSE_BRACE = "}"
COMMA = ","
OPEN_BRACKET = "("
CLOSE_BRACKET = ")"
EXIT = "EXIT"
EMPTY = ""
DEBUG = True

# MoveEvaluator constants
NEXT = 'next'
NOT_NEXT = '!next'
FUTURE = 'future'
NOT_FUTURE = '!future'

# Basic roles
SPEAKER = "Speaker"
LISTENER = "Listener"

# InteractionMove json attribute keys
MOVE_ID = "move_id"
MOVE_NAME = "move_name"
ARTIFACT = "artifact"
ARTIFACT_KEY = "artifact_key"
ARTIFACT_ID = "artifact_id"
ARTIFACT_DATA = "artifact_data"
PLAYER_NAME = "player_name"
ROLE = "role"
FINAL = "final"

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Errors
WRONG_MESSAGE_FORMAT = "WRONG_MESSAGE_FORMAT"
MESSAGE_HAS_NO_ID = "MESSAGE_HAS_NO_ID"
