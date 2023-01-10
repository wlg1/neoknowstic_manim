from manim import *

class FractalDMT(Scene):
    def construct(self):
        # Create the initial shape (a circle)
        shape = Circle(radius=1, color=BLUE)

        # Add the shape to the scene
        self.add(shape)

        # Animate the transformation of the shape into a fractal
        self.play(
            shape.apply_function, lambda p: (p[0]/2, p[1]/2),
            run_time=1
        )
        self.play(
            shape.apply_function, lambda p: (p[0]/2 - p[1]/2, p[0]/2 + p[1]/2),
            run_time=1
        )
        self.play(
            shape.apply_function, lambda p: (p[0]/2 + p[1]/2, p[0]/2 - p[1]/2),
            run_time=1
        )
        self.play(
            shape.apply_function, lambda p: (p[0]/2, -p[1]/2),
            run_time=1
        )

