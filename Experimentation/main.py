#!/usr/bin/env python

from midiutil import MIDIFile
from random import randint
from datetime import datetime
import mg_lib

degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
degrees2 = mg_lib.major_scale(60)
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 100   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(3)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(0, time, tempo)
MyMIDI.addTempo(1, time, tempo)

bar = []
i = 0
phrase = mg_lib.generate_phrase(60)

# NoteAdder 1 (best result IMO)
#for j in range(20):
#    if j % 3 != 0:
#        bar = mg_lib.generate_bar(mg_lib.major_scale(60 + ((j % 2) * 12)))
#    for note in bar:
#        i += note.duration
#        MyMIDI.addNote(track, channel, note.pitch, i, note.duration, volume)


# NoteAdder 2
#for note in phrase:
#    i += note.duration
#    MyMIDI.addNote(track, channel, note.pitch, i, note.duration, volume)

# NoteAdder 3
#for i, pitch in enumerate(degrees2):
#    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)


n_phrases = 20
chord_list = []
# ChordAdder Harmonie
for j in range(n_phrases):
    chord_prog = mg_lib.generate_chord_progression(48)
    for chord in chord_prog:
        MyMIDI.addNote(0, 0, chord[0], time + i, 4, volume)
        MyMIDI.addNote(0, 0, chord[1], time + i, 4, volume)
        MyMIDI.addNote(0, 0, chord[2], time + i, 4, volume)
        i += 4
        chord_list.append(chord)

# RythmAdder Percussions
i = 0
drum_bar = mg_lib.generate_crazy_drum_bar()
for j in range(4 * n_phrases):
    for pitch in drum_bar:
        if pitch != -1:
            MyMIDI.addNote(2, 9, pitch, time + i, 0.25, volume)
        i += 0.25

# MelodyAdder
i = 0
for chord in chord_list:
    melody = mg_lib.generate_melody(chord)
    for pitch in melody:
        MyMIDI.addNote(1, 1, pitch, time + i, 0.5, volume)
        i += 0.5

with open("output_" + str(datetime.now()) + ".mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
