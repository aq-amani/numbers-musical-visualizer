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

def number_mapper_chromatic(number_list, start_note_name, start_octave, end_octave):
    """Map a list of numbers to a list of notes on a, possibly multioctave, chromatic scale

    Arguments:
    number_list -- List of numbers to map
    start_note_name -- name of note to start from for mapping
    start_octave -- octave of starting note
    end_octave -- octave of the ending note for mapping
    """
    out_list = []
    start_note = Note(start_note_name, start_octave)
    mapping_targets = start_note.get_consecutive_notes(12 * (end_octave - start_octave + 1))
    print(f'Mapping note range : {mapping_targets[0].name}{mapping_targets[0].octave} ~ {mapping_targets[-1].name}{mapping_targets[-1].octave}')

    for number in number_list:
        idx = number % len(mapping_targets)
        out_list.append(mapping_targets[idx])
    return out_list, mapping_targets

def number_mapper_to_scale(number_list, scale_name, root_note_name, octave, length = None):
    """Map a list of numbers to a list of notes

    Arguments:
    number_list -- List of numbers to map
    scale_name -- Name of musical scale to use as mapping target
    root_note_name -- Name of the root note of the scale
    octave -- octave of the root note
    length -- Specify for non-standard scale lengths(ex. when spanning multiple octaves). Defaults to standard scale length
    """
    out_list = []
    scale_length = len(mt.all_scale_info[scale_name]['signature']) if not length else length
    mapping_targets = mt.construct_scale(Note(root_note_name, octave), mt.all_scale_info[scale_name]['signature'], scale_length)
    print('Mapping note range :')
    print(*[n.name+str(n.octave) for n in mapping_targets], sep = ', ')
    for number in number_list:
        target = mapping_targets[number % scale_length]
        out_list.append(target)
    return out_list, mapping_targets

def number_mapper_to_scale_with_backing(number_list, scale_name, root_note_name, octave, p_list, backing_list, length = None):
    """Map a list of numbers to a list of notes with backing notes

    Arguments:
    number_list -- List of numbers to map
    scale_name -- Name of musical scale to use as mapping target
    root_note_name -- Name of the root note of the scale
    octave -- octave of the root note
    p_list -- Prime list to compare against
    backing_list -- list to use as backing. Normally list of integers.
    length -- Specify for non-standard scale lengths(ex. when spanning multiple octaves). Defaults to standard scale length
    """
    out_list = []
    scale_length = len(mt.all_scale_info[scale_name]['signature']) if not length else length
    mapping_targets = mt.construct_scale(Note(root_note_name, octave), mt.all_scale_info[scale_name]['signature'], scale_length)
    print('Mapping note range :')
    print(*[n.name+str(n.octave) for n in mapping_targets], sep = ', ')
    for number in range(0,backing_list[-1]+1):
        if number not in p_list:
            out_list.append(Note('A', 2)) if number % 2 == 0 else out_list.append(Note('E', 2))
        else:
            idx = number_list.pop(0) % len(mapping_targets)
            out_list.append(mapping_targets[idx])
    return out_list, mapping_targets

def string_to_int_list(number_string):
    """Convert a string of numbers to a list of integers

    Arguments:
    number_string -- string containing numbers to convert
    """
    int_list = []
    for c in number_string:
        int_list.append(int(c))
    return int_list

def note_color_mapper(note_list):
    """Maps note objects to colors

    Arguments:
    note_list -- list of note objects
    """
    # For HSV color mapping
    #r,g,b = colorsys.hsv_to_rgb(mp.color_map[mapped_notes[frame_number].name], 1.0, 1.0)
    #color = (r, g, b, 1)

    # Different color shades according to octave
    #octave =  mapped_notes[frame_number].octave
    #color = (octave/7 * (r/255), octave/7 * (g/255), octave/7 * (b/255), 1)
    color_list = []
    for n in note_list:
        if n.octave == 2:
            color = (236/255, 236/255, 236/255, 1)
        else:
            r,g,b = color_map[n.name]
            color = (r/255, g/255, b/255, 1)
        color_list.append(color)
    return color_list
