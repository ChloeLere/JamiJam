from note import Note
from chord import Chord
import random

def generate_melody(chord_progression, drum_sentence, volume, time):
    res = []
    current_time = time
    for chord in chord_progression:
        bar = []
        bar_time = 0
        while bar_time <= 4:
            duration = random.choice([0.25, 0.5, 1])
            bar.append(Note(random.choice(chord.chord) + 60, duration, volume, 1, 1, bar_time + current_time, "melody"))
            bar_time += duration
        current_time += 4
        res.append(bar)
    return res