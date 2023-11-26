'''
This is a software tool that maintains the central projection of an image on one plane and 
reproduces it on another plane and 
saves the image in one of the graphic formats.
developed by Obrotskyi Myroslav group: KM-22.
'''
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

# Reading data from a file
data = np.loadtxt('DS7.txt')

# Construction of a Voronoi diagram
vor = Voronoi(data)

# canvas size
canvas_size = (960, 540)

# Creating a graphic
fig, ax = plt.subplots(figsize=(canvas_size[0] / 100, canvas_size[1] / 100), dpi=100)

# Displaying the Voronoi diagram
voronoi_plot_2d(vor, ax=ax)

# Saving the result in a graphic format file (PNG)
plt.savefig('voronoi_diagram.png')

# Show result
plt.show()

