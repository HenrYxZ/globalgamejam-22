WIDTH = 640
HEIGHT = 480
FPS = 60

BG_SCALE = HEIGHT / 1024
TOP_LANE_Y = 272 * BG_SCALE
BOTTOM_LANE_Y = 50 * BG_SCALE
MTS_TO_PIXELS = WIDTH / 10
ACC = 5 # mt/s^2
X_ACC = ACC * MTS_TO_PIXELS # pixels/s^2?

TREE_FOOTPRINT = 1.5
TREE_OFFSET = 0.3
TREE_PROB = 0.65

ROCKS_FOOTPRNT = 6
ROCKS_OFFSET = 2
ROCKS_PROB = 0.3

LVL_LENGTH = 500
PARTITION_SIZE = 20

SKY_PARALLAX = 0.25
BG_LOOP_POINT = 1024
SKY_LOOP_POINT = 1024
