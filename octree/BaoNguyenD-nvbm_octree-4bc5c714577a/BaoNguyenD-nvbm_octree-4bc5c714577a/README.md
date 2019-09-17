# README #
The persistent merge octree implementation that run in memory simulate NVRAM (NONVOLATILE MEMORY)
New version of octree: call as pm_octree 
Where
 V0 is an octree at time T0
 V1 is an octree at time T1

 V1 and V0 share an "sub-tree" called as C0 which lies on DRAM
 In the simulation process, we have the RAM-BOUND, if the size of C0 reach the threshold then we need to choose 
a subtree of C0 to merge back to NVBM (which was the V1)

To run:

Simply type 'make' to compile the code

Then to create the tree from input file (e.g example.txt and input.txt) just simply type:

./octree <input> 

Note : input format should has appropriated coordinate for each octant
Example format <x> <y> <z> <type> <tag> <value>

There are several test case marked with #DEFINE tag.
For example to test tree operations with locational based:
 - uncomment #define LOCATION 1
To test with valued based:
 - uncomment #define VALUE 1 
To save output to file for other visulization later:
 - Uncomment #define EXTRACTMESH 1 and comment out #define DEBUG then:
./octree <input>  >  <OUTPUT>

then run:


For others test just remove command in the source code and run the program normally as 
./octree <input>   

For mpi:

mpirun -n <number of PE> ./octree <input>

examples.txt: A empty tree divided up to level 6 without any specific information.
The refine function in this program for testing purpose is Rotating a "disk" in 3D dimension 90 degree. In the simulation
process, we refine the octants that satify the refine condition (which is octants lie on a "new disk".
Maximum level is defined by user (8 in this test case)
One can implement the refine functions to server his/her own purpose. 
