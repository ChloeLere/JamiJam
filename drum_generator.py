from midiutil import MIDIFile
from datetime import datetime
import copy
import random

# this is for testing ==========================================================
track    = 0
channel  = 9
time     = 0    # In beats
duration = 1    # In beats
tempo    = 100   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(10, time, tempo)

# ==============================================================================

# returns something like: {
# right_hand: [int:16],
# left_hand: [int:16],
# right_foot: [int:16],
# left_foot: [int:16],
# }
def base_4_4():
    hihats = []
    for i in range(16):
        if i % 2 == 0:
            hihats.append(6)
        else:
            hihats.append(-1)

    snares = []
    kick = []
    for i in range(2):
        snares = snares + ([-1] * 4)
        snares.append(2)
        snares = snares + ([-1] * 3)
        kick.append(0)
        kick += ([-1] * 7)
    return [hihats, snares, [-1] * 16, kick]

def base_metal():
    kick = [0] * 16
    snares = []
    hihats = []
    for i in range(4):
        hihats.append(6)
        hihats += ([-1] * 3)
        if i % 2 != 0:
            snares.append(2)
        else:
            snares.append(-1)
        snares += ([-1] * 3)
    return [hihats, snares, [-1] * 16, kick]

def base_swing():
    rides = []
    hihat_closes = []
    for i in range(2):
        rides.append(23)
        rides += ([-1] * 3)
        rides.append(23)
        rides += ([-1] * 2)
        rides.append(23)
        hihat_closes += [-1] * 4
        hihat_closes.append(34)
        hihat_closes += [-1] * 3
    return [rides, [-1] * 16, hihat_closes, [-1] * 16]

def base_motown_groove():
    snares = []
    for i in range(4):
        snares.append(2)
        snares += [-1] * 3
    hihats = []
    for i in range(8):
        hihats.append(6)
        hihats.append(-1)
    kicks = []
    kicks.append(0)
    kicks += [-1] * 7
    for i in range(2):
        kicks += [-1] * 2
        kicks.append(0)
        kicks.append(-1)
    return [hihats, snares, [-1] * 16, kicks]

def generate_bar():
    r = random.randint(0, 3)
    if r == 0:
        return base_4_4()
    elif r == 1:
        return base_metal()
    elif r == 2:
        return base_swing()
    return base_motown_groove()

# move one note randomly in an empty space
# (hand = which array of note is edited)
def move_note(bar: list, hand = 1):
    idxs = []
    empties = []
    for i in range(len(bar[hand])):
        if bar[hand][i] != -1:
            idxs.append(i)
        else:
            empties.append(i)
    if len(empties) == 0:
        return bar
    src = random.choice(idxs)
    dest = random.choice(empties)
    bar[hand][dest] = bar[hand][src]
    bar[hand][src] = -1
    return bar

# add one random note in an empty space
# (hand = which array of note is edited)
def add_note(bar: list, hand = 1):
    empties = []
    for i in range(len(bar[hand])):
        if bar[hand][i] == -1:
            empties.append(i)
    if len(empties) == 0:
        return bar
    new = random.choice(empties)
    bar[hand][new] = random.randint(0, 48)
    return bar

# Generate a 4 bar sequence following the motif
# motif = "aaba" || "abab" || "abac" || "aabb"
def generate_sentence():
    a = generate_bar()
    b = copy.deepcopy(a)
    b = move_note(b)
    b = move_note(b, 3)
    c = copy.deepcopy(b)
    c = move_note(c)
    c = add_note(c, 2)
    c = add_note(c, 2)
    r = random.randrange(0, 3)
    match r:
        case 1:
            return [a, a, b, a]
        case 2:
            return [a, b, a, b]
        case 3:
            return [a, b, a, c]
        case 4:
            return [a, a, b, b]
    return [a, b, a, b]


# this is for testing ==========================================================

bars = generate_sentence()

s = 0
for bar in bars:
    for x in bar:
        i = 0
        for note in x:
            if note != -1:
                MyMIDI.addNote(track, channel, note + 36, i + (s * 4), 0.25, volume)
            i += 0.25
    s += 1

with open("output_" + str(datetime.now()) + ".mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)

# ==============================================================================
