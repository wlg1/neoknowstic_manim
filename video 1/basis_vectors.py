from manim import *

class basis(Scene):
    def construct(self):   
        numberplane = NumberPlane()
        red = Vector([1, 0, 0], color=RED)
        blue = Vector([0, 1, 0], color=BLUE)

        self.add(numberplane)
        self.play(GrowArrow(red))
        self.play(GrowArrow(blue))

        self.wait(1)

        basis_words = Text("Basis Vectors").shift(DOWN)
        self.play(Write(basis_words))
        self.wait(1)

        red2 = Vector([2, 0, 0], color=RED)
        blue2 = Vector([0, 1.5, 0], color=BLUE)
        self.play(Transform(red, red2), Transform(blue, blue2))

        self.wait(1)

        red3 = Vector([2, 0, 0], color=RED).shift(UP*1.5)
        self.play(Transform(red, red3))

        self.wait(1)
        
        catWord = Text("Cat", color=BLUE, font_size=25).move_to([0, 1.5, 0]).shift(UP*0.3+LEFT*0.5)
        foodWord = Text("Food", color=RED, font_size=25).move_to([2, 1.5, 0]).shift(UP*0.3+RIGHT*0.5)
        self.play(FadeIn(catWord, foodWord))

        self.wait(1)

