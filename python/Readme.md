# The Game in Python

## Multiplayer

How to start the server:
```sh
cd backend
npm i
node index.js
```

Only two player can play simultaneously.  
To play with other people you have to release the port `3000`.  
The protocol is `TCP`  
After that you have to change the server in `main.py` (line `24`) to you public [IP-address](https://whatismyip.com).  