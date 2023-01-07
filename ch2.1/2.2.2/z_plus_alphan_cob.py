from manim import *
import numpy as np

class test(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=False,
            include_foreground_plane=False,  #get rid of grid lines
            # include_background_plane=False,  #get rid of transforming grid lines
            show_basis_vectors=False,
        )
# 
# class VectorArrow(Scene):
    def construct(self):
#         numberplane = NumberPlane()
#         self.add(numberplane)

        z = np.array([1, 1, 0])
        n = np.array([1, 2, 0])
        n2 = np.array([2, 1, 0])
        c = np.array([-0.6, 1.2, 0])
        
        z_plus_n_alp1 = z + n
        z_plus_n_alp2 = z - 1*n
        z_plus_n_alp3 = z - 1.5*n
        
        z_plus_n2_alp1 = z + n2
        z_plus_n2_alp2 = z - 1*n2
        z_plus_n2_alp3 = z - 1.5*n2
        
        z_plus_c_alp1 = z + c
        z_plus_c_alp2 = z - 1*c
        z_plus_c_alp3 = z - 1.5*c
        
        vec_z = Vector(list(z), buff=0, color='white',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        self.add(vec_z)
        
        vec_n2 = Arrow(list(z), list(z_plus_n2_alp1), buff=0, color='blue',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3)
        self.add_transformable_mobject(vec_n2)
        
        vec_n = Arrow(list(z), list(z_plus_n_alp1), buff=0, color='red',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3)
        self.add_transformable_mobject(vec_n)
        
        vec_c = Arrow(list(z), list(z_plus_c_alp1), buff=0, color='#A020F0',
            stroke_width=5, max_tip_length_to_length_ratio=0.2, 
            max_stroke_width_to_length_ratio=5)
        self.add_transformable_mobject(vec_c)
        
        # vec_zn = Vector(list(z_plus_n2_alp1), buff=0, color='silver',
        #     stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #     max_stroke_width_to_length_ratio=3) #darker red
        # label_zn = Tex('$z+ n$', color='silver', 
        #             font_size=40).next_to(vec_n.get_end(), 
        #             2.5*LEFT + DOWN)
        # self.add(vec_zn)
        
        # vec_zn2 = Vector(list(z_plus_n_alp2), buff=0, color='silver',
        #     stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #     max_stroke_width_to_length_ratio=3) #darker red
        # label_zn2 = Tex('$z + (-1)n$', color='silver', 
        #             font_size=40).next_to(vec_zn2.get_end(), 
        #             RIGHT + 0.6*UP)
        # self.add(vec_zn2)
        
        vec_n2_alp2 = Arrow(list(z), list(z_plus_n2_alp2), buff=0, color='blue',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3)
        self.add_transformable_mobject(vec_n2_alp2)
        
        vec_n_alp2 = Arrow(list(z), list(z_plus_n_alp2), buff=0, color='red',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3)
        self.add_transformable_mobject(vec_n_alp2)
        
        vec_c_alp2 = Arrow(list(z), list(z_plus_c_alp2), buff=0, color='#A020F0',
            stroke_width=5, max_tip_length_to_length_ratio=0.2, 
            max_stroke_width_to_length_ratio=5)
        self.add_transformable_mobject(vec_c_alp2)
        
        # vec_zn3 = Vector(list(z_plus_n_alp3), buff=0, color='silver',
        #     stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #     max_stroke_width_to_length_ratio=3) #darker red
        # label_zn3 = Tex('$z - 1.5n$', color='silver', 
        #             font_size=40).next_to(vec_zn3.get_end(), 
        #             RIGHT + 0.5*DOWN)
        # self.add(vec_zn3)
        
        vec_n2_alp3 = Arrow(list(z), list(z_plus_n2_alp3), buff=0, color='blue',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3)
        self.add_transformable_mobject(vec_n2_alp3)
        
        vec_n_alp3 = Arrow(list(z), list(z_plus_n_alp3), buff=0, color='red',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3)
        self.add_transformable_mobject(vec_n_alp3)
        
        vec_c_alp3 = Arrow(list(z), list(z_plus_c_alp3), buff=0, color='#A020F0',
            stroke_width=5, max_tip_length_to_length_ratio=0.2, 
            max_stroke_width_to_length_ratio=5)
        self.add_transformable_mobject(vec_c_alp3)
        
        ####
        orig_n2 = Vector(list(n2), buff=0, color='blue',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3)
        self.add_transformable_mobject(orig_n2)
        
        # z1 = Dot(list(z), color='blue')
        # z2 = Dot(list(z_plus_n_alp1), color='red')
        # z3 = Dot(list(z_plus_n_alp2), color='green')
        # z4 = Dot(list(z_plus_n_alp3), color='white')
        # self.add_transformable_mobject(z2, z3, z4)
        # 
        # b2 = Dot(list(z_plus_n2_alp1), color='red')
        # b3 = Dot(list(z_plus_n2_alp2), color='green')
        # b4 = Dot(list(z_plus_n2_alp3), color='white')
        # self.add_transformable_mobject(b2, b3, b4)
        
        label_n2 = Tex('$n_2$', color='blue', 
                    font_size=40).next_to(orig_n2.get_end(), 
                    RIGHT)
        label_n1 = Tex('$z + \\alpha * n_1$', color='red', 
                    font_size=40).next_to(vec_n.get_end(), 
                    RIGHT + DOWN)
        label_c = Tex('$z + \\alpha * c$', color='#A020F0', 
                    font_size=40).next_to(vec_c.get_end(), 
                    UP)
        
        group = VGroup(label_n2, label_n1, label_c)
        self.play(FadeIn(group))
        
        self.remove(vec_z)
        
        matrix = [[0.4, 0.2], [-0.3333, 0.6667]]
        self.apply_matrix(matrix)
        self.wait(0)