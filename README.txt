Overview

This project implements an OARSMT (Obstacle-Avoiding Rectilinear Steiner Minimum Tree) algorithm. The test executable in the oarsmt folder constructs a Steiner tree based on given pin coordinates and obstacle locations.


Files

1. test – The compiled executable for the OARSMT algorithm.
2. pins.csv – Input file containing the coordinates of the pins.
3. obstacles.csv – Input file containing the coordinates of rectangular obstacles.
4. tree_results.csv – Output file recording the edges of the generated Steiner tree.
5. plotrouting.py – Python script to visualize the routing result.
6. tree_plot.jpg – Example image showing the plotted Steiner tree with obstacles.


How to Run

In the oarsmt directory, use the following command to execute the program:

./test [pins file name] [obstacles file name]


Example

./test pins.csv obstacles.csv


After execution:

1. The program will print the runtime and the total wirelength of the generated Steiner tree.
2. The routing result (tree edges) will be saved in tree_results.csv.


Visualization

To visualize the Steiner tree and obstacles, run:

python plotrouting.py

This will generate a plot similar to the example image tree_plot.jpg.