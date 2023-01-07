from manim import *
        
class VectorArrow(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)

        vec_z = Vector([3, 1, 0], buff=0, color='white',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3)
        label_z = Tex('$\\vec{z} = [3, 1]$', color='white', 
                    font_size=40).scale(0.6).next_to(vec_z.get_end(), 
                    LEFT + UP)
        self.add(vec_z, label_z)
        
        vec_z_plus_n1 = Arrow([3, 1, 0], [4.5, 2, 0], buff=0, color='red',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        label_z_plus_n1 = Tex('$\\vec{z} + \\vec{n_1} = [4.5, 2]$', color='red', 
                font_size=40).scale(0.6).next_to(vec_z_plus_n1.get_end(), 
                UP)
        self.add(vec_z_plus_n1, label_z_plus_n1)
        
        ###
        vec_z_plus_n1_2 = Arrow([3, 1, 0], [1.5, 0, 0], buff=0, color='red',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        label_z_plus_n1_2 = Tex('$\\vec{z} - \\vec{n_1}$', color='red', 
                font_size=40).scale(0.6).next_to(vec_z_plus_n1_2.get_end(), 
                DOWN)
        label_z_plus_n1_2_mat = Tex('$= [1.5, 0]$', color='red', 
                font_size=40).scale(0.6).next_to(vec_z_plus_n1_2.get_end(), 
                2.5*DOWN)
        self.add(vec_z_plus_n1_2, label_z_plus_n1_2, label_z_plus_n1_2_mat)
        
        vec_z_plus_c_2 = Arrow([3, 1, 0], [3, 0, 0], buff=0, color='#A020F0',
            stroke_width=5, max_tip_length_to_length_ratio=0.2, 
            max_stroke_width_to_length_ratio=5) 
        label_z_plus_c_2 = Tex('$\\vec{z} - \\vec{c} = [3, 0]$', color='#A020F0', 
                font_size=40).scale(0.6).next_to(vec_z_plus_c_2.get_end(), 
                RIGHT + DOWN)
        self.add(vec_z_plus_c_2, label_z_plus_c_2)
        ###
        vec_z_plus_n1_3 = Arrow([3, 1, 0], [0, -1, 0], buff=0, color='red',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        label_z_plus_n1_3 = Tex('$\\vec{z} - 2\\vec{n_1} = [0, -1]$', color='red', 
                font_size=40).scale(0.6).next_to(vec_z_plus_n1_3.get_end(), 
                DOWN)
        self.add(vec_z_plus_n1_3, label_z_plus_n1_3)
        
        vec_z_plus_c_3 = Arrow([3, 1, 0], [3, -1, 0], buff=0, color='#A020F0',
            stroke_width=5, max_tip_length_to_length_ratio=0.2, 
            max_stroke_width_to_length_ratio=5) 
        label_z_plus_c_3 = Tex('$\\vec{z} - 2\\vec{c} = [3, -1]$', color='#A020F0', 
                font_size=40).scale(0.6).next_to(vec_z_plus_c_3.get_end(), 
                RIGHT + DOWN)
        self.add(vec_z_plus_c_3, label_z_plus_c_3)
        ###
        
        vec_z_plus_c = Arrow([3, 1, 0], [3, 2, 0], buff=0, color='#A020F0',
            stroke_width=5, max_tip_length_to_length_ratio=0.2, 
            max_stroke_width_to_length_ratio=5) 
        label_z_plus_c = Tex('$\\vec{z} + \\vec{c} = [3, 2]$', color='#A020F0', 
                font_size=40).scale(0.6).next_to(vec_z_plus_c.get_end(), 
                LEFT + UP)
        self.add(vec_z_plus_c, label_z_plus_c)
        
        vec_n2 = Vector([3, 0, 0], buff=0, color='blue',
            stroke_width=3, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=2) 
        label_n2 = Tex('$\\vec{n_2}$', color='blue', 
                font_size=40).scale(0.6).next_to(vec_n2.get_end(), 
                LEFT + UP)
        self.add(vec_n2, label_n2)
    
        # START = (3,-10,0)
        # END =   (3,10,0)
        # x_line = Line(START,END, color='green')
        # self.add(x_line)