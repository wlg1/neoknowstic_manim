from manim import *

class CatFace(Scene):
    def construct(self):    
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
        
        left_eye = Dot(color=WHITE).move_to([-1, 0.5, 0])
        right_eye = Dot(color=WHITE).move_to([1, 0.5, 0])
        
        nose_line_1 = Line([-0.5, 0, 0], [0.5, 0, 0])
        nose_line_2 = Line([-0.5, 0, 0], [0, nose_tip, 0])
        nose_line_3 = Line([0, nose_tip, 0], [0.5, 0, 0])
                
        whisker_1 = Line([-1, -0.3, 0], [-2, -0.5, 0]) # left down
        whisker_2 = Line([-1, -0.3, 0], [-2, 0.5, 0]) # left up
        whisker_3 = Line([1, -0.3, 0], [2, -0.5, 0]) # right down
        whisker_4 = Line([1, -0.3, 0], [2, 0.5, 0])  # right up
                                
        self.add(face, left_eye, right_eye, left_ear, right_ear)
        self.add(whisker_1, whisker_2, whisker_3, whisker_4)
        self.add(nose_line_1, nose_line_2, nose_line_3)
        self.bring_to_back(left_ear, right_ear)
        
        
        ############################
        # left_ear_1 = Line([0, 0, 0], [0.5, ear_length, 0])
        # left_ear_1 = Line([0.5, 0, 0], [0.5, ear_length, 0])
        # left_ear_2 = Line([0.5, ear_length, 0], [1, 0, 0])
        # left_ear = VGroup(left_ear_1, left_ear_2).move_to([-1, 2, 0])
        
        # nose_down = True  # if true, tip is facing down (negatives)
        # nose = Polygon(np.array([0, 0, 0]), np.array([1, 0, 0]), np.array([0.5, nose_height, 0]), color=WHITE)
        # nose.move_to([0, 0, 0])
        # if nose_down:
            # nose.rotate(180*DEGREES)