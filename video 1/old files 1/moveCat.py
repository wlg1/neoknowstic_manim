from manim import *

class MoveCat(Scene):
    def construct(self):
        image = ImageMobject("cat.png")
        image.generate_target()
        self.add(image)
        image.target.shift(5*LEFT)
        
        center_image = ImageMobject("cat-removebg-preview.png")
        self.add(center_image)
        
        DS_image = ImageMobject("dataSample-removebg-preview.png")
        self.add(DS_image)
        
        self.play(MoveToTarget(image))
        