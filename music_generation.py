from midiutil import MIDIFile
import random
from datetime import datetime
import mg_lib

class MusicGeneration:
    def __init__(self, tempo=-1, feeling="brightness", file_name="output_" + str(datetime.now())):
        self.duration = 1
        self.volume = 100
        self.tempo = tempo
        if tempo < 0:
            self.tempo = random.randint(40, 200)
        self.feeling = feeling
        #echellenote
        #echelletype
        #rytme

        self.introduction = False
        self.verse = False
        self.pre_chorus = False
        self.refrain = False
        self.post_chorus = False
        self.bridge = False
        self.conclusion = False

        if (random.randint(0, 10) <= 5):
            self.introduction = True

        if (random.randint(0, 10) <= 7):
            self.verse = True
        
        if (random.randint(0, 10) <= 2):
            self.pre_chorus = True
        
        if (random.randint(0, 10) <= 9):
            self.refrain = True

        if (random.randint(0, 10) <= 1):
            self.post_chorus = True

        if (random.randint(0, 10) <= 4):
            self.bridge = True
        
        if (random.randint(0, 10) <= 6):
            self.conclusion = True
        self.my_midi = MIDIFile(3)

        self.file_name = file_name

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
        return
    
    def generate_verse(self):
        return
    
    def generate_pre_chorus(self):
        return
    
    def generate_refrain(self):
        return
    
    def generate_post_chorus(self):
        return
    
    def generate_bridge(self):
        return
    
    def generate_conclusion(self):
        return
    
    def create_file(self):
        with open(self.file_name + ".mid", "wb") as output_file:
            self.my_midi.writeFile(output_file)