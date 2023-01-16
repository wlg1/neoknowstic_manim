from manim import *

class ManimScene(Scene):
    def construct(self):
    
        ###### Make the cat person ############
        ear_length = 2.75  #lowest is 2. each +1 is 0.25
        nose_tip = 0.5  # each unit of 1 is 0.25. 3 is 0.75, etc
        
        #############
        '''Some evidence suggests that how much a cat person enjoys naps can be predicted by measuring their nose tips and ear lengths.'''
        left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length, 0])
        left_ear_2 = Line([-1, ear_length, 0], [0, 0, 0])
        left_ear = VGroup(left_ear_1, left_ear_2)
        
        right_ear_1 = Line([1.5, 0, 0], [1, ear_length, 0])
        right_ear_2 = Line([1, ear_length, 0], [0, 0, 0])
        right_ear = VGroup(right_ear_1, right_ear_2)
                
        face = Circle(radius=1.75, color=WHITE, fill_color=BLACK, fill_opacity=1).move_to([0, 0, 0])
        
        left_eye = Dot(color=WHITE).move_to([-1, 0.5, 0])
        right_eye = Dot(color=WHITE).move_to([1, 0.5, 0])
        # left_eye = ArcBetweenPoints([-0.3, -0.75,0], [0.3, -0.75,0]).rotate(180*DEGREES).move_to([-1, 0.5, 0])
        # right_eye = ArcBetweenPoints([-0.3, -0.75,0], [0.3, -0.75,0]).rotate(180*DEGREES).move_to([1, 0.5, 0])
        
        nose_line_1 = Line([-0.5, 0, 0], [0.5, 0, 0])
        nose_line_2 = Line([-0.5, 0, 0], [0, nose_tip, 0])
        nose_line_3 = Line([0, nose_tip, 0], [0.5, 0, 0])
                
        whisker_1 = Line([-1, -0.3, 0], [-2, -0.5, 0]) # left down
        whisker_2 = Line([-1, -0.3, 0], [-2, 0.5, 0]) # left up
        whisker_3 = Line([1, -0.3, 0], [2, -0.5, 0]) # right down
        whisker_4 = Line([1, -0.3, 0], [2, 0.5, 0])  # right up
        
        # mouth = ArcBetweenPoints([-0.5, -0.75,0], [0.5, -0.75,0])
                                
        self.add(face, left_eye, right_eye, left_ear, right_ear)
        self.add(whisker_1, whisker_2, whisker_3, whisker_4)
        self.add(nose_line_1, nose_line_2, nose_line_3)
        self.bring_to_back(left_ear, right_ear)
        
        zzz = Text("...zZz...", font_size = 40, color=WHITE).move_to([2.2, 1.8,0])
        
        # self.play(Write(zzz))
        # self.wait(1)
        # self.play(Unwrite(zzz))
        
        ##################
        # Highlight nose
        '''For example, a lot of cat people with long nose tips'''
        
        #grow it?
        
        nose_line_1_color = Line([-0.5, 0, 0], [0.5, 0, 0], color=RED)
        nose_line_2_color = Line([-0.5, 0, 0], [0, nose_tip, 0], color=RED)
        nose_line_3_color = Line([0, nose_tip, 0], [0.5, 0, 0], color=RED)
        
        self.play(Transform(nose_line_1, nose_line_1_color), Transform(nose_line_2, nose_line_2_color), Transform(nose_line_3, nose_line_3_color))
        self.wait(1)
        
        ##################
        # Highlight ears
        ''' and long ears are said to enjoy naps.'''
            
        left_ear_1_color = Line([-1.5, 0, 0], [-1, ear_length, 0], color=BLUE)
        left_ear_2_color = Line([-1, ear_length, 0], [0, 0, 0], color=BLUE)
        left_ear_color = VGroup(left_ear_1_color, left_ear_2_color)
        
        right_ear_1_color = Line([1.5, 0, 0], [1, ear_length, 0], color=BLUE)
        right_ear_2_color = Line([1, ear_length, 0], [0, 0, 0], color=BLUE)
        right_ear_color = VGroup(right_ear_1_color, right_ear_2_color)
    
        # self.add(left_ear_color)
        # self.bring_to_back(left_ear_color)
        # self.play(Create(left_ear_color))
        self.play(Transform(left_ear, left_ear_color), Transform(right_ear, right_ear_color))
        self.wait(1)
        
        # on enjoy- transform -- into smile?
        
        ##################
        '''But we don't know the exact set of rules to figure this out.'''
        
        nap_eqn = Text('? * nose_tip + ? * ear_length = nap happy').shift(DOWN)
        self.play(Write(nap_eqn))
        
        ##################
        '''We can also predict how much each cat person enjoys caps by measuring their ear lengths and nose tips, using different weighings of these features than before. But again, we also don't know this formula.'''
        
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        
        self.add(face, left_eye, right_eye, left_ear, right_ear)
        self.add(whisker_1, whisker_2, whisker_3, whisker_4)
        self.add(nose_line_1, nose_line_2, nose_line_3)
        self.bring_to_back(left_ear, right_ear)
        
        thought = ImageMobject('thought.png').move_to([2.2, 1.8,0]).scale(1.5)
        self.add(thought)
        self.wait(2)
        
        ##################
        '''So we're going to have to find what these rules are using a neural network.'''
        
        
        
        ##################
    
        # cat = ImageMobject("cat.png").scale(1.5)
        # self.play(FadeIn(cat))
        
        # face_2 = Line([0,0,0], [0.66,0,0], color = RED, stroke_width=5).shift(LEFT*1.37 + UP*0.2)
        # body_2 = Ellipse(color=BLUE, height=1, width=2.1, stroke_width=5).shift(DOWN*0.1 + RIGHT*0.12)
        # face_box = Rectangle(color=WHITE, height=3, width=5, stroke_width=5)
        
        # self.wait(1)        
        # self.play(FadeIn(face_box))
        # self.wait(1)
        # self.play(GrowFromCenter(face_2))
        # self.wait(1)
        # self.play(GrowFromCenter(body_2))
        # self.wait(3)