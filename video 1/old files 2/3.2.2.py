from manim import *
from random import randint, random


class VectorArrow(VectorScene, Scene):
    def setup(self):
        Scene.setup(self)
        VectorScene.setup(self)
        
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        
        faceText = Text('Face \nLength', 
            font_size=16).next_to([1,0,0], DOWN*2)
        arrow_c = self.add_vector([1, 0, 0], buff=0, color='#FA8072',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #light red
        backgroundRectangle1 = BackgroundRectangle(faceText, color=BLACK, fill_opacity=1)
        
        bodyText = Text('Body \nSize', 
            font_size=16).next_to([0,1,0], LEFT*2.5)
        arrow_d = self.add_vector([0, 1, 0], buff=0, color='#ADD8E6',
            stroke_width=4, max_tip_length_to_length_ratio=0.15, 
            max_stroke_width_to_length_ratio=5)
        backgroundRectangle2 = BackgroundRectangle(bodyText, color=BLACK, fill_opacity=1)
                        
        self.play(FadeIn(backgroundRectangle1,faceText,backgroundRectangle2, bodyText))
        
        ########## Recreate basis data samples
                        
        face_1 = Rectangle(color=WHITE, height=0.15, width=0.32, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        face_1.move_to(np.array([1, 0, 0])).shift(UP*0.1 + LEFT*0.25)
        face_box = Rectangle(color=WHITE, height=0.75, width=1.05, stroke_width=1)
        face_box.move_to(np.array([1, 0, 0]))
        
        add_face = GrowFromPoint(face_1, [1, 0, 0])
        add_faceBox = GrowFromPoint(face_box, [1, 0, 0])
        self.play(add_face, add_faceBox)
              
        body_1 = Ellipse(color=WHITE, height=0.15, width=0.42, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        body_1.move_to(np.array([0, 1, 0])).shift(DOWN*0.1 + RIGHT*0.1)
        body_box = Rectangle(color=WHITE, height=0.75, width=1.05, stroke_width=1)
        body_box.move_to(np.array([0, 1, 0]))
        
        add_body = GrowFromPoint(body_1, [0, 1, 0])
        add_bodyBox = GrowFromPoint(body_box, [0, 1, 0])
        self.play(add_body, add_bodyBox)
              
        ######### Scale and move to (0.5, 0), (0, 2)
              
        # generate_target() doesn't seem to be able to use in a group animation since it plays directly
        face_2 = Rectangle(color=WHITE, height=0.15, width=0.16, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        face_2.move_to(np.array([0.5, 0, 0])).shift(UP*0.1 + LEFT*0.25)
        face_box_2 = Rectangle(color=WHITE, height=0.75, width=1.05, stroke_width=1)
        face_box_2.move_to(np.array([0.5, 0, 0]))
        self.play(Transform(face_1, face_2), Transform(face_box, face_box_2))
        
        body_2 = Ellipse(color=WHITE, height=0.3, width=0.84, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        body_2.move_to(np.array([0, 2, 0])).shift(DOWN*0.1 + RIGHT*0.1)
        body_box_2 = Rectangle(color=WHITE, height=0.75, width=1.05, stroke_width=1)
        body_box_2.move_to(np.array([0, 2, 0]))
        self.play(Transform(body_1, body_2), Transform(body_box, body_box_2))
        
        self.wait(1)
        
        ######### Move to (0.5, 2)
        
        # will leave a copy behind if this isn't done
        self.remove(face_1, body_1, face_box, body_box)
        
        face_3 = Rectangle(color=WHITE, height=0.15, width=0.16, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        face_3.move_to(np.array([0.5, 2, 0])).shift(UP*0.1 + LEFT*0.25)
        face_box_3 = Rectangle(color=WHITE, height=0.75, width=1.05, stroke_width=1)
        face_box_3.move_to(np.array([0.5, 2, 0]))
        
        body_3 = Ellipse(color=WHITE, height=0.3, width=0.84, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        body_3.move_to(np.array([0.5, 2, 0])).shift(DOWN*0.1 + RIGHT*0.1)
        body_box_3 = Rectangle(color=WHITE, height=0.75, width=1.05, stroke_width=1)
        body_box_3.move_to(np.array([0.5, 2, 0]))
        
        self.play(Transform(face_2, face_3), Transform(face_box_2, face_box_3), Transform(body_2, body_3), Transform(body_box_2, body_box_3))
        
        self.wait(1)
        
        dot1 = Dot([0.5, 0, 0], radius=0.08)
        dot1_text = Text('(0.5, 0)', font_size=16).next_to(dot1, DOWN*0.5)
        
        dot2 = Dot([0,2,0], radius=0.08)
        dot2_text = Text('(0, 2)', font_size=16).next_to(dot2, 0.3*LEFT+UP*0.6)
        
        self.play(FadeIn(dot1, dot1_text, dot2, dot2_text))
        
        ######### Show equations for imgs and [0.5, 2]
               
        eqn_background = Rectangle(color=WHITE, height=1.5, width=5.2, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background.move_to(np.array([3.8, 2, 0]))
        
        equal_sign = Text('=', font_size=32)
        equal_sign.move_to(np.array([1.5, 2, 0]))
        
        scalar_1_face = MathTex(r"0.5 \ * \ ")
        scalar_1_face.move_to(np.array([2.2, 2, 0])).scale(0.7)
        
        face_1_eqn = Rectangle(color=WHITE, height=0.15, width=0.32, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        face_1_eqn.move_to(np.array([3.2, 2, 0])).shift(UP*0.1 + LEFT*0.25)
        face_box_eqn = Rectangle(color=WHITE, height=0.75, width=1.05, stroke_width=1)
        face_box_eqn.move_to(np.array([3.2, 2, 0]))
        
        plus_sign = Text('+', font_size=32)
        plus_sign.move_to(np.array([4.1, 2, 0]))
        
        scalar_2_body = MathTex(r"2 \ * \ ")
        scalar_2_body.move_to(np.array([4.7, 2, 0])).scale(0.7)
        
        body_1_eqn = Ellipse(color=WHITE, height=0.15, width=0.42, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        body_1_eqn.move_to(np.array([5.6, 2, 0])).shift(DOWN*0.1 + RIGHT*0.1)
        body_box_eqn = Rectangle(color=WHITE, height=0.75, width=1.05, stroke_width=1)
        body_box_eqn.move_to(np.array([5.6, 2, 0]))
        
        self.play(FadeIn(eqn_background, equal_sign, scalar_1_face, face_1_eqn, face_box_eqn, plus_sign, scalar_2_body, body_1_eqn, body_box_eqn))
        
        self.wait(2)
                
        ######### Show vector equations for [0.5, 2]
        
        eqn_background_2 = Rectangle(color=WHITE, height=1.5, width=5.2, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background_2.move_to(np.array([3.8, 0, 0]))
        
        equal_sign_2 = Text('=', font_size=32)
        equal_sign_2.move_to(np.array([1.5, 0, 0]))
        
        scalar_1 = MathTex(r"0.5 \ * \ ")
        scalar_1.move_to(np.array([2.3, 0, 0])).scale(0.7)
        
        mat_1 = MathTex(r"\begin{bmatrix} 1 \\ 0 \end{bmatrix}")
        mat_1.move_to(np.array([3.2, 0, 0])).scale(0.85)
        
        plus_sign_2 = Text('+', font_size=32)
        plus_sign_2.move_to(np.array([4.1, 0, 0]))
        
        scalar_2 = MathTex(r"2 \ * \ ")
        scalar_2.move_to(np.array([4.7, 0, 0])).scale(0.7)
        
        mat_2 = MathTex(r"\begin{bmatrix} 0 \\ 1 \end{bmatrix}")
        mat_2.move_to(np.array([5.4, 0, 0])).scale(0.85)
        
        self.play(FadeOut(backgroundRectangle1, faceText, backgroundRectangle2, bodyText), FadeIn(eqn_background_2, equal_sign_2, scalar_1, mat_1, scalar_2, plus_sign_2, mat_2, shift=DOWN))
        
        ######### Multiply scalars into vectors and imgs
        
        face_1_eqn_2 = Rectangle(color=WHITE, height=0.15, width=0.16, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        face_1_eqn_2.move_to(np.array([3.2, 2, 0])).shift(UP*0.1 + LEFT*0.25)
        
        body_1_eqn_2 =  Ellipse(color=WHITE, height=0.3, width=0.84, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        body_1_eqn_2.move_to(np.array([5.6, 2, 0])).shift(DOWN*0.1 + RIGHT*0.1)
        
        mat_1_2 = MathTex(r"\begin{bmatrix} 0.5 \\ 0 \end{bmatrix}")
        mat_1_2.move_to(np.array([3.2, 0, 0])).scale(0.85)
        
        mat_2_2 = MathTex(r"\begin{bmatrix} 0 \\ 2 \end{bmatrix}")
        mat_2_2.move_to(np.array([5.4, 0, 0])).scale(0.85)
        
        self.wait(1)
        
        self.play(FadeOut(scalar_1, scalar_1_face, shift=RIGHT), Transform(mat_1, mat_1_2), Transform(face_1_eqn, face_1_eqn_2))
        
        self.wait(1)
        self.play(FadeOut(scalar_2, scalar_2_body, shift=RIGHT), Transform(mat_2, mat_2_2), Transform(body_1_eqn, body_1_eqn_2))
                
        self.wait(2)
        
        ######### Sum up vectors to get [0.5, 2]
        
        dot3_text = Text('(0.5, 2)', font_size=16).next_to([0.5,2,0], DOWN*2)
                
        mat_3 = MathTex(r"\begin{bmatrix} 0.5 \\ 2 \end{bmatrix}")
        mat_3.move_to(np.array([3.2, 0, 0])).scale(0.85)
                
        self.play(FadeOut(dot1_text, dot2_text))
        self.remove(mat_1, mat_2)
        self.play(dot1.animate.move_to(np.array([0.5,2,0])), dot2.animate.move_to(np.array([0.5,2,0])), FadeOut(plus_sign_2, mat_2_2, shift=LEFT*2), Transform(mat_1_2, mat_3))
        self.play(FadeIn(dot3_text))
                        
        self.wait(2)
        
        
        
        
        