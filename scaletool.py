notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
from guitar import *
from PIL import Image, ImageFont, ImageDraw, ImageChops

terms = [
     1.9077733860358759e+001,
     1.1306223907600044e+002,
    -2.9142652838298613e+000,
     3.2981806170195319e-002
]

def generate_scale_image(tuning, key_center, scale_name):
    title_text = key_center + " " + scale_name + " in " + ''.join(tuning)
    tuning.reverse()

    # Defining Fonts
    font_large = ImageFont.truetype("Font\PlayfairDisplay-Medium.ttf", 45)
    font_small = ImageFont.truetype("Font\PlayfairDisplay-Medium.ttf", 29)
    fret_image = Image.open("Images/guitar_fret.png")
    output = ImageDraw.Draw(fret_image)
    output.text((800,108), title_text, (0, 0, 0), anchor="mb", font=font_large)
    tuning.reverse()
    # print(header)
    for t in range(len(tuning)):
        g = Guitar_String(tuning[t], key_center, scale_name)
        sc = g.scale
        if(tuning[t] in sc):
            output.text((53, 300 - (29*t)), tuning[t], (0, 0, 0), font= font_small)
        else:
            output.text((53, 300 - (29*t)), "X", (0, 0, 0), font= font_small)
        starting_note_index = notes.index(g.open_note)
        for x in range (1, 25):
            current_note = notes[(x + starting_note_index) % len(notes)]
            if current_note in sc:
                note_mark = Image.open("Images\\" + "".join(current_note) + ".png")
                if current_note == key_center:
                    note_mark = invert_color(note_mark)
                fret_image.paste(note_mark, (round(regress(x)), 306 - (29 * t)), mask=note_mark)
                # fret_image.paste(note_mark, (1478 , 306 - (29 * t)), mask=note_mark)

    return fret_image

# def prompt_key_center():
#     key_center = input("Insert your desired major key_center: ").capitalize()
#     if key_center not in notes:
#         raise Exception("This is not a valid key_center.")
#     return key_center

# def prompt_tuning():
#     print("Insert your desired tuning starting from the lowest string. Accidental notes should be typed with a '#'.")
#     sequence = ['','','','','','']
#     for i in range(0,6):
#         sequence[i] = input("String " + str(6 - i) + ": ").capitalize()
#         if sequence[i] not in notes:
#             raise Exception("This is not a valid note.")
#     return sequence
        
    
def regress(x):
    t = 1
    r = 0
    for c in terms:
        r += c * t
        t *= x
    return r

def invert_color(img):
    red_channel, green_channel, blue_channel, alpha_channel = img.split()
    
    # Invert the color channels
    inverted_red_channel = red_channel.point(lambda p: 255 - p)
    inverted_green_channel = green_channel.point(lambda p: 255 - p)
    inverted_blue_channel = blue_channel.point(lambda p: 255 - p)
    
    # Combine the inverted color channels with the original alpha channel
    img = Image.merge("RGBA", (inverted_red_channel, inverted_green_channel, inverted_blue_channel, alpha_channel))

    return img                          
    

