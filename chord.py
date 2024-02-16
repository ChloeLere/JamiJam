from midiutil import MIDIFile

class Chord():
    def __init__(self, chord, duration, volume, track, channel, time, instruments = None) -> None:
        self.chord = chord
        self.duration = duration
        self.volume = volume
        self.track = track
        self.channel = channel
        self.time = time
        self.instruments = instruments
    
    def add_to_midi(self, midi_file: MIDIFile):
        for note in self.chord:
            midi_file.addNote(self.track, self.channel, note, self.time, self.duration, self.volume)
    