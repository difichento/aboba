from Globals import Globals


class Command:
    @staticmethod
    def execute():
        pass


def _clear_cells():
    for i in range(len(Globals.cells)):
        Globals.cells[i].object = "background"


class StartGameMenu(Command):
    @staticmethod
    def execute():
        Globals.current_window = "game"


class StartEditorMenu(Command):
    @staticmethod
    def _clear_cells():
        for i in range(len(Globals.cells)):
            Globals.cells[i].object = "background"

    @staticmethod
    def execute():
        _clear_cells()
        Globals.current_level = None
        Globals.current_window = "editor"


class StartGameEditor(Command):
    @staticmethod
    def execute():
        Globals.current_window = "game"


class Commands:
    _start_game_menu_com = StartGameMenu()
    _start_editor_menu_com = StartEditorMenu()
    _start_game_editor_com = StartGameEditor()

    @staticmethod
    def start_game_menu():
        Commands._start_game_menu_com.execute()

    @staticmethod
    def start_editor_menu():
        Commands._start_editor_menu_com.execute()

    @staticmethod
    def start_game_editor():
        Commands._start_game_editor_com.execute()
