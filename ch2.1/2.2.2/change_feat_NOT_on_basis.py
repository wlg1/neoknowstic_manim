from manim import *
        
class VectorArrow(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        
        vec_n1 = Vector([1, 2, 0], buff=0, color='red',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        label_n1 = Tex('$n_1$', color='red', font_size=40).scale(0.6).next_to(vec_n1.get_end(), 
                        LEFT*0.8 + UP*0.8)
        vec_n2 = Vector([2, 1, 0], buff=0, color='blue',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker blue
        label_n2 = Tex('$n_2$', color='blue', font_size=40).scale(0.6).next_to(vec_n2.get_end(), 
                        RIGHT*0.5 + DOWN*0.8)
        self.add(vec_n1, label_n1, vec_n2, label_n2)
        
        arrow_C = Arrow([1.6, 0.8, 0], [1, 2, 0], buff=0, color='#A020F0',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        label_c = Tex('$c$', color='#A020F0', 
            font_size=40).scale(0.6).next_to(arrow_C.get_end(), 
            1.5*RIGHT + DOWN)
        self.add(arrow_C, label_c)
        
        