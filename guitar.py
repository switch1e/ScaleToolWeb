notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
from PIL import Image, ImageFont, ImageDraw 

# used for reordering of scale steps
def cyclically_reorder_list(lst, start):
            n = len(lst)
            start %= n  # Ensure start is within the valid range
            
            # Create the reordered list using slicing and concatenation
            reordered_list = lst[start:] + lst[:start]
            
            return reordered_list

class Guitar_String:

    def __init__(self, open_note, key_center, scale):
        self.open_note = open_note
        self.key_center = key_center
        self.scale = scale
        # self.scale = self.build_scale()

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
