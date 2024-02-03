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
tempo    = 120   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(degrees2):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

with open("output.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
