import socketio

class Multiplayer:
    def __init__(self, server, port):
        self.server = server
        self.port = port
        self.second_player_position = None

    def connect(self):
        self.sio = socketio.Client()
        self.sio.connect(f"{self.server}:{self.port}")

        @self.sio.on("movement")
        def on_movement(data):
            self.second_player_position = data
            # position = data.split(",")
            # position = [int(numeric_string) for numeric_string in position]
            # print(data)
            # print(position)
            # self.second_player_position = position

    def send_movement(self, position):
        # position_string = f"{position[0]},{position[1]}"
        self.sio.emit("movement", position)

    def disconnect(self):
        self.sio.disconnect()