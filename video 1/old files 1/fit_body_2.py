from manim import *
from random import randint, random


class VectorArrow(VectorScene, Scene):
    def setup(self):
        Scene.setup(self)
        VectorScene.setup(self)
        
    def construct(self):
        ##########################
        cat = ImageMobject("cat.png").scale(1.5)
        data_pt = ImageMobject("data pt.png").scale(1.5)
        # self.add(cat)
        #################################
        
        face_1 = Rectangle(color=RED, height=0, width=1.32, stroke_width=5).shift(LEFT + UP*0.2)
        body_1 = Ellipse(color=BLUE, height=0.5, width=1, stroke_width=5).shift(RIGHT*0.1)
        # self.add(face_1, body_1)
        
        face_2a = Rectangle(color=WHITE, height=0.65, width=0.66, stroke_width=2).shift(LEFT*1.03 + UP*0.55)
        
        face_2 = Line([0,0,0], [0.66,0,0], color = RED, stroke_width=5).shift(LEFT*1.37 + UP*0.2)
        body_2 = Ellipse(color=BLUE, height=1, width=2.1, stroke_width=5).shift(DOWN*0.1 + RIGHT*0.12)
        face_box = Rectangle(color=WHITE, height=3, width=5, stroke_width=5)
          
        self.add(face_2, body_2, face_box)
        
        # self.wait(2)