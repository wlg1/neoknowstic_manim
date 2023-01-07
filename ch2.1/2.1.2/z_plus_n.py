from manim import *
from operator import add
        
class VectorArrow(Scene):
    def construct(self):
        numberplane = NumberPlane(x_range=(- 7.111111111111111, 7.111111111111111, 1), 
                                    y_range=(- 4.0, 4.0, 1))
        self.add(numberplane)
        
        z = [[0,0,0], [3, 1, 0]]
        n_origin = [[0,0,0], [0.5, 2, 0]]
        z_plus_n = [ [0,0,0], list( map(add, z[1], n_origin[1]) ) ]
        z_plus_2n = [ [0,0,0], list( map(add, z[0], n_origin[0]) ) ]
        
        vec_z = Vector(z[1], buff=0, color='blue',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        label_z = Tex('$z$', 
                    font_size=40).next_to(vec_z.get_end(), 
                    LEFT + UP).set_color(BLUE)
        self.add(vec_z, label_z)
        
        vec_n = Arrow(z[1], z_plus_n[1], buff=0, color='orange',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        label_n = Tex('$n$', 
                    font_size=40).next_to(vec_n.get_end(), 
                    UP).set_color(ORANGE)
        self.add(vec_n, label_n)
        
        vec_zn = Arrow([0, 0, 0], z_plus_n[1], buff=0, color='silver',
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
        