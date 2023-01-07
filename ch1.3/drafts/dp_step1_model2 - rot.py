from manim import *
        
class VectorArrow(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        
        face = ImageMobject("face1_nonum.png")
        face.scale(0.4)
        face.move_to(np.array([2, 1, 0]))
        self.add(face)
        
        body = ImageMobject("body1_nonum.png")
        body.scale(0.4)
        body.move_to(np.array([-1, 1, 0]))
        self.add(body)
        
        arrow_v = Arrow(ORIGIN, [1, 0, 0], buff=0, color='#FA8072',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #light red
        arrow_w = Arrow(ORIGIN, [0, 1, 0], buff=0, color='#CCCCFF',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #light blue
        self.add(arrow_v, arrow_w)
        
        arrow_c = Arrow(ORIGIN, [2, 1, 0], buff=0, color='#E74C3C',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        arrow_d = Arrow(ORIGIN, [-1, 1, 0], buff=0, color='#3498DB',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker blue
        self.add(arrow_c, arrow_d)
        
        arrow_face_x = Arrow([0, -0.1, 0], [2, -0.1, 0], buff=0, color='#E74C3C',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        text_1 = Tex('$\\vec{face}_x$', font_size=30).next_to(arrow_face_x.get_end(), 
            LEFT+UP*1.1)
        arrow_body_x = Arrow([0, -0.1, 0], [-1, -0.1, 0], buff=0, color='#3498DB',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        text_2 = Tex('$\\vec{body}_x$', font_size=30).next_to(arrow_body_x.get_end(), 
            RIGHT*0.3+UP*1.1)
        self.add(arrow_face_x, text_1, arrow_body_x, text_2)
        