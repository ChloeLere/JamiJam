# Music Generator Library

from midiutil import MIDIFile
from note import Note
from chord import Chord
from scale import Scale
import random
import pandas as pd

def major_triad(root):
    return [root, root + 4, root + 7]

def minor_triad(root):
    return [root, root + 3, root + 7]

def major_scale(root):
    res = [root]
    for i in range(6):
        if (i != 2):
            res.append(res[len(res) - 1] + 2)
        else:
            res.append(res[len(res) - 1] + 1)
    return res

def minor_scale(root):
    res = [root]
    for i in range(6):
        if (i != 1):
            res.append(res[len(res) - 1] + 2)
        else:
            res.append(res[len(res) - 1] + 1)
    return res

# Generate a 4 beats bar
# scale is a list of allowed pitches
def generate_bar(scale):
    res = []

    idx = random.randrange(0, len(scale))
    current = scale[idx]

    for i in range(4):

        current = random.choice(scale)

        r = random.randint(0, 3)
        if r == 0:
            res.append(Note(random.choice(scale), 1, 100))
        elif r == 1:
            for i in range(2):
                res.append(Note(random.choice(scale), 0.5, 100))
        elif r == 2:
            for i in range(4):
                res.append(Note(random.choice(scale), 0.25, 100))
        elif r == 3:
            res.append(Note(random.choice(scale), 1, 0))
    return res

def generate_phrase(root):
    bar1 = generate_bar(major_scale(root))
    bar2 = bar1
    bar3 = generate_bar(major_scale(root))
    bar4 = generate_bar(major_scale(root))
    return bar1 + bar2 + bar3 + bar4

# 1 5 6 4
# 6 4 1 5
# 1 6 4 5
# 4 5 3 6
# 1 5 4 5
def generate_chord_progression(root, is_minor, volume, time, instruments): #ajouter is major or minor
    scale = Scale(root, is_minor)
    res = [
        Chord(scale.getTriad(random.choice([1, 6])), 4, volume, 0, 0, time, instruments),
        Chord(scale.getTriad(random.randint(4, 6)), 4, volume, 0, 0, time + 4, instruments),
        Chord(scale.getTriad(random.randint(1, 6)), 4, volume, 0, 0, time + 8, instruments),
        Chord(scale.getTriad(random.randint(4,5)), 4, volume, 0, 0, time + 12, instruments)]
    return res

# chord = the current chord played along the bar
def generate_melody(chord, volume, time, instruments):
    res = []
    t = time
    for i in range(8):
        if i == 0:
            res.append(Note(chord[0] + 12, 0.5, volume, 1, 1, t, instruments))
            t += 0.5
            continue
        res.append(Note(random.choice(chord) + 12, 0.5, volume, 1, 1, t, instruments))
        t += 0.5
    return res

