from manim import *

class VectorArrow(Scene):
    def construct(self):
        
        answer = Dot([4, -0.1, 0], color='#9B59B6', radius=0.08)
        
        text_1 = Tex('$0.5 * \\vec{face}_x + 2 * \\vec{body}_x$', font_size=30).next_to(answer, 
            UP*6)
        m_x = Matrix([[-2], [0]]).scale_to_fit_height(0.75).next_to(answer, 
            LEFT*1.3+UP*2)
        text_2 = Tex('+', font_size=30).next_to(answer, 
            UP*4)
        m_y = Matrix([[2.5], [0]]).scale_to_fit_height(0.75).next_to(answer, 
            RIGHT*1.2+UP*2)
        text_3 = Tex('=', font_size=30).next_to(answer, 
            LEFT*6.5+DOWN*3)
        m_ans = Matrix([[4], [0]]).scale_to_fit_height(0.85).next_to(answer, 
            LEFT*4+DOWN*1.5)
        
        m_z = Matrix([[1], [0]]).scale_to_fit_height(0.75).next_to(answer, 
            RIGHT*1.2+DOWN*7)
                    
        self.add(answer, text_1, m_x, m_y, m_z,
                text_3, m_ans)
        