from note import Note
from note import basic_notes
import mt_toolbox as mt

note_list = list(basic_notes)

# Red at C
#color_map = {
#    "C" 		: (255,0,0),
#    "C#" 		: (139,0,0),
#    "D" 		: (255,128,0),
#    "D#" 		: (205,133,0),
#    "E" 	    : (255,255,0),
#    "F" 		: (0,255,0),
#    "F#" 		: (0,139,0),
#    "G" 		: (0,0,255),
#    "G#" 		: (0,0,139),
#    "A" 		: (128,0,128),
#    "A#" 		: (85,26,139),
#    "B" 	    : (75,0,130),
#}

# Red at A (since red light frequency is 440THz
# and sound frequency of A at 4th octave is 440Hz)
color_map = {
    "A" 		: (255,0,0),
    "A#" 		: (139,0,0),
    "B" 		: (255,128,0),
    "C" 		: (205,133,0),
    "C#" 	    : (255,255,0),
    "D" 		: (0,255,0),
    "D#" 		: (0,139,0),
    "E" 		: (0,0,255),
    "F" 		: (0,0,139),
    "F#" 		: (128,0,128),
    "G" 		: (85,26,139),
    "G#" 	    : (75,0,130),
}
## Hue based color map. Red at A (max 360)
#color_map = {
#    "A" 		: 0/360, # R
#    "A#" 		: 15/360, # orange red
#    "B" 		: 30/360, # orange
#    "C" 		: 60/360, # Yellow
#    "C#" 	    : 90/360, # greenish yellow
#    "D" 		: 120/360, # G
#    "D#" 		: 150/360, # blueish green
#    "E" 		: 180/360, # B
#    "F" 		: 210/360, #
#    "F#" 		: 240/360,
#    "G" 		: 270/360,
#    "G#" 	    : 285/360,
#}

    Arguments:
    number_list -- List of numbers to map
    """
    notename_list = []
    for number in number_list:
        mod = number % 12
        target = note_list[mod]
        print(f'{number} --> {mod}')
        notename_list.append(target)
    return notename_list

def number_mapper_to_scale(number_list, scale_name, root_note_name, octave=4):
    """Map a list of numbers to a list of notes depending on mode

    Arguments:
    number_list -- List of numbers to map
    """
    notename_list = []
    scale_length = len(mt.all_scale_info[scale_name]['signature'])
    scale_notes = mt.construct_scale(Note(root_note_name, octave), mt.all_scale_info[scale_name]['signature'])
    for number in number_list:
        target = scale_notes[number % scale_length].name
        print(f'{number} --> {target}')
        notename_list.append(target)
    return notename_list




def note_sequencer(notename_list, octave):
    """Create a list of note objects

    Arguments:
    notename_list -- List of note names
    octave -- octave to use for notes
    """
    note_list = []
    for note in notename_list:
        note_list.append(Note(note, octave))
    return note_list

def string_to_int_list(number_string):
    """Convert a string of numbers to a list of integers

    Arguments:
    number_string -- string containing numbers to convert
    """
    int_list = []
    for c in number_string:
        int_list.append(int(c))
    return int_list

def number_to_mod(number_list, mod):
    """Map a list of numbers to a list of notes depending on mode

    Arguments:
    number_list -- List of numbers to map
    """
    for number in number_list:
        target = number % mod
        print(f'{number} --> {target}')
