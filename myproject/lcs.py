from big_ol_pile_of_manim_imports import *

# x = "ABCBDAB"
x = "1234"
y = "BDCABA"


class MyGrid(VMobject):
    def __init__(self, width, height, distance, **kwargs):
        self.distance = distance
        self.width = width * self.distance
        self.height = height * self.distance
        VMobject.__init__(self, **kwargs)

    def generate_points(self):
        distance = 0.5
        rect = Rectangle(
            height=self.height,
            width=self.width,
            stroke_width=0.5,
            fill_color=BLUE_A,
            fill_opacity=1,
        )
        self.add(rect)
        for x in np.arange(self.distance, self.width, self.distance):
            self.add(Line(
                [x - self.width / 2, -self.height / 2, 0],
                [x - self.width / 2, self.height / 2, 0],
            ))
        for y in np.arange(self.distance, self.height, self.distance):
            self.add(Line([-self.width / 2, y - self.height / 2, 0], [self.width / 2, y - self.height / 2, 0]))


class LCSScene(Scene):
    CONFIG = {
        "width": len(x) + 1,
        "height": len(y) + 1,
        "distance": 0.5,
    }

    def construct(self):
        self.createRect()

    def createRect(self):
        grid = MyGrid(
            self.width,
            self.height,
            self.distance,
        ).to_edge(RIGHT)

        anim = []
        test = ["1"]
        for word in test:
            label = TexMobject(word)
            #print((2 * (index + 1) / self.width - 1.0) * RIGHT + UP)
            # label.next_to(grid, (2 * (index + 1) / self.width - 1.0) * RIGHT + UP)
            label.move_to(grid, 0.5 * LEFT + UP)
            anim.append(FadeIn(label))

        self.play(
            ShowCreation(grid),
            *anim,
        )
        self.wait()
        self.grid = grid
