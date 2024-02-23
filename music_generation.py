from midiutil import MIDIFile
import random
from datetime import datetime
import mg_lib
import pandas as pd
from note import Note
from chord import Chord
import drum_generator
import melody_generator
import data

#false -> major
#true -> minor
#pour scale

class MusicGeneration:
    def __init__(self, tempo=-1, feeling="brightness", file_name="output_" + str(datetime.now())):
        self.chord_list = []
        self.note_list = []
        self.drums_list = []
        self.bass_list = []
        self.duration = 1
        self.volume = 100
        self.tempo = tempo
        self.time = 0
        if tempo < 0:
            self.tempo = random.randint(40, 200)
        self.feeling = feeling
        #rytme
        self.root_degrees, self.name_degrees, type_note, self.list_matching_degrees = data.get_degrees_by_feeling(feeling)

        self.is_minor = (type_note == "Minor")
        self.introduction = self.have_to_generate(5)
        self.verse = True
        self.refrain = self.have_to_generate(9)
        self.pre_chorus = self.have_to_genrate_post_pre(2)
        self.post_chorus = self.have_to_genrate_post_pre(1)
        self.bridge = self.have_to_generate(4)
        self.conclusion = self.have_to_generate(6)

        self.my_midi = MIDIFile(4)

        self.file_name = file_name
    
    def have_to_genrate_post_pre(self, pourcentage):
        if (self.refrain == False):
            return False
        if (random.randint(0, 10) <= pourcentage):
            return True
        return False
    
    def have_to_generate(self, pourcentage):
        if (random.randint(0, 10) <= pourcentage):
            return True
        return False

    def generate_midi(self):
        self.my_midi.addTempo(0, 0, self.tempo)
        have_refrain = False
        number_loop_max = random.randint(1, 3)
        list_chord_refrain = []
        list_note_refrain = []
        list_drums_refrain = []
        list_base_refrain = []
        
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
                    list_chord_refrain, list_note_refrain, list_drums_refrain, list_base_refrain = self.generate_refrain()
                    have_refrain = True
                else:
                    list_chord_refrain, list_note_refrain, list_drums_refrain, list_base_refrain = self.add_new_refrain(list_chord_refrain, list_note_refrain, list_drums_refrain, list_base_refrain)
                self.chord_list += list_chord_refrain
                self.note_list += list_note_refrain
                self.drums_list += list_drums_refrain
                self.bass_list += list_base_refrain
            if self.post_chorus:
                self.generate_post_chorus()

        if self.conclusion:
            self.generate_conclusion()

        self.create_file()

    def generic_generation(self, name_part, degrees):
        harmonie = mg_lib.generate_chord_progression(degrees, self.is_minor, self.volume, self.time, name_part)
        self.chord_list += harmonie
        drums = drum_generator.generate_sentence(self.time, 2)
        self.drums_list += drums
        self.note_list += melody_generator.generate_melody(harmonie, drums, self.volume, self.time)
        self.bass_list += melody_generator.generate_melody(harmonie, drums, self.volume, self.time, 36, 3)
        self.time += 16
        return
    

    def generate_introduction(self, n_phrases = 1): #entre 1 ou 2
        #The introduction may also be based around the chords used in the verse, chorus, or bridge
        #retirer les deux premiere bar d'un instrument aléatoir (pas les chord)
        print("Introduction")
        degrees = data.get_new_note(self.list_matching_degrees, self.name_degrees, self.root_degrees)
        harmonie_list_tmp = []
        drums_list_tmp = []
        note_list_tmp = []
        bass_list_tmp = []

        for n in range(0, n_phrases):
            harmonie = mg_lib.generate_chord_progression(degrees, self.is_minor, self.volume, self.time, "introduction")
            harmonie_list_tmp += harmonie
            drums = drum_generator.generate_sentence(self.time, 2)
            drums_list_tmp += drums
            note_list_tmp += melody_generator.generate_melody(harmonie, drums, self.volume, self.time)
            bass_list_tmp += melody_generator.generate_melody(harmonie, drums, self.volume, self.time, 36, 3)
            self.time += 16
        
        rand = random.randint(0, 10)
        if (rand <= 3):
            drums_list_tmp = drums_list_tmp[2:]
        elif rand >= 7:
            note_list_tmp = note_list_tmp[2:]
        else:
            bass_list_tmp = bass_list_tmp[2:]

        self.chord_list += harmonie_list_tmp
        self.drums_list += drums_list_tmp
        self.note_list += note_list_tmp
        self.bass_list += bass_list_tmp
    
    def generate_verse(self, n_phrases = 4): # entre 2 et 8
        #an AABB or ABAB rhyme scheme.
        print("Verse")
        for n in range(0, n_phrases):
            self.generic_generation("verse", self.root_degrees)
    
    def generate_pre_chorus(self, n_phrases = 1): #1 ou 0.25 (donc une bar)
        print("Pre chorus")
        for n in range(0, n_phrases):
            self.generic_generation("pre", self.root_degrees)
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
        list_base_refrain = []
    
        for n in range(0, n_phrases):
            harmonie = mg_lib.generate_chord_progression(self.root_degrees, self.is_minor, self.volume, self.time, "refrain")
            list_chord_refrain += harmonie
            drums = drum_generator.generate_sentence(self.time, 2)
            list_drums_refrain += drums
            list_note_refrain += melody_generator.generate_melody(harmonie, drums, self.volume, self.time)
            list_base_refrain += melody_generator.generate_melody(harmonie, drums, self.volume, self.time, 36, 3)
            self.time += 16
    
        print("Refrain")
        return list_chord_refrain, list_note_refrain, list_drums_refrain, list_base_refrain

    def add_new_refrain(self, list_chord_refrain, list_note_refrain, list_drums, list_base_refrain, n_phrase = 4):
        new_list_chord_refrain = []
        new_list_note_refrain = []
        new_list_drums_refrain = []
        new_list_base_refrain = []

        t = 0
        for chord in list_chord_refrain:
            new_list_chord_refrain.append(Chord(chord.chord, chord.duration, chord.volume, chord.track, chord.channel, self.time + t, chord.instruments))
            t += chord.duration

        t = 0
        for bar in list_note_refrain:
            bar_list = []
            for note in bar:
                bar_list.append(Note(note.pitch, note.duration, note.volume, note.track, note.channel, self.time + t, note.instruments))
                t += note.duration
            new_list_note_refrain.append(bar_list)
        

        t = 0
        for bar in list_drums:
            bar_t = t
            new_bar = []
            for seq in bar:
                new_seq = []
                seq_t = bar_t
                for note in seq:
                    new_seq.append(Note(note.pitch, note.duration, note.volume, note.track, note.channel, self.time + seq_t, note.instruments))
                    seq_t += 0.25
                new_bar.append(new_seq)
            t += 4
            new_list_drums_refrain.append(new_bar)


        current_time = self.time
        for bar in list_base_refrain:
            new_bar = []
            bar_t = 0
            for note in bar:
                new_bar.append(Note(note.pitch, note.duration, note.volume, note.track, note.channel, bar_t + current_time, note.instruments))
                bar_t += note.duration
            current_time += 4
            new_list_base_refrain.append(new_bar)


        self.time += 16 * n_phrase
    
        print("Repetition refrain")

        return new_list_chord_refrain, new_list_note_refrain, new_list_drums_refrain, new_list_base_refrain
    
    def generate_post_chorus(self, n_phrases = 1): #1 ou 0.25 (donc une bar)
        print("Post chorus")
        for n in range(0, n_phrases):
            self.generic_generation("post", self.root_degrees)
        return
    
    def generate_bridge(self, n_phrases = 4):  #entre 2 et 8
        print("Bridge")
        for n in range(0, n_phrases):
            self.generic_generation("bridge", self.root_degrees)
        return
    
    def generate_conclusion(self, n_phrases = 1):# 1 ou 2
        print("Conclusion")
        harmonie_list_tmp = []
        drums_list_tmp = []
        note_list_tmp = []
        bass_list_tmp = []

        degrees = data.get_new_note(self.list_matching_degrees, self.name_degrees, self.root_degrees)
        for n in range(0, n_phrases):
            harmonie = mg_lib.generate_chord_progression(degrees, self.is_minor, self.volume, self.time, "conclusion")
            harmonie_list_tmp += harmonie
            drums = drum_generator.generate_sentence(self.time, 2)
            drums_list_tmp += drums
            note_list_tmp += melody_generator.generate_melody(harmonie, drums, self.volume, self.time)
            bass_list_tmp += melody_generator.generate_melody(harmonie, drums, self.volume, self.time, 36, 3)
            self.time += 16

        volume = self.volume
        for chord in harmonie_list_tmp:
            chord.volume = volume
            volume -= 15
            
        volume = self.volume
        for bar in note_list_tmp: 
            for note in bar:
                note.volume = volume
            volume -= 15

        volume = self.volume
        for bar in bass_list_tmp: 
            for note in bar:
                note.volume = volume
            volume -= 15

        volume = self.volume
        for bar in drums_list_tmp:
            for part in bar:
                for note in part:
                    note.volume = volume
            volume -= 15

        self.chord_list += harmonie_list_tmp
        self.drums_list += drums_list_tmp
        self.note_list += note_list_tmp
        self.bass_list += bass_list_tmp
    
    def create_file(self):

        for chord in self.chord_list:
            for note in chord.chord:
                self.my_midi.addNote(chord.track, chord.channel, note + 48, chord.time, chord.duration, chord.volume)

        for bar in self.note_list: #ERROR PROVOQUE ICI
            for note in bar:
                note.add_to_midi(self.my_midi)
        
        for bar in self.bass_list:
            for note in bar:
                note.add_to_midi(self.my_midi)
    
        for bar in self.drums_list:
            for part in bar:
                for note in part:
                    note.add_to_midi(self.my_midi)
        
        with open(self.file_name + ".mid", "wb") as output_file:
            self.my_midi.writeFile(output_file)
        print("DONE===========================================================", self.time)