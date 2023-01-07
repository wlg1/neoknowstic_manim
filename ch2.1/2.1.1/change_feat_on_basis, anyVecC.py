from manim import *
        
class VectorArrow(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)

        vec_V = Vector([3, 2, 0], buff=0, color='red',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        label_v = vec_V.coordinate_label().scale(0.6).next_to(vec_V.get_end(), 
                    RIGHT*3.5 + DOWN*0.5).set_color(RED)
        vec_V_name = Tex('$\\vec{z}=$', font_size=30).next_to(vec_V.get_end(), 
                    RIGHT*1 + DOWN).set_color(RED)
                            
        vec_W = Vector([3, 1, 0], buff=0, color='#CBC3E3',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        # '$\\begin{bmatrix} 3 \\ 2 \\end{bmatrix} + (-1) * \\begin{bmatrix} 0 \\ 1 \\end{bmatrix} $'
        label_W1 = Tex('$\\vec{z} + (-1) * \\vec{y}$', 
                    color = '#CBC3E3', font_size=40).scale(0.6).next_to(vec_W.get_end(), 
                    RIGHT*1.3 + DOWN)
        y_1 = Arrow([3,2,0], [3, 1, 0], buff=0, color='blue',
            stroke_width=5, max_tip_length_to_length_ratio=0.2, 
            max_stroke_width_to_length_ratio=5) 
        # self.add(vec_V, label_1, vec_V_name, vec_W, label_2)
        
        vec_W2 = Vector([3, 2.5, 0], buff=0, color='orange',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        label_W2 = Tex('$\\vec{z} + (1.5) * \\vec{y}$', 
                    color = 'orange', font_size=40).scale(0.6).next_to(vec_W2.get_end(), 
                    RIGHT*1.3)
        y_2 = Arrow([3,2,0], [3, 2.5, 0], buff=0, color='yellow',
            stroke_width=6, max_tip_length_to_length_ratio=0.3, 
            max_stroke_width_to_length_ratio=6) 
        # vec_W3 = Vector([3, -0.5, 0], buff=0, color='blue',
        #     stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #     max_stroke_width_to_length_ratio=3) 
        # self.add(vec_V, vec_W, vec_W2, vec_W3)
        
        self.add(vec_V, vec_W, vec_W2, y_1, y_2)
        self.add(vec_V_name, label_v, label_W1, label_W2)
        
        # arrow_C = Arrow([3, -2, 0], [3, 5, 0], buff=0, color='green',
        #     stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #     max_stroke_width_to_length_ratio=3) 
        # C = Tex('$C = \\vec{v} - (\\vec{v} \\cdot \\vec{x}) * \\vec{x}$', 
        #             font_size=40).scale(0.6).next_to(arrow_C.get_end(), 
        #             RIGHT*1.3+DOWN*2).set_color(GREEN)
        # self.add(arrow_C, C)
        
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