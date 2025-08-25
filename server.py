from random import randint

from flask import Flask, request
from flask_cors import CORS, cross_origin

from client import ClientData, ClientStatus
from playback import PlaybackData

from typing import Dict


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


def generate_id(clients: Dict[int, ClientData]) -> int:
    id = randint(0, 2147483647)
    while id in clients:
        id = randint(0, 2147483647)

    return id


clients: Dict[int, ClientData] = dict()
playback = PlaybackData()


@app.route("/join", methods=["GET"])
@cross_origin()
def join():
    username = request.args.get("username")

    if username is None:
        print("Recieved no username")
        return "Join Request missing username", 400

    id = generate_id(clients)
    client = ClientData(username, id)
    clients.update({id: client})

    response = {"id": id, username: "username"}

    return response, 200


@app.route("/leave", methods=["GET"])
@cross_origin()
def leave():
    id = request.args.get("id")

    if id is None:
        print("Recieved no id")
        return "Leave Request missing id", 400

    id = int(id)
    clients.pop(id, None)
    return {}, 200


@app.route("/ready", methods=["GET"])
@cross_origin()
def ready():
    id = request.args.get("id")
    video_time = request.args.get("videoTime")

    if id is None:
        print("Recieved no id")
        return "Ready Request missing id", 400

    if video_time is None:
        print("Received no videoTime")

        return "Ready Request missing VideoTime", 400

    id = int(id)
    video_time = float(video_time)

    client = clients[id]
    client.video_time = video_time
    client.status = ClientStatus.READY

    return {}, 200


@app.route("/pause", methods=["GET"])
@cross_origin()
def pause():
    id = request.args.get("id")

    if id is None:
        print("Recieved no id")
        return "Pause Request missing id", 400

    id = int(id)
    client = clients[id]
    client.status = ClientStatus.PAUSED

    return {}, 200


@app.route("/time", methods=["GET"])
@cross_origin()
def update_time():
    id = request.args.get("id")
    video_time = request.args.get("videoTime")

    if id is None:
        print("Recieved no id")
        return "Time Request missing id", 400

    if video_time is None:
        print("Recieved no videTime")
        return "Time Request missing videoTime", 400

    id = int(id)
    video_time = float(video_time)

    clients[id].video_time = video_time
    return {}, 200


@app.route("/check", methods=["GET"])
@cross_origin()
def check():

    response = dict()

    clients_status = []
    for client in clients.values():
        clients_status.append(client.as_dict())
    response["clients"] = clients_status

    ready_count = 0
    for client in clients.values():
        client.print()

        if client.status == ClientStatus.READY:
            ready_count += 1

    print(f"Users ready: ({ready_count}/{len(clients)})")

    video_time = min(map(lambda client: client.video_time, clients.values()))

    if ready_count == len(clients):
        print(f"playback.video_time = {video_time}")
        playback.video_time = video_time
        playback.play()
    else:
        playback.pause()

    response["playback"] = playback.as_dict()
    print(response["playback"])

    return response, 200
