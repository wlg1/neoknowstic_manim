from manim import *
import pdb

class scene_3_1(Scene):
    def construct(self):
        ####################
        '''Now, we can also measure Nap Smile along a number line called Nap Space.'''
                
        ear_length = 1.5  #lowest is 0.5. each +1 is 0.5; largest is 1.5
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
        
        # faceBlack = cat_person_1[0].copy()
        # faceBlack.color=BLACK
        # self.add(faceBlack)
        
        box = Rectangle(color=BLACK, height=5.7, width=6, stroke_width=0.01, fill_color=BLACK).shift(UP*0.33)
        box.z_index = 0
        
        cat_person_zzz = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), mouth_smile.copy(), zzz.copy(), box.copy()).scale(0.3)  
        
        nap_space = NumberLine(
            x_range=[-1, 4, 1],
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        ).scale(2)
        
        cat_person_zzz.move_to(nap_space.number_to_point(1))
        
        self.add(nap_space, cat_person_zzz)
                
        self.wait(3)
        
        napSpaceName = Text('Nap Space', font_size=40).shift(DOWN*2.5)
        self.play(Write(napSpaceName))
        self.wait(1)
        
        ####################
        '''Each positive unit measures how big their smile is.'''
                
        mouth_smile_2 = mouth_smile.copy().scale(1.5)
        # cat_person_zzz_2 = cat_person_zzz.copy() #doesn't work b/c scale mouth
        # cat_person_zzz_2[-3] = mouth_smile_2
        cat_person_zzz_2 = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), mouth_smile_2.copy(), zzz.copy(), box.copy()).scale(0.3) 
        cat_person_zzz_2.move_to(nap_space.number_to_point(2))
                
        self.play(Transform(cat_person_zzz, cat_person_zzz_2))
        
        self.wait(1)
        
        mouth_smile_3 = mouth_smile.copy().scale(2)
        cat_person_zzz_3 = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), mouth_smile_3.copy(), zzz.copy(), box.copy()).scale(0.3) 
        cat_person_zzz_3.move_to(nap_space.number_to_point(3))
                
        self.play(Transform(cat_person_zzz, cat_person_zzz_3))
        
        self.wait(1)
        
        ####################
        '''Let's take an example where the longer a cat person's nose tip was, the more they liked naps. '''
                
        #curtain = Square(10, color=BLACK)
        ## self.play(FadeIn(curtain))
        #self.remove(*[mob for mob in self.mobjects])
        faceBlack = cat_person_zzz[0].copy()
        faceBlack.color=BLACK
        faceBlack.z_index = 2
        self.add(faceBlack)
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != faceBlack])
        self.remove(faceBlack)
        
        cat_person_1 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), box.copy()).scale(0.4).shift(LEFT*4+UP*1.5)
        faceBlack = cat_person_1[0].copy()
        faceBlack.color=BLACK
        faceBlack.z_index = 2
        self.add(faceBlack)
        self.play(FadeIn(cat_person_1))
        
        into = Arrow([0,0,0],[1,0,0]).scale(4).shift(LEFT*0.5+UP*1.5)
        self.play(FadeIn(into))
                
        cat_person_1_zzz = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), mouth_smile_2.copy(), zzz.copy(), box.copy()).scale(0.4).shift(RIGHT*4+UP*1.5)
        faceBlack = cat_person_1_zzz[0].copy()
        faceBlack.color=BLACK
        faceBlack.z_index = 2
        self.add(faceBlack)
        self.play(FadeIn(cat_person_1_zzz))
        
        self.wait(1)
                
        '''A cat person with a nose tip of 1 unit had 2 Nap Smile units,'''        
                
        text_1 = Text("1").shift(LEFT*2+UP*1.5)
        self.play(FadeIn(text_1))
        self.wait(1)
        text_2 = Text("2").shift(RIGHT*2+UP*1.5)
        self.play(FadeIn(text_2))
        
        self.wait(1)
        
        '''a cat person with 2 nose tip units had 4, and so forth.'''
        
        text_3 = Text("2").shift(LEFT*2+DOWN*1.5)
        text_4 = Text("4").shift(RIGHT*2+DOWN*1.5)
        
        nose_tip = 0.6
        nose_line_2_2 = Line([-0.5, 0, 0], [0, nose_tip, 0])
        nose_line_3_2 = Line([0, nose_tip, 0], [0.5, 0, 0])
        nose_2 = VGroup(nose_line_1, nose_line_2_2, nose_line_3_2)
        for nl in nose_2:
            nl.z_index=3
            nl.stroke_width=2
            
        cat_person_2 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear.copy(), right_ear.copy(), nose_2.copy(), whiskers.copy(), box.copy()).scale(0.4).shift(LEFT*4+DOWN*1.5)
        faceBlack = cat_person_2[0].copy()
        faceBlack.color=BLACK
        faceBlack.z_index = 2
        self.add(faceBlack)
        self.play(FadeIn(text_3, cat_person_2))
        
        into_2 = Arrow([0,0,0],[1,0,0]).scale(4).shift(LEFT*0.5+DOWN*1.5)
        self.play(FadeIn(into_2))
        
        mouth_smile_4 = mouth_smile.copy().scale(2.5)
        
        cat_person_2_zzz = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear.copy(), right_ear.copy(), nose_2.copy(), whiskers.copy(), mouth_smile_4.copy(), zzz.copy(), box.copy()).scale(0.4).shift(RIGHT*4+DOWN*1.5)
        faceBlack = cat_person_2_zzz[0].copy()
        faceBlack.color=BLACK
        faceBlack.z_index = 2
        self.add(faceBlack)
        self.play(FadeIn(text_4, cat_person_2_zzz))
                        
        self.wait(2)
        
        ####################
        '''We notice a pattern here that's somewhat like unit conversion. For instance, for every 1 meter, there are 3.28 feet. So if an person is 2 meters tall, they're also 6.56 feet tall.'''
        
        
        
        
        