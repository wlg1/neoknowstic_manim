from manim import *

class FactoryScene(Scene):
    def construct(self):
        # Create the factory floor
        floor = Rectangle(width=8, height=4, fill_color=GRAY, fill_opacity=0.5)

        # Create the conveyor belt
        conveyor_belt = Line(start=floor.get_left() + DOWN, end=floor.get_right() + DOWN)

        # Create the first box
        box1 = Rectangle(width=0.5, height=0.5, fill_color=YELLOW, fill_opacity=0.5)
        box1.move_to(conveyor_belt.get_start() + UP)

        # Create the second box
        box2 = Rectangle(width=0.5, height=0.5, fill_color=YELLOW, fill_opacity=0.5)
        box2.move_to(conveyor_belt.get_start() + UP)

        # Add the floor, conveyor belt, and boxes to the scene
        self.add(floor)
        self.add(conveyor_belt)
        self.add(box1)
        self.add(box2)

        # Animate the boxes moving along the conveyor belt
        self.play(
            box1.animate.move_to(RIGHT * 4)
        )
        self.play(
            box2.animate.move_to(RIGHT * 4)
        )
