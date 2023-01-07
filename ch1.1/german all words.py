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
        
        """
        2 -1
        1 1
        
        inv:
        0.33333333333333333333	0.33333333333333333334
	    -0.33333333333333333333	0.66666666666666666666
        
        """
        
        poison= ImageMobject("poison.jpg")
        poison.scale(0.4)
        poison.move_to(np.array([-1, 2, 0]))
        
        gift= ImageMobject("gift.jpg")
        gift.scale(0.5)
        gift.move_to(np.array([0.3333, 1.6667, 0]))
        
        arrow_1 = Arrow(ORIGIN, [-1, 2, 0], buff=0, color='#CBC3E3',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #light purple        
        text_1 = Tex('gift').next_to(arrow_1.get_end(), LEFT*0.7+UP*1.1)
        
        self.add(poison, gift, arrow_1, text_1)
        
        arrow_c = Arrow(ORIGIN, [1, 0, 0], buff=0, color='#FA8072',
            stroke_width=5, max_tip_length_to_length_ratio=0.2, 
            max_stroke_width_to_length_ratio=4) #light red
        arrow_d = Arrow(ORIGIN, [0, 1, 0], buff=0, color='#ADD8E6',
            stroke_width=5, max_tip_length_to_length_ratio=0.2, 
            max_stroke_width_to_length_ratio=4) #light blue
        self.add(arrow_c, arrow_d)
        
        arrow_2 = Arrow(ORIGIN, [-4, 1, 0], buff=0, color='#38004F',
            stroke_width=4, max_tip_length_to_length_ratio=0.07, 
            max_stroke_width_to_length_ratio=3) #light red
        text_2 = Tex('poison').next_to(arrow_2.get_end(), UP*1.5)
        
        arrow_3 = Arrow(ORIGIN, [0.3333, 1.6667, 0], buff=0, color='#E7CA11',
            stroke_width=4, max_tip_length_to_length_ratio=0.15, 
            max_stroke_width_to_length_ratio=3) #light blue
        text_3 = Tex('geschenk').next_to(arrow_3.get_end(), RIGHT*0.7+UP*1.1)
        
        self.add(arrow_2, arrow_3, text_2, text_3)
