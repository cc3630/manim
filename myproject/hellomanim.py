# coding:utf-8
from big_ol_pile_of_manim_imports import *


class MyCircle(Circle):
    def __init__(self, **kwargs):
        Circle.__init__(self, **kwargs)

    def generate_points(self):
        anchors = np.array([
            np.cos(a) * RIGHT + np.sin(a) * UP
            for a in np.linspace(self.start_angle + self.angle, self.start_angle, self.num_anchors)
        ])
        # Figure out which control points will give the
        # Appropriate tangent lines to the circle
        d_theta = self.angle / (self.num_anchors - 1.0)
        tangent_vectors = np.zeros(anchors.shape)
        tangent_vectors[:, 1] = -anchors[:, 0]
        tangent_vectors[:, 0] = anchors[:, 1]
        handles1 = anchors[:-1] + (d_theta / 3) * tangent_vectors[:-1]
        handles2 = anchors[1:] - (d_theta / 3) * tangent_vectors[1:]
        self.set_anchors_and_handles(anchors, handles1, handles2)
        self.scale(self.radius, about_point=ORIGIN)


class HelloManim(Scene):
    def construct(self):
        circle = MyCircle(color='#ffff00', radius=2.5, start_angle=PI)
        self.play(ShowCreation(circle))
        self.wait()
