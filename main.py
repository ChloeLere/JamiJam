from midiutil import MIDIFile
from random import randint
from datetime import datetime
from music_generation import MusicGeneration
import mg_lib

def main():
    music_gen = MusicGeneration()
    music_gen.generate_midi()
    #print(mg_lib.generate_chord_progression(48, True))
    #print(mg_lib.generate_crazy_drum_bar())
    #print(mg_lib.generate_melody(48))
    a = ['a', 'b', 'c']
    b = ['d', 'e']
    a += b 
    print(a)


    return


main()