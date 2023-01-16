from manim import *

class scene_2_1(Scene):
    def construct(self):
        ##############
        '''To show why neural networks use matrix multiplication, let’s start with an example where in the future, cat people roam the world. '''
        self.wait(2)
        
        ear_length = 1.5  #lowest is 0.5. each +1 is 0.5; largest is 1.5
        nose_tip = 0.5  # each unit of 1 is 0.25. 3 is 0.75, etc
        
        left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0])
        left_ear_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0])
        left_ear = VGroup(left_ear_1, left_ear_2)
        
        right_ear_1 = Line([1.5, 0, 0], [1, ear_length+1.5, 0])
        right_ear_2 = Line([1, ear_length+1.5, 0], [0, 0, 0])
        right_ear = VGroup(right_ear_1, right_ear_2)
                
        face_outline = Circle(radius=1.75, color=WHITE, fill_color=BLACK, fill_opacity=1).move_to([0, 0, 0])
        
        left_eye = Dot(color=WHITE).move_to([-1, 0.5, 0])
        right_eye = Dot(color=WHITE).move_to([1, 0.5, 0])
        
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
                    
        cat_person_1 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy()).scale(0.75).move_to(np.array([-3, 1, 0]))   
        cat_person_1[5].color=PURPLE
        cat_person_1[6].color=PURPLE
        faceBlack = cat_person_1[0].copy()
        faceBlack.color=BLACK
        self.add(faceBlack)
        
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
            
        cat_person_2 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear_2.copy(), right_ear_2.copy(), nose_2.copy(), whiskers.copy()).scale(0.75).move_to(np.array([3, 2, 0]))   
        cat_person_2[5].color=GREEN
        cat_person_2[6].color=GREEN
        faceBlack2 = cat_person_2[0].copy()
        faceBlack2.color=BLACK
        self.add(faceBlack2)
        
        ear_length = 1  #lowest is 0.5. each +1 is 0.5; largest is 1.5
        nose_tip = 0.25  # each unit of 1 is 0.25. 3 is 0.75, etc
        left_ear_1_3 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0])
        left_ear_2_3 = Line([-1, ear_length+1.5, 0], [0, 0, 0])
        left_ear_3 = VGroup(left_ear_1_3, left_ear_2_3)
        right_ear_1_3 = Line([1.5, 0, 0], [1, ear_length+1.5, 0])
        right_ear_2_3 = Line([1, ear_length+1.5, 0], [0, 0, 0])
        right_ear_3 = VGroup(right_ear_1_3, right_ear_2_3)
        nose_line_2_3 = Line([-0.5, 0, 0], [0, nose_tip, 0])
        nose_line_3_3 = Line([0, nose_tip, 0], [0.5, 0, 0])
        nose_3 = VGroup(nose_line_1, nose_line_2_3, nose_line_3_3)
        left_ear_3.z_index=1
        right_ear_3.z_index=1
        for nl in nose_3:
            nl.z_index=3
            
        cat_person_3 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear_3.copy(), right_ear_3.copy(), nose_3.copy(), whiskers.copy()).scale(0.75).move_to(np.array([-1, -2, 0]))   
        faceBlack3 = cat_person_3[0].copy()
        faceBlack3.color=BLACK
        self.add(faceBlack3)
        
        self.play(FadeIn(cat_person_1))
        self.wait(1.5)
        self.play(FadeIn(cat_person_2))
        self.wait(1.5)
        self.play(FadeIn(cat_person_3))
        
        ##############
        '''Some evidence suggests that how much a cat person enjoys naps...'''
               
        left_eye = ArcBetweenPoints([-0.3, -0.75,0], [0.3, -0.75,0]).rotate(180*DEGREES).move_to([-1, 0.5, 0])
        right_eye = ArcBetweenPoints([-0.3, -0.75,0], [0.3, -0.75,0]).rotate(180*DEGREES).move_to([1, 0.5, 0])
        left_eye.z_index=3
        right_eye.z_index=3
        
        mouth_smile = ArcBetweenPoints([-0.5, -0.75,0], [0.5, -0.75,0])
                              
        cat_person_zzz = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear_3.copy(), right_ear_3.copy(), nose_3.copy(), whiskers.copy())
        
        zzz = Text("...zZz...", font_size = 40, color=WHITE).move_to([2.2, 1.8,0])
        
        self.play(FadeOut(cat_person_1, cat_person_2), Transform(cat_person_3, cat_person_zzz))
        self.remove(faceBlack, faceBlack2, faceBlack3)
        
        self.play(Write(zzz))
        self.wait(1)
        self.play(Unwrite(zzz))
        
        ###################
        ### Highlight nose
        '''... can be predicted by measuring how far away their nose tips are from the center of their face. We call this measurement, 'Nose tip'.'''
                
        self.wait(1.5)
        
        nose_line_1_color = Line([-0.5, 0, 0], [0.5, 0, 0], color=RED)
        nose_line_2_color = Line([-0.5, 0, 0], [0, nose_tip, 0], color=RED)
        nose_line_3_color = Line([0, nose_tip, 0], [0.5, 0, 0], color=RED)
        
        self.play(Transform(cat_person_zzz[5][0], nose_line_1_color), Transform(cat_person_zzz[5][1], nose_line_2_color), Transform(cat_person_zzz[5][2], nose_line_3_color), Write(zzz))
        
        self.wait(3)
        
        nap_eqn = Text('Nose Tip').shift(DOWN*2.5)
        self.play(Write(nap_eqn), Unwrite(zzz))        
               
        ###################
        #'''For example, many cat people with long nose tips are said to enjoy naps. It's always the case that the more a cat person smiles when napping, the more they enjoy it. '''
        
        self.play(FadeOut(nap_eqn))  
        self.wait(1)
        
        nose_tip = 0.75
        nose_line_2_4 = Line([-0.5, 0, 0], [0, nose_tip, 0], color=RED)
        nose_line_3_4 = Line([0, nose_tip, 0], [0.5, 0, 0], color=RED)
        cat_person_zzz[5][1].z_index = 5
        cat_person_zzz[5][2].z_index = 5
        nose_line_2_4.z_index = 5
        nose_line_3_4.z_index = 5
        
        # do this else leaves orig white lines behind
        noseBlack = cat_person_zzz[5][1].copy()
        noseBlack.color=BLACK
        noseBlack.z_index = 4
        self.add(noseBlack)
        noseBlack2 = cat_person_zzz[5][2].copy()
        noseBlack2.color=BLACK
        noseBlack2.z_index = 4
        self.add(noseBlack2)
        # self.remove(cat_person_zzz[5][1], cat_person_zzz[5][2])
        # self.remove(nose_line_2_color, nose_line_3_color)
        # self.add(nose_line_2_color, nose_line_3_color)
        # self.play(Transform(nose_line_2_color, nose_line_2_4), Transform(nose_line_3_color, nose_line_3_4))
        self.play(Transform(cat_person_zzz[5][1], nose_line_2_4), Transform(cat_person_zzz[5][2], nose_line_3_4))
        self.wait(3)
        
        mouth_smile = ArcBetweenPoints([-0.5, -0.75,0], [0.5, -0.75,0])
        mouth_smile.z_index=4
        self.play(GrowFromCenter(mouth_smile))
        self.wait(2)
        
        ###################
        #'''We measure how much they enjoy naps using a metric called 'Nap Smile', or just shortened to 'Naps'. '''
        
        nap_eqn = Text('Nap Smile').shift(DOWN*2.5)
        self.play(Write(nap_eqn))
        self.wait(1)
        nap_eqn2 = Text('Naps').shift(DOWN*2.5)
        self.play(Transform(nap_eqn, nap_eqn2))
        self.wait(2)
        
        self.wait(4)
        
        ####################
        #'''But we don't know just how proportional nose tips are to enjoying naps. For example, how big of a Nap Smile does a cat person with a nose of size 3 have, compared to a cat person with a nose of size 2? A slightly bigger smile, or a much bigger smile? '''
        #
        ## self.play(*[FadeOut(mob)for mob in self.mobjects])
        #
        ## cat_person_1.scale(1).move_to(np.array([-2, 0, 0]))   
        ## cat_person_2.scale(1).move_to(np.array([2, 0, 0]))   
        
        