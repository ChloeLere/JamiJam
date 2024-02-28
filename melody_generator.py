## JAMIJAM
## Developed by Clovis Schneider & Chloé Lere

from note import Note
from chord import Chord
import random

def generate_melody(chord_progression, volume, time, pitch_bend = 60, track=1):
    res = []
    current_time = time
    for chord in chord_progression:
        bar = []
        bar_time = 0
        while bar_time <= 4:
            duration = random.choice([0.25, 0.5, 1.0])
            pitch = random.choice(chord.chord) + pitch_bend
            bar.append(Note(pitch, duration, volume, track, track, bar_time + current_time))
            bar_time += duration
        current_time += 4
        res.append(bar)
    return res