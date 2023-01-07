from manim import *
from random import randint, random

# class Coordimgs(VectorScene):
#     def __init__(self):
#         VectorScene.__init__(
#             self,
#             show_basis_vectors = True,
#         )
# 
#     def construct(self):
#         self.add_axes()
        
class VectorArrow(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        
        face = ImageMobject("face1_nonum.png")
        face.scale(0.4)
        face.move_to(np.array([1, 0, 0]))
        self.add(face)
        
        body = ImageMobject("body1_nonum.png")
        body.scale(0.4)
        body.move_to(np.array([0, 1, 0]))
        self.add(body)
        
        k = Dot([0.3077, 0.4615, 0], color='orange', radius=0.07)
        j = Dot([-0.4615, 0.3077, 0], color='green', radius=0.07)
        self.add(k,j)
        
        arrow_c = Arrow(ORIGIN, [1, 0, 0], buff=0, color='#FA8072',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #light red
        arrow_d = Arrow(ORIGIN, [0, 1, 0], buff=0, color='#CCCCFF',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #light blue
        self.add(arrow_c, arrow_d)