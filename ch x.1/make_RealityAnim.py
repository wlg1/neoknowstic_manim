from manim import *
from random import randint, random

class RealityAnim(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=False,
            include_foreground_plane=False,  #get rid of grid lines
            # include_background_plane=False,  #get rid of grid lines
            show_basis_vectors=False,
        )

    def construct(self):
        
        poison= ImageMobject("poison.jpg")
        poison.scale(0.7)
        poison.move_to(np.array([-4, 1, 0]))
        
        # gift= ImageMobject("gift.jpg")
        # gift.scale(0.7)
        # gift.move_to(np.array([-1, 2, 0]))
        # 
        # yinyang= ImageMobject("yinyang.jpeg")
        # yinyang.scale(0.7)
        # yinyang.move_to(np.array([-1, 1, 0])) # w-axis
        # 
        # circle= ImageMobject("circle.jpeg")
        # circle.scale(0.7)
        # circle.move_to(np.array([2, 1, 0])) # v-axis
        # 
        # blackcircle= ImageMobject("blackcircle.jpeg")
        # blackcircle.scale(0.7)
        # blackcircle.move_to(np.array([-2, -1, 0])) # w-axis
        # 
        # xobj = ImageMobject("X.jpeg")
        # xobj.scale(0.7)
        # xobj.move_to(np.array([0.333, 0.667, 0])) # w-axis
        
        self.add_transformable_mobject(poison)
        # self.add_transformable_mobject(gift)
        # self.add_transformable_mobject(yinyang)
        # self.add_transformable_mobject(circle)
        # self.add_transformable_mobject(blackcircle)
        # self.add_transformable_mobject(xobj)
                
        # 4 transforms in, 3 transforms back, then loop
                
        # M1            
        x1 = -0.3
        y1 = 0.7
        x2 = 0.9
        y2 = 0.4
        matrix = [[x1, x2], [y1, y2]]
        self.apply_matrix(matrix)
        self.wait(0)
        
        # # M2
        # x1 = 1.1
        # y1 = -0.5
        # x2 = -0.4
        # y2 = 0.7
        # matrix = [[x1, x2], [y1, y2]]
        # self.apply_matrix(matrix)
        # self.wait(0)
        # 
        # # inv of M2
        # x1 = 1.228
        # y1 = 0.702
        # x2 = 0.877
        # y2 = 1.930
        # matrix = [[x1, x2], [y1, y2]]
        # self.apply_matrix(matrix)
        # self.wait(0)
        
        # ROTATION
        # M2
        x1 = 1
        y1 = 1
        x2 = -1
        y2 = 1
        matrix = [[x1, x2], [y1, y2]]
        self.apply_matrix(matrix)
        self.wait(0)
        
        # STRETCHING
        # M3
        x1 = 1.4
        y1 = 0
        x2 = 0
        y2 = 1
        matrix = [[x1, x2], [y1, y2]]
        self.apply_matrix(matrix)
        self.wait(0)
        
        # inv of M3
        x1 = 0.71428571428571428571	
        y1 = 0
        x2 = 0
        y2 = 1
        matrix = [[x1, x2], [y1, y2]]
        self.apply_matrix(matrix)
        self.wait(0)
                
        # inv of M2
        x1 = 0.5
        y1 = -0.5
        x2 = 0.5
        y2 = 0.5
        matrix = [[x1, x2], [y1, y2]]
        self.apply_matrix(matrix)
        self.wait(0)
        
        # inv of M1
        x1 = -0.5333333333
        y1 = 0.93333333333
        x2 = 1.2
        y2 = 0.4
        matrix = [[x1, x2], [y1, y2]]
        self.apply_matrix(matrix)
        self.wait(0)
        