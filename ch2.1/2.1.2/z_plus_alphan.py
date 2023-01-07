from manim import *
import numpy as np
        
class VectorArrow(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        
        z = np.array([3, 1, 0])
        n = np.array([0.5, 2, 0])
        z_plus_n_alp1 = z + n
        z_plus_n_alp2 = z - 1*n
        z_plus_n_alp3 = z - 1.5*n
        
        
        
        vec_z = Vector(list(z), buff=0, color='blue',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        label_z = Tex('$z$', 
                    font_size=40).next_to(vec_z.get_end(), 
                    LEFT + UP).set_color(BLUE)
        self.add(vec_z, label_z)
        
        vec_n = Arrow(list(z), list(z_plus_n_alp1), buff=0, color='orange',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        label_n = Tex('$n$', 
                    font_size=40).next_to(vec_n.get_end(), 
                    UP).set_color(ORANGE)
        self.add(vec_n, label_n)
        
        vec_zn = Vector(list(z_plus_n_alp1), buff=0, color='silver',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        label_zn = Tex('$z+ n$', color='silver', 
                    font_size=40).next_to(vec_n.get_end(), 
                    3*LEFT + DOWN)
        self.add(vec_zn, label_zn)
        
        vDotx_arrow = Arrow([3, 0.9, 0], [3.5, 0.9, 0], buff=0, color='red',
            stroke_width=7, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=5) 
        dashed_x = DashedLine([3.01, 0.9, 0], [3.65, 0.9, 0], color='black')
        vDotx_name = Tex('0.5', 
                    font_size=30).next_to(vDotx_arrow.get_end(), 
                    DOWN).set_color(RED)
        self.add(vDotx_arrow, dashed_x, vDotx_name)
                
        vDoty_arrow = Arrow([3.5, 1, 0], [3.5, 3, 0], buff=0, color='yellow',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        dashed_y = DashedLine([3.5, 0.9, 0], [3.5, 2.65, 0], color='black')
        vDoty_name = Tex('2', 
                    font_size=30).next_to(vDoty_arrow.get_end(), 
                    RIGHT+DOWN*1.5).set_color(YELLOW)
        self.add(vDoty_arrow, dashed_y, vDoty_name)
        
        vec_zn2 = Vector(list(z_plus_n_alp2), buff=0, color='silver',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        label_zn2 = Tex('$z + (-1)n$', color='silver', 
                    font_size=40).next_to(vec_zn2.get_end(), 
                    RIGHT + 0.6*UP)
        self.add(vec_zn2, label_zn2)
        
        vec_n2 = Arrow(list(z), list(z_plus_n_alp2), buff=0, color='orange',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        # label_n2 = Tex('$(-1)*n$', 
        #             font_size=40).next_to(vec_n2.get_end(), 
        #             RIGHT).set_color(ORANGE)
        # self.add(vec_n2, label_n2)
        self.add(vec_n2)
        
        vec_zn3 = Vector(list(z_plus_n_alp3), buff=0, color='silver',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        label_zn3 = Tex('$z - 1.5n$', color='silver', 
                    font_size=40).next_to(vec_zn3.get_end(), 
                    RIGHT + 0.5*DOWN)
        self.add(vec_zn3, label_zn3)
        
        vec_n3 = Arrow(list(z), list(z_plus_n_alp3), buff=0, color='orange',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        # label_n3 = Tex('$-1.5n$', 
        #             font_size=40).next_to(vec_n3.get_end(), 
        #             RIGHT).set_color(ORANGE)
        # self.add(vec_n3, label_n3)
        self.add(vec_n3)