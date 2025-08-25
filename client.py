from enum import Enum
from typing import Dict, Union


class ClientStatus(Enum):
    PAUSED = 0
    READY = 1
    PLAYING = 2

    def __str__(self):
        if self == ClientStatus.PAUSED:
            return "paused"
        if self == ClientStatus.READY:
            return "ready"
        if self == ClientStatus.PLAYING:
            return "playing"

        return "unreachable"


class ClientData:
    def __init__(self, username: str, id: int):
        self._username = username
        self._id = id
        self._status = ClientStatus.PAUSED
        self._video_time: float = 0.0

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value: str):
        self._username = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: ClientStatus):
        self._status = value

    @property
    def video_time(self) -> float:
        return self._video_time

    @video_time.setter
    def video_time(self, value: float):
        self._video_time = value

    def as_dict(self) -> Dict[str, Union[int, str]]:
        return {
            "username": self.username,
            "status": str(self.status),
        }

    def print(self):
        print(f"Client {self._id}:")
        print(f"    username: {self._username}")
        print(f"    status: {self.status}")

        print()
