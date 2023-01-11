from manim import *

class ManimScene(Scene):
    def construct(self):
    
        '''Each of these features can be measured using a basic measuring unit, such as a unit 1 face length, or a unit 1 body size.'''
        
        faceText = Text('Nose \nTip').shift(LEFT*5 + UP*1.5)
        bodyText = Text('Ear \nLength').shift(LEFT*5 + DOWN*1.5)
        self.add(faceText, bodyText)
        
        # self.wait(4)
        
        ear_length = 2  #lowest is 2. each +1 is 0.25
        nose_tip = 0.5  # each unit of 1 is 0.25. 3 is 0.75, etc
        
        ##########        
        left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length, 0])
        left_ear_2 = Line([-1, ear_length, 0], [0, 0, 0])
        left_ear = VGroup(left_ear_1, left_ear_2)
        
        right_ear_1 = Line([1.5, 0, 0], [1, ear_length, 0])
        right_ear_2 = Line([1, ear_length, 0], [0, 0, 0])
        right_ear = VGroup(right_ear_1, right_ear_2)
        
        face = Circle(radius=1.75, color=BLACK, fill_color=BLACK, fill_opacity=1).move_to([0, 0, 0])
        ears = VGroup(face, left_ear, right_ear)
        
        face_box = Rectangle(color=WHITE, height=1.9, width=2.65, stroke_width=1).shift(UP*1.5)
                
        #face_1_text = Text("1")
        #face_1_text.scale(0.4 * face_1.get_height() / face_1_text.get_height()).move_to(face_1.get_center())
        
        face.z_index=1
        left_ear.z_index=0
        right_ear.z_index=0
        
        self.add(face)
        self.play(FadeIn(left_ear, right_ear))
    
        #face_1 = Rectangle(color=WHITE, height=0.65, width=1.32, stroke_width=1).shift(LEFT*0.6 + UP*1.75)
        #face_box = Rectangle(color=WHITE, height=1.9, width=2.65, stroke_width=1).shift(UP*1.5)
        #face_1_text = Text("1")
        #face_1_text.scale(0.4 * face_1.get_height() / face_1_text.get_height()).move_to(face_1.get_center())
        #self.play(FadeIn(face_1, face_box, face_1_text))
        #
        #self.wait(1.5)
        #
        #body_1 = Ellipse(color=WHITE, height=0.5, width=1.05, stroke_width=1).shift(RIGHT*0.25 + DOWN*1.6)
        #body_box = Rectangle(color=WHITE, height=1.9, width=2.65, stroke_width=1).shift(DOWN*1.5)
        #body_1_text = Text("1")
        #body_1_text.scale(0.5 * body_1.get_height() / body_1_text.get_height()).move_to(body_1.get_center())
        #self.play(FadeIn(body_1, body_box, body_1_text))
        #
        #self.wait(2)
        #
        ####### Analogy to space and time
        #
        #'''Think of these basic measuring units as just like using 1 meter to measure distance, or 1 second to measure time.'''
        #
        #meter = Arrow([0,0,0], [1,0,0]).shift(RIGHT*3 + UP*1.75).scale(1.5)
        #meter_text = Text("1 meter").shift(RIGHT*4 + UP*1.35).scale(0.5)
        #self.play(FadeIn(meter), FadeIn(meter_text, shift=DOWN*0.3))
        #
        #self.wait(1)
        #
        #meter_2 = Arrow([0,0,0], [1,0,0]).shift(RIGHT*3.75 + UP*1.75).scale(1.5)
        #meter_text_2 = Text("2 meters").shift(RIGHT*4 + UP*1.35).scale(0.5)
        #self.play(FadeIn(meter_2, shift=RIGHT), Transform(meter_text, meter_text_2))
        #
        #self.wait(2)
        #
        ## https://www.reddit.com/r/manim/comments/j3s49p/timerstopwatch/
        #sec = Integer(0).shift(RIGHT*5 + DOWN*1.75)
        #self.add(sec)
        #self.clock = 0
        #def update_timer(mob, dt):
        #    self.clock += dt
        #    mob.set_value(self.clock)
        #sec.add_updater(update_timer)
        #        
        #self.wait(3)
        #        
        #self.remove(meter, meter_text, meter_2, sec)
        #
        ####### Make copy to right
        #
        #'''We can grow or shrink basic measuring units to get different measurements. '''
        #
        #face_copy = Rectangle(color=WHITE, height=0.65, width=1.32, stroke_width=1).shift(RIGHT*4.4 + UP*1.75)
        #face_box_copy = Rectangle(color=WHITE, height=1.9, width=2.65, stroke_width=1).shift(RIGHT*5 + UP*1.5)
        #body_copy = Ellipse(color=WHITE, height=0.5, width=1.05, stroke_width=1).shift(RIGHT*5.25 + DOWN*1.6)
        #body_box_copy = Rectangle(color=WHITE, height=1.9, width=2.65, stroke_width=1).shift(RIGHT*5 + DOWN*1.5)
        #
        #self.play(FadeIn(face_copy, face_box_copy, body_copy, body_box_copy, shift=RIGHT*5))
        #        
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
        
        