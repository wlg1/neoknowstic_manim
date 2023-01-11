from manim import *
import pdb

class VectorArrow(VectorScene, Scene):
    def setup(self):
        Scene.setup(self)
        VectorScene.setup(self)
        
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        
        # self.wait(3)
        
        '''The data samples in this dataset can be represented as points in a coordinate space, using nose tip and ear length as axes. '''
        
        faceText = Text('Nose \nTip', 
            font_size=16).next_to([1,0,0], DOWN*2.4)
        arrow_c = self.add_vector([1, 0, 0], buff=0, color='#FA8072',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #light red
        backgroundRectangle1 = BackgroundRectangle(faceText, color=BLACK, fill_opacity=1)
        self.play(FadeIn(backgroundRectangle1, faceText))
        
        bodyText = Text('Ear \nLength', 
            font_size=16).next_to([0,1,0], LEFT*2.5)
        arrow_d = self.add_vector([0, 1, 0], buff=0, color='#ADD8E6',
            stroke_width=4, max_tip_length_to_length_ratio=0.15, 
            max_stroke_width_to_length_ratio=5)
        backgroundRectangle2 = BackgroundRectangle(bodyText, color=BLACK, fill_opacity=1)
        self.play(FadeIn(backgroundRectangle2, bodyText))
                
        self.remove(arrow_c, arrow_d)
        
        # self.wait(1)
        
        ########
        '''Note that each data point here corresponds to a data sample of a basic measuring unit.'''
        
        nose_tip = 0.3
        
        nose_box = Rectangle(color=WHITE, height=5.4, width=5.7, stroke_width=1, fill_color=BLACK, fill_opacity=1).shift(UP*0.33)
        
        nose_line_1 = Line([-0.5, 0, 0], [0.5, 0, 0], stroke_width=1)
        nose_line_2 = Line([-0.5, 0, 0], [0, nose_tip, 0], stroke_width=1)
        nose_line_3 = Line([0, nose_tip, 0], [0.5, 0, 0], stroke_width=1)
        nose = VGroup(nose_line_1, nose_line_2, nose_line_3)
        
        face_outline = Circle(radius=1.75, color=WHITE, fill_color=BLACK, fill_opacity=1, stroke_width=1).move_to([0, 0, 0])
        left_eye = Dot(color=WHITE).move_to([-1, 0.5, 0])
        right_eye = Dot(color=WHITE).move_to([1, 0.5, 0])
        
        whisker_1 = Line([-1, -0.3, 0], [-2.3, -0.5, 0], stroke_width=1) # left down
        whisker_2 = Line([-1, -0.3, 0], [-2.3, 0.5, 0], stroke_width=1) # left up
        whisker_3 = Line([-1, -0.3, 0], [-2.3, 0, 0], stroke_width=1) # left middle
        whisker_4 = Line([1, -0.3, 0], [2.3, -0.5, 0], stroke_width=1) # right down
        whisker_5 = Line([1, -0.3, 0], [2.3, 0.5, 0], stroke_width=1)  # right up
        whisker_6 = Line([1, -0.3, 0], [2.3, 0, 0], stroke_width=1) # left middle
        whiskers = VGroup(whisker_1, whisker_2, whisker_3, whisker_4, whisker_5, whisker_6)
        
        # nose_box.z_index=(nose.z_index - 1) #this will set to -1, but it will be behind coordinate system
        
        # this won't work b/c once it's added, nose box copy will be at 1, too
        # nose_group = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), nose.copy(), whiskers.copy())
        # nose_group.z_index=1
        # nose_box.z_index=0
        # nose_group.add(nose_box.copy())
        # nose_group.scale(0.2).move_to(np.array([1, 0, 0]))
        
        # nose_group.z_index=1
        # nose_group[5].z_index=(nose_group.z_index - 1) # b/c the displayed nose_box is a copy, make sure to set that one, not the original
        
        # nose_group = VGroup(face_outline, left_eye, right_eye, nose, whiskers, nose_box.copy()).scale(0.2).move_to(np.array([1, 0, 0]))

        #face_black is at 2, so set higher than 2 to overlap it
        
        for nl in nose:
            nl.z_index=3
        
        face_outline.z_index=3
        left_eye.z_index=3
        right_eye.z_index=3
        nose_box.z_index=0
        
        for whisk in whiskers:
            whisk.z_index=3
        
        nose_group = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), nose.copy(), whiskers.copy(), nose_box.copy()).scale(0.175).move_to(np.array([1, 0, 0]))
        
        nose_1_text = Text("1", font_size=13).move_to(np.array([1, 0, 0])).shift(UP*0.3+RIGHT*0.3)
        nose_1_text.z_index=3
        
        self.play(GrowFromPoint(nose_group, [1, 0, 0]))
        # self.play(FadeIn(nose_1_text))
        
        #################
        
        ear_length = 0.5
        
        left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0], stroke_width=1)
        left_ear_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0], stroke_width=1)
        left_ear = VGroup(left_ear_1, left_ear_2)
        
        right_ear_1 = Line([1.5, 0, 0], [1, ear_length+1.5, 0], stroke_width=1)
        right_ear_2 = Line([1, ear_length+1.5, 0], [0, 0, 0], stroke_width=1)
        right_ear = VGroup(right_ear_1, right_ear_2)
        
        face_black = Circle(radius=1.75, color=BLACK, fill_color=BLACK, fill_opacity=1)
        
        ear_box = Rectangle(color=WHITE, height=5.4, width=5.7, stroke_width=1, fill_color=BLACK, fill_opacity=1).shift(UP*0.33)
        
        face_black.z_index=2
        left_ear.z_index=1
        right_ear.z_index=1
        ear_box.z_index=0
        
        ears = VGroup(face_black.copy(), left_ear.copy(), right_ear.copy(), ear_box.copy()).scale(0.175).move_to(np.array([0, 1, 0]))
                        
        # ear_1_text = Text("1", font_size=13).move_to(np.array([0.4, 1.3, 0]))
        # ear_1_text.z_index=1
                
        self.add(ears[0])  #face_black copy
        self.play(GrowFromPoint(ears, [0, 1, 0]))
        # self.play(FadeIn(ear_1_text))
        
        self.wait(1)
        #self.wait(4)
               
        ################# Move to (1, 1)
        
        '''We can add together the unit 1 face length and the unit 1 body size to form a data sample with a unit 1 face length and a unit 1 body size.'''
        
        nose_group_2 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), nose.copy(), whiskers.copy(), nose_box.copy()).scale(0.175).move_to(np.array([1, 1, 0]))
        
        ears_2 = VGroup(face_black.copy(), left_ear.copy(), right_ear.copy(), ear_box.copy()).scale(0.175).move_to(np.array([1, 1, 0]))
        
        # self.play(FadeOut(nose_1_text, ear_1_text))
        self.play(Transform(nose_group, nose_group_2), Transform(ears, ears_2))
             
        # self.wait(3)
        
        ########## Show equations for imgs and [1,1]
               
        eqn_background = Rectangle(color=WHITE, height=1.4, width=4, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background.move_to(np.array([3.7, 1, 0]))
        
        equal_sign = Text('=', font_size=32)
        equal_sign.move_to(np.array([2, 1, 0]))
        
        nose_group_eqn = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), nose.copy(), whiskers.copy(), nose_box.copy()).scale(0.175).move_to(np.array([3, 1, 0]))
        
        plus_sign = Text('+', font_size=32)
        plus_sign.move_to(np.array([4, 1, 0]))
        
        ears_eqn = VGroup(face_black.copy(), left_ear.copy(), right_ear.copy(), ear_box.copy()).scale(0.175).move_to(np.array([5, 1, 0]))
        
        self.play(FadeIn(eqn_background, equal_sign, nose_group_eqn, plus_sign, ears_eqn))
        
        self.wait(3)
        
        ######### Show data pts for [1,1]
        
        '''Notice that this is the same as adding the data points (1,0), and (0,1). '''
        
        dot1 = Dot([1,0,0], radius=0.1)
        dot1_text = Text('(1, 0)', font_size=16).next_to(dot1, 0.3*LEFT+UP*0.5)
        
        dot2 = Dot([0,1,0], radius=0.1)
        dot2_text = Text('(0, 1)', font_size=16).next_to(dot2, 0.3*LEFT+UP*0.6)
        
        dot1.z_index = 4
        dot2.z_index = 4
        
        self.play(FadeIn(dot1, dot1_text, dot2, dot2_text))
        
        self.wait(3)
        
        ######### Show vector equations for [1,1]
        
        '''We can represent these data points as vectors'''
        
        eqn_background_2 = Rectangle(color=WHITE, height=1.4, width=4, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background_2.move_to(np.array([3.7, -1, 0]))
        
        equal_sign_2 = Text('=', font_size=32)
        equal_sign_2.move_to(np.array([2, -1, 0]))
        
        mat_1 = MathTex(r"\begin{bmatrix} 1 \\ 0 \end{bmatrix}")
        mat_1.move_to(np.array([3, -1, 0])).scale(0.85)
        
        plus_sign_2 = Text('+', font_size=32)
        plus_sign_2.move_to(np.array([4, -1, 0]))
        
        mat_2 = MathTex(r"\begin{bmatrix} 0 \\ 1 \end{bmatrix}")
        mat_2.move_to(np.array([5, -1, 0])).scale(0.85)
        
        self.play(FadeOut(backgroundRectangle1, backgroundRectangle2, faceText, bodyText), FadeIn(eqn_background_2, equal_sign_2, mat_1, plus_sign_2, mat_2, shift=DOWN))
        
        self.wait(3)
        
        ######### Sum up vectors to get [1,1]
        
        ''', and show that adding these data sample images together is the same as vector addition.'''
               
        # dot1 = Dot([1,1,0], radius=0.08)
        dot3_text = Text('(1, 1)', font_size=16).next_to([1, 1, 0], 0.3*LEFT+DOWN*2.5)
                             
        mat_3 = MathTex(r"\begin{bmatrix} 1 \\ 1 \end{bmatrix}")
        mat_3.move_to(np.array([3, -1, 0])).scale(0.85)
        
        # to move obj using move_to instead of transform, use .animate.move_to
        self.play(FadeOut(dot1_text, dot2_text))
        self.remove(mat_1, mat_2)
        self.play(dot1.animate.move_to(np.array([1, 1, 0])), dot2.animate.move_to(np.array([1, 1, 0])), FadeOut(plus_sign_2, mat_2, shift=LEFT*2), Transform(mat_1, mat_3))
        self.play(FadeIn(dot3_text))
                       
        self.wait(3)
        
        ##########
        # reset all
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != numberplane])
        
        ########## Recreate basis data samples
                   
        nose_tip = 0.3
        
        nose_box = Rectangle(color=WHITE, height=5.4, width=5.7, stroke_width=1, fill_color=BLACK, fill_opacity=1).shift(UP*0.33)
        
        nose_line_1 = Line([-0.5, 0, 0], [0.5, 0, 0], stroke_width=1)
        nose_line_2 = Line([-0.5, 0, 0], [0, nose_tip, 0], stroke_width=1)
        nose_line_3 = Line([0, nose_tip, 0], [0.5, 0, 0], stroke_width=1)
        nose = VGroup(nose_line_1, nose_line_2, nose_line_3)
        
        face_outline = Circle(radius=1.75, color=WHITE, fill_color=BLACK, fill_opacity=1, stroke_width=1).move_to([0, 0, 0])
        left_eye = Dot(color=WHITE).move_to([-1, 0.5, 0])
        right_eye = Dot(color=WHITE).move_to([1, 0.5, 0])
        
        whisker_1 = Line([-1, -0.3, 0], [-2.3, -0.5, 0], stroke_width=1) # left down
        whisker_2 = Line([-1, -0.3, 0], [-2.3, 0.5, 0], stroke_width=1) # left up
        whisker_3 = Line([-1, -0.3, 0], [-2.3, 0, 0], stroke_width=1) # left middle
        whisker_4 = Line([1, -0.3, 0], [2.3, -0.5, 0], stroke_width=1) # right down
        whisker_5 = Line([1, -0.3, 0], [2.3, 0.5, 0], stroke_width=1)  # right up
        whisker_6 = Line([1, -0.3, 0], [2.3, 0, 0], stroke_width=1) # left middle
        whiskers = VGroup(whisker_1, whisker_2, whisker_3, whisker_4, whisker_5, whisker_6)
        
        for nl in nose:
            nl.z_index=3
        
        face_outline.z_index=3
        left_eye.z_index=3
        right_eye.z_index=3
        nose_box.z_index=0
        
        for whisk in whiskers:
            whisk.z_index=3
        
        nose_group = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), nose.copy(), whiskers.copy(), nose_box.copy()).scale(0.175).move_to(np.array([1, 0, 0]))
        
        nose_text_a = Text('(1, 0)', font_size=16).next_to([1,0,0], 0.3*LEFT+DOWN*2.5)        
        self.play(GrowFromPoint(nose_group, [1, 0, 0]), FadeIn(nose_text_a))
        
        #################
        # Move nose left and right
        
        nose_tip_2 = 0.6
        nose_line_2_2 = Line([-0.5, 0, 0], [0, nose_tip_2, 0], stroke_width=1)
        nose_line_3_2 = Line([0, nose_tip_2, 0], [0.5, 0, 0], stroke_width=1)
        nose_2 = VGroup(nose_line_1, nose_line_2_2, nose_line_3_2)
        for nl in nose_2:
            nl.z_index=3
        nose_group_2 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), nose_2.copy(), whiskers.copy(), nose_box.copy()).scale(0.175).move_to(np.array([2, 0, 0]))
        
        nose_text_b = Text('(2, 0)', font_size=16).next_to([2,0,0], 0.3*LEFT+DOWN*2.5)
        self.play(FadeOut(nose_text_a), Transform(nose_group, nose_group_2), FadeIn(nose_text_b))
        
        nose_tip = 0.9
        nose_line_2_3 = Line([-0.5, 0, 0], [0, nose_tip, 0], stroke_width=1)
        nose_line_3_3 = Line([0, nose_tip, 0], [0.5, 0, 0], stroke_width=1)
        nose_3 = VGroup(nose_line_1, nose_line_2_3, nose_line_3_3)
        for nl in nose_3:
            nl.z_index=3
        nose_group_3 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), nose_3.copy(), whiskers.copy(), nose_box.copy()).scale(0.175).move_to(np.array([3, 0, 0]))
        
        nose_text_c = Text('(3, 0)', font_size=16).next_to([3,0,0], 0.3*LEFT+DOWN*2.5)
        self.play(FadeOut(nose_text_b), Transform(nose_group, nose_group_3), FadeIn(nose_text_c))
        
        nose_tip = -0.3
        nose_line_2_4 = Line([-0.5, 0, 0], [0, nose_tip, 0], stroke_width=1)
        nose_line_3_4 = Line([0, nose_tip, 0], [0.5, 0, 0], stroke_width=1)
        nose_4 = VGroup(nose_line_1, nose_line_2_4, nose_line_3_4)
        for nl in nose_4:
            nl.z_index=3
        nose_group_4 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), nose_4.copy(), whiskers.copy(), nose_box.copy()).scale(0.175).move_to(np.array([-1, 0, 0]))
                
        dot1_text = Text('(-1, 0)', font_size=16).next_to([-1,0,0], 0.3*LEFT+DOWN*2.5)
        self.play(FadeOut(nose_text_c), Transform(nose_group, nose_group_4), FadeIn(dot1_text))
        
        #################
        
        ear_length = 0.5
        
        left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0], stroke_width=1)
        left_ear_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0], stroke_width=1)
        left_ear = VGroup(left_ear_1, left_ear_2)
        
        right_ear_1 = Line([1.5, 0, 0], [1, ear_length+1.5, 0], stroke_width=1)
        right_ear_2 = Line([1, ear_length+1.5, 0], [0, 0, 0], stroke_width=1)
        right_ear = VGroup(right_ear_1, right_ear_2)
        
        face_black = Circle(radius=1.75, color=BLACK, fill_color=BLACK, fill_opacity=1)
        
        ear_box = Rectangle(color=WHITE, height=5.4, width=5.7, stroke_width=1, fill_color=BLACK, fill_opacity=1).shift(UP*0.33)
        
        face_black.z_index=2
        left_ear.z_index=1
        right_ear.z_index=1
        ear_box.z_index=0
        
        ears = VGroup(face_black.copy(), left_ear.copy(), right_ear.copy(), ear_box.copy()).scale(0.175).move_to(np.array([0, 1, 0]))
                        
        self.add(ears[0])  #face_black copy
        ears_text_a = Text('(0, 1)', font_size=16).next_to([0,1,0], 0.3*RIGHT+DOWN*2.3)     
        self.play(GrowFromPoint(ears, [0, 1, 0]), FadeIn(ears_text_a))
        
        self.wait(1)
        
        #self.wait(4)
        
        ########## Scale ears
                     
        ear_length = 1
        left_ear_1_2 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0], stroke_width=1)
        left_ear_2_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0], stroke_width=1)
        left_ear_2 = VGroup(left_ear_1_2, left_ear_2_2)
        
        right_ear_1_2 = Line([1.5, 0, 0], [1, ear_length+1.5, 0], stroke_width=1)
        right_ear_2_2 = Line([1, ear_length+1.5, 0], [0, 0, 0], stroke_width=1)
        right_ear_2 = VGroup(right_ear_1_2, right_ear_2_2)
        ears_2 = VGroup(face_black.copy(), left_ear_2, right_ear_2, ear_box.copy()).scale(0.175).move_to(np.array([0, 2, 0]))
                
        dot2_text = Text('(0, 2)', font_size=16).next_to([0,2,0], 0.3*LEFT+UP*2.3)
        self.play(FadeOut(ears_text_a), Transform(ears, ears_2), FadeIn(dot2_text))
        
        self.wait(1)
        
        ########## Move to (-1, 2)
        ## will leave a copy behind if this isn't done
        #self.remove(face_1, body_1, face_box, body_box)
        ## or just move orig instead of the transformed 
        # generate_target() doesn't seem to be able to use in a group animation since it plays directly
        
        nose_group_5 = nose_group_4.copy().move_to(np.array([-1, 2, 0]))
        
        ears_3 = ears_2.copy().move_to(np.array([-1, 2, 0]))
                
        self.play(Transform(nose_group, nose_group_5), Transform(ears, ears_3))
        
        self.wait(1)
                
        ########## Show equations for imgs and [-1, 2]
              
        eqn_background = Rectangle(color=WHITE, height=1.5, width=5.2, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background.move_to(np.array([2.8, 2, 0]))
        
        equal_sign = Text('=', font_size=32)
        equal_sign.move_to(np.array([0.5, 2, 0]))
        
        scalar_1_face = MathTex(r"-1 \ * \ ")
        scalar_1_face.move_to(np.array([1.2, 2, 0])).scale(0.7)
        
        nose_group_eqn = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), nose.copy(), whiskers.copy(), nose_box.copy()).scale(0.175).move_to(np.array([2.2, 2, 0]))
                        
        plus_sign = Text('+', font_size=32)
        plus_sign.move_to(np.array([3.1, 2, 0]))
        
        scalar_2_body = MathTex(r"2 \ * \ ")
        scalar_2_body.move_to(np.array([3.7, 2, 0])).scale(0.7)
        
        ears_eqn = VGroup(face_black.copy(), left_ear.copy(), right_ear.copy(), ear_box.copy()).scale(0.175).move_to(np.array([4.6, 2, 0]))
        
        self.play(FadeIn(eqn_background, equal_sign, scalar_1_face, nose_group_eqn, plus_sign, scalar_2_body, ears_eqn))
        
        self.wait(2)
               
        ########## Show vector equations for [0.5, 2]
        
        eqn_background_2 = Rectangle(color=WHITE, height=1.5, width=5.2, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background_2.move_to(np.array([2.8, 0, 0]))
        
        equal_sign_2 = Text('=', font_size=32)
        equal_sign_2.move_to(np.array([0.5, 0, 0]))
        
        scalar_1 = MathTex(r"-1 \ * \ ")
        scalar_1.move_to(np.array([1.3, 0, 0])).scale(0.7)
        
        mat_1 = MathTex(r"\begin{bmatrix} 1 \\ 0 \end{bmatrix}")
        mat_1.move_to(np.array([2.2, 0, 0])).scale(0.85)
        
        plus_sign_2 = Text('+', font_size=32)
        plus_sign_2.move_to(np.array([3.1, 0, 0]))
        
        scalar_2 = MathTex(r"2 \ * \ ")
        scalar_2.move_to(np.array([3.7, 0, 0])).scale(0.7)
        
        mat_2 = MathTex(r"\begin{bmatrix} 0 \\ 1 \end{bmatrix}")
        mat_2.move_to(np.array([4.4, 0, 0])).scale(0.85)
                
        dot1 = Dot([-1, 0, 0], radius=0.08)
        dot2 = Dot([0,2,0], radius=0.08)
        dot1.z_index = 4
        dot2.z_index = 4
        
        #FadeOut(backgroundRectangle1, faceText, backgroundRectangle2, bodyText), 
        self.play(FadeIn(eqn_background_2, equal_sign_2, scalar_1, mat_1, scalar_2, plus_sign_2, mat_2, shift=DOWN), FadeIn(dot1, dot2))
        
        self.wait(2)
        
        ########## Multiply scalars into vectors and imgs
        
        nose_group_eqn_2 = nose_group_4.copy().move_to(np.array([2.2, 2, 0]))
        ears_eqn_2 = ears_2.copy().move_to(np.array([4.6, 2, 0]))
        
        # face_1_eqn_2 = Rectangle(color=WHITE, height=0.15, width=0.16, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        # face_1_eqn_2.move_to(np.array([2.2, 2, 0])).shift(UP*0.1 + LEFT*0.25)
        
        # body_1_eqn_2 =  Ellipse(color=WHITE, height=0.3, width=0.84, stroke_width=1,fill_color = BLACK, fill_opacity=1)
        # body_1_eqn_2.move_to(np.array([4.6, 2, 0])).shift(DOWN*0.1 + RIGHT*0.1)
        
        mat_1_2 = MathTex(r"\begin{bmatrix} -1 \\ 0 \end{bmatrix}")
        mat_1_2.move_to(np.array([2.2, 0, 0])).scale(0.85)
        
        mat_2_2 = MathTex(r"\begin{bmatrix} 0 \\ 2 \end{bmatrix}")
        mat_2_2.move_to(np.array([4.4, 0, 0])).scale(0.85)
        
        self.wait(1)
        
        self.play(FadeOut(scalar_1, scalar_1_face, shift=RIGHT), Transform(mat_1, mat_1_2), Transform(nose_group_eqn, nose_group_eqn_2))
        
        self.wait(1)
        self.play(FadeOut(scalar_2, scalar_2_body, shift=RIGHT), Transform(mat_2, mat_2_2), Transform(ears_eqn, ears_eqn_2))
              
        self.wait(2)
        
        ########## Sum up vectors to get [-1, 2]
        
        dot3_text = Text('(-1, 2)', font_size=16).next_to([-1,2,0], LEFT*0.3 + DOWN*2.5)
              
        mat_3 = MathTex(r"\begin{bmatrix} -1 \\ 2 \end{bmatrix}")
        mat_3.move_to(np.array([2.2, 0, 0])).scale(0.85)
              
        self.play(FadeOut(dot1_text, dot2_text))
        self.remove(mat_1, mat_2)
        self.play(dot1.animate.move_to(np.array([-1,2,0])), dot2.animate.move_to(np.array([-1,2,0])), FadeOut(plus_sign_2, mat_2_2, shift=LEFT*2), Transform(mat_1_2, mat_3))
        self.play(FadeIn(dot3_text))
                      
        self.wait(2)
        
        
        
        