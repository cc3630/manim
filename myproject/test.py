# coding:utf-8
import numpy as np

LOW_QUALITY_FRAME_DURATION = 1. / 15
MEDIUM_QUALITY_FRAME_DURATION = 1. / 30
PRODUCTION_QUALITY_FRAME_DURATION = 1. / 60

# There might be other configuration than pixel shape later...
PRODUCTION_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 1440,
    "pixel_width": 2560,
}

HIGH_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 1080,
    "pixel_width": 1920,
}

MEDIUM_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 720,
    "pixel_width": 1280,
}

LOW_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 480,
    "pixel_width": 854,
}

DEFAULT_PIXEL_HEIGHT = PRODUCTION_QUALITY_CAMERA_CONFIG["pixel_height"]
DEFAULT_PIXEL_WIDTH = PRODUCTION_QUALITY_CAMERA_CONFIG["pixel_width"]

DEFAULT_POINT_DENSITY_2D = 25
DEFAULT_POINT_DENSITY_1D = 250

DEFAULT_STROKE_WIDTH = 4

FRAME_HEIGHT = 8.0
FRAME_WIDTH = FRAME_HEIGHT * DEFAULT_PIXEL_WIDTH / DEFAULT_PIXEL_HEIGHT
FRAME_Y_RADIUS = FRAME_HEIGHT / 2
FRAME_X_RADIUS = FRAME_WIDTH / 2

SMALL_BUFF = 0.1
MED_SMALL_BUFF = 0.25
MED_LARGE_BUFF = 0.5
LARGE_BUFF = 1

DEFAULT_MOBJECT_TO_EDGE_BUFFER = MED_LARGE_BUFF
DEFAULT_MOBJECT_TO_MOBJECT_BUFFER = MED_SMALL_BUFF


# All in seconds
DEFAULT_ANIMATION_RUN_TIME = 1.0
DEFAULT_POINTWISE_FUNCTION_RUN_TIME = 3.0
DEFAULT_WAIT_TIME = 1.0


ORIGIN = np.array((0., 0., 0.))
UP = np.array((0., 1., 0.))
DOWN = np.array((0., -1., 0.))
RIGHT = np.array((1., 0., 0.))
LEFT = np.array((-1., 0., 0.))
IN = np.array((0., 0., -1.))
OUT = np.array((0., 0., 1.))
X_AXIS = np.array((1., 0., 0.))
Y_AXIS = np.array((0., 1., 0.))
Z_AXIS = np.array((0., 0., 1.))

# Useful abbreviations for diagonals
UL = UP + LEFT
UR = UP + RIGHT
DL = DOWN + LEFT
DR = DOWN + RIGHT

TOP = FRAME_Y_RADIUS * UP
BOTTOM = FRAME_Y_RADIUS * DOWN
LEFT_SIDE = FRAME_X_RADIUS * LEFT
RIGHT_SIDE = FRAME_X_RADIUS * RIGHT

PI = np.pi
TAU = 2 * PI
DEGREES = TAU / 360


def generate_points():
    anchors = np.array([np.cos(a) * RIGHT + np.sin(a) * UP for a in np.linspace(0, 2 * PI, 9)])
    # Figure out which control points will give the
    # Appropriate tangent lines to the circle
    d_theta = 2 * PI / (9 - 1.0)
    tangent_vectors = np.zeros(anchors.shape)
    print(tangent_vectors)
    tangent_vectors[:, 1] = anchors[:, 0]
    print(tangent_vectors)
    tangent_vectors[:, 0] = -anchors[:, 1]
    print(tangent_vectors)
    handles1 = anchors[:-1] + (d_theta / 3) * tangent_vectors[:-1]
    print(handles1)
    handles2 = anchors[1:] - (d_theta / 3) * tangent_vectors[1:]
    print(handles2)

generate_points()