
class Note():
    def __init__(self, pitch, duration, volume, track, channel, time, instruments = None) -> None:
        self.pitch = pitch
        self.duration = duration
        self.volume = volume
        self.track = track
        self.channel = channel
        self.time = time

        self.instruments = instruments