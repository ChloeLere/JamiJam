# Music Generator Library

from midiutil import MIDIFile
from note import Note
import random

def major_chord(root):
    return [root, root + 4, root + 7]

def minor_chord(root):
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
    bar2 = generate_bar(minor_scale(root))
    bar3 = bar2
    bar4 = generate_bar(major_scale(root))
    return bar1 + bar2 + bar3 + bar4
