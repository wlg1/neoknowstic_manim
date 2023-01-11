from manim import *

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
                        
        #face_1_text = Text("1")
        #face_1_text.scale(0.4 * face_1.get_height() / face_1_text.get_height()).move_to(face_1.get_center())
        
        ear_box.z_index=2
        face_black.z_index=1
        # face_ears.z_index=1
        left_ear.z_index=0
        right_ear.z_index=0
        
        self.add(face_black)  #to cover ear bottoms
        self.play(FadeIn(left_ear, right_ear, ear_box))
    
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
        
        nose_group = VGroup(face_outline, left_eye, right_eye, nose, whiskers, nose_box).scale(0.5).shift(UP*1.8)
                        
        self.play(FadeIn(nose_group))
        
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
        ears_copy = ears.copy()
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
        #'''For example, we can make the unit 1 body twice as big to get the unit 2 body, '''
        #        
        #self.wait(4)
        #
        #body_2 = Ellipse(color=WHITE, height=1, width=2.1, stroke_width=1).shift(RIGHT*5.12 + DOWN*1.6)
        #self.play(Transform(body_copy, body_2))
        #
        #body_2_text = Text("2")
        #body_2_text.scale(0.2 * body_2.get_height() / body_2_text.get_height()).move_to(body_2.get_center())
        #self.play(FadeIn(body_2_text))
        #
        #'''or cut the unit 1 face in half to get the unit 0.5 face.'''
        #
        #self.wait(2)  
        #
        #face_2 = Rectangle(color=WHITE, height=0.65, width=0.66, stroke_width=1).shift(RIGHT*4.97 + UP*2.05)
        #self.play(Transform(face_copy, face_2))
        #
        #face_2_text = Text("0.5")
        #face_2_text.scale(0.3 * face_2.get_height() / face_2_text.get_height()).move_to(face_2).shift(RIGHT*0.7)
        #self.play(FadeIn(face_2_text))
        #
        #self.wait(2)
        
        