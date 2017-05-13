from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from factory.ArtifactFactory import ArtifactFactory
from interface.IArtifact import IArtifact
from helpers.Constants import *
from settings.db_settings import Base


class InteractionMove(Base):
    __counter = 0

    __tablename__ = 'InteractionMove'

    player_name = Column(String(100))
    move_id = Column(Integer, primary_key=True)
    move_name = Column(String(100))
    artifact = Column(String(100))
    role = Column(String(100))
    final = Column(Boolean)

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

