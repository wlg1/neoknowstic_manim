from manim import *
import pdb

class scene_5_1(Scene):
    def construct(self):                
        ear_length = 0.5  #lowest is 0.5. each +1 is 0.5; largest is 1.5
        nose_tip = 0.3  # each unit of 1 is 0.25. 3 is 0.75, etc
        
        left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0])
        left_ear_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0])
        left_ear = VGroup(left_ear_1, left_ear_2)
        
        right_ear_1 = Line([1.5, 0, 0], [1, ear_length+1.5, 0])
        right_ear_2 = Line([1, ear_length+1.5, 0], [0, 0, 0])
        right_ear = VGroup(right_ear_1, right_ear_2)
                
        face_outline = Circle(radius=1.75, color=WHITE, fill_color=BLACK, fill_opacity=1, stroke_width=2).move_to([0, 0, 0])
        
        left_eye = Dot(color=WHITE).move_to([-1, 0.5, 0])
        right_eye = Dot(color=WHITE).move_to([1, 0.5, 0])
        left_eye.z_index=3
        right_eye.z_index=3
        
        left_eye_zzz = ArcBetweenPoints([-0.3, -0.75,0], [0.3, -0.75,0], stroke_width=2).rotate(180*DEGREES).move_to([-1, 0.5, 0])
        right_eye_zzz = ArcBetweenPoints([-0.3, -0.75,0], [0.3, -0.75,0], stroke_width=2).rotate(180*DEGREES).move_to([1, 0.5, 0])
        left_eye_zzz.z_index=3
        right_eye_zzz.z_index=3
        
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
        
        left_ear.z_index=1
        right_ear.z_index=1
               
        face_outline.z_index=3
        left_eye.z_index=3
        right_eye.z_index=3
        
        for er in left_ear:
            er.stroke_width=2
        for er in right_ear:
            er.stroke_width=2
            
        for nl in nose:
            nl.z_index=3
            nl.stroke_width=2  #default is 4
        
        for whisk in whiskers:
            whisk.z_index=3
            whisk.stroke_width=2
                   
        mouth_smile = ArcBetweenPoints([-0.5, -0.75,0], [0.5, -0.75,0], stroke_width=2)
        mouth_smile.z_index=3
                
        zzz = Text("...zZz...", font_size = 35, color=WHITE).move_to([2.2, 1.8,0])
        zzz.z_index=3
        
        box = Rectangle(color=BLACK, height=5.7, width=6, stroke_width=1, fill_color=BLACK).shift(UP*0.33)
        box.z_index = -1
        
        ####################
        '''When using our equation to predict nap enjoyment, we find that there's cases where using nose isn't enough. '''
                                
        '''We found that Tom has a nose of 1 unit, yet has a Nap Smile of 2.25, '''                        
        text_1 = Text("1").shift(LEFT*2+UP*1.5)
        text_2 = Text("2.5").shift(RIGHT*2+UP*1.5)
                
        cat_person_1 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), box.copy()).scale(0.4).shift(LEFT*4+UP*1.5)
        faceBlack = cat_person_1[0].copy()
        faceBlack.color=BLACK
        faceBlack.z_index = 2
        self.add(faceBlack)
        self.play(FadeIn(text_1, cat_person_1))
        
        into = Arrow([0,0,0],[1,0,0]).scale(4).shift(LEFT*0.5+UP*1.5)
        self.play(FadeIn(into))
        
        #mouth smile 2.25
        mouth_smile_3 = mouth_smile.copy().scale(1.625) # +scale of 0.5 is 1 unit
                
        cat_person_1_zzz = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), mouth_smile_3.copy(), zzz.copy(), box.copy()).scale(0.4).shift(RIGHT*4+UP*1.5)
        faceBlack = cat_person_1_zzz[0].copy()
        faceBlack.color=BLACK
        faceBlack.z_index = 2
        self.add(faceBlack)
        self.play(FadeIn(text_2, cat_person_1_zzz))
        
        self.wait(2)
                        
        '''while Lauren also has a nose of 1 unit, yet has a Nap Smile of 3.5. '''
        
        text_3 = Text("1").shift(LEFT*2+DOWN*1.5)
        text_4 = Text("3.5").shift(RIGHT*2+DOWN*1.5)
        
        ear_length = 1.5
        left_ear_1_2 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0])
        left_ear_2_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0])
        left_ear_2 = VGroup(left_ear_1_2, left_ear_2_2)
        for nl in left_ear_2:
            nl.z_index=1
            nl.stroke_width=2
        right_ear_1_2 = Line([1.5, 0, 0], [1, ear_length+1.5, 0])
        right_ear_2_2 = Line([1, ear_length+1.5, 0], [0, 0, 0])
        right_ear_2 = VGroup(right_ear_1_2, right_ear_2_2)
        for nl in right_ear_2:
            nl.z_index=1
            nl.stroke_width=2
            
        cat_person_2 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear_2.copy(), right_ear_2.copy(), nose.copy(), whiskers.copy(), box.copy()).scale(0.4).shift(LEFT*4+DOWN*1.5)
        faceBlack = cat_person_2[0].copy()
        faceBlack.color=BLACK
        faceBlack.z_index = 2
        self.add(faceBlack)
        self.play(FadeIn(text_3, cat_person_2))
        
        into_2 = Arrow([0,0,0],[1,0,0]).scale(4).shift(LEFT*0.5+DOWN*1.5)
        self.play(FadeIn(into_2))
        
        #3.5 is 1+(0.5*2 + 0.5/2)
        mouth_smile_4 = mouth_smile.copy().scale(2.25)
        
        cat_person_2_zzz = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear_2.copy(), right_ear_2.copy(), nose.copy(), whiskers.copy(), mouth_smile_4.copy(), zzz.copy(), box.copy()).scale(0.4).shift(RIGHT*4+DOWN*1.5)
        faceBlack = cat_person_2_zzz[0].copy()
        faceBlack.color=BLACK
        faceBlack.z_index = 2
        self.add(faceBlack)
        self.play(FadeIn(text_4, cat_person_2_zzz))
                        
        self.wait(2)
        
        # self.add(text_1, text_2, text_3, text_4, into, into_2, cat_person_1, cat_person_1_zzz, cat_person_2, cat_person_2_zzz)
        
        ####################
        
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        cat_person_1 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), box.copy()).scale(0.7).shift(LEFT*5) 
        faceBlack = cat_person_1[0].copy()
        # faceBlack.color=BLACK
        # faceBlack.z_index = 4
        # self.add(faceBlack)
        # for item in cat_person_1:
            # item.z_index = 5
        # cat_person_1[3].z_index = 3   
        # cat_person_1[4].z_index = 3
        # cat_person_1[-1].z_index = -1
        
        self.play(GrowFromPoint(cat_person_1, cat_person_1.get_center()))
        
        nose_group_1 = VGroup(cat_person_1[0].copy(), cat_person_1[5].copy(), cat_person_1[-1].copy())  
        nose_group_1[0].z_index = 2    
        
        ear_group = VGroup(cat_person_1[0].copy(), cat_person_1[3].copy(), cat_person_1[4].copy(), cat_person_1[-1].copy()) 
        ear_group[0].z_index = 2
        # ear_group = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.7) 
        
        # self.play(FadeIn(nose_box))
        self.add(nose_group_1, ear_group)
              
        nose_group_1.generate_target()
        nose_group_1.target.shift(RIGHT*5)
        self.play(MoveToTarget(nose_group_1))  
              
        ear_group.generate_target()
        ear_group.target.shift(RIGHT*10)
        self.play(MoveToTarget(ear_group))  
        self.wait(2)
        
        ####################
        
        self.play(FadeOut(cat_person_1, nose_group_1))
        self.remove(faceBlack)
        
        ear_group_1 = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.3) 
        # ear_group.copy().scale(0.3)  
        # ear_group_1 = VGroup(cat_person_1[0].copy(), cat_person_1[3].copy(), cat_person_1[4].copy()) .scale(0.3)  
                
        ear_space = NumberLine(
            x_range=[-1, 4, 1],
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        ).scale(2)
        
        ear_group_1.move_to(ear_space.number_to_point(1))
        
        self.play(FadeIn(ear_space), Transform(ear_group, ear_group_1))
        
        earSpaceName = Text('Ear Space', font_size=40).shift(DOWN*2.5)
        self.play(Write(earSpaceName))
        
        self.wait(2)
                
        ####################
        '''Just like with nose tip, we also have an ear length of 1 unit, 2 units, and 3 units'''
        
        self.wait(2)
        
        ear_length = 1
        left_ear_1_2 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0])
        left_ear_2_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0])
        left_ear_2 = VGroup(left_ear_1_2, left_ear_2_2)
        right_ear_1_2 = Line([1.5, 0, 0], [1, ear_length+1.5, 0])
        right_ear_2_2 = Line([1, ear_length+1.5, 0], [0, 0, 0])
        right_ear_2 = VGroup(right_ear_1_2, right_ear_2_2)
        for er in left_ear_2:
            er.z_index=1
            er.stroke_width=2
        for er in right_ear_2:
            er.z_index=1
            er.stroke_width=2
        ear_group_2 = VGroup(face_outline.copy(), left_ear_2.copy(), right_ear_2.copy(), box.copy()).scale(0.3).move_to(ear_space.number_to_point(2))
        
                
        self.play(Transform(ear_group, ear_group_2))
        
        self.wait(2)
        
        ear_length = 1.5
        left_ear_1_3 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0])
        left_ear_2_3 = Line([-1, ear_length+1.5, 0], [0, 0, 0])
        left_ear_3 = VGroup(left_ear_1_3, left_ear_2_3)
        right_ear_1_3 = Line([1.5, 0, 0], [1, ear_length+1.5, 0])
        right_ear_2_3 = Line([1, ear_length+1.5, 0], [0, 0, 0])
        right_ear_3 = VGroup(right_ear_1_3, right_ear_2_3)
        for er in left_ear_3:
            er.z_index=1
            er.stroke_width=2
        for er in right_ear_3:
            er.z_index=1
            er.stroke_width=2
        ear_group_3 = VGroup(face_outline.copy(), left_ear_3.copy(), right_ear_3.copy(), box.copy()).scale(0.3).move_to(ear_space.number_to_point(3))
                
        self.play(Transform(ear_group, ear_group_3))
        
        self.wait(2)
        
        ####################
        
        self.play(FadeIn(ear_group_1, ear_group_2))
        
        self.wait(2)
        
        