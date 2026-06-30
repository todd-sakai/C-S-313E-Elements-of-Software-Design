# Homework 11: Topological Sort

## Overview
This assignment implements a topological sort algorithm on a directed graph represented by an adjacency matrix. To ensure a deterministic sorting order, the program utilizes a minimum priority queue to track the next vertices to process. Additionally, it features a cycle detection mechanism using a modified Depth-First Search (DFS) to verify that the graph is acyclic before attempting the sort.

## Concepts Covered
* Graph data structures and Adjacency Matrix representations (using 2D Python lists)
* Topological Sort algorithm implementation
* Cycle detection using modified Depth-First Search (DFS) state tracking
* Priority Queues (`MinPriorityQueue`) for deterministic vertex ordering