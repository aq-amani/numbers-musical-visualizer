import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading
import sys
sys.path.append('./music-theory/')
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import argparse

import playback as pb
import mapper as mp
import number_sequences as sq
import mt_toolbox as mt

# animation parameters
growth_rate = 500
initial_size = 1000
max_visible_notes = 200

#music parameters
music_thread = threading.Thread(target=pb.play_midi_file, args=(pb.midi_filename,))
mapped_notes = []
mapped_colors = []
map = []
number_list = []
#Text parameters
symbol = ''
sequence_name = ''
mapping_type = ''
# initialize the plot
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])
fig.canvas.manager.set_window_title('Number Sequence Musical Visualizer')

plotted_notes = np.zeros(max_visible_notes, dtype=[('position', float, 2),
                                      ('size',     float, 1),
                                      ('growth_rate',   float, 1),
                                      ('color',    float, 4)])

plotted_notes['position'] = (0.5, 0.5)
plotted_notes['growth_rate'] = growth_rate

scat = ax.scatter(plotted_notes['position'][:, 0], plotted_notes['position'][:, 1],
                  s=plotted_notes['size'], lw=2, edgecolors=plotted_notes['color'],
                  facecolors='None')

fig_text = plt.figtext(0.5, 0.5, '', c = 'white', fontweight = 'bold', ha = 'center', va = 'center', fontsize=12)
info_string = ''
info_text = plt.figtext(0.02, 0.85, info_string, c = 'white', fontweight = 'bold', fontsize=12)

def init_plot():
    #print("initializing plot")
    pass

def refresh_graph(frame_number):
    fig.patch.set_facecolor('black')

    current_index = frame_number % max_visible_notes

    # Make all colors more transparent as time progresses.
    plotted_notes['color'][:, 3] -= 1.0/len(plotted_notes)
    plotted_notes['color'][:, 3] = np.clip(plotted_notes['color'][:, 3], 0, 1)

    # Make all circles bigger.
    plotted_notes['size'] += plotted_notes['growth_rate']
    # Set size for newly spawn circles
    plotted_notes['size'][current_index] = initial_size
    # Set growth rate for new circles
    plotted_notes['growth_rate'][current_index] = growth_rate

    # set circle color based on the corrospondong musical note
    color = mapped_colors[frame_number]

    plotted_notes['color'][current_index] = color

    # Update the scatter collection, with the new colors, sizes and positions.
    scat.set_edgecolors(plotted_notes['color'])
    scat.set_sizes(plotted_notes['size'])
    scat.set_offsets(plotted_notes['position'])
    # Update text
    fig_text.set_text(symbol)
    info_text.set_text(f'Currently playing: {sequence_name}\nNumber mapping: To {mapping_type} scale\nNote mapping range: {map[0].name}{map[0].octave}~{map[-1].name}{map[-1].octave}\nCurrent number/digit: {number_list[frame_number]}\nCurrent note: {mapped_notes[frame_number].name}{mapped_notes[frame_number].octave}')
    # start playing music with the first frame
    if frame_number == 0:
        music_thread.start()

def main():
    global mapped_notes
    global map
    global symbol
    global sequence_name
    global mapping_type
    global number_list
    global mapped_colors

    parser = argparse.ArgumentParser(description='play_numbers.py: A script to visually and musically represent number sequences')

    parser.add_argument('-n','--sequenceName', choices=list(sq.number_sequences.keys()), help='Number sequence name', default = 'Pi', metavar = '')
    parser.add_argument('-m','--mapping', choices=list(mt.all_scale_info.keys()).extend(['chromatic']),  help='Chromatic mapping or scale name for scale mapping', default = 'chromatic', metavar = '')
    parser.add_argument('-r','--root', choices=list(mt.basic_notes.keys()), help='Scale root or note to start from', default = 'C', metavar = '')
    parser.add_argument('-s','--startOctave', choices=[i for i in range(0, 8)], help='Start note octave setting.', default = 4, type = int, metavar = '')
    parser.add_argument('-e','--endOctave', choices=[i for i in range(0, 8)], help='End note octave setting.', default = 4, type = int, metavar = '')
    parser.add_argument('-l','--scaleLength', help='End note octave setting.', default = 24, type = int, metavar = '')

    args = vars(parser.parse_args())

    sequence_name = args['sequenceName']
    number_list = sq.number_sequences[sequence_name]['data']
    if type(number_list) == str:
        number_list = mp.string_to_int_list(number_list)
    symbol = sq.number_sequences[sequence_name]['symbol']
    mapping_type = args['mapping']
    root_note =  args['root']
    start_octave = args['startOctave']
    end_octave = args['endOctave']
    scale_length = args['scaleLength']

    if mapping_type == 'chromatic':
        mapped_notes, map = mp.number_mapper_chromatic(number_list, root_note, start_octave, end_octave)
    else:
        mapped_notes, map = mp.number_mapper_to_scale(number_list, mapping_type, root_note, start_octave, scale_length)

    mapped_colors = mp.note_color_mapper(mapped_notes)

    pb.create_midi(mapped_notes, 'scale', t=1)

    # init function used to avoid repeating the initial frame
    animation = FuncAnimation(fig, refresh_graph, init_func = init_plot, interval=150, frames=len(mapped_notes), repeat = False)
    plt.show()

if __name__ == "__main__":
    main()
