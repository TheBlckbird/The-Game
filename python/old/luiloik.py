class Game:
    def __init__(self, size, player_start_position, box_position, button_position, player_icon="@", wall_icon="#", box_icon="O", button_icon="·"):
        self.wall_icon = wall_icon
        self.player_icon = player_icon
        self.box_icon = box_icon
        self.button_icon = button_icon

        self.player_position = player_start_position
        self.box_position = box_position
        self.button_position = button_position

        self.size = size
        self.board = self.create_board(self.size, self.size * 2, self.player_position, self.box_position)
        self.display(self.board)
        self.start()


    def start(self):
        direction = input("Direction: ")
        self.move_player(direction, self.player_position)


    def move_player(self, direction, player_position):
        controls = ["w", "a", "s", "d"]

        if direction not in controls:
            self.start()

        x = player_position[0]
        y = player_position[1]

        new_x = x
        new_y = y

        self.board[x][y] = " "


        if direction == "w":
                new_x = x - 1

        elif direction == "a":
                new_y = y - 1

        elif direction == "s":
                new_x = x + 1

        elif direction == "d":
                new_y = y + 1

        
        if self.board[new_x][new_y] == self.box_icon:
            if self.move_box(direction, [new_x, new_y]) == False:
                self.board[x][y] = self.player_icon
                self.display(self.board)
                self.start()
                return


        if self.board[new_x][new_y] != self.wall_icon:

            self.board[new_x][new_y] = self.player_icon
            self.player_position = [new_x, new_y]
        
        else:
            self.board[x][y] = self.player_icon

        self.display(self.board)
        self.start()

    def move_box(self, direction, box_position):
        controls = ["w", "a", "s", "d"]

        if direction not in controls:
            self.start()

        x = box_position[0]
        y = box_position[1]

        new_x = x
        new_y = y

        self.board[x][y] = " "


        if direction == "w":
                new_x = x - 1

        elif direction == "a":
                new_y = y - 1

        elif direction == "s":
                new_x = x + 1

        elif direction == "d":
                new_y = y + 1


        if self.board[new_x][new_y] != self.wall_icon:

            self.board[new_x][new_y] = self.box_icon
            self.box_position = [new_x, new_y]
            return_value = True

            if self.box_position == self.button_position:
                self.display(self.board)
                print("You win!")
                input("Press Enter to exit...")
                exit()
        
        else:
            self.board[x][y] = self.box_icon
            return_value = False

        # self.display(self.board)
        # self.start()

        return return_value


    def create_board(self, size_x, size_y, player_position, box_position):
        board = []
        for row in range(size_x):
            board.append([])
            for column in range(size_y):

                if (
                    row == 0 or
                    row == size_x - 1 or
                    column == 0 or
                    column == size_y - 1
                    ):

                    board[row].append(self.wall_icon)

                elif row == player_position[0] and column == player_position[1]:
                    board[row].append(self.player_icon)

                elif row == box_position[0] and column == box_position[1]:
                    board[row].append(self.box_icon)

                elif row == self.button_position[0] and column == self.button_position[1]:
                    board[row].append(self.button_icon)
                
                else:
                    board[row].append(" ")

        return board

    def display(self, coordinates):
        for coordinate_row in coordinates:
            for coordinate in coordinate_row:
                print(coordinate, end="")
            print()


game = Game(size=17, player_start_position=[9, 10], box_position=[9, 9], button_position=[9, 17])