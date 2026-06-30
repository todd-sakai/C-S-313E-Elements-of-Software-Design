# Homework 10: Bucket Fill (DFS & BFS)

## Overview
This assignment implements a "bucket fill" image editing operation using graph traversal algorithms. The program reads a text-based representation of an image, modeling it as a graph of interconnected `ColorVertex` objects where edges connect adjacent pixels of the same color. It then executes the bucket fill request to recolor the target area using both Breadth-First Search (BFS) and an iterative Depth-First Search (DFS), visually printing the step-by-step state of the image as nodes are traversed.

## Concepts Covered
* Graph data structures (Vertices and Adjacency Matrices)
* Breadth-First Search (BFS) implementation using a Queue
* Iterative Depth-First Search (DFS) implementation using a Stack
* Object-oriented programming and traversal state tracking (e.g., tracking visited flags and previous colors)