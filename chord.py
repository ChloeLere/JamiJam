
class Chord():
    def __init__(self, chord, duration, volume, track, channel, time, instruments = None) -> None:
        self.chord = chord
        self.duration = duration
        self.volume = volume
        self.track = track
        self.channel = channel
        self.time = time
        self.instruments = instruments