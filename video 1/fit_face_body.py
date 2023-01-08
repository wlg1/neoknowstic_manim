from manim import *
from random import randint, random


class VectorArrow(VectorScene, Scene):
    def setup(self):
        Scene.setup(self)
        VectorScene.setup(self)
        
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        
        ##########################
        face = ImageMobject("face 1.png")
        face.scale(0.5)
        face.move_to(np.array([1, 0, 0]))
        self.add(face)
        
        body = ImageMobject("body 1.png")
        body.scale(0.5)
        body.move_to(np.array([0, 1, 0]))
        self.add(body)
        #################################
                
        face_1 = Rectangle(color=RED, height=0.15, width=0.32, stroke_width=1)
        face_1.move_to(np.array([1, 0, 0])).shift(UP*0.1 + LEFT*0.25)
        face_box = Rectangle(color=RED, height=0.75, width=1.05, stroke_width=1)
        face_box.move_to(np.array([1, 0, 0]))
        
        body_1 = Ellipse(color=RED, height=0.15, width=0.42, stroke_width=1)
        body_1.move_to(np.array([0, 1, 0])).shift(DOWN*0.05 + RIGHT*0.1)
        body_box = Rectangle(color=RED, height=0.75, width=1.05, stroke_width=1)
        body_box.move_to(np.array([0, 1, 0]))
        
        self.add(face_1, face_box, body_1, body_box)
        
        # self.wait(2)