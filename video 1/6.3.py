from manim import *
import pdb

class scene_5_1(Scene):
    def construct(self):      
        numberplane = NumberPlane()

        # vec1 = Vector([2/4.5625, 0.75/4.5625])

        # vec2 = Vector([80/4.5625, 30/4.5625], color = PURPLE)
        # # vec2 = Vector([8/4.5625, 3/4.5625], color = PURPLE)
        # # vec2.z_index = vec1-1

        vec1 = Vector([4/4.5625, 1.5/4.5625])
        vec2 = Vector([1.5/4.5625, (9/16)/4.5625])
        vec3 = Vector([2/4.5625, 0.75/4.5625])
        vec4 = Vector([2, 0.75])

        self.add(numberplane, vec2)
        self.add(vec1, vec3, vec4)

        dot1 = Dot([2, -(8/3), 0])
        orthLine = Line([4/4.5625, 1.5/4.5625,0], [2, -(8/3),0])

        self.add(dot1, orthLine)