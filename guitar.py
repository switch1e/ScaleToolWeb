notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
from PIL import Image, ImageFont, ImageDraw 

class Guitar_String:
    def __init__(self, open_note, key):
        self.open_note = open_note
        self.key = key

    def build_scale(self):
        start_i = notes.index(self.key)
        scale = []
        scale.append(self.key)
        i = start_i + 2
        scale.append(notes[i % len(notes)])
        i = i + 2
        scale.append(notes[i % len(notes)])
        i = i + 1
        scale.append(notes[i % len(notes)])
        i = i + 2
        scale.append(notes[i % len(notes)])
        i = i + 2
        scale.append(notes[i % len(notes)])
        i = i + 2
        scale.append(notes[i % len(notes)])
        return scale

    def build_string(self):
        sc = self.build_scale()
        output = ""
        if self.open_note in sc:
            if len(self.open_note) == 1:
                output = output + self.open_note + " "
            else:
                output = output + self.open_note
        else:
            output = output + "X "
        starting_note_index = notes.index(self.open_note)
        for x in range (1, 24):
            if notes[(x + starting_note_index) % len(notes)] in sc:
                f = Fret(notes[(x + starting_note_index) % len(notes)])
            else:
                f = Fret('X')
            output = output + str(f)
        return output


# class Fret:
#     def __init__(self, note):
#         self.note = note
    
#     def __str__(self):
#         if(self.note == 'X'):
#             return "|     "
#         elif(len(self.note) == 2):
#             return "|  " + self.note + " "
#         else:
#             return "|  " + self.note + "  "
