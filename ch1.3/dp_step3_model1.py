from manim import *
        
class VectorArrow(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        
        face = ImageMobject("face1_nonum.png")
        face.scale(0.4)
        face.move_to(np.array([1, 0, 0]))
        self.add(face)
        
        body = ImageMobject("body1_nonum.png")
        body.scale(0.4)
        body.move_to(np.array([0, 1, 0]))
        self.add(body)
        
        arrow_face = Arrow(ORIGIN, [1, 0, 0], buff=0, color='#FA8072',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #light red
        text_1 = Tex('$\\vec{face}$', font_size=30).next_to(arrow_face.get_end(), 
                    RIGHT*0.3+UP*1.1)
        arrow_body = Arrow(ORIGIN, [0, 1, 0], buff=0, color='#ADD8E6',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #light blue
        text_2 = Tex('$\\vec{body}$', font_size=30).next_to(arrow_body.get_end(), 
                    LEFT*0.3+DOWN*1.1)
        self.add(arrow_face, arrow_body)
        
        arrow_x = Arrow([0, -0.1, 0], [0.5, -0.1, 0], buff=0, color='#FA8072',
            stroke_width=6, max_tip_length_to_length_ratio=0.3, 
            max_stroke_width_to_length_ratio=5) 
        dashed_x = DashedLine([0.01, -0.1, 0], [0.35, -0.1, 0], color='black')
        text_3 = Tex('$0.5 * \\vec{face}_{face} + 2 * \\vec{body}_{face} = $', font_size=30).next_to(dashed_x.get_end(), 
            RIGHT*0.3+DOWN*1.1)
        m_x = Matrix([[0.5], [0]]).scale_to_fit_height(0.75).next_to(dashed_x.get_end(), 
            RIGHT*3.7+DOWN*4)
        text_4 = Tex(' + ', font_size=30).next_to(dashed_x.get_end(), 
            RIGHT*7+DOWN*5)
        m_y = Matrix([[0], [0]]).scale_to_fit_height(0.75).next_to(dashed_x, 
            RIGHT*8.7+DOWN*4)
        dot_y = Dot([0.5, -0.1, 0], color='#ADD8E6', radius = 0.08)
        answer = Dot([0.5, 0, 0], color='#9B59B6', radius=0.08)
        
        self.add(arrow_x, dashed_x, text_3, m_x, text_4, m_y, dot_y, answer)
        