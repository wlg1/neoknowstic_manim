from manim import *

class ManimScene(Scene):
    def construct(self):
    
        ###### Make the cat person ############
        ear_length = 2.75  #lowest is 2. each +1 is 0.25
        nose_tip = 0.5  # each unit of 1 is 0.25. 3 is 0.75, etc
        
        #############
        left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length, 0])
        left_ear_2 = Line([-1, ear_length, 0], [0, 0, 0])
        left_ear = VGroup(left_ear_1, left_ear_2)
        
        right_ear_1 = Line([1.5, 0, 0], [1, ear_length, 0])
        right_ear_2 = Line([1, ear_length, 0], [0, 0, 0])
        right_ear = VGroup(right_ear_1, right_ear_2)
                
        face = Circle(radius=1.75, color=WHITE, fill_color=BLACK, fill_opacity=1).move_to([0, 0, 0])
        
        # left_eye = Dot(color=WHITE).move_to([-1, 0.5, 0])
        # right_eye = Dot(color=WHITE).move_to([1, 0.5, 0])
        left_eye = ArcBetweenPoints([-0.3, -0.75,0], [0.3, -0.75,0]).rotate(180*DEGREES).move_to([-1, 0.5, 0])
        right_eye = ArcBetweenPoints([-0.3, -0.75,0], [0.3, -0.75,0]).rotate(180*DEGREES).move_to([1, 0.5, 0])
        
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
        
        self.play(Write(zzz))
        self.wait(1)
        self.play(Unwrite(zzz))
        
        # for i in range(3):
            # self.play(FadeIn(zzz, shift=RIGHT))
            # self.play(GrowFromPoint(zzz, [2.2, 1.8,0]))
            # self.play(FadeOut(zzz, shift=LEFT))