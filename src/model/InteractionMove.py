

class InteractionMove:
    __counter = 0

    def __init__(self, move_type: str = None, content: str = None, player_id: str = None, role: str = None):
        InteractionMove.__counter += 1
        self.__move_id = InteractionMove.__counter
        self.__move_type = move_type
        self.__content = content
        self.__player_id = player_id
        self.__role = role

    def __set_player_id(self, player_id_tmp: str = None):
        self.__player_id = player_id_tmp

    def __get_player_id(self) -> str:
        return self.__player_id

    def __get_move_id(self) -> int:
        return self.__move_id

    def __set_move_id(self, move_id_tmp: int = None):
        self.__move_id = move_id_tmp

    player_id = property(__get_player_id, __set_player_id, None)
    move_id = property(__get_move_id, __set_move_id, None)