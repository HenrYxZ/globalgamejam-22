import numpy as np


from constants import *
from tree import Tree


rng = np.random.default_rng()
OFFSET_Y = 64 * BG_SCALE


class LevelMaker:
    @staticmethod
    def create_trees(footprint, length, tree_prob, offset, partition_size):
        iterations = int(length // footprint)
        tree_probs = rng.random(iterations)
        offsets = rng.random(iterations) * offset
        offsets_y = rng.random(iterations) * OFFSET_Y
        current_partition = 1
        trees = [[]]
        for i in range(iterations):
            pos = footprint * i + offsets[i]
            if pos > (current_partition * partition_size):
                trees.append([])
                current_partition += 1
            if tree_probs[i] <= tree_prob:
                x = pos
                y = HEIGHT - 506 * BG_SCALE + offsets_y[i]
                trees[current_partition - 1].append([x, y])
        return trees

    @staticmethod
    def create_obstacles(footprint, length, prob, offset, partition_size):
        iterations = int(length // footprint)
        probs = rng.random(iterations)
        offsets = rng.random(iterations) * offset
        channels = rng.random(iterations)
        current_partition = 1
        obstacles = [[]]
        for i in range(iterations):
            pos = footprint * i + offsets[i]
            if pos > (current_partition * partition_size):
                obstacles.append([])
                current_partition += 1
            if probs[i] <= prob:
                x = pos
                y = TOP_LANE_Y if channels[i] < 0.5 else BOTTOM_LANE_Y
                obstacles[current_partition - 1].append([x, y])
        return obstacles
