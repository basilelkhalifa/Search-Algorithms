
# BLOCK WORLD <h1>

The block world is a sliding puzzle that consists of an area that is divided into a grid of size 4x4 (see Figure below). Different 
coloured blocks occupy different proportions of the grid.


![](/BlockWorld/sample_images/sample_state.png)

*Each blue block occupies a region of size 1x1 in the environment.*

*Each green block occupies a region of size 1x2 or 2x1 in the environment.*

*Each red block occupies a region of size 2x2 in the environment.*

*There are 2 white blocks (each of size 1x1) representing blank space in the environment.*

The configuration shown in Figure 2.1 is represented by the following 2D array:
[ [1,2,1,1], [1,2,4,4], [2,2,4,4], [1,1,0,0] ] where 0 represents a blank space, 1 represents a blue block, 2 represents a green block, and 4 represents a red block.
Each block in the block world can slide into an empty space adjacent to it, as long as it can fit into that space. The figure below illustrates the successor states that result from the initial configuration.


![](/BlockWorld/sample_images/expanded.png)
Assume that the red block is trying to find its way out of the environment, and the only door is at the bottom left corner. The goal test for this puzzle is therefore to find a configuration that has the red block at the bottom left corner. An example of such a goal state is given in the firgure below.

![](/BlockWorld/sample_images/goal_state.png)

In the following repo, the puzzle is solved using the breadth-fisrt search the depth-first search and a* search algorithms.
