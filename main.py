from midiutil import MIDIFile
from datetime import datetime
from music_generation import MusicGeneration
from appJar import gui
import pandas as pd
import random

win = gui('Test')

def get_list_emotion():
    file_result = pd.read_csv("./data/MusicalScaleTable.csv")
    list_emotions = []
    for index, row in file_result.iterrows():
        list_emotions += row["emotion"].replace(" ", "").split(',')
    return set(list_emotions)


def generate(btn):
    emotion = win.getOptionBox("Emotion : ")
    filename = win.getEntry("File name : ")
    tempo = win.getSpinBox("Tempo : ") #faire en sorte de pouvoir avoir un tempo aleatoir
    if filename == "":
        filename = "output_" + str(datetime.now())
    music_gen = MusicGeneration(int(tempo), emotion, filename) 
    music_gen.generate_midi()

def main():
    win.addLabel("f1","Name is a musique generator.")
    win.addLabel("f2","You can choose to modify some option before genereting your music")
    win.addLabelOptionBox("Emotion : ", get_list_emotion())
    win.addLabelEntry("File name : ")
    win.addLabelSpinBoxRange("Tempo : ", 40, 200)
    win.setSpinBox("Tempo : ", int(random.gauss(100, 10)))

    win.addButton("Generate", generate)
    win.go()

    
    return


main()