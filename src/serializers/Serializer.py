from concrete.artifacts import Artifact
from helpers.JsonSerializer import JsonSerializer
from model import Dialogue, InteractionMove, GameStatus


class ArtifactSerializer(JsonSerializer):
    __attributes__ = ['data']
    __required__ = []
    __attribute_serializer__ = dict()
    __object_class__ = Artifact.Artifact


class DialogueSerializer(JsonSerializer):
    __attributes__ = ['id', 'dialogueDescription']
    __required__ = ['id', 'dialogueDescription']
    __attribute_serializer__ = dict()
    __object_class__ = Dialogue.Dialogue


class InteractionMoveSerializer(JsonSerializer):
    __attributes__ = ['relativeId', 'playerName', 'moveName', 'artifact', 'role', 'final']
    __required__ = ['playerName', 'moveName']
    __attribute_serializer__ = dict(artifact='artifact')
    __object_class__ = InteractionMove.InteractionMove

    def __init__(self):
        self.serializers['artifact'] = dict(
            serialize=lambda x:
            ArtifactSerializer().serialize(x),
            deserialize=lambda x:
            ArtifactSerializer().deserialize(x)
        )


class GameStatusSerializer(JsonSerializer):
    __attributes__ = ['id', 'dialogueId', 'turns_counter', 'new_turn', 'initial_turn', 'speakers', 'current_speaker',
                      'last_interaction_move', 'last_move', 'mandatory_moves', 'available_moves', 'past_moves',
                      'all_players_did_move', 'status']
    __required__ = ['id', 'dialogueId']
    __attribute_serializer__ = dict(last_interaction_move='last_interaction_move', mandatory_moves='mandatory_moves',
                                    available_moves='available_moves')
    __object_class__ = GameStatus.GameStatus

    def __init__(self):
        self.serializers['last_interaction_move'] = dict(
            serialize=lambda x:
            InteractionMoveSerializer().serialize(x),
            deserialize=lambda x:
            InteractionMoveSerializer().deserialize(x)
        )
        self.serializers['available_moves'] = dict(
            serialize=lambda d:
            {key: [InteractionMoveSerializer().serialize(v) for v in d[key]] for key in d.keys()},
            deserialize=lambda d:
            {key: [InteractionMoveSerializer().deserialize(v) for v in d[key]] for key in d.keys()},
        )
        self.serializers['mandatory_moves'] = dict(
            serialize=lambda d:
            {key: [InteractionMoveSerializer().serialize(v) for v in d[key]] for key in d.keys()},
            deserialize=lambda d:
            {key: [InteractionMoveSerializer().deserialize(v) for v in d[key]] for key in d.keys()},
        )
