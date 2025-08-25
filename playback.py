import time
from enum import Enum
from typing import Dict


class PlaybackStatus(Enum):
    PAUSED = 0
    PLAYING = 1

    def __str__(self):
        if self == PlaybackStatus.PAUSED:
            return "paused"

        if self == PlaybackStatus.PLAYING:
            return "playing"

        return "unreachable"


class PlaybackData:
    def __init__(self) -> None:
        self._status: PlaybackStatus = PlaybackStatus.PAUSED
        self._video_time: float = 0.0
        self._play_time: int = 0

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: PlaybackStatus):
        self._status = value

    @property
    def video_time(self):
        return self._video_time

    @video_time.setter
    def video_time(self, value: float):
        self._video_time = value

    @property
    def play_time(self) -> float:
        return self._play_time

    @play_time.setter
    def play_time(self, value):
        if self.status == PlaybackStatus.PAUSED:
            self._play_time = value

    def play(self):
        if self.status == PlaybackStatus.PLAYING:
            return

        self.play_time = int(time.time() * 1000) + 5000
        self.status = PlaybackStatus.PLAYING

    def pause(self):
        if self.status == PlaybackStatus.PAUSED:
            return

        self.status = PlaybackStatus.PAUSED

    def as_dict(self) -> Dict[str, str | int | float]:
        return {
            "status": str(self.status),
            "videoTime": self.video_time,
            "playTime": self.play_time,
        }
