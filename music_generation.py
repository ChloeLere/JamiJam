from midiutil import MIDIFile
import random
from datetime import datetime
import mg_lib
import pandas as pd
from note import Note
from chord import Chord
import drum_generator

#false -> major
#true -> mminor
#pour scale



class MusicGeneration:
    def __init__(self, tempo=-1, feeling="brightness", file_name="output_" + str(datetime.now())):
        self.chord_list = []
        self.note_list = []
        self.drums_list = []
        self.duration = 1
        self.volume = 100
        self.tempo = tempo
        self.time = 0
        if tempo < 0:
            self.tempo = random.randint(40, 200)
        self.feeling = feeling
        #rytme
        self.root_degrees, self.name_degrees, type_note, self.list_matching_degrees = mg_lib.get_degrees_by_feeling(feeling)

        self.is_minor = True
        if (type_note == "Major"):
            self.is_minor = False
        self.introduction = self.have_to_generate(5)
        self.verse = True
        self.pre_chorus = self.have_to_generate(2)
        self.refrain = self.have_to_generate(9)
        self.post_chorus = self.have_to_generate(1)
        self.bridge = self.have_to_generate(4)
        self.conclusion = self.have_to_generate(6)

        self.my_midi = MIDIFile(3)

        self.file_name = file_name
    
    def have_to_generate(self, pourcentage):
        if (random.randint(0, 10) <= pourcentage):
            return True
        return False

    def generate_midi(self):
        self.my_midi.addTempo(0, 0, self.tempo)
        have_refrain = False
        number_loop_max = random.randint(1, 3)
        

        if self.introduction:
            self.generate_introduction()
        
        for number_loop in range(0, number_loop_max):
            if self.verse:
                self.generate_verse()
            if self.pre_chorus:
                self.generate_pre_chorus()
            if number_loop == number_loop_max - 1 and self.bridge:
                self.generate_bridge()
            if self.refrain: 
                if have_refrain == False:
                    list_chord_refrain, list_note_refrain, list_drums_refrain = self.generate_refrain()
                    have_refrain = True
                else: 
                    list_chord_refrain, list_note_refrain, list_drums_refrain = self.add_new_refrain(list_chord_refrain, list_note_refrain, list_drums_refrain)
                self.chord_list += list_chord_refrain
                self.note_list += list_note_refrain
                self.drums_list += list_drums_refrain
            if self.post_chorus:
                self.generate_post_chorus()

        if self.conclusion:
            self.generate_conclusion()

        self.create_file()

    def generate_introduction(self, n_phrases = 1): #entre 1 ou 2
        #The introduction may also be based around the chords used in the verse, chorus, or bridge
        print("Introduction")
        return
    
    def generate_verse(self, n_phrases = 4): # entre 2 et 8
        #an AABB or ABAB rhyme scheme.
        print("Verse")
        return
    
    def generate_pre_chorus(self, n_phrases = 1): #1 ou 0.25 (donc une bar)
        print("Pre chorus")
        return
    
    def generate_refrain(self, n_phrases = 4): #entre 2 et 8
        #les fonction finirons par tous renvoyer des phrases 
        #generate_percussions : generate_drum_bar -> bcp changer
        #generate_harmonie : generate_chord_progression 
        #generate_bass : osef
        #generate_lead : generate_melody -> prend le resultat de harmonie
        list_chord_refrain = []
        list_note_refrain = []
        list_drums_refrain = []
    
        for n in range(0, n_phrases):
            harmonie = mg_lib.generate_chord_progression(self.root_degrees, self.is_minor, self.volume, self.time, "refrain")
            list_chord_refrain += harmonie
            drums = drum_generator.generate_sentence(self.time, 2)
            list_drums_refrain += drums
            for y in range(4):
                list_note_refrain += mg_lib.generate_melody(harmonie[y].chord, self.volume, self.time, "refrain")
                self.time += 4
    
        print("Refrain")
        return list_chord_refrain, list_note_refrain, list_drums_refrain

    def add_new_refrain(self, list_chord_refrain, list_note_refrain, list_drums, n_phrase = 4):
        new_list_chord_refrain = []
        new_list_note_refrain = []
        new_list_drums_refrain = []
        t = 0
        for chord in list_chord_refrain:
            new_list_chord_refrain.append(Chord(chord.chord, chord.duration, chord.volume, chord.track, chord.channel, self.time + t, chord.instruments))
            t += chord.duration

        t = 0
        for note in list_note_refrain:
            new_list_note_refrain.append(Note(note.pitch, note.duration, note.volume, note.track, note.channel, self.time + t, note.instruments))
            t += note.duration

        t = 0
        for bar in list_drums:
            bar_t = t
            for note in bar:
                if note.pitch != -1:
                    new_list_drums_refrain.append(Note(note.pitch, note.duration, note.volume, note.track, note.channel, self.time + bar_t, note.instruments))
                bar_t += 0.25
            t += 4
        self.time += 16 * n_phrase
    
        print("Repetition refrain")

        return new_list_chord_refrain, new_list_note_refrain, new_list_drums_refrain
    
    def generate_post_chorus(self, n_phrases = 1): #1 ou 0.25 (donc une bar)
        print("Post chorus")
        return
    
    def generate_bridge(self, n_phrases = 4):  #entre 2 et 8
        print("Bridge")
        return
    
    def generate_conclusion(self, n_phrases = 1):# 1 ou 2
        print("Conclusion")
        return
    
    def create_file(self):
        for chord in self.chord_list:
            for note in chord.chord:
                self.my_midi.addNote(chord.track, chord.channel, note + 48, chord.time, chord.duration, chord.volume)
           
        for note in self.note_list:
            self.my_midi.addNote(note.track, note.channel, note.pitch + 48, note.time, note.duration, note.volume)
    
        for bar in self.drums_list:
            for part in bar:
                for note in part:
                    note.add_to_midi(self.my_midi)
        
        with open(self.file_name + ".mid", "wb") as output_file:
            self.my_midi.writeFile(output_file)