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
        
        # c = np.array([1, 1, 0])
        c = np.array([4.3, 2.5, 0])
        vec_c = Vector(list(c), buff=0, color='yellow',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3)
        # self.add_transformable_mobject(vec_c)
        
        d = np.array([5, 5, 0])
        vec_d = Vector(list(d), buff=0, color='pink',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3)
        # self.add_transformable_mobject(vec_d)
        
        cat = np.array([2, 0.5, 0])
        vec_cat = Vector(list(cat), buff=0, color='white',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3)
        self.add_transformable_mobject(vec_cat)

        x = np.array([0.4, 0.2, 0])
        vec_x = Vector(list(x), buff=0, color='green',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        self.add_transformable_mobject(vec_x)
        
        y = np.array([-0.2, 0.4, 0])
        vec_y = Vector(list(y), buff=0, color='purple',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        self.add_transformable_mobject(vec_y)
                       
        matrix = [[2, 1], [-1, 2]]
        self.apply_matrix(matrix)
        self.wait(0)
        
        
        '''
        #short face, big body
        # cat = Vector([0.5, 1.5, 0], buff=0, color='orange',
            # stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            # max_stroke_width_to_length_ratio=3) 
        # self.add_transformable_mobject(cat)
        
        # long face, small body
        # rat = Vector([1.5, 0.5, 0], buff=0, color='yellow',
            # stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            # max_stroke_width_to_length_ratio=3) 
        # self.add_transformable_mobject(rat)
        
        # a is body, b is face
        # y is cat, x is rat
        
        ## or long tail, small body is house cat
        ## so short tail, big body is bobcat (lynx), which are wild
        # green considers 0.6 tail, 0.4 body to be 1 house cat, 0 bobcat
        # purple considers 0.4 tail, 0.6 body to be 1 bobcat, 0 house cat
        
        # thus, too long of a tail is house cat, too big of a body is bobcat
        
        # this is too easily separable. we need to mix and match cases!
        # it's a good introduction. for the next example, try using
            # 3D to 2D?'''