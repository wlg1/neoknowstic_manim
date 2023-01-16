from manim import *
import pdb

class scene_2_3(Scene):
    def construct(self):
        '''We're going to have to figure this out by using a neural network that takes in a cat person's nose tip as input, and predicts their nap enjoyment level.'''
    
        inNode_1 = Circle(radius=0.5, color=WHITE, fill_color=WHITE, fill_opacity=1, stroke_width=1).move_to([-2, 0, 0])
        outNode = Circle(radius=0.5, color=WHITE, fill_color=WHITE, fill_opacity=1, stroke_width=1).move_to([2, 0, 0])
        
        conn_1 = Line([-2, 0, 0], [2, 0, 0])
        
        self.play(FadeIn(inNode_1, outNode))
        self.play(FadeIn(conn_1))
        
        ##################################################
        ear_length = 1  #lowest is 0.5. each +1 is 0.5; largest is 1.5
        nose_tip = -0.5  # each unit of 1 is 0.25. 3 is 0.75, etc
        
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
        
        # faceBlack3 = face_outline.copy()
        # faceBlack3.color=BLACK
        # faceBlack3.z_index = 2
        # self.add(faceBlack3)
        
        cat_face = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy()).scale(0.3).move_to([-3.5, 0, 0])
        # self.play(FadeIn(cat_face))
        
        # self.wait(1.5)
        
        nose_face = VGroup(face_outline.copy(), nose.copy()).scale(0.3).move_to(np.array([-3, 1, 0])).move_to([-3.5, 0, 0])   
        
        # self.play(FadeOut(cat_face[1], cat_face[2], cat_face[3], cat_face[4], cat_face[6]))
        # self.play(Transform(cat_face, nose_face))
        
        # self.add(nose_face)
        # self.play(FadeOut(cat_face))
        
        self.play(FadeIn(nose_face))
        
        # self.wait(1)
        
        conn_1_a = Line([-2, 0, 0], [2, 0, 0], stroke_width=10)
        self.play(Transform(nose_face, conn_1_a))
                
        # self.wait(1)
                               
        zzz = Text("...zZz...", font_size = 40, color=WHITE).move_to([2.2, 1.8,0])
        cat_person_zzz = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), zzz.copy() )
        cat_person_zzz.scale(0.3).move_to([3.5, 0, 0])  

        # cat_person_zzz[3].z_index = -1
        # cat_person_zzz[4].z_index = -1
        
        # self.play(Transform(conn_1_a, cat_person_zzz))
        # self.add(Line([-2, 0, 0], [2, 0, 0]))
        self.play(Transform(conn_1, cat_person_zzz[0]), FadeIn(cat_person_zzz, shift=RIGHT))  # from left to RIGHT
        
        # for i in range(0,2):
        zzz_2 = cat_person_zzz[-1].copy()
        self.play(Unwrite(cat_person_zzz[-1]))
        self.wait(1)
        self.play(Write(zzz_2))
        
        # self.play(Unwrite(cat_person_zzz[-1]))
        # self.wait(0.5)
        # self.play(Write(cat_person_zzz[-1]))
        