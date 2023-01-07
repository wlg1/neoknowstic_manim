from manim import *

class SquareToCircle(Scene):
    def construct(self):
        #define the unmoving objects
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        # tell what animations to do using the unmoving objects
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))