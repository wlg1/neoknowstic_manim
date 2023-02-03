from manim import *
import pdb

class scene_5_1(Scene):
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

        # find intervals by pythagorean theorem

        # NS_unit_1 = Line([x, 0.1,0], [x, -0.1, 0], color=WHITE, stroke_width=1)
        # self.add(NS_unit_1)

        # sqrt( (2/4.5625)^2 + (0.75/4.5625)^2 ) = 0.46816
            # what 'impt meaning' does this map to in IS? probably nothing sigf
        # notice the denom of orth proj is (2)^2 + (0.75)^2 = 4.5625
            # dead end; seems not related
            # 4.5625 also where [2, 0.75] maps to in nap space
                # b/c MM is [2, 0.75] * [2, 0.75]
                # not true for other values b/c they are [2, 0.75] * [x,y], which doesn't square x and y
        # sqrt( (4/4.5625)^2 + (1.5/4.5625)^2 ) = 0.93632 = 0.46816 * 2

        # disregard below; actually you can't roatte nap space directly to this vector [2, 0.75]. the ortho proj is NOT the result of a rotation! It is an orth proj.

        # if you place nap space on x-axis (purp) and rotate it, the 1 is sent to 
        # the 2*0.46816 "length" mark IN TERMS OF INPUT SPACE, but it will be '2' on nap space b/c nap space considers '0.46816' to be '1'. This is like how feet and meters differ, or meters and kilometers. 1 kilometer considers '1000' to be '1'.  1 meter considers '0.001' to be '1'. 
            # show nose DM being sent there
                # may transf it to colored N or dot b/c too small
            # model != data pts, and since vectors built on data pts, != vectors either


        ###############
        # get coordinate space, nose ear spaces, and nap_space_IS

        # numberplane = NumberPlane()

        # ###
        # ear_space_vert = NumberLine(
        #     x_range=[-7, 7, 1],
        #     rotation=90 * DEGREES,
        #     include_numbers=True,
        #     label_direction=LEFT)
            