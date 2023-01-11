from manim import *
import pdb

class ManimScene(Scene):
    def construct(self):
    
        '''Each of these features can be measured using a basic measuring unit, such as a unit 1 face length, or a unit 1 body size.'''
        
        faceText = Text('Nose \nTip').shift(LEFT*5.5 + UP*1.5)
        bodyText = Text('Ear \nLength').shift(LEFT*5 + DOWN*1.5)
        self.add(faceText, bodyText)
        
        # self.wait(4)
        
        ear_length = 0.5  #lowest is 0.5
        nose_tip = 0.25  # each unit of 1 is 0.25. 3 is 0.75, etc
        
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
        
        self.add(face_black)  #to cover ear bottoms
        self.play(FadeIn(left_ear, right_ear, ear_box, ear_1_text))
    
        self.wait(1.5)
        
        ###################
    
        nose_line_1 = Line([-0.5, 0, 0], [0.5, 0, 0])
        nose_line_2 = Line([-0.5, 0, 0], [0, nose_tip, 0])
        nose_line_3 = Line([0, nose_tip, 0], [0.5, 0, 0])
        nose_box = Rectangle(color=WHITE, height=5, width=6, stroke_width=1).shift(UP*0.33)
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
        
        nose_group = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), nose.copy(), whiskers.copy(), nose_box.copy()).scale(0.5).shift(UP*1.8)
                        
        nose_1_text = Text("1", font_size=28).shift(UP*3.1)
                        
        self.play(FadeIn(nose_group, nose_1_text))
        
        self.wait(2)
                
        ####### Analogy to space and time
        
        '''Think of these basic measuring units as just like using 1 meter to measure distance, or 1 second to measure time.'''
        
        meter = Arrow([0,0,0], [1,0,0]).shift(RIGHT*3 + UP*1.75).scale(1.5)
        meter_text = Text("1 meter").shift(RIGHT*4 + UP*1.35).scale(0.5)
        self.play(FadeIn(meter), FadeIn(meter_text, shift=DOWN*0.3))
        
        self.wait(1)
        
        meter_2 = Arrow([0,0,0], [1,0,0]).shift(RIGHT*3.75 + UP*1.75).scale(1.5)
        meter_text_2 = Text("2 meters").shift(RIGHT*4 + UP*1.35).scale(0.5)
        self.play(FadeIn(meter_2, shift=RIGHT), Transform(meter_text, meter_text_2))
        
        self.wait(2)
        
        # https://www.reddit.com/r/manim/comments/j3s49p/timerstopwatch/
        sec = Integer(0).shift(RIGHT*4 + DOWN*1.75)
        self.add(sec)
        self.clock = 0
        def update_timer(mob, dt):
           self.clock += dt
           mob.set_value(self.clock)
        sec.add_updater(update_timer)
               
        self.wait(3)
               
        self.remove(meter, meter_text, meter_2, sec)
        
        ####### Make copy to right
        
        '''We can grow or shrink basic measuring units to get different measurements. '''
                
        face_black_copy = face_black.copy()
        # ears_copy = ears.copy()
        # ears_copy.add(face_black_copy)
        # left_ear_copy = left_ear.copy()
        left_ear_1_c = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0])
        left_ear_2_c = Line([-1, ear_length+1.5, 0], [0, 0, 0])
        left_ear_copy = VGroup(left_ear_1_c, left_ear_2_c)
        
        right_ear_1_copy = Line([1.5, 0, 0], [1, ear_length+1.5, 0])
        right_ear_2_copy = Line([1, ear_length+1.5, 0], [0, 0, 0])
        right_ear_copy = VGroup(right_ear_1_copy, right_ear_2_copy)
        
        face_black_copy = Circle(radius=1.75, color=BLACK, fill_color=BLACK, fill_opacity=1).move_to([0, 0, 0]).scale(0.5).shift(DOWN*2.1)
        
        ear_box_copy = Rectangle(color=WHITE, height=5.7, width=6, stroke_width=1).shift(UP*0.33)
        
        # right_ear_copy = right_ear.copy()
        # ear_box_copy = ear_box.copy()
        # ears_copy = VGroup(face_black_copy, left_ear_copy, right_ear_copy, ear_box_copy)
        ears_copy = VGroup(left_ear_copy, right_ear_copy, ear_box_copy).scale(0.5).shift(DOWN*2.1)
        ears_copy.add(face_black_copy)
        
        ears_copy.generate_target()
        ears_copy.target.shift(RIGHT*4.8)
        
        nose_group_copy = nose_group.copy()
        nose_group_copy.generate_target()
        nose_group_copy.target.shift(RIGHT*4.8)
        
        self.add(ears_copy, nose_group_copy)
        self.play(MoveToTarget(ears_copy), MoveToTarget(nose_group_copy))
        
        self.wait(2)
        
        # self.add(face_black_copy)
        # self.play(FadeIn(face_black_copy, left_ear_copy, right_ear_copy, ear_box_copy, shift=RIGHT*5))
                
        ####### Scale copy
        #
        #'''For example, at the bottom right, we can make the unit 1 ear twice as big to get the unit 2 ear, '''
               
        # self.wait(4)
        
        ear_length_2 = 1
        left_ear_1_2 = Line([-1.5, 0, 0], [-1, ear_length_2+1.5, 0])
        left_ear_2_2 = Line([-1, ear_length_2+1.5, 0], [0, 0, 0])
        left_ear_2 = VGroup(left_ear_1_2, left_ear_2_2)
        
        right_ear_1_2 = Line([1.5, 0, 0], [1, ear_length_2+1.5, 0])
        right_ear_2_2 = Line([1, ear_length_2+1.5, 0], [0, 0, 0])
        right_ear_2 = VGroup(right_ear_1_2, right_ear_2_2)
        
        ear_box_2 = Rectangle(color=WHITE, height=5.7, width=6, stroke_width=1).shift(UP*0.33)
        ears_2 = VGroup(left_ear_2, right_ear_2, ear_box_2).scale(0.5).shift(DOWN*2.1+RIGHT*4.8)
                
        ear_2_text = Text("2", font_size=28).shift(DOWN*0.8+RIGHT*4.8)
        
        self.play(Transform(left_ear_copy, left_ear_2), Transform(right_ear_copy, right_ear_2), FadeIn(ear_2_text))
        
        #ISSUE: transform goes to unscaled version. the issue is scale(0.5) doesn't work when copy vgroup, so need to re-create from scratch then scale group instead of just copying group. 
        #also, scale works different depending on which objects are scaled together in a group, so you must recreate all objs that were scaled together, even if they aren't going to be transformed, as the recreation makes them (eg. ear_box) their orig size before being transformed
        # in nose group, instead of scaling the original, we scale copies of the original so it's still intact. that way, instead of re-creating the original, we can just make copies of it and scale those. only nose needs to be re-created so its values can be adjusted
        
        self.wait(2)  
                
        '''or cut it in half to get the unit 0.5 ear.'''
        
        ear_length_3 = 0.25
        left_ear_1_3 = Line([-1.5, 0, 0], [-1, ear_length_3+1.5, 0])
        left_ear_2_3 = Line([-1, ear_length_3+1.5, 0], [0, 0, 0])
        left_ear_3 = VGroup(left_ear_1_3, left_ear_2_3)
        
        right_ear_1_3 = Line([1.5, 0, 0], [1, ear_length_3+1.5, 0])
        right_ear_2_3 = Line([1, ear_length_3+1.5, 0], [0, 0, 0])
        right_ear_3 = VGroup(right_ear_1_3, right_ear_2_3)
        
        ear_box_3 = Rectangle(color=WHITE, height=5.7, width=6, stroke_width=1).shift(UP*0.33)
        ears_2 = VGroup(left_ear_3, right_ear_3, ear_box_3).scale(0.5).shift(DOWN*2.1+RIGHT*4.8)
                
        ear_3_text = Text("0.5", font_size=28).shift(DOWN*0.8+RIGHT*4.8)
                
        self.play(Transform(left_ear_copy, left_ear_3), Transform(right_ear_copy, right_ear_3), Transform(ear_2_text, ear_3_text))
                
        self.wait(2)  
        
        ##############
        '''At the top right, the higher the nose tip points, the higher the value. '''
        
        # nose_2 = nose.copy()
        # nose_2[1].end[1] = 0.75
        # nose_2[2].start[1] = 0.75
        nose_tip_2 = 1
        nose_line_1_2 = Line([-0.5, 0, 0], [0.5, 0, 0])
        nose_line_2_2 = Line([-0.5, 0, 0], [0, nose_tip_2, 0])
        nose_line_3_2 = Line([0, nose_tip_2, 0], [0.5, 0, 0])
        nose_2 = VGroup(nose_line_1_2, nose_line_2_2, nose_line_3_2)
        
        nose_group_2 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), nose_2, whiskers.copy(), nose_box.copy()).scale(0.5).shift(UP*1.8).shift(RIGHT*4.8)
                        
        nose_2_text = Text("2", font_size=28).shift(UP*3.1).shift(RIGHT*4.8)
                        
        self.play(Transform(nose_group_copy, nose_group_2), FadeIn(nose_2_text))
        # self.play(FadeOut(nose_group_copy[3]), FadeIn(nose_group_2), FadeIn(nose_2_text))
              
        self.wait(2)
        
        ##############
        
        '''It can also point down to get a negative measurement.'''
        
        nose_tip_3 = -0.25
        nose_line_1_3 = Line([-0.5, 0, 0], [0.5, 0, 0])
        nose_line_2_3 = Line([-0.5, 0, 0], [0, nose_tip_3, 0])
        nose_line_3_3 = Line([0, nose_tip_3, 0], [0.5, 0, 0])
        nose_3 = VGroup(nose_line_1_3, nose_line_2_3, nose_line_3_3)
        
        nose_group_3 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), nose_3, whiskers.copy(), nose_box.copy()).scale(0.5).shift(UP*1.8).shift(RIGHT*4.8)
                        
        nose_3_text = Text("-1", font_size=28).shift(UP*3.1).shift(RIGHT*4.8)
                        
                        
        self.play(Transform(nose_group_copy, nose_group_3), Transform(nose_2_text, nose_3_text))
        
        self.wait(2)
        
        #########################
        ''' The lower the tip points, the lower the value.'''
        
        nose_tip_4 = -0.75
        nose_line_1_4 = Line([-0.5, 0, 0], [0.5, 0, 0])
        nose_line_2_4 = Line([-0.5, 0, 0], [0, nose_tip_4, 0])
        nose_line_3_4 = Line([0, nose_tip_4, 0], [0.5, 0, 0])
        nose_4 = VGroup(nose_line_1_4, nose_line_2_4, nose_line_3_4)
        
        nose_group_4 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), nose_4, whiskers.copy(), nose_box.copy()).scale(0.5).shift(UP*1.8).shift(RIGHT*4.8)
                        
        nose_4_text = Text("-3", font_size=28).shift(UP*3.1).shift(RIGHT*4.8)
                        
        self.play(Transform(nose_group_copy, nose_group_4), Transform(nose_2_text, nose_4_text))
        
        self.wait(2)