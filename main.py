#!/usr/bin/env python

from midiutil import MIDIFile
from random import randint
import mg_lib

degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
degrees2 = mg_lib.major_scale(60)
track    = 0
channel  = 5
time     = 0    # In beats
duration = 1    # In beats
tempo    = 90   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

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
for note in phrase:
    i += note.duration
    MyMIDI.addNote(track, channel, note.pitch, i, note.duration, volume)

# NoteAdder 3
#for i, pitch in enumerate(degrees2):
#    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

with open("output.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
