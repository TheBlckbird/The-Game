// import WebSocket, { WebSocketServer } from 'ws';

// const wss = new WebSocketServer({ port: 8080 });


// wss.on('connection', function connection(ws) {

//     ws.on('message', function message(data) {
//         const regex = /\[\d+,\d+\]/;
//         if (data.toString().match(regex)) {
//             const [x, y] = JSON.parse(data);
//             console.log(`x: ${x}, y: ${y}`);
//         }
//     });

// })

const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/test/index.html');
});

let users = 0;

io.on('connection', (socket) => {
    if (users < 2) {
        users++;
        console.log("a user connected");
    } else {
        socket.disconnect();
        console.log("too many users");
    }

    socket.on('disconnect', () => {
        console.log('user disconnected');
        users--;
    });

    socket.on("movement", (msg) => {
        const regex = /^\d+,\d+$/;

        // socket.broadcast.emit("message", msg);
        
        if (typeof msg !== "string") {
            socket.broadcast.emit("movement", msg);
            // if (msg.match(regex)) {
            //     socket.broadcast.emit("movement", msg);
            //     console.log(msg);
            // } else  {
            //     console.log("invalid movement");
            // }
        }
    });

    socket.send('hello');
});

server.listen(3000, () => {
    console.log('listening on *:3000');
});
