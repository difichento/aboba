from Globals import Globals


class Command:
    def __init__(self, destination):
        self.destination = destination

    @staticmethod
    def execute():
        pass


class StartGameMenu(Command):
    def execute(self):
        self.destination.current_window = "game"


class StartEditorMenu(Command):
    @staticmethod
    def _clear_cells():
        for i in range(len(Globals.cells)):
            Globals.cells[i].object = "background"

    def execute(self):
        StartEditorMenu._clear_cells()
        self.destination.current_level = None
        self.destination.current_window = "editor"


class StartGameEditor(Command):
    def execute(self):
        self.destination.current_window = "game"


class CommandsRunner:
    def __init__(self, start_game_menu_com, start_editor_menu_com, start_game_editor_com):
        self._start_game_menu_com = start_game_menu_com
        self._start_editor_menu_com = start_editor_menu_com
        self._start_game_editor_com = start_game_editor_com

    def start_game_menu(self):
        self._start_game_menu_com.execute()

    def start_editor_menu(self):
        self._start_editor_menu_com.execute()

    def start_game_editor(self):
        self._start_game_editor_com.execute()


commands_runner = CommandsRunner(StartGameMenu(Globals), StartEditorMenu(Globals), StartGameEditor(Globals))
