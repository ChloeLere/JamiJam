# JamiJam

## Description

This project aims to create simple yet *hearable* midi files for amateurs to
edit them in their preferred DAW (Fruity Loops, Ableton, LMMS).

## Execution

To execute the program, either:

### Download and launch the executable

Go to the release tab and download the last version.
This version should already fix one of the issues related to midiutil.

### Run it yourself

If you go this route, you will have to implement a custom fix for a known issue in the midiutil library.

```bash
pip install midiutil
```

Implement the last custom fix for this: [Issue #24](https://github.com/MarkCWirt/MIDIUtil/issues/24) (take the one from  fornof or kevinlinxc):

```python
# midiutil/MidiFile.py
# line 888
                    else:
                        try:
                            stack[noteeventkey].pop()
                            tempEventList.append(event)
                        except IndexError as e:
                            print("IndexError skipped")
```

Then run it ^^

```bash
./jamijam
```

## Tracks

The resulting midi file contains 4 tracks:

- harmonics/chords
- melody/lead
- drums (on channel 10)
- bass

## Authors

- [Clovis Schneider](clovis.schneider@epitech.eu)
- [Chloé Lere](chloe.lere@epitech.eu)
