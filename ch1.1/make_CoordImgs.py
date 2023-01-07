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
        
        face = ImageMobject("face1.png")
        face.scale(0.55)
        face.move_to(np.array([1, 0, 0]))
        self.add(face)
        
        body = ImageMobject("body1.png")
        body.scale(0.55)
        body.move_to(np.array([0, 1, 0]))
        self.add(body)
        
        # cat = ImageMobject("cat.png")
        # cat.scale(0.55)
        # cat.move_to(np.array([0.5, 2, 0]))
        # self.add(cat)
        # cat_text = Text('(0.5, 2)', font_size=16).next_to(cat, UP)
        # 
        # dot1 = Dot([0.5,0,0], radius=0.07)
        # dot2 = Dot([0,2,0], radius=0.07)
        # dot1_text = Text('(0.5, 0)', font_size=16).next_to(dot1, DOWN)
        # dot2_text = Text('(0, 2)', font_size=16).next_to(dot2, LEFT*0.5+DOWN*0.5)
        # self.add(dot1, dot2, dot1_text, dot2_text)
        # 
        # arrow_c = Arrow(ORIGIN, [1, 0, 0], buff=0, color='#FA8072',
        #     stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #     max_stroke_width_to_length_ratio=3) #light red
        # arrow_d = Arrow(ORIGIN, [0, 1, 0], buff=0, color='#CCCCFF',
        #     stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #     max_stroke_width_to_length_ratio=3) #light blue
        # arrow_cat = Arrow(ORIGIN, [0.5, 2, 0], buff=0, color='#CBC3E3',
        #     stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #     max_stroke_width_to_length_ratio=3) #light purple
        # self.add(arrow_c, arrow_d, arrow_cat)
        
        arrow_c = Arrow(ORIGIN, [1, 0, 0], buff=0, color='#FA8072',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #light red
        arrow_d = Arrow(ORIGIN, [0, 1, 0], buff=0, color='#CCCCFF',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #light blue
        self.add(arrow_c, arrow_d)
        
        
        # tip_text_v = Tex('v').next_to(arrow_v.get_end(), RIGHT)
        # tip_text_v_c = Tex(r'$v_c$').next_to(arrow_v_c.get_end(), RIGHT*0.7+DOWN*1.1)
        # tip_text_w = Tex('w').next_to(arrow_w.get_end(), LEFT)
        # tip_text_w_c = Tex(r'$w_c$').next_to(arrow_w_c.get_end(), LEFT*0.7+DOWN*1.1)
        # self.add(tip_text_v, tip_text_v_c, tip_text_w, tip_text_w_c)