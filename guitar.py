notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
from PIL import Image, ImageFont, ImageDraw 

class Guitar_String:

    def __init__(self, open_note, key_center, scale_name):
        self.open_note = open_note
        self.key_center = key_center
        self.scale_name = scale_name
        self.scale = self.build_scale()

    def build_scale(self):
        start_index = notes.index(self.key_center)
        sc = []
        major_steps = [2, 2, 1, 2, 2, 2]
        minor_steps = [2, 1, 2, 2, 1, 2]
        minor_pent_steps = [3, 2, 2, 3]
        major_pent_steps = [2, 2, 3, 2]
        harmonic_minor_steps = [2, 1, 2, 2, 1, 3]
        step_list = []
        
        if self.scale_name == "Major":
            step_list = major_steps
        elif self.scale_name == "Minor":
            step_list = minor_steps
        elif self.scale_name == "Minor Pentatonic":
            step_list = minor_pent_steps
        elif self.scale_name == "Major Pentatonic":
            step_list = major_pent_steps
        elif self.scale_name == "Harmonic Minor":
            step_list = harmonic_minor_steps
        else:
            # Handle unknown scale names or default case
            step_list = []  # Set an appropriate default value
            
        sc.append(self.key_center)

        i = start_index
        for j in step_list:
            i = i + j
            sc.append(notes[i % len(notes)])
        return sc

    def build_string(self):
        sc = self.scale
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
