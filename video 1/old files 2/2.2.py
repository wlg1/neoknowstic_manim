from manim import *

class ManimScene(Scene):
    def construct(self):
        cat = ImageMobject("cat.png").scale(1.5)
        self.play(FadeIn(cat))
        
        face_2 = Line([0,0,0], [0.66,0,0], color = RED, stroke_width=5).shift(LEFT*1.37 + UP*0.2)
        body_2 = Ellipse(color=BLUE, height=1, width=2.1, stroke_width=5).shift(DOWN*0.1 + RIGHT*0.12)
        face_box = Rectangle(color=WHITE, height=3, width=5, stroke_width=5)
        
        self.wait(1)        
        self.play(FadeIn(face_box))
        self.wait(1)
        self.play(GrowFromCenter(face_2))
        self.wait(1)
        self.play(GrowFromCenter(body_2))
        self.wait(3)