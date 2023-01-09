class Board:
    def __init__(self, width, height):
        self.width = width + 2
        self.height = height + 2
        
        generate = self.generate_board()
        self.board = generate[0]
        self.walls = generate[1]        

    def generate_board(self):
        board = []
        walls = []

        for y in range(self.height):
            row = []
            for x in range(self.width):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    row.append("#")
                    walls.append([x, y])
                
                else:
                        row.append(" ")
            board.append(row)

        return [board, walls]