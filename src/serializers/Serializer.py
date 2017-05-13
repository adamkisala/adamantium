from helpers.JsonSerializer import JsonSerializer
from model import Dialogue


class DialogueSerializer(JsonSerializer):
    __attributes__ = ['id', 'dialogueDescription']
    __required__ = ['id', 'dialogueDescription']
    __attribute_serializer__ = dict()
    __object_class__ = Dialogue
