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
                       
        self.wait(4)
        
        
        
        