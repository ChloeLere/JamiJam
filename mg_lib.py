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

# 36 = kick
# 38 = snare
# 42 = hihat (closed)
# -1 = silence
# every 1/4 must be filled
def generate_drum_bar():
    res = []
    for i in range(4):
        for j in range(4):
            if i == 0 and j == 0:
                res.append(36)
            elif j == 0:
                if random.randint(0, 1) == 1:
                    res.append(38)
                else:
                    res.append(42)
            else:
                if random.randint(0, 1) == 1:
                    res.append(42)
                else:
                    res.append(-1)
    return res

def generate_crazy_drum_bar():
    res = []
    for i in range(16):
        r = random.randint(0, 4)
        if r == 1:
            res.append(36)
        elif r == 2:
            res.append(38)
        elif r == 3:
            res.append(42)
        elif r == 4:
            res.append(-1)
    return res

# chord = the current chord played along the bar
def generate_melody(chord, volume, time, instruments):
    res = []
    for i in range(8):
        if i == 0:
            res.append(Note(chord[0] + 12, 0.5, volume, 1, 1, time + 0.5, instruments))
            continue
        res.append(Note(random.choice(chord) + 12, 0.5, volume, 1, 1, time + 0.5, instruments))
    return res

def get_degrees_by_feeling(feeling):
    file_result = pd.read_csv("./data/MusicalScaleTable.csv")
    match_row = pd.DataFrame({})
    for index, row in file_result.iterrows():
        list_emotions = row["emotion"].replace(" ", "").split(',')
        for emotion in list_emotions:
            if emotion == feeling:
                match_row = pd.concat([match_row, row.to_frame().T], ignore_index=True)
    random_row = match_row.sample(n=1)
    return random_row["root"].values[0], random_row["name"].values[0], random_row["type"].values[0], match_row
