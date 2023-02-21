from manim import *
from random import randint, random

class scene_9_0(Scene):
    def construct(self):
        numb = NumberLine(
            x_range=[0, 5, 1],
            color=WHITE,
            include_numbers=True,
            label_direction=DOWN,
        )

        numb1 = numb.copy().shift(UP*1.5)
        numb2 = numb.copy().shift(DOWN*1.5)

        apple1 = ImageMobject("apple.jpg").move_to(numb1.number_to_point(1)).shift(UP*0.5).scale(0.6)
        apple2 = apple1.copy().move_to(numb1.number_to_point(2)).shift(UP*0.5)

        orange1 = ImageMobject("orange.jpg").move_to(numb2.number_to_point(1)).shift(UP*0.5).scale(0.2)
        orange2 = ImageMobject("orange.jpg").move_to(numb2.number_to_point(2)).shift(UP*0.5).scale(0.2)

        dot = Dot(color=PURPLE, radius = 0.2, fill_opacity=1).move_to(numb.number_to_point(2))

        self.add(apple1, apple2, orange1, orange2)
        self.wait(2)
        self.play(FadeIn(numb1, numb2))
        self.wait(2)
        self.play(FadeOut(apple1, apple2, orange1, orange2))
        self.play(Transform(numb1, numb), Transform(numb2, numb))
        self.play(GrowFromCenter(dot))

        self.wait(2)

        self.play(FadeOut(dot, numb1, numb2))

        apple3 = ImageMobject("apple.jpg").shift(LEFT*2.5)
        apple4 = ImageMobject("apple.jpg").shift(LEFT*3.5+UP)
        apple5 = ImageMobject("apple.jpg").shift(LEFT*3.5+DOWN)
        numb3 = numb.copy().shift(RIGHT*4)
        neq = MathTex(r"\neq").scale(3)

        self.play(FadeIn(apple3, apple4, apple5, neq, numb3))
        self.wait(2)