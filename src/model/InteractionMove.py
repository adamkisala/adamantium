

class InteractionMove:
    def __init__(self):
        self.__move_id = None
        self.__move_type = None
        self.__content = None
        self.__player_id = None
        self.__role = None

    def __set_player_id(self, player_id_tmp: str = None):
        self.__player_id = player_id_tmp

    def __get_player_id(self) -> str:
        return self.__player_id

    player_id = property(__get_player_id, __set_player_id, None)
