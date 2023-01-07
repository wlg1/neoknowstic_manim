from manim import *

class VectorArrow(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        
        face = ImageMobject("face1_nonum.png")
        face.scale(0.4)
        face.move_to(np.array([-2, 2.5, 0]))
        self.add(face)
        
        body = ImageMobject("body1_nonum.png")
        body.scale(0.4)
        body.move_to(np.array([2.5, -2, 0]))
        self.add(body)
        
        arrow_c = Arrow(ORIGIN, [-2, 2.5, 0], buff=0, color='#E74C3C',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        text_c = Tex('$\\vec{face} = $', font_size=30).next_to(arrow_c.get_end(), 
            LEFT*4.3+UP*1.1)
        m_c = Matrix([[-2], [2.5]]).scale_to_fit_height(0.75).next_to(arrow_c.get_end(), 
            LEFT+UP*1.1)
        arrow_d = Arrow(ORIGIN, [2.5, -2, 0], buff=0, color='#3498DB',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker blue
        text_d = Tex('$\\vec{body} = $', font_size=30).next_to(arrow_d.get_end(), 
            RIGHT*0.5+UP*1.1)
        m_d = Matrix([[2.5], [-2]]).scale_to_fit_height(0.75).next_to(arrow_d.get_end(), 
            RIGHT*5.3+UP*1.1)
        self.add(arrow_c, arrow_d)
        # self.add(arrow_c, text_c, m_c, arrow_d, text_d, m_d)
        
        # -2*0.5 = -1 ; 2.5*2 = 5
        
        arrow_face_x = Arrow([0, -0.1, 0], [-1, -0.1, 0], buff=0, color='#E74C3C',
            stroke_width=6, max_tip_length_to_length_ratio=0.3, 
            max_stroke_width_to_length_ratio=5) 
        dashed_face_x = DashedLine([-0.01, -0.1, 0], [-0.65, -0.1, 0], color='black')
        text_1 = Tex('$0.5 * \\vec{face}_x = $', font_size=30).next_to(dashed_face_x.get_end(), 
            LEFT*4+UP*1.1)
        m_x = Matrix([[-1], [0]]).scale_to_fit_height(0.75).next_to(dashed_face_x.get_end(), 
                        LEFT+UP*1.1)
        arrow_body_x = Arrow([0, 0.1, 0], [5, 0.1, 0], buff=0, color='#3498DB',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        dashed_body_x = DashedLine([0.01, 0.1, 0], [4.65, 0.1, 0], color='black')
        text_2 = Tex('$2 * \\vec{body}_x = $', font_size=30).next_to(arrow_body_x.get_end(), 
            LEFT*0.5+UP*1.1)
        m_y = Matrix([[5], [0]]).scale_to_fit_height(0.75).next_to(arrow_body_x.get_end(), 
            RIGHT+UP*1.1)
        self.add(arrow_face_x, dashed_face_x, text_1, m_x,
                arrow_body_x, dashed_body_x, text_2, m_y)
        