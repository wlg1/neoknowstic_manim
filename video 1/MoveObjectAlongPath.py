from manim import *

class MoveObjectAlongPath(Scene):
    def construct(self):
        # Create a list of points for the object to move along
        points = [LEFT, RIGHT, UP, DOWN, LEFT+UP, RIGHT+UP, RIGHT+DOWN, LEFT+DOWN]

        # Create a circle to represent the moving object
        circle = Circle(radius=0.3, color=BLUE)

        # Create a path using the list of points
        path = VMobject()
        path.set_points_smoothly([*map(lambda p: [p[0], p[1], 0], points)])

        # Add the path and the circle to the scene
        self.add(path, circle)

        # Move the circle along the path using the MoveAlongPath class
        self.play(MoveAlongPath(circle, path), run_time=5)
