from manim import *

class scene_2_2(Scene):
    def construct(self):
        ##############        
        ear_length = 1.5  #lowest is 0.5. each +1 is 0.5; largest is 1.5
        nose_tip = 0.5  # each unit of 1 is 0.25. 3 is 0.75, etc
        
        left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0])
        left_ear_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0])
        left_ear = VGroup(left_ear_1, left_ear_2)
        
        right_ear_1 = Line([1.5, 0, 0], [1, ear_length+1.5, 0])
        right_ear_2 = Line([1, ear_length+1.5, 0], [0, 0, 0])
        right_ear = VGroup(right_ear_1, right_ear_2)
                
        face_outline = Circle(radius=1.75, color=WHITE, fill_color=BLACK, fill_opacity=1).move_to([0, 0, 0])
        
        # left_eye = Dot(color=WHITE).move_to([-1, 0.5, 0])
        # right_eye = Dot(color=WHITE).move_to([1, 0.5, 0])
        left_eye = ArcBetweenPoints([-0.3, -0.75,0], [0.3, -0.75,0]).rotate(180*DEGREES).move_to([-1, 0.5, 0])
        right_eye = ArcBetweenPoints([-0.3, -0.75,0], [0.3, -0.75,0]).rotate(180*DEGREES).move_to([1, 0.5, 0])
        
        nose_line_1 = Line([-0.5, 0, 0], [0.5, 0, 0])
        nose_line_2 = Line([-0.5, 0, 0], [0, nose_tip, 0])
        nose_line_3 = Line([0, nose_tip, 0], [0.5, 0, 0])
        nose = VGroup(nose_line_1, nose_line_2, nose_line_3)
        
        whisker_1 = Line([-1, -0.3, 0], [-2.3, -0.5, 0]) # left down
        whisker_2 = Line([-1, -0.3, 0], [-2.3, 0.5, 0]) # left up
        whisker_3 = Line([-1, -0.3, 0], [-2.3, 0, 0]) # left middle
        whisker_4 = Line([1, -0.3, 0], [2.3, -0.5, 0]) # right down
        whisker_5 = Line([1, -0.3, 0], [2.3, 0.5, 0])  # right up
        whisker_6 = Line([1, -0.3, 0], [2.3, 0, 0]) # r mid                 
        whiskers = VGroup(whisker_1, whisker_2, whisker_3, whisker_4, whisker_5, whisker_6)          
        
        mouth = Ellipse(width=0.4, height=0.8, color=WHITE).move_to([0, -0.75, 0])
               
        left_ear.z_index=1
        right_ear.z_index=1
               
        face_outline.z_index=3
        left_eye.z_index=3
        right_eye.z_index=3
                
        for nl in nose:
            nl.z_index=3
        
        for whisk in whiskers:
            whisk.z_index=3
        
        mouth_smile = ArcBetweenPoints([-0.5, -0.75,0], [0.5, -0.75,0])
        mouth_smile2 = ArcBetweenPoints([-0.5, -0.75,0], [0.5, -0.75,0])
        mouth_smile.z_index=3
        mouth_smile2.z_index=3
        
        cat_person_1 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), mouth_smile).scale(0.75)
        cat_person_1[5].color=PURPLE
        cat_person_1[6].color=PURPLE
        
        ear_length = 0.5  #lowest is 0.5. each +1 is 0.5; largest is 1.5
        nose_tip = 0.75  # each unit of 1 is 0.25. 3 is 0.75, etc
        left_ear_1_2 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0])
        left_ear_2_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0])
        left_ear_2 = VGroup(left_ear_1_2, left_ear_2_2)
        right_ear_1_2 = Line([1.5, 0, 0], [1, ear_length+1.5, 0])
        right_ear_2_2 = Line([1, ear_length+1.5, 0], [0, 0, 0])
        right_ear_2 = VGroup(right_ear_1_2, right_ear_2_2)
        nose_line_2_2 = Line([-0.5, 0, 0], [0, nose_tip, 0])
        nose_line_3_2 = Line([0, nose_tip, 0], [0.5, 0, 0])
        nose_2 = VGroup(nose_line_1, nose_line_2_2, nose_line_3_2)
        left_ear_2.z_index=1
        right_ear_2.z_index=1
        for nl in nose_2:
            nl.z_index=3
            
        cat_person_2 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear_2.copy(), right_ear_2.copy(), nose_2.copy(), whiskers.copy(), mouth_smile2).scale(0.75)  
        cat_person_2[5].color=GREEN
        cat_person_2[6].color=GREEN
        
        ####################
        '''But we don't know just how proportional nose tips are to enjoying naps. For example, how big of a Nap Smile does a cat person with a nose of size 3 have, compared to a cat person with a nose of size 2? A slightly bigger smile, or a much bigger smile? '''
        
        self.wait(3)
        
        
        cat_person_1.scale(1).move_to(np.array([-2.5, 0.25, 0])) 
        faceBlack = cat_person_1[0].copy()
        faceBlack.color=BLACK
        self.add(faceBlack)        
        cat_person_2.scale(1).move_to(np.array([2.5, 0, 0]))  
        faceBlack3 = cat_person_2[0].copy()
        faceBlack3.color=BLACK
        self.add(faceBlack3)
        
        # self.play(FadeIn(cat_person_1, cat_person_2))
        self.play(FadeIn(cat_person_2))
        self.wait(2)
        self.play(FadeIn(cat_person_1))
        
        self.wait(2)
        
        mouth_smile_big = mouth_smile2.copy().scale(1.5) # +scale of 0.5 is 1 unit
        mouth_smile_bigger = mouth_smile2.copy().scale(2.5)
        
        self.play(Transform(mouth_smile2, mouth_smile_big))
        self.play(Transform(mouth_smile2, mouth_smile_bigger))
        self.wait(1)
        