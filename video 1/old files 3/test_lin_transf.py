from manim import *
import numpy as np

class test(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
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

        a = np.array([1, 0, 0])
        vec_a = Vector(list(a), buff=0, color='red',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        self.add_transformable_mobject(vec_a)
        
        b = np.array([0, 1, 0])
        vec_b = Vector(list(b), buff=0, color='blue',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3)
        self.add_transformable_mobject(vec_b)

        x = np.array([0.6, 0.4, 0])
        vec_x = Vector(list(x), buff=0, color='green',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        self.add_transformable_mobject(vec_x)
        
        y = np.array([0.4, 0.6, 0])
        vec_y = Vector(list(y), buff=0, color='purple',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        self.add_transformable_mobject(vec_y)
        
        #short face, big body
        cat = Vector([0.5, 1.5, 0], buff=0, color='orange',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        self.add_transformable_mobject(cat)
        
        #long face, small body
        rat = Vector([1.5, 0.5, 0], buff=0, color='yellow',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        self.add_transformable_mobject(rat)
        
        # a is body, b is face
        # y is cat, x is rat
        
        ## or long tail, small body is house cat
        ## so short tail, big body is bobcat (lynx), which are wild
        # green considers 0.6 tail, 0.4 body to be 1 house cat, 0 bobcat
        # purple considers 0.4 tail, 0.6 body to be 1 bobcat, 0 house cat
        
        
        
        #z = np.array([3, 1, 0])
        #n = np.array([0.5, 2, 0])
        #z_plus_n_alp1 = z + n
        #z_plus_n_alp2 = z - 1*n
        #z_plus_n_alp3 = z - 1.5*n
        #
        #vec_z = Vector(list(z), buff=0, color='blue',
        #    stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #    max_stroke_width_to_length_ratio=3) #darker red
        #label_z = Tex('$z$', 
        #            font_size=40).next_to(vec_z.get_end(), 
        #            LEFT + UP).set_color(BLUE)
        #self.add(vec_z)
        #
        #vec_n = Arrow(list(z), list(z_plus_n_alp1), buff=0, color='orange',
        #    stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #    max_stroke_width_to_length_ratio=3) #darker red
        #label_n = Tex('$n$', 
        #            font_size=40).next_to(vec_n.get_end(), 
        #            UP).set_color(ORANGE)
        #self.add_transformable_mobject(vec_n)
        #
        #vec_zn = Vector(list(z_plus_n_alp1), buff=0, color='silver',
        #    stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #    max_stroke_width_to_length_ratio=3) #darker red
        #label_zn = Tex('$z+ n$', color='silver', 
        #            font_size=40).next_to(vec_n.get_end(), 
        #            2.5*LEFT + DOWN)
        #self.add(vec_zn)
        #
        #vec_zn2 = Vector(list(z_plus_n_alp2), buff=0, color='silver',
        #    stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #    max_stroke_width_to_length_ratio=3) #darker red
        #label_zn2 = Tex('$z + (-1)n$', color='silver', 
        #            font_size=40).next_to(vec_zn2.get_end(), 
        #            RIGHT + 0.6*UP)
        #self.add(vec_zn2)
        #
        #vec_n2 = Arrow(list(z), list(z_plus_n_alp2), buff=0, color='orange',
        #    stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #    max_stroke_width_to_length_ratio=3) #darker red
        ## label_n2 = Tex('$(-1)*n$', 
        #            # font_size=40).next_to(vec_n2.get_end(), 
        #            # RIGHT).set_color(ORANGE)
        ## self.add(vec_n2, label_n2)
        #self.add_transformable_mobject(vec_n2)
        #
        #vec_zn3 = Vector(list(z_plus_n_alp3), buff=0, color='silver',
        #    stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #    max_stroke_width_to_length_ratio=3) #darker red
        #label_zn3 = Tex('$z - 1.5n$', color='silver', 
        #            font_size=40).next_to(vec_zn3.get_end(), 
        #            RIGHT + 0.5*DOWN)
        #self.add(vec_zn3)
        #
        #vec_n3 = Arrow(list(z), list(z_plus_n_alp3), buff=0, color='orange',
        #    stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #    max_stroke_width_to_length_ratio=3) #darker red
        ## label_n3 = Tex('$-1.5n$', 
        #            # font_size=40).next_to(vec_n3.get_end(), 
        #            # RIGHT).set_color(ORANGE)
        ## self.add(vec_n3, label_n3)
        #self.add_transformable_mobject(vec_n3)
        #
        #orig_n = Vector(list(n), buff=0, color='orange',
        #    stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #    max_stroke_width_to_length_ratio=3)
        #label_n = Tex('$n$', color='orange', 
        #            font_size=40).next_to(orig_n.get_end(), 
        #            UP)
        #self.add_transformable_mobject(orig_n)
        #
        #z1 = Dot(list(z), color='blue')
        #z2 = Dot(list(z_plus_n_alp1), color='red')
        #z3 = Dot(list(z_plus_n_alp2), color='green')
        #z4 = Dot(list(z_plus_n_alp3), color='white')
        #self.add_transformable_mobject(z1, z2, z3, z4)
        #
        #self.add(label_n)
        #self.play(FadeIn(label_n))
        #self.play(FadeIn(label_n))
        
        matrix = [[3, -2], [-2, 3]]
        self.apply_matrix(matrix)
        self.wait(0)