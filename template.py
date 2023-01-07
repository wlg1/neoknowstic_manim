from manim import *
        
class VectorArrow(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        
        arrow_c = Arrow(ORIGIN, [1, -1.5, 0], buff=0, color='#E74C3C',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        arrow_d = Arrow(ORIGIN, [1.5, 1, 0], buff=0, color='#3498DB',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker blue
        self.add(arrow_c, arrow_d)
    