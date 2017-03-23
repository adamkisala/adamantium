from sqlalchemy import Column
from sqlalchemy import String

from settings.db_settings import Base


class Dialogue(Base):
    __tablename__ = 'Dialogue'

    id = Column(String, primary_key=True)
    dialogueDescription = Column(String)
