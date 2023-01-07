from manim import *
        
class VectorArrow(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)

        vec_V = Vector([0.5, 2, 0], buff=0, color='orange',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        label_1 = Tex('$n$', 
                    font_size=40).next_to(vec_V.get_end(), 
                    UP).set_color(ORANGE)
        self.add(vec_V, label_1)
        
        vDotx_arrow = Arrow([0, -0.1, 0], [0.5, -0.1, 0], buff=0, color='red',
            stroke_width=7, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=5) 
        dashed_x = DashedLine([0.01, -0.1, 0], [0.65, -0.1, 0], color='black')
        vDotx_name = Tex('0.5', 
                    font_size=30).next_to(vDotx_arrow.get_end(), 
                    DOWN).set_color(RED)
        self.add(vDotx_arrow, dashed_x, vDotx_name)
                
        vDoty_arrow = Arrow([0.5, 0, 0], [0.5, 2, 0], buff=0, color='yellow',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        dashed_y = DashedLine([0.5, 0.01, 0], [0.5, 1.65, 0], color='black')
        vDoty_name = Tex('2', 
                    font_size=30).next_to(vDoty_arrow.get_end(), 
                    RIGHT+DOWN*1.5).set_color(YELLOW)
        self.add(vDoty_arrow, dashed_y, vDoty_name)
        