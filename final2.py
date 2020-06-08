import webcolors
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt

from skimage import io

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS2_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name
r=int(input('RED'))
g=int(input('GREEN'))
b=int(input('BLUE'))
requested_colour = (r, g, b)
actual_name, closest_name = get_colour_name(requested_colour)

print ("Actual colour name:", actual_name, ", closest colour name:", closest_name)


def colorsug1(r,g,b):
	temp=r
	r=g
	g=temp
	
	
	requested_colour = (r, g, b)
	actual_name, closest_name = get_colour_name(requested_colour)

	print ("Actual colour name:", actual_name, ", closest colour name:", closest_name)
	
	return requested_colour
     

colorsug1(r,g,b)



def colorsug2(r,g,b):
	temp1=r
	r=b
	b=temp1
	
	
	requested_colour = (r, g, b)
	actual_name, closest_name = get_colour_name(requested_colour)

	print ("Actual colour name:", actual_name, ", closest colour name:", closest_name)
	
	return requested_colour

colorsug2(r,g,b)


	
palette = np.array([[ r,   g,   b], # index 0: red
                    [  g, r,   b], # index 1: green
                        [  b,   g, r], # index 2: blue
                        [255, 255,   255], # index 5: yellow
                         ], dtype=np.uint8)
     

m, n = 4,6

indices = np.random.randint(0, len(palette), size=(m, n))

indices

io.imshow(palette[indices])
	
	