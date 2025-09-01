# media-sync-server

**media-sync-server** is a server that handles real-time video synchronisation across multiple clients.

This is the back-end for the [media-sync-client](https://github.com/AYM-123/media-sync-server).

## Features
- Automatic pause detection
- Always synchronising with the user that is furthest behind
- clear UI that shows all users' status

## Installation

You can clone this repository on your server machine with
```
git clone https://github.com/AYM-123/media-sync-client.git
```

## Running the server

You can use `uv` to run this app
```
uv run flask --app server.py run
```
