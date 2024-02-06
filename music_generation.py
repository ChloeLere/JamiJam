from midiutil import MIDIFile
import random
from datetime import datetime
import mg_lib

class MusicGeneration:
    def __init__(self, tempo=-1, feeling="joy"):
        self.time = 0
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


    def generate_midi(self):
        return
    
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
        return