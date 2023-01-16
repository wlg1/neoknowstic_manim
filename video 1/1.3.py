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
        
        eqn = VGroup(m1, x, equal_sign, A)
        self.add(m1, x, equal_sign, A)
           
        self.wait(3)
        rec_1 = SurroundingRectangle(m1.get_rows()[0])
        m1.add(rec_1)
        self.play(FadeIn(rec_1))
        
        self.wait(1)
        rec_2 = SurroundingRectangle(x.get_columns()[0])
        x.add(rec_2)
        self.play(FadeIn(rec_2))
        
        rec_3 = SurroundingRectangle(A.get_entries()[0])
        A.add(rec_3)
        self.play(FadeIn(rec_3))
        
        eqn_2 = VGroup(m1.copy(), x.copy(), equal_sign.copy(), A.copy()).scale(0.6).move_to([-4,1,0])
        self.play(Transform(eqn, eqn_2))
        
        # inNode_1 = Circle(radius=0.5, color=WHITE, fill_color=WHITE, fill_opacity=1, stroke_width=1).move_to([-1, 1.5, 0])
        # inNode_2 = Circle(radius=0.5, color=WHITE, fill_color=WHITE, fill_opacity=1, stroke_width=1).move_to([-1, -1.5, 0])
        # outNode = Circle(radius=0.5, color=WHITE, fill_color=WHITE, fill_opacity=1, stroke_width=1).move_to([3, 0, 0])
        
        # conn_1 = Line([-1, 1.5, 0], [3, 0, 0])
        # conn_2 = Line([-1, -1.5, 0], [3, 0, 0])
        
        # NN = VGroup(inNode_1, inNode_2, outNode, conn_1, conn_2).scale(0.6)
        
        NN = ImageMobject("neural1.jpg").scale(1.3).shift(RIGHT*1.6)
        self.play(FadeIn(NN))
        
        self.wait(4)
        