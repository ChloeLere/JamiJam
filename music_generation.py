from midiutil import MIDIFile
import random
from datetime import datetime
import mg_lib
import pandas as pd


class MusicGeneration:
    def __init__(self, tempo=-1, feeling="brightness", file_name="output_" + str(datetime.now())):
        self.duration = 1
        self.volume = 100
        self.tempo = tempo
        if tempo < 0:
            self.tempo = random.randint(40, 200)
        self.feeling = feeling
        #rytme
        self.root_degrees, self.name_degrees, self.type, self.list_matching_degrees = mg_lib.get_degrees_by_feeling(feeling)

        self.introduction = self.have_to_generate(5)
        self.verse = self.have_to_generate(7)
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
        number_loop_max = random.randint(3, 5)

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
                self.generate_refrain()
            if self.post_chorus:
                self.generate_post_chorus()

        if self.conclusion:
            self.generate_conclusion()

        self.create_file()

    def generate_introduction(self):
        print("Introduction")
        return
    
    def generate_verse(self):
        print("Verse")
        return
    
    def generate_pre_chorus(self):
        print("Pre chorus")
        return
    
    def generate_refrain(self):
        print("Refrain")
        return
    
    def generate_post_chorus(self):
        print("Post chorus")
        return
    
    def generate_bridge(self):
        print("Bridge")
        return
    
    def generate_conclusion(self):
        print("Conclusion")
        return
    
    def create_file(self):
        with open(self.file_name + ".mid", "wb") as output_file:
            self.my_midi.writeFile(output_file)