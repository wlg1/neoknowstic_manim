from manim import *
from random import randint, random

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

    def construct(self):
        # face1= ImageMobject("face1.png")
        # face1.scale(0.3)
        # face1.move_to(np.array([1, 0, 0]))
        # self.add_transformable_mobject(face1)
        # 
        # body1= ImageMobject("body1.png")
        # body1.scale(0.3)
        # body1.move_to(np.array([0, 1, 0]))
        # self.add_transformable_mobject(body1)
        
        # k = Dot([0.6, -0.2, 0], color='orange')
        # j = Dot([0.2, 0.6, 0], color='green')
        # self.add_transformable_mobject(k,j)
        
        # arrow_c = Arrow(ORIGIN, [1, 0, 0], buff=0, color='#FA8072') #light red
        # arrow_d = Arrow(ORIGIN, [0, 1, 0], buff=0, color='#CCCCFF') #light blue
        c = Dot([1, 0, 0], color='#FA8072')
        d = Dot([0, 1, 0], color='#CCCCFF')
        self.add_transformable_mobject(c, d)
        
        # cat_image = ImageMobject("cat.png")
        # cat_image.scale(0.25)
        # cat_image.move_to(np.array([0.5, 2, 0]))
        # self.add(cat_image)
        
        cat = Dot([0.5, 2, 0])
        self.add_transformable_mobject(cat)
        
        # arrow_cat = Arrow(ORIGIN, [0.5, 2, 0], buff=0, color='#CBC3E3') #light purple
        # self.add(arrow_cat)
        
        # self.play(FadeOut(cat_image))
        
        #matrix = [[1, 1.5], [-1.5, 1]]  #rotation
        matrix = [[-2, 2.5], [2.5, -2]]
        self.apply_matrix(matrix)
        self.wait(0)
        