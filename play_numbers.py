import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading
import sys
sys.path.append('../music-theory/')

import playback as pb
import mapper as mp
import number_sequences as sq

# animation parameters
growth_rate = 500
initial_size = 1000
max_visible_notes = 200

#music parameters
music_thread = threading.Thread(target=pb.play_midi_file, args=(pb.midi_filename,))

# initialize the plot
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

plotted_notes = np.zeros(max_visible_notes, dtype=[('position', float, 2),
                                      ('size',     float, 1),
                                      ('growth_rate',   float, 1),
                                      ('color',    float, 4)])

plotted_notes['position'] = (0.5, 0.5)
plotted_notes['growth_rate'] = growth_rate

scat = ax.scatter(plotted_notes['position'][:, 0], plotted_notes['position'][:, 1],
                  s=plotted_notes['size'], lw=2, edgecolors=plotted_notes['color'],
                  facecolors='None')
def init_plot():
    print("initializing plot")

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

    # set circle color based on the corrospondong musical note
    r,g,b = mp.color_map[note_names[frame_number]]
    color = (r/255, g/255, b/255, 1)
    plotted_notes['color'][current_index] = color
    # Set growth rate for new circles
    plotted_notes['growth_rate'][current_index] = growth_rate

    # Update the scatter collection, with the new colors, sizes and positions.
    scat.set_edgecolors(plotted_notes['color'])
    scat.set_sizes(plotted_notes['size'])
    scat.set_offsets(plotted_notes['position'])
    fig_text.set_text(number_list[frame_number])
    print(frame_number)
    # start playing music with the first frame
    if frame_number == 0:
        music_thread.start()



########
#number_list = sq.primes
#number_list = mp.string_to_int_list(sq.phi)
number_list = [i for i in range(0,11)]
note_names = mp.number_mapper_chromatic(number_list)
#note_names = ['C', 'D', 'E', 'F','G', 'A', 'B','C', 'D', 'E', 'F','G', 'A', 'B','C', 'D', 'E', 'F','G', 'A', 'B','C', 'D', 'E', 'F','G', 'A', 'B']
#note_names =mp.number_mapper_to_scale(number_list, 'Minor', 'A')
mapped_notes = mp.note_sequencer(note_names, 4)
pb.create_midi(mapped_notes, 'scale', t=1)
##
fig_text = plt.figtext(0.49, 0.495, number_list[0], c = 'white', fontweight = 'bold')

# init function used to avoid repeating the initial frame
animation = FuncAnimation(fig, refresh_graph, init_func = init_plot, interval=150, frames=len(note_names), repeat = False)
plt.show()
