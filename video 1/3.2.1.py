from manim import *
from random import randint, random


class VectorArrow(VectorScene, Scene):
    def setup(self):
        Scene.setup(self)
        VectorScene.setup(self)
        
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        
        self.wait(3)
        
        '''The data samples in this dataset can be represented as points in a coordinate space, using face length and body size as axes. '''
        
        faceText = Text('Face \nLength', 
            font_size=16).next_to([1,0,0], DOWN*2)
        arrow_c = self.add_vector([1, 0, 0], buff=0, color='#FA8072',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #light red
        backgroundRectangle1 = BackgroundRectangle(faceText, color=BLACK, fill_opacity=1)
        self.play(FadeIn(backgroundRectangle1, faceText))
        
        bodyText = Text('Body \nSize', 
            font_size=16).next_to([0,1,0], LEFT*2.5)
        arrow_d = self.add_vector([0, 1, 0], buff=0, color='#ADD8E6',
            stroke_width=4, max_tip_length_to_length_ratio=0.15, 
            max_stroke_width_to_length_ratio=5)
        backgroundRectangle2 = BackgroundRectangle(bodyText, color=BLACK, fill_opacity=1)
        self.play(FadeIn(backgroundRectangle2, bodyText))
                
        self.remove(arrow_c, arrow_d)
        
        self.wait(1)
        
        ########
        '''Note that each data point here corresponds to a data sample of a basic measuring unit.'''
        
        face_1 = Rectangle(color=WHITE, height=0.15, width=0.32, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        face_1.move_to(np.array([1, 0, 0])).shift(UP*0.1 + LEFT*0.25)
        face_box = Rectangle(color=WHITE, height=0.75, width=1.05, stroke_width=1)
        face_box.move_to(np.array([1, 0, 0]))
        
        add_face = GrowFromPoint(face_1, [1, 0, 0])
        add_faceBox = GrowFromPoint(face_box, [1, 0, 0])
        self.play(add_face, add_faceBox)
        
        face_1_text = Text("1")
        face_1_text.scale(0.8 * face_1.get_height() / face_1_text.get_height()).move_to(face_1.get_center())
        self.play(FadeIn(face_1_text))
        
        body_1 = Ellipse(color=WHITE, height=0.15, width=0.42, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        body_1.move_to(np.array([0, 1, 0])).shift(DOWN*0.1 + RIGHT*0.1)
        body_box = Rectangle(color=WHITE, height=0.75, width=1.05, stroke_width=1)
        body_box.move_to(np.array([0, 1, 0]))
        
        add_body = GrowFromPoint(body_1, [0, 1, 0])
        add_bodyBox = GrowFromPoint(body_box, [0, 1, 0])
        self.play(add_body, add_bodyBox)
        
        body_1_text = Text("1")
        body_1_text.scale(0.7 * body_1.get_height() / body_1_text.get_height()).move_to(body_1.get_center())
        self.play(FadeIn(body_1_text))
        
        self.wait(4)
                
        ################ Move to (1, 1)
        
        '''We can add together the unit 1 face length and the unit 1 body size to form a data sample with a unit 1 face length and a unit 1 body size.'''
        
        # will leave a copy behind if this isn't done
        self.remove(face_1, body_1, face_box, body_box, face_1_text, body_1_text,backgroundRectangle1,backgroundRectangle2)
        
        face_2 = Rectangle(color=WHITE, height=0.15, width=0.32, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        face_2.move_to(np.array([1, 1, 0])).shift(UP*0.07 + LEFT*0.23)
        face_box_2 = Rectangle(color=WHITE, height=0.75, width=1.05, stroke_width=1)
        face_box_2.move_to(np.array([1, 1, 0]))
        
        body_2 = Ellipse(color=WHITE, height=0.15, width=0.42, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        body_2.move_to(np.array([1, 1, 0])).shift(DOWN*0.07 + RIGHT*0.09)
        body_box_2 = Rectangle(color=WHITE, height=0.75, width=1.05, stroke_width=1)
        body_box_2.move_to(np.array([1, 1, 0]))
                
        self.play(Transform(face_1, face_2), Transform(face_box, face_box_2), Transform(body_1, body_2), Transform(body_box, body_box_2))
       
        self.wait(3)
        
        ######### Show equations for imgs and [1,1]
                
        eqn_background = Rectangle(color=WHITE, height=1.5, width=4, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background.move_to(np.array([3.7, 1, 0]))
        
        equal_sign = Text('=', font_size=32)
        equal_sign.move_to(np.array([2, 1, 0]))
        
        face_1_eqn = Rectangle(color=WHITE, height=0.15, width=0.32, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        face_1_eqn.move_to(np.array([3, 1, 0])).shift(UP*0.1 + LEFT*0.25)
        face_box_eqn = Rectangle(color=WHITE, height=0.75, width=1.05, stroke_width=1)
        face_box_eqn.move_to(np.array([3, 1, 0]))
        
        plus_sign = Text('+', font_size=32)
        plus_sign.move_to(np.array([4, 1, 0]))
        
        body_1_eqn = Ellipse(color=WHITE, height=0.15, width=0.42, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        body_1_eqn.move_to(np.array([5, 1, 0])).shift(DOWN*0.1 + RIGHT*0.1)
        body_box_eqn = Rectangle(color=WHITE, height=0.75, width=1.05, stroke_width=1)
        body_box_eqn.move_to(np.array([5, 1, 0]))
        
        self.play(FadeIn(eqn_background, equal_sign, face_1_eqn, face_box_eqn, plus_sign, body_1_eqn, body_box_eqn))
        
        self.wait(3)
        
        ######### Show data pts for [1,1]
        
        '''Notice that this is the same as adding the data points (1,0), and (0,1). '''
        
        dot1 = Dot([1,0,0], radius=0.1)
        dot1_text = Text('(1, 0)', font_size=16).next_to(dot1, 0.3*LEFT+UP*0.5)
        
        dot2 = Dot([0,1,0], radius=0.1)
        dot2_text = Text('(0, 1)', font_size=16).next_to(dot2, 0.3*LEFT+UP*0.6)
        
        self.play(FadeIn(dot1, dot1_text, dot2, dot2_text))
        
        self.wait(3)
        
        ######### Show vector equations for [1,1]
        
        '''We can represent these data points as vectors'''
        
        eqn_background_2 = Rectangle(color=WHITE, height=1.5, width=4, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background_2.move_to(np.array([3.7, -1, 0]))
        
        equal_sign_2 = Text('=', font_size=32)
        equal_sign_2.move_to(np.array([2, -1, 0]))
        
        mat_1 = MathTex(r"\begin{bmatrix} 1 \\ 0 \end{bmatrix}")
        mat_1.move_to(np.array([3, -1, 0])).scale(0.85)
        
        plus_sign_2 = Text('+', font_size=32)
        plus_sign_2.move_to(np.array([4, -1, 0]))
        
        mat_2 = MathTex(r"\begin{bmatrix} 0 \\ 1 \end{bmatrix}")
        mat_2.move_to(np.array([5, -1, 0])).scale(0.85)
        
        self.play(FadeOut(faceText, bodyText), FadeIn(eqn_background_2, equal_sign_2, mat_1, plus_sign_2, mat_2, shift=DOWN))
        
        self.wait(3)
        
        ######### Sum up vectors to get [1,1]
        
        ''', and show that adding these data sample images together is the same as vector addition.'''
                
        # dot1 = Dot([1,1,0], radius=0.08)
        dot3_text = Text('(1, 1)', font_size=16).next_to([1, 1, 0], 0.3*LEFT+DOWN*2)
                              
        mat_3 = MathTex(r"\begin{bmatrix} 1 \\ 1 \end{bmatrix}")
        mat_3.move_to(np.array([3, -1, 0])).scale(0.85)
        
        # to move obj using move_to instead of transform, use .animate.move_to
        self.play(FadeOut(dot1_text, dot2_text))
        self.remove(mat_1, mat_2)
        self.play(dot1.animate.move_to(np.array([1, 1, 0])), dot2.animate.move_to(np.array([1, 1, 0])), FadeOut(plus_sign_2, mat_2, shift=LEFT*2), Transform(mat_1, mat_3))
        self.play(FadeIn(dot3_text))
                        
        self.wait(4)
        
        
        
        