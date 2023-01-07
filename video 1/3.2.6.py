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
        
        faceText = Text('Face \nLength', 
            font_size=16).next_to([1,0,0], DOWN*1.5)
        arrow_c = Arrow(ORIGIN, [1, 0, 0], buff=0, color='#FA8072',
            stroke_width=4, max_tip_length_to_length_ratio=0.15, 
            max_stroke_width_to_length_ratio=5) #light red
        self.add(faceText, arrow_c)
            
        bodyText = Text('Body \nSize', 
            font_size=16).next_to([0,1,0], LEFT)
        arrow_d = Arrow(ORIGIN, [0, 1, 0], buff=0, color='#ADD8E6',
            stroke_width=4, max_tip_length_to_length_ratio=0.15, 
            max_stroke_width_to_length_ratio=5)
        self.add(bodyText, arrow_d)
        
        dot1 = Dot([1,0,0], radius=0.05, color='#FA8072')
        dot1_text = Text('(1, 0)', font_size=16, color='#FA8072').next_to(dot1, RIGHT*2+UP*0.5)
        face = ImageMobject("face1.png")
        face.scale(0.55)
        face.move_to(np.array([1, 0, 0]))
        self.add(face)
        
        dot2 = Dot([1,1,0], radius=0.05, color='gold')
        dot2_text = Text('(1, 1)', font_size=16, color='gold').next_to(dot2, RIGHT*1.5+UP*1.5)
        oneone = ImageMobject("1 1.png")
        oneone.scale(0.55)
        oneone.move_to(np.array([1, 1, 0]))
        self.add(oneone)
                
        dot3 = Dot([0.5,2,0], radius=0.05, color = '#CBC3E3')
        dot3_text = Text('(0.5, 2)', font_size=16, color = '#CBC3E3').next_to(dot3, UP*1.5)
        cat = ImageMobject("cat.png")
        cat.scale(0.55)
        cat.move_to(np.array([0.5, 2, 0]))
        self.add(cat)
                
        self.add(dot1, dot2, dot3, dot1_text, dot2_text, dot3_text)
        

        
        