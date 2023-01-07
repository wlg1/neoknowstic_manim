from manim import *
        
class VectorArrow(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)

        vec_V = Vector([3, 2, 0], buff=0, color='red',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        label_1 = vec_V.coordinate_label().scale(0.6).next_to(vec_V.get_end(), 
                    LEFT*1.3+UP*1.1).set_color(RED)
        vec_V_name = Tex('$\\vec{v}=$', font_size=30).next_to(vec_V.get_end(), 
                    LEFT*3.5+UP*1.5).set_color(RED)
                            
        vec_W = Vector([3, 1, 0], buff=0, color='blue',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        label_2 = vec_W.coordinate_label().scale(0.6).next_to(vec_W.get_end(), 
                    RIGHT*1.3+DOWN*1).set_color(BLUE)
        self.add(vec_V, label_1, vec_V_name, vec_W, label_2)
        
        arrow_C = Arrow([4, 0, 0], [3, 2, 0], buff=0, color='green',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        
        C = Tex('$non-orth vector$', font_size=30).scale(0.6).next_to(arrow_C.get_end(), 
                    RIGHT*1.3+DOWN*2).set_color(GREEN)
        self.add(arrow_C, C)
        
        # vDotx_arrow = Arrow([0, -0.1, 0], [3, -0.1, 0], buff=0, color='pink',
        #     stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #     max_stroke_width_to_length_ratio=3) 
        # dashed_x = DashedLine([0.01, -0.1, 0], [2.65, -0.1, 0], color='black')
        # vDotx_name = Tex('$(\\vec{v} \\cdot \\vec{x}) * \\vec{x}$', 
        #             font_size=30).next_to(vDotx_arrow.get_end(), 
        #             LEFT*3.3+DOWN*1.3).set_color(PINK)
        # self.add(vDotx_arrow, dashed_x, vDotx_name)
        
        # START = (3,-10,0)
        # END =   (3,10,0)
        # x_line = Line(START,END, color='green')
        # self.add(x_line)