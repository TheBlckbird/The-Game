class Player:
    def __init__(self, position, walls):
        self.position = position
        self.walls = walls

    def move(self, direction):
        direction = direction.lower()
        x = self.position[0]
        y = self.position[1]

        new_x = x
        new_y = y

        if direction == "w":
            new_y -= 1
        
        elif direction == "a":
            new_x -= 1

        elif direction == "s":
            new_y += 1

        elif direction == "d":
            new_x += 1

        if [new_x, new_y] not in self.walls:
            self.position = [new_x, new_y]