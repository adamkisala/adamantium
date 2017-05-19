import uuid

import datetime
from sqlalchemy import Boolean, DateTime
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from factory.ArtifactFactory import ArtifactFactory
from interface.IArtifact import IArtifact
from helpers.Constants import *
from settings.db_settings import Base


class InteractionMove(Base):

    __tablename__ = 'InteractionMove'

    playerName = Column(String(100))
    id = Column(String(36), primary_key=True)
    relativeId = Column(Integer)
    moveName = Column(String(100))
    artifact = Column(String(100))
    role = Column(String(100))
    final = Column(Boolean)
    dateCreated = Column(DateTime)

    def __init__(self, id: str = None, relativeId: int = None, moveName: str = EMPTY, artifact: str = EMPTY,
                 playerName: str = EMPTY, role: str = EMPTY, final: bool = False):
        if id is None:
            self.__id = uuid.uuid4()
        else:
            self.__id = id
        self.__moveName = moveName
        self.relativeId = relativeId
        self.__artifact = ArtifactFactory.create_artifact(artifact)
        self.__playerName = playerName
        self.__role = role
        self.__final = final
        self.__dateCreated = datetime.datetime.utcnow()
