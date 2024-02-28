## JAMIJAM
## Developed by Clovis Schneider & Chloé Lere

from midiutil import MIDIFile

class Chord():
    def __init__(self, chord, duration, volume, track, channel, time) -> None:
        self.chord = chord
        self.duration = duration
        self.volume = volume
        self.track = track
        self.channel = channel
        self.time = time
    
    def add_to_midi(self, midi_file: MIDIFile):
        for note in self.chord:
            midi_file.addNote(self.track, self.channel, note, self.time, self.duration, self.volume)
    