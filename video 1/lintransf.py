from manim import *
from random import randint, random

class test(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            include_background_plane=True, include_foreground_plane=False, background_plane_kwargs=None, foreground_plane_kwargs=None, show_coordinates=False, show_basis_vectors=True, 
        )

    def construct(self):
        # dot = Vector(np.array([-1, 2, 0]))
        # self.add_transformable_mobject(dot)
        
        # dot2 = Vector(np.array([1, 1, 0]))
        # self.add_transformable_mobject(dot2)

        ###
        # dot = Vector(np.array([2, 0.75, 0]))
        # self.add_transformable_mobject(dot)
        
        # dot2 = Vector(np.array([-0.75, 2, 0]))
        # self.add_transformable_mobject(dot2)

        # matrix = [[2, 0.75], [-0.75, 2]]
        # self.apply_matrix(matrix)
        # self.wait(0)
        
        ###
        # dot = Vector(np.array([2, 1, 0]))
        # self.add_transformable_mobject(dot)
        
        # dot2 = Vector(np.array([-2, 2, 0]))
        # self.add_transformable_mobject(dot2)

        # matrix = [[2, 1], [-2, 2]]
        # self.apply_matrix(matrix)
        # self.wait(0)
        
        ####        
        # dot = Vector(np.array([1, 1, 0]))
        # self.add_transformable_mobject(dot)
        
        # # dot3 = Vector(np.array([2, 3, 0]))
        # # columns of inverse go to basis
        # dot3 = Vector(np.array([0.15384615384615384616, 0.23076923076923076923, 0]))
        # self.add_transformable_mobject(dot3)
        
        # # dot4 = Vector(np.array([-3, 2, 0]))
        # dot4 = Vector(np.array([-0.23076923076923076922, 0.15384615384615384615, 0]))
        # self.add_transformable_mobject(dot4)

        # matrix = [[2, 3], [-3, 2]]
        # self.apply_matrix(matrix)
        # self.wait(0)

        ###
        dot = Vector(np.array([1, 1, 0]))
        self.add_transformable_mobject(dot)

        matrix = [[2, 1], [-1, 2]]
        self.apply_matrix(matrix)
        self.wait(0)