from board import Board
from player import Player
from display import Display
from multiplayer import Multiplayer

class Game:
    def __init__(self, board_width, board_height, player_start_position, box_positions, player_icon="@", wall_icon="#", box_icon="O"):
        self.wall_icon = wall_icon
        self.player_icon = player_icon
        self.box_icon = box_icon

        self.player_position = player_start_position
        self.box_positions = box_positions

        self.board_class = Board(board_width, board_height)
        self.board = self.board_class.board
        self.walls = self.board_class.walls
        self.display = Display(board=self.board, walls=self.walls)
        self.player = Player(self.player_position, self.walls)

        self.multiplayer_game = False
        multiplayer_question = input("Do you want to play multiplayer? (not really working) (y/N): ")
        if multiplayer_question == "y":
            self.multiplayer = Multiplayer(server="http://localhost", port=3000)
            self.multiplayer.connect()
            self.multiplayer_game = True

        self.update()

    def update(self):
        second_player_position = None

        if self.multiplayer_game:

            if self.multiplayer.second_player_position is not None:
                second_player_position_strings = self.multiplayer.second_player_position
                second_player_position = [int(numeric_string) for numeric_string in second_player_position_strings]
                
        self.display.display(player_position=self.player.position, box_positions=self.box_positions, second_player_position=second_player_position)

        player_action = input("Action: ")
        self.actions(player_action)
        self.update()

    def on_press(self, key):
        # await self.actions(key.char)
        

        if hasattr(key, "char"):
            char = key.char
            self.actions(char[0])
            self.update()
        
        
    def actions(self, player_action):

        # check if terminal on focus


        if player_action == "q":
            if self.multiplayer_game:
                self.multiplayer.disconnect()
            input("Press enter to exit...")
            exit()

        old_player_position = self.player.position
        self.player.move(player_action)

        if old_player_position != self.player.position and self.multiplayer_game:
            self.multiplayer.send_movement(self.player.position)
        

board = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", "#", "#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", "#", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", " ", "#", "#", " ", "#"],
    ["#", " ", " ", "#", " ", " ", "#", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]


game = Game(board_width=12, board_height=5, player_start_position=[1, 1], box_positions=[[2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2]])