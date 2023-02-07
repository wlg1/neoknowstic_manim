from manim import *
import pdb

class scene_6_3(Scene):
    def construct(self):      
        numberplane = NumberPlane()

        # vec1 = Vector([2/4.5625, 0.75/4.5625])

        # vec2 = Vector([80/4.5625, 30/4.5625], color = PURPLE)
        # # vec2 = Vector([8/4.5625, 3/4.5625], color = PURPLE)
        # # vec2.z_index = vec1-1

        vec2 = Vector([1.5/4.5625, (9/16)/4.5625]) #0.75
        vec3 = Vector([2/4.5625, 0.75/4.5625])  #1
        vec1 = Vector([4/4.5625, 1.5/4.5625]) #2
        vec4 = Vector([2, 0.75]) #4.(9/16) = 4.5625

        self.add(numberplane, vec2)
        self.add(vec1, vec3, vec4)

        dot1 = Dot([2, -(8/3), 0])
        orthLine = Line([4/4.5625, 1.5/4.5625,0], [2, -(8/3),0])

        self.add(dot1, orthLine)


        ###############
        # get coordinate space, nose ear spaces, and nap_space_IS

        # numberplane = NumberPlane()

        # ###
        # ear_space_vert = NumberLine(
        #     x_range=[-7, 7, 1],
        #     rotation=90 * DEGREES,
        #     include_numbers=True,
        #     label_direction=LEFT)
            