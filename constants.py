WIDTH = 640
HEIGHT = 480
FPS = 120

BG_SCALE = HEIGHT / 1024
TOP_LANE_Y = 272 * BG_SCALE
BOTTOM_LANE_Y = 50 * BG_SCALE
PIXELS_TO_MTS = WIDTH / 10
ACC = 5 # mt/s^2
X_ACC = ACC * PIXELS_TO_MTS # pixels/s^2?
