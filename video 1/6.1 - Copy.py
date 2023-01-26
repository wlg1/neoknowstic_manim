from manim import *
import pdb

class scene_6_1(Scene):
    def construct(self):
        ####################
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
        
        cat_person_zzz = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), mouth_smile.copy(), zzz.copy(), box.copy()).scale(0.3)  
        
        nap_space = NumberLine(
            x_range=[-1, 4, 1],
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        ).scale(2)
        
        ####################
        '''First, let's see how to predict Nap Smile using Ear Length. We notice that the longer a cat person's ears are, the more they enjoy naps. But relatively speaking, ear length doesn't have as much impact on nap enjoyment as nose tip does. For example, a cat person with an ear length of 2 would only enjoy naps by 0.5 units more than a cat person with an length of 1. '''

        cat_person_1 = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.4).shift(LEFT*4+UP*1.5)
        faceBlack = cat_person_1[0].copy()
        faceBlack.color=BLACK
        faceBlack.z_index = 2
        self.add(faceBlack)
        
        into = Arrow([0,0,0],[1,0,0]).scale(4).shift(LEFT*0.5+UP*1.5)

        mouth_smile_2 = mouth_smile.copy().scale(0.5)
                
        cat_person_1_zzz = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), mouth_smile_2.copy(), zzz.copy(), box.copy()).scale(0.4).shift(RIGHT*4+UP*1.5)
        faceBlack = cat_person_1_zzz[0].copy()
        faceBlack.color=BLACK
        faceBlack.z_index = 2
        self.add(faceBlack)
                        
        text_1 = Text("1").shift(LEFT*2+UP*1.5)
        text_2 = Text("0.5").shift(RIGHT*2+UP*1.5)
        
        ###########

        text_3 = Text("2").shift(LEFT*2+DOWN*1.5)
        text_4 = Text("1").shift(RIGHT*2+DOWN*1.5)
        
        ear_length = 1
        left_ear_1_2 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0])
        left_ear_2_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0])
        left_ear_2 = VGroup(left_ear_1_2, left_ear_2_2)        
        right_ear_1_2 = Line([1.5, 0, 0], [1, ear_length+1.5, 0])
        right_ear_2_2 = Line([1, ear_length+1.5, 0], [0, 0, 0])
        right_ear_2 = VGroup(right_ear_1_2, right_ear_2_2)
        left_ear_2.z_index=1
        right_ear_2.z_index=1
        for er in left_ear_2:
            er.stroke_width=2
        for er in right_ear_2:
            er.stroke_width=2
            
        cat_person_2 = VGroup(face_outline.copy(), left_ear_2.copy(), right_ear_2.copy(), box.copy()).scale(0.4).shift(LEFT*4+DOWN*1.5)
        faceBlack = cat_person_2[0].copy()
        faceBlack.color=BLACK
        faceBlack.z_index = 2
        self.add(faceBlack)
        
        into_2 = Arrow([0,0,0],[1,0,0]).scale(4).shift(LEFT*0.5+DOWN*1.5)
        
        mouth_smile_4 = mouth_smile.copy().scale(1.5)
        
        cat_person_2_zzz = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear_2.copy(), right_ear_2.copy(), nose.copy(), whiskers.copy(), mouth_smile_4.copy(), zzz.copy(), box.copy()).scale(0.4).shift(RIGHT*4+DOWN*1.5)
        faceBlack = cat_person_2_zzz[0].copy()
        faceBlack.color=BLACK
        faceBlack.z_index = 2
        self.add(faceBlack)
               
        #########
        
        self.play(FadeIn(cat_person_1))
        self.play(FadeIn(into))
        self.play(FadeIn(cat_person_1_zzz))
        
        self.play(FadeIn(cat_person_2))
        self.play(FadeIn(into_2))
        self.play(FadeIn(cat_person_2_zzz))

        self.wait(2)

        self.play(FadeIn(text_3, text_4))
        self.play(FadeIn(text_2, text_1))
                    
        self.wait(2)
        
        ########################################
        '''So we get the equation: (0.5) * ear = nap'''
        
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        eqn_1 = Tex("(0.5) * (1 Ear) = 0.5 Nap", font_size=53)
        self.play(FadeIn(eqn_1))

        self.wait(1)

        # eqn_w = Tex("W * (0.5 Ear) = W*(0.5) Nap", font_size=53)
        # self.play(Transform(eqn_1, eqn_w))

        # self.wait(2)
        
        ########################################
        '''And visually speaking, this means that for every one unit of nose tip, there are two units of Nap Smile.'''
        
        ear_space = NumberLine(
            x_range=[0, 4, 1],
            include_numbers=True,
            label_direction=UP,
        ).scale(2).shift(UP*2+LEFT)
        
        nap_space = NumberLine(
            x_range=[0, 4, 1],
            include_numbers=True,
            label_direction=DOWN,
        ).scale(2).shift(DOWN*2+LEFT)
        
        earName = Text("Ear").shift(UP*2+RIGHT*5)
        napName = Text("Nap").shift(DOWN*2+RIGHT*5)
        
        eqn_1.generate_target()
        eqn_1.target.shift(RIGHT*3.5)      
        weight_1 = Tex("0.5 * ", font_size=53).move_to(ear_space.number_to_point(1)).shift(DOWN*1.5)
        
        eqn_1_copy = eqn_1.copy()
        self.play(MoveToTarget(eqn_1), GrowFromPoint(ear_space, eqn_1), GrowFromPoint(nap_space, eqn_1), Transform(eqn_1_copy, weight_1), FadeIn(earName, napName))
        
        ##################
        # convert ear to nap
        
        ear_group_1 = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.3) 
        
        ear_unit_1 = Line(ear_space.number_to_point(0), ear_space.number_to_point(1), stroke_width=10, color=BLUE)
        ear_group_1.move_to(ear_space.number_to_point(1))  
        
        self.play(GrowFromPoint(ear_unit_1, ear_space.number_to_point(0)), FadeIn(ear_group_1))
        
        # move and connect from ear space to middle
                
        # copy on orig ear space
        ear_unit_1_copy = ear_unit_1.copy()
        ear_group_1_copy = ear_group_1.copy()
        
        # in middle
        ear_unit_2 = Line(ear_space.number_to_point(0), ear_space.number_to_point(0.5), stroke_width=10, color='#ADD8E6').shift(DOWN*1.5)
        ear_group_2 = ear_group_1.copy().move_to(ear_space.number_to_point(0.5)).shift(DOWN*1.5)
        
        #conns down
        ear_dot = Dot(ear_space.number_to_point(1), radius=0.01)
        mid_dot = Dot(ear_space.number_to_point(0.5), radius=0.01).shift(DOWN*1.5) #use this instead of ear_unit_2 b/c ear_unit_2's center not small enough
        conn_1 = Line(ear_dot, mid_dot.get_center())
        
        self.play(Transform(ear_unit_1_copy, ear_unit_2), Transform(ear_group_1_copy, ear_group_2), Transform(eqn_1_copy, ear_unit_2), GrowFromPoint(conn_1, ear_space.number_to_point(1)))
        self.add(mid_dot)
        
        self.wait(1)
                
        # move and connect from middle to nap space        
        ear_group_2_b = ear_group_1.copy().move_to(nap_space.number_to_point(0.5))
        ear_unit_2_b = Line(nap_space.number_to_point(0), nap_space.number_to_point(0.5), stroke_width=10, color='#ADD8E6')
        nap_dot = Dot(nap_space.number_to_point(0.5), radius=0.01)
        conn_2 = Line(mid_dot, nap_dot)
        self.remove(weight_1, eqn_1_copy) #else will leave behind
        self.play(Transform(ear_unit_1_copy, ear_unit_2_b), Transform(ear_group_1_copy, ear_group_2_b), GrowFromPoint(conn_2, ear_group_2))
        
        self.wait(1)
        weight_line = Line(ear_dot, nap_dot)
        both_conns = VGroup(conn_1, conn_2)
        self.remove(mid_dot)
        self.play(Transform(both_conns, weight_line))
        
        self.wait(1)

        ##################

        # ear_nose_objs = VGroup(eqn_1, ear_space, nap_space, earName, napName, ear_unit_1, ear_group_1, ear_unit_1_copy, ear_group_1_copy, both_conns)
                
        # # ear_nose_objs_top = ear_nose_objs.scale(0.3)

        # self.play(ScaleInPlace(ear_nose_objs, 0.5))

        # nose_group_1 = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.3) 
        
        # # nose_group_1 = VGroup(face_outline.copy(), nose.copy()).scale(0.3)  
        # nose_unit_1 = Line(nose_space.number_to_point(0), nose_space.number_to_point(1), stroke_width=10, color=RED)
        # nose_group_1.move_to(nose_space.number_to_point(1))  

        # nose_space = NumberLine(
        #     x_range=[0, 4, 1],
        #     include_numbers=True,
        #     label_direction=UP,
        # ).scale(1).shift(DOWN*2+LEFT)