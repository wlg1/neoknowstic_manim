from manim import *

class scene_8_mat(Scene):
    def construct(self):
        m1 = Matrix([["w_{11}", "w_{12}"], ["w_{21}", "w_{22}"]]).scale(2)

        self.wait(1)

        m2 = Matrix([["w_{11}", "w_{12}"], ["w_{21}", "w_{22}"]]).scale(2)
        ent = m2.get_entries()
        ent[0].set_color(YELLOW)
        rec_1 = SurroundingRectangle(ent[0])
        self.play(Transform(m1, m2), FadeIn(rec_1))

        self.wait(1)