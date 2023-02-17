from manim import *
from random import randint, random

class test(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
        )

    def construct(self):
        dot = Dot(np.array([-4, 1, 0]))
        self.add_transformable_mobject(dot)
        
        matrix = [[2, -1], [1, 1]]
        self.apply_matrix(matrix)
        self.wait(0)
        