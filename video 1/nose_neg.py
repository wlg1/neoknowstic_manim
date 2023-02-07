from manim import *
import pdb

class ManimScene(Scene):
    def construct(self):
    
        '''Each of these features can be measured using a basic measuring unit, such as a unit 1 face length, or a unit 1 body size.'''
        
        faceText = Text('Nose \nTip').shift(LEFT*5.5 + UP*1.5)
        bodyText = Text('Ear \nLength').shift(LEFT*5 + DOWN*1.5)
        # self.add(faceText, bodyText)
        
        # self.wait(4)
        
        ear_length = 0.5  #lowest is 0.5
        nose_tip = 0.3  # each unit of 1 is 0.3. 3 is 0.9, etc
        
        ##########        
        left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0])
        left_ear_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0])
        left_ear = VGroup(left_ear_1, left_ear_2)
        
        right_ear_1 = Line([1.5, 0, 0], [1, ear_length+1.5, 0])
        right_ear_2 = Line([1, ear_length+1.5, 0], [0, 0, 0])
        right_ear = VGroup(right_ear_1, right_ear_2)
        
        face_black = Circle(radius=1.75, color=BLACK, fill_color=BLACK, fill_opacity=1).move_to([0, 0, 0]).scale(0.5).shift(DOWN*2.1)
        
        face_ears = Circle(radius=1.75, color=WHITE).move_to([0, 0, 0])
        ear_box = Rectangle(color=WHITE, height=5.7, width=6, stroke_width=1).shift(UP*0.33)
        ears = VGroup(left_ear, right_ear, ear_box).scale(0.5).shift(DOWN*2.1)
                        
        ear_1_text = Text("1", font_size=28).shift(DOWN*0.8)
        
        ear_box.z_index=2
        face_black.z_index=1
        # face_ears.z_index=1
        left_ear.z_index=0
        right_ear.z_index=0
                
        ###################
    
        nose_line_1 = Line([-0.5, 0, 0], [0.5, 0, 0])
        nose_line_2 = Line([-0.5, 0, 0], [0, nose_tip, 0])
        nose_line_3 = Line([0, nose_tip, 0], [0.5, 0, 0])
        nose_box = Rectangle(color=WHITE, height=5.7, width=6, stroke_width=1).shift(UP*0.33)
        nose = VGroup(nose_line_1, nose_line_2, nose_line_3)
                     
        face_outline = Circle(radius=1.75, color=WHITE, fill_color=BLACK, fill_opacity=1).move_to([0, 0, 0])
        left_eye = Dot(color=WHITE).move_to([-1, 0.5, 0])
        right_eye = Dot(color=WHITE).move_to([1, 0.5, 0])
        
        whisker_1 = Line([-1, -0.3, 0], [-2.3, -0.5, 0]) # left down
        whisker_2 = Line([-1, -0.3, 0], [-2.3, 0.5, 0]) # left up
        whisker_3 = Line([-1, -0.3, 0], [-2.3, 0, 0]) # left middle
        whisker_4 = Line([1, -0.3, 0], [2.3, -0.5, 0]) # right down
        whisker_5 = Line([1, -0.3, 0], [2.3, 0.5, 0])  # right up
        whisker_6 = Line([1, -0.3, 0], [2.3, 0, 0]) # left middle
        whiskers = VGroup(whisker_1, whisker_2, whisker_3, whisker_4, whisker_5, whisker_6)
        
        nose_group = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), nose.copy(), whiskers.copy(), nose_box.copy())
                        
        nose_1_text = Text("1", font_size=66).shift(RIGHT*5)
                        
        self.play(GrowFromPoint(nose_group, nose_group.get_center()), FadeIn(nose_1_text))
        
        self.wait(2)
                
        #######
        '''It can also point down to get a negative measurement.'''
        
        nose_tip_3 = -0.3
        nose_line_1_3 = Line([-0.5, 0, 0], [0.5, 0, 0])
        nose_line_2_3 = Line([-0.5, 0, 0], [0, nose_tip_3, 0])
        nose_line_3_3 = Line([0, nose_tip_3, 0], [0.5, 0, 0])
        nose_3 = VGroup(nose_line_1_3, nose_line_2_3, nose_line_3_3)
        
        nose_group_3 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), nose_3, whiskers.copy(), nose_box.copy())
                        
        nose_3_text = Text("-1", font_size=66).shift(RIGHT*5)
                                                
        self.play(Transform(nose_group, nose_group_3), Transform(nose_1_text, nose_3_text))
        
        self.wait(2)
        
        #########################
        ''' The lower the tip points, the lower the value.'''
        
        nose_tip_4 = -0.9
        nose_line_1_4 = Line([-0.5, 0, 0], [0.5, 0, 0])
        nose_line_2_4 = Line([-0.5, 0, 0], [0, nose_tip_4, 0])
        nose_line_3_4 = Line([0, nose_tip_4, 0], [0.5, 0, 0])
        nose_4 = VGroup(nose_line_1_4, nose_line_2_4, nose_line_3_4)
        
        nose_group_4 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), nose_4, whiskers.copy(), nose_box.copy())
                        
        nose_4_text = Text("-3", font_size=66).shift(RIGHT*5)
                        
        self.play(Transform(nose_group, nose_group_4), Transform(nose_1_text, nose_4_text))
        
        self.wait(2)