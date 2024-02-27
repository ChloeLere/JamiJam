from midiutil import MIDIFile

class Note():
    def __init__(self, pitch, duration, volume, track, channel, time) -> None:
        self.pitch = pitch
        self.duration = duration
        self.volume = volume
        self.track = track
        self.channel = channel
        self.time = time
    
    def add_to_midi(self, midi_file: MIDIFile):
        if self.pitch == -1:
            return
        midi_file.addNote(self.track, self.channel, self.pitch, self.time, self.duration, self.volume)