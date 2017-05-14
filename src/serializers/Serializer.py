from helpers.JsonSerializer import JsonSerializer
from model import Dialogue, InteractionMove


class DialogueSerializer(JsonSerializer):
    __attributes__ = ['id', 'dialogueDescription']
    __required__ = ['id', 'dialogueDescription']
    __attribute_serializer__ = dict()
    __object_class__ = Dialogue.Dialogue


class InteractionMoveSerializer(JsonSerializer):
    __attributes__ = ['playerName', 'moveName', 'artifact', 'role', 'final']
    __required__ = ['playerName', 'moveName']
    __attribute_serializer__ = dict()
    __object_class__ = InteractionMove.InteractionMove
