from manim import *
from random import randint, random


class VectorArrow(VectorScene, Scene):
    def setup(self):
        Scene.setup(self)
        VectorScene.setup(self)
        
    def construct(self):
        ##########################
        cat = ImageMobject("cat.png").scale(1.5)        
        cat2 = ImageMobject("cat.png").scale(0.5)
        face = Rectangle(color=RED, height=0, width=1.32, stroke_width=5).shift(LEFT + UP*0.2)
        self.add(cat)
        
        # shape to img doesn't work, but img to img does
        
        self.play(Transform(cat, cat2))
        
        self.wait(2)