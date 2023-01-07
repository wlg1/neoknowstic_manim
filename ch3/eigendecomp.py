from manim import *
class test(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
        )
    def construct(self):
        matrix = [[-0.3, 0.9], [0.7, 0.4]]
        self.apply_matrix(matrix)
        self.wait(0)
        
        matrix = [[1, -1], [1, 1]]
        self.apply_matrix(matrix)
        self.wait(0)