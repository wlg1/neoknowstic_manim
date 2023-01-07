from manim import *
from random import randint, random

class RealityAnim(LinearTransformationScene, MovingCameraScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=False,
            include_foreground_plane=False,  #get rid of grid lines
            include_background_plane=False,  #get rid of grid lines
            show_basis_vectors=False,
            # i_hat_color = '#000000',  #make basis vector black
            # j_hat_color = '#000000',
            # foreground_plane_kwargs = {
            # "x_range" : np.array([-100, 100, 1]),
            # "y_range" : np.array([-100, 100, 1]),
            # "x_length" : 100,
            # "y_length" : 100,
            # },
        )
        # MovingCameraScene.__init__(self)

    def construct(self):
        # self.play(self.camera_frame.set_width(20))
        # dot = Dot(np.array([-1, 2, 0]))
        # dot2 = Dot(np.array([-4, 1, 0]))
        
        # mob = Circle()
        # mob.move_to(RIGHT+UP*2)
        # mob2 = Square()
        # mob2.move_to(RIGHT+UP*2)
        
        poison= ImageMobject("poison.jpg")
        poison.scale(0.7)
        poison.move_to(np.array([-4, 1, 0]))
        
        gift= ImageMobject("gift.jpg")
        gift.scale(0.7)
        gift.move_to(np.array([-1, 2, 0]))
        
        yinyang= ImageMobject("yinyang.jpeg")
        yinyang.scale(0.7)
        yinyang.move_to(np.array([-1, 1, 0])) # w-axis
        
        # Don't use Mobj circle b/c this is made up of pts in the coord sys; but 
        # we want it to represent just one pt
        # circle = Circle(color=WHITE, fill_opacity=1) # v-axis
        # circle.move_to(np.array([2, 1, 0]))
        circle= ImageMobject("circle.jpeg")
        circle.scale(0.7)
        circle.move_to(np.array([2, 1, 0])) # v-axis
        
        blackcircle= ImageMobject("blackcircle.jpeg")
        blackcircle.scale(0.7)
        blackcircle.move_to(np.array([-2, -1, 0])) # w-axis

        # self.add_background_mobject(dot) #doesn't move
        # self.add_transformable_mobject(dot) #moves w/ transformation
        # self.add_transformable_mobject(dot2)
        # self.add_transformable_mobject(mob)
        # self.add_transformable_mobject(mob2)
        
        self.add_transformable_mobject(poison)
        self.add_transformable_mobject(gift)
        self.add_transformable_mobject(yinyang)
        self.add_transformable_mobject(circle)
        self.add_transformable_mobject(blackcircle)
        
        # myVec = Vector([-1, 2])
        # self.add_moving_mobject(myVec)
        # self.add_transformable_mobject(myVec)
        
        # self.add_moving_mobject(dot)
                
        for i in range(10):
            # c = randint(0, 10)
            # d = randint(0, 10)
            # k = randint(0, 10)
            # j = randint(0, 10)
            c = random()  #keep it small b/w 0 and 1 so imgs not out of bounds
            d = random()
            k = random()
            j = random()
            matrix = [[c, d], [k, j]]
            self.apply_matrix(matrix)
            self.wait(0)
        
        # matrix = [[2, -1], [1, 1]]
        # self.apply_matrix(matrix)
        # self.wait(0)
        