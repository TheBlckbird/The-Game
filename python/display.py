import os
import platform
from termcolor import colored

class Display:
    def __init__(self, board, walls, player_icon="@", box_icon="O", player_color="cyan", box_color="red", multiplayer_color="green"):
        self.board = board
        self.walls = walls
        
        self.player_icon = player_icon
        self.box_icon = box_icon

        self.player_color = player_color
        self.box_color = box_color
        self.multiplayer_color = multiplayer_color


        # self.display(player_position=player_position, box_positions=box_positions)

    def display(self, player_position, box_positions, second_player_position=None):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

        display_string = """"""

        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if [x, y] in self.walls:
                    pass

                elif [x, y] == player_position:
                    
                    print(colored(self.player_icon, self.player_color), end=" ")
                    # print("@", end=" ")
                    # display_string += "@ "
                    continue

                elif [x, y] == second_player_position:
                    print(colored(self.player_icon, self.multiplayer_color), end=" ")
                    # print("@", end=" ")
                    # display_string += "@ "
                    continue

                elif [x, y] in box_positions:
                    print(colored(self.box_icon, self.box_color), end=" ")
                    # print("O", end=" ")
                    # display_string += "$ "
                    continue
                
                print(self.board[y][x], end=" ")
                # display_string += self.board[x][y] + " "
            
            print()
            # display_string += ("\n")

        # print(display_string)