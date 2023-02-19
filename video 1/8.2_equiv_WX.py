from manim import *
import pdb

class scene_8_equiv_WX(Scene):
    def construct(self):  
        row1 = MathTex(r"\begin{bmatrix} w_{11} \ \ w_{12} \\\\ w_{21} \ \ w_{22} \end{bmatrix} \ \begin{bmatrix} x_{1} \\\\ x_{2} \end{bmatrix} = \begin{bmatrix} w_{11} * x_{1} + w_{12} * x_{2} \\\\ w_{21} * x_{1} + w_{22} * x_{2} \end{bmatrix}").shift(UP*2.5)

        self.add(row1)

        row2 = MathTex(r"= \begin{bmatrix} w_{11} \ \ w_{12} \\\\ w_{21} \ \ w_{22} \end{bmatrix} \ \begin{bmatrix} x_{1} \\\\ 0 \end{bmatrix} + \begin{bmatrix} w_{11} \ \ w_{12} \\\\ w_{21} \ \ w_{22} \end{bmatrix} \ \begin{bmatrix} 0 \\\\ x_{2} \end{bmatrix}")
        
        self.add(row2)

        row3 = MathTex(r"= x_{1} * \begin{pmatrix} \begin{bmatrix} w_{11} \ \ w_{12} \\\\ w_{21} \ \ w_{22} \end{bmatrix} \ \begin{bmatrix} 1 \\\\ 0 \end{bmatrix} \end{pmatrix} + x_{2} * \begin{pmatrix} \begin{bmatrix} w_{11} \ \ w_{12} \\\\ w_{21} \ \ w_{22} \end{bmatrix} \ \begin{bmatrix} 0 \\\\ 1 \end{bmatrix} \end{pmatrix}").shift(DOWN*2.5)
        
        self.add(row3)

        row3_up = row3.copy().shift(UP*2.5)

        row4 = MathTex(r"= x_{1} * \begin{pmatrix} \begin{bmatrix} w_{11} * 1 + w_{12} * 0 \\\\ w_{21} * 1 + w_{22} * 0 \end{bmatrix} \end{pmatrix} + x_{2} * \begin{pmatrix} \begin{bmatrix} w_{11} * 0 + w_{12} * 1 \\\\ w_{21} * 0 + w_{22} * 1 \end{bmatrix} \end{pmatrix}").shift(DOWN*2.5)
        
        self.play(FadeOut(row2, shift=UP), Transform(row3, row3_up), FadeIn(row4, shift=DOWN))
        self.wait(2)
        
        row3_up_up = row3_up.copy().shift(UP*2.5)

        row4_up = row4.copy().shift(UP*2.5)
        
        row5 = MathTex(r"= x_{1} * \begin{pmatrix} \begin{bmatrix} w_{11} \\\\ w_{21} \end{bmatrix} \end{pmatrix} + x_{2} * \begin{pmatrix} \begin{bmatrix} w_{12} \\\\ w_{22} \end{bmatrix} \end{pmatrix}").shift(DOWN*2.5)
        
        self.play(FadeOut(row1, shift=UP), Transform(row3, row3_up_up), Transform(row4, row4_up), FadeIn(row5, shift=DOWN))
        self.wait(2)
