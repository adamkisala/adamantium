from factory.ArtifactFactory import ArtifactFactory
from interface.IArtifact import IArtifact
from helpers.Constants import *


class InteractionMove:
    __counter = 0

    def __init__(self, move_id: int = None, move_name: str = EMPTY, artifact: str = EMPTY, player_name: str = EMPTY,
                 role: str = EMPTY, final: bool = False):
        if move_id is None:
            InteractionMove.__counter += 1
            self.__move_id = InteractionMove.__counter
        else:
            self.__move_id = move_id
        self.__move_type = move_name
        self.__artifact = ArtifactFactory.create_artifact(artifact)
        self.__player_id = player_name
        self.__role = role
        self.__final = final

    def __set_player_id(self, player_id_tmp: str = None):
        self.__player_id = player_id_tmp

    def __get_player_id(self) -> str:
        return self.__player_id

    def __get_move_id(self) -> int:
        return self.__move_id

    def __set_move_id(self, move_id_tmp: int = None):
        self.__move_id = move_id_tmp

    def __set_move_type(self, move_type_tmp: str = None):
        self.__move_type = move_type_tmp

    def __get_move_type(self) -> str:
        return self.__move_type

    def __set_artifact(self, content_tmp: IArtifact = None):
        self.__artifact = content_tmp

    def __get_artifact(self) -> IArtifact:
        return self.__artifact

    def __set_role(self, role_tmp: str = None):
        self.__role = role_tmp

    def __get_role(self) -> str:
        return self.__role

    def __set_final(self, final_tmp: bool = None):
        self.__final = final_tmp

    def __get_final(self) -> bool:
        return self.__final

    player_name = property(__get_player_id, __set_player_id, None)
    move_id = property(__get_move_id, __set_move_id, None)
    move_name = property(__get_move_type, __set_move_type, None)
    artifact = property(__get_artifact, __set_artifact, None)
    role = property(__get_role, __set_role, None)
    final = property(__get_final, __set_final, None)
