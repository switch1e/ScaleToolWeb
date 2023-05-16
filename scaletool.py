notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
from guitar import *
from PIL import Image, ImageFont, ImageDraw, ImageChops

# Coefficients for the regression formula
terms = [
    1.9077733860358759e+001,
    1.1306223907600044e+002,
    -2.9142652838298613e+000,
    3.2981806170195319e-002
]

def build_scale(key_center, scale_name):
    # Get the index of the key center note
    start_index = notes.index(key_center)
    sc = []
    
    # Define the step lists for various scales
    major_steps = [2, 2, 1, 2, 2, 2, 1]
    minor_pent_steps = [3, 2, 2, 3, 2]
    harmonic_minor_steps = [2, 1, 2, 2, 1, 3, 1]
    step_list = []
    
    # Determine the step list based on the scale name
    if scale_name == "Major":
        step_list = major_steps
    elif scale_name == "Minor":
        step_list = cyclically_reorder_list(major_steps, 5)
    elif scale_name == "Dorian":
        step_list = cyclically_reorder_list(major_steps, 1)
    elif scale_name == "Phrygian":
        step_list = cyclically_reorder_list(major_steps, 2)
    elif scale_name == "Lydian":
        step_list = cyclically_reorder_list(major_steps, 3)
    elif scale_name == "Mixolydian":
        step_list = cyclically_reorder_list(major_steps, 4)
    elif scale_name == "Locrian":
        step_list = cyclically_reorder_list(major_steps, 6)
    elif scale_name == "Minor Pentatonic":
        step_list = minor_pent_steps
    elif scale_name == "Major Pentatonic":
        step_list = cyclically_reorder_list(minor_pent_steps, 1)
    elif scale_name == "Harmonic Minor":
        step_list = harmonic_minor_steps
    else:
        # Handle unknown scale names or default case
        step_list = []  # Set an appropriate default value

    sc.append(key_center)

    i = start_index
    # Iterate over the step list and add notes to the scale
    for j in step_list[:-1]:
        i = i + j
        sc.append(notes[i % len(notes)])
    
    return sc



def generate_scale_image(tuning, key_center, scale_name):
    # Create the title text for the image
    title_text = key_center + " " + scale_name + " in " + ''.join(tuning)
    tuning.reverse()

    # Defining Fonts
    font_large = ImageFont.truetype("Font/PlayfairDisplay-Medium.ttf", 45)
    font_small = ImageFont.truetype("Font/PlayfairDisplay-Medium.ttf", 29)
    fret_image = Image.open("Images/guitar_fret.png")
    output = ImageDraw.Draw(fret_image)
    
    # Draw the title on the image
    output.text((800, 108), title_text, (0, 0, 0), anchor="mb", font=font_large)
    
    tuning.reverse()
    
    # Build the scale based on the key center and scale name
    sc = build_scale(key_center, scale_name)
    
    # Iterate over each string in the tuning
    for t in range(len(tuning)):
        g = Guitar_String(tuning[t], key_center, scale_name)
        
        # Draw the note or 'X' for each string depending on whether it's in the scale
        if tuning[t] in sc:
            output.text((53, 300 - (29 * t)), tuning[t], (0, 0, 0), font=font_small)
        else:
            output.text((53, 300 - (29 * t)), "X", (0, 0, 0), font=font_small)
        
        starting_note_index = notes.index(g.open_note)
        
        # Iterate over each fret position
        for x in range(1, 25):
            current_note = notes[(x + starting_note_index) % len(notes)]
            
            # Draw the note mark on the fretboard image if it's in the scale
            if current_note in sc:
                note_mark = Image.open("Images/" + "".join(current_note) + ".png")
                
                # Invert the color of the note mark if it matches the key center
                if current_note == key_center:
                    note_mark = invert_color(note_mark)
                
                fret_image.paste(note_mark, (round(regress(x)), 306 - (29 * t)), mask=note_mark)

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