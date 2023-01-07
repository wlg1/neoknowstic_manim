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
        
        dot1 = Dot([1,0,0], radius=0.07)
        dot1_text = Text('(1, 0)', font_size=16).next_to(dot1, LEFT*0.5+DOWN*0.5)
        
        dot2 = Dot([1,1,0], radius=0.07)
        dot2_text = Text('(1, 1)', font_size=16).next_to(dot2, RIGHT*0.5+DOWN*0.5)
        
        dot3 = Dot([0.5,2,0], radius=0.07)
        dot3_text = Text('(0.5, 2)', font_size=16).next_to(dot3, UP*0.5)
        
        self.add(dot1, dot2, dot3, dot1_text, dot2_text, dot3_text)
        # tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
        
        # tip_text_v = Tex('v').next_to(arrow_v.get_end(), RIGHT)
        # tip_text_v_c = Tex(r'$v_c$').next_to(arrow_v_c.get_end(), RIGHT*0.7+DOWN*1.1)
        # tip_text_w = Tex('w').next_to(arrow_w.get_end(), LEFT)
        # tip_text_w_c = Tex(r'$w_c$').next_to(arrow_w_c.get_end(), LEFT*0.7+DOWN*1.1)
        # self.add(tip_text_v, tip_text_v_c, tip_text_w, tip_text_w_c)