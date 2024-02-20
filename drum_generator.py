from midiutil import MIDIFile
from datetime import datetime
import copy
import random
from note import Note

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
    if empties == [] or idxs == []:
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
    if empties == []:
        return bar
    new = random.choice(empties)
    bar[hand][new] = random.randint(0, 48)
    return bar

# Generate a 4 bar sequence following the motif
# motif = "aaba" || "abab" || "abac" || "aabb"
def generate_sentence(time, track = 0):
    a = generate_bar()
    b = copy.deepcopy(a)
    b = move_note(b)
    b = move_note(b, 3)
    c = copy.deepcopy(b)
    c = move_note(c)
    c = add_note(c, 2)
    c = add_note(c, 2)
    sentence = []
    r = random.randrange(0, 3)
    match r:
        case 0:
            sentence = [a, a, b, a]
        case 1:
            sentence = [a, b, a, b]
        case 2:
            sentence = [a, b, a, c]
        case 3:
            sentence = [a, a, b, b]
    i = time
    res = []
    for bar in sentence:
        res.append(convert_bar_to_notes(bar, time, track))
        time += 4
    return res

def convert_bar_to_notes(bar, time, track = 0):
    return list(map(lambda member: convert_pitch_to_notes(member, time, track), bar))

def convert_pitch_to_notes(pitch_list: list, time, track = 0):
    res = []
    i = time
    for pitch in pitch_list:
        if pitch != -1:
            pitch += 36
        res.append(Note(pitch, 0.25, 100, track, 9, i, "drums"))
        i += 0.25
    return res

# Outdated
def append_drums_to_midi(drum_part, midi_file: MIDIFile, time, track = 0):
    current_time = time
    for bar in drum_part:
        for note in bar:
            midi_file.addNote(note.track, note.channel, note.pitch + 36, note.time, note.duration, note.volume)
        
