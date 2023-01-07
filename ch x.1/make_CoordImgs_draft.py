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
        dot = Dot(ORIGIN)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        # tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
        # self.add(numberplane, dot, arrow, origin_text, tip_text)
        self.add(numberplane, dot)
        
        arrow_v = Arrow(ORIGIN, [2, 1, 0], buff=0, color='#FA8072') #light red
        arrow_v_c = Arrow(ORIGIN, [2, 0, 0], buff=0, color='#CD5C5C') #dark red
        arrow_w = Arrow(ORIGIN, [-1, 1, 0], buff=0, color='#CCCCFF') #light blue
        arrow_w_c = Arrow(ORIGIN, [-1, 0, 0], buff=0, color='#6495ED') #dark blue
        self.add(arrow_v, arrow_w, arrow_v_c, arrow_w_c)
        
        tip_text_v = Tex('v').next_to(arrow_v.get_end(), RIGHT)
        tip_text_v_c = Tex(r'$v_c$').next_to(arrow_v_c.get_end(), RIGHT*0.7+DOWN*1.1)
        tip_text_w = Tex('w').next_to(arrow_w.get_end(), LEFT)
        tip_text_w_c = Tex(r'$w_c$').next_to(arrow_w_c.get_end(), LEFT*0.7+DOWN*1.1)
        self.add(tip_text_v, tip_text_v_c, tip_text_w, tip_text_w_c)