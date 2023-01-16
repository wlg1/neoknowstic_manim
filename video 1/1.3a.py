from manim import *
import pdb

class scene_1_3(Scene):
    def construct(self):
        m1 = Matrix([["w_{11}", "w_{12}"], ["w_{21}", "w_{22}"]])
        m1.move_to([-2.5,0,0])
                
        x = Matrix([["x_{1}"], ["x_{2}"]])
        x.move_to([0,0,0])
        
        equal_sign = Text('=')
        equal_sign.move_to(np.array([1.1, 0, 0]))
        
        A = Matrix([["a_{11}", "a_{12}"], ["a_{21}", "a_{22}"]])
        A.move_to([3,0,0])
        
        # self.add(m1, x, equal_sign, A)
        
        self.wait(3)
        self.play(FadeIn(m1))
        self.wait(2)
        self.play(FadeIn(x))
        self.wait(2)
        self.play(FadeIn(equal_sign))
        self.wait(2)
        self.play(FadeIn(A))
        
        
        rec_1 = SurroundingRectangle(m1.get_rows()[0])
        # rec_2 = SurroundingRectangle(m1.get_rows()[1])        
        # self.play(Transform(rec_1, rec_2))
        
        # self.wait(3)
        # self.play(FadeIn(rec_1))
        
        # self.wait(2)
        # rec_2 = SurroundingRectangle(x.get_columns()[0])
        # x.add(rec_2)
        # self.play(FadeIn(rec_2))
        
        # rec_3 = SurroundingRectangle(A.get_entries()[0])
        # A.add(rec_3)
        # self.play(FadeIn(rec_3))
        
        
        