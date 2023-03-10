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
        
        box = Rectangle(color=BLACK, height=5.7, width=6, stroke_width=0.01, fill_color=BLACK).shift(UP*0.33)
        box.z_index = -2
                
        ####################
        '''First, let's see how to predict Nap Smile using Ear Length. We notice that the longer a cat person's ears are, the more they enjoy naps. But relatively speaking, ear length doesn't have as much impact on nap enjoyment as nose tip does. For example, a cat person with an ear length of 2 would only enjoy naps by 0.75 units more than a cat person with an length of 1. '''

        cat_person_1 = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.4).shift(LEFT*4+UP*1.5)
        faceBlack_0 = cat_person_1[0].copy()
        faceBlack_0.color=BLACK
        faceBlack_0.z_index = 2
        self.add(faceBlack_0)
        
        into = Arrow([0,0,0],[1,0,0]).scale(4).shift(LEFT*0.5+UP*1.5)

        mouth_smile_2 = mouth_smile.copy().scale(0.7)
                
        cat_person_1_zzz = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), mouth_smile_2.copy(), zzz.copy(), box.copy()).scale(0.4).shift(RIGHT*4+UP*1.5)
        faceBlack_1 = cat_person_1_zzz[0].copy()
        faceBlack_1.color=BLACK
        faceBlack_1.z_index = 2
        self.add(faceBlack_1)
                        
        text_1 = Text("1").shift(LEFT*2+UP*1.5)
        text_2 = Text("0.75").shift(RIGHT*2+UP*1.5)
        
        ###########

        text_3 = Text("2").shift(LEFT*2+DOWN*1.5)
        text_4 = Text("1.5").shift(RIGHT*2+DOWN*1.5)
        
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
        
        mouth_smile_4 = mouth_smile.copy().scale(1.25)
        
        cat_person_2_zzz = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear_2.copy(), right_ear_2.copy(), nose.copy(), whiskers.copy(), mouth_smile_4.copy(), zzz.copy(), box.copy()).scale(0.4).shift(RIGHT*4+DOWN*1.5)
        faceBlack_2 = cat_person_2_zzz[0].copy()
        faceBlack_2.color=BLACK
        faceBlack_2.z_index = 2
        self.add(faceBlack_2)
               
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
        '''So we get the equation: (0.75) * ear = nap'''
        
        self.play(*[FadeOut(mob)for mob in [text_1, text_2, text_3, text_4, into, into_2]], *[ShrinkToCenter(mob)for mob in [cat_person_1, cat_person_2, cat_person_1_zzz, cat_person_2_zzz, faceBlack, faceBlack_2, faceBlack_0, faceBlack_1]])
                
        eqn_1 = MathTex(r"0.75 \ \frac{Nap}{Ear} * (1 \ Ear) = 0.75 \ Nap", font_size=45, tex_to_color_map={
            "(1 \ Ear)": BLUE
        })
        self.play(FadeIn(eqn_1))

        self.wait(2)

        # eqn_w = Tex("W * (0.5 Ear) = W*(0.5) Nap", font_size=45)
        # self.play(Transform(eqn_1, eqn_w))

        # self.wait(2)
        
        ########################################
        '''The Data Measurement at point 1 in ear is sent to point 0.5 in Nap, '''
        
        ear_space = NumberLine(
            x_range=[0, 5, 1],
            include_numbers=True,
            label_direction=UP,
        ).scale(1.2).shift(UP*2.5+LEFT*1.6)
        
        nap_space = NumberLine(
            x_range=[0, 5, 1],
            include_numbers=True,
            label_direction=DOWN,
        ).scale(1.2).shift(LEFT*1.6)
        
        earName = Text("Ear").shift(UP*2.5+RIGHT*4.2).scale(0.75)
        napName = Text("Nap").shift(RIGHT*4.2).scale(0.75)
        
        eqn_1_top = eqn_1.copy() 
        eqn_1_top.shift(UP*1.5+RIGHT*3.7).scale(0.75)
        weight_1 = Tex("0.75 * ", font_size=45).move_to(ear_space.number_to_point(1)).shift(DOWN*1).scale(0.75)
        
        eqn_1_copy = eqn_1.copy()
        self.play(Transform(eqn_1, eqn_1_top), GrowFromPoint(ear_space, eqn_1), GrowFromPoint(nap_space, eqn_1), Transform(eqn_1_copy, weight_1), FadeIn(earName, napName))
        
        self.wait(2)

        ##################
        # convert ear to nap
        
        ear_group_1 = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.2).move_to(ear_space.number_to_point(1)).shift(UP*0.2)   
        
        # ear_unit_1 = Line(ear_space.number_to_point(0), ear_space.number_to_point(1), stroke_width=10, color=BLUE)
        ear_vec_line = Line(ear_space.number_to_point(0), ear_space.number_to_point(0.95), color=BLUE, fill_opacity=0.9)
        ear_vec_line.z_index = 4
        ear_vec_tip = Triangle(fill_color=BLUE, fill_opacity=0.9, color=BLUE).scale(0.07).rotate(-90*DEGREES).move_to(ear_space.number_to_point(0.95))
        ear_vec_tip.z_index = 4
        ear_unit_1 = VGroup(ear_vec_line, ear_vec_tip)
        
        self.play(GrowFromPoint(ear_unit_1, ear_space.number_to_point(0)), GrowFromPoint(ear_group_1, ear_space.number_to_point(0)))
        
        # move and connect from ear space to middle
                
        # copy on orig ear space
        ear_unit_1_copy = ear_unit_1.copy()
        ear_group_1_copy = ear_group_1.copy()
        
        # in middle
        # ear_unit_2 = Line(ear_space.number_to_point(0), ear_space.number_to_point(0.75), stroke_width=10, color='#ADD8E6').shift(DOWN*1)        
        ear_vec_line_2 = Line(ear_space.number_to_point(0), ear_space.number_to_point(0.7), color='#ADD8E6', fill_opacity=0.9)
        ear_vec_line_2.z_index = 5
        ear_vec_tip_2 = Triangle(fill_color='#ADD8E6', fill_opacity=0.9, color='#ADD8E6').scale(0.07).rotate(-90*DEGREES).move_to(ear_space.number_to_point(0.7))
        ear_vec_tip_2.z_index = 5
        ear_unit_2 = VGroup(ear_vec_line_2, ear_vec_tip_2).shift(DOWN*1)   

        ear_group_2 = ear_group_1.copy().move_to(ear_space.number_to_point(0.75)).shift(DOWN*1).shift(UP*0.2)
        
        #conns down
        ear_dot = Dot(ear_space.number_to_point(1), radius=0.01)
        mid_dot = Dot(ear_space.number_to_point(0.75), radius=0.01).shift(DOWN*1) #use this instead of ear_unit_2 b/c ear_unit_2's center not small enough
        conn_1 = Line(ear_dot, mid_dot.get_center())
        
        self.play(Transform(ear_unit_1_copy, ear_unit_2), Transform(ear_group_1_copy, ear_group_2), Transform(eqn_1_copy, ear_unit_2), GrowFromPoint(conn_1, ear_space.number_to_point(1)))
        self.add(mid_dot)
        
        self.wait(2)
                
        # move and connect from middle to nap space        
        ear_group_2_b = ear_group_1.copy().move_to(nap_space.number_to_point(0.75)).shift(UP*0.2)
        # ear_unit_2_b = Line(nap_space.number_to_point(0), nap_space.number_to_point(0.75), stroke_width=10, color='#ADD8E6')
        ear_vec_line_2_b = Line(nap_space.number_to_point(0), nap_space.number_to_point(0.7), color='#ADD8E6', fill_opacity=0.9)
        ear_vec_line_2_b.z_index = 5
        ear_vec_tip_2_b = Triangle(fill_color='#ADD8E6', fill_opacity=0.9, color='#ADD8E6').scale(0.07).rotate(-90*DEGREES).move_to(nap_space.number_to_point(0.7))
        ear_vec_tip_2_b.z_index = 5
        ear_unit_2_b = VGroup(ear_vec_line_2_b, ear_vec_tip_2_b).shift(UP*0.1)

        nap_dot = Dot(nap_space.number_to_point(0.75), radius=0.01).shift(UP*0.2)
        conn_2 = Line(mid_dot, nap_dot)
        self.remove(weight_1, eqn_1_copy) #else will leave behind
        self.play(Transform(ear_unit_1_copy, ear_unit_2_b), Transform(ear_group_1_copy, ear_group_2_b), GrowFromPoint(conn_2, ear_group_2))
        
        self.wait(2)
        weight_line_ear = Line(ear_dot, nap_dot)
        both_conns_ear = VGroup(conn_1, conn_2)
        self.remove(mid_dot)
        self.play(Transform(both_conns_ear, weight_line_ear))
        
        self.wait(2)

        ##################
        # ear_nose_objs = VGroup(eqn_1, ear_space, nap_space, earName, napName, ear_unit_1, ear_group_1, ear_unit_1_copy, ear_group_1_copy, both_conns)  
        # self.play(ScaleInPlace(ear_nose_objs, 0.5))
        ##################
        '''just like how the Data Measurement at point 1 in nose was sent to point 2 in Nap.'''

        eqn_2 = MathTex(r"2 \ \frac{Nap}{Nose} * (1 \ Nose) = 2 \ Nap", font_size=45, tex_to_color_map={
            "(1 \ Nose)": RED
        }).shift(DOWN*1.5+RIGHT*3.7).scale(0.75)
        self.play(FadeIn(eqn_2))

        nose_space = NumberLine(
            x_range=[0, 5, 1],
            include_numbers=True,
            label_direction=DOWN,
        ).scale(1.2).shift(DOWN*2.5+LEFT*1.6)

        noseName = Text("Nose").shift(DOWN*2.5+RIGHT*4.2).scale(0.75)
        
        weight_2 = Tex("2 * ", font_size=45).move_to(nose_space.number_to_point(1)).shift(UP*1).scale(0.75)
        
        self.play(GrowFromPoint(nose_space, eqn_2), GrowFromPoint(weight_2, eqn_2), FadeIn(noseName))
        
        self.wait(2)

        nose_group_1 = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.2).move_to(nose_space.number_to_point(1)).shift(UP*0.2)     

        # nose_unit_1 = Line(nose_space.number_to_point(0), nose_space.number_to_point(1), stroke_width=10, color=RED)        
        nose_vec_line = Line(nose_space.number_to_point(0), nose_space.number_to_point(0.95), color=RED, fill_opacity=0.9)
        nose_vec_line.z_index = 4
        nose_vec_tip = Triangle(fill_color=RED, fill_opacity=0.9, color=RED).scale(0.07).rotate(-90*DEGREES).move_to(nose_space.number_to_point(0.95))
        nose_vec_tip.z_index = 4
        nose_unit_1 = VGroup(nose_vec_line, nose_vec_tip)
        # .shift(UP)

        self.play(GrowFromPoint(nose_unit_1, nose_space.number_to_point(0)), GrowFromPoint(nose_group_1, nose_space.number_to_point(0)))
        
        # move and connect from nose space to middle
                
        # copy on orig nose space
        nose_unit_1_copy = nose_unit_1.copy()
        nose_group_1_copy = nose_group_1.copy()
        
        # in middle
        # nose_unit_2 = Line(nose_space.number_to_point(0), nose_space.number_to_point(2), stroke_width=10, color='#FF8BA0').shift(UP)
        nose_vec_line_2 = Line(nose_space.number_to_point(0), nose_space.number_to_point(1.95), color=RED, fill_opacity=0.9)
        nose_vec_line_2.z_index = 4
        nose_vec_tip_2 = Triangle(fill_color=RED, fill_opacity=0.9, color=RED).scale(0.07).rotate(-90*DEGREES).move_to(nose_space.number_to_point(1.95))
        nose_vec_tip_2.z_index = 4
        nose_unit_2 = VGroup(nose_vec_line_2, nose_vec_tip_2).shift(UP)

        nose_group_2 = nose_group_1.copy().move_to(nose_space.number_to_point(2)).shift(UP).shift(UP*0.2)
        
        #conns down
        nose_dot = Dot(nose_space.number_to_point(1), radius=0.01)
        mid_dot = Dot(nose_space.number_to_point(2), radius=0.01).shift(UP) #use this instead of nose_unit_2 b/c nose_unit_2's center not small enough
        conn_1 = Line(nose_dot, mid_dot.get_center())
        
        # self.remove(nose_unit_1_copy)
        self.play(Transform(nose_unit_1_copy, nose_unit_2), Transform(nose_group_1_copy, nose_group_2), Transform(weight_2, nose_unit_2), GrowFromPoint(conn_1, nose_space.number_to_point(1)))
        self.add(mid_dot)
        
        # self.remove(nose_unit_1_copy)

        self.wait(2)
                
        # move and connect from middle to nap space        
        nose_group_2_b = nose_group_1.copy().move_to(nap_space.number_to_point(2)).shift(UP*0.2)

        # nose_unit_2_b = Line(nap_space.number_to_point(0), nap_space.number_to_point(2), stroke_width=10, color='#FF8BA0')        
        nose_vec_line_2_b = Line(nap_space.number_to_point(0), nap_space.number_to_point(1.95), color='#FF8BA0', fill_opacity=0.9)
        nose_vec_line_2_b.z_index = 4
        nose_vec_tip_2_b = Triangle(fill_color='#FF8BA0', fill_opacity=0.9, color='#FF8BA0').scale(0.07).rotate(-90*DEGREES).move_to(nap_space.number_to_point(1.95))
        nose_vec_tip_2_b.z_index = 4
        nose_unit_2_b = VGroup(nose_vec_line_2_b, nose_vec_tip_2_b)
        # .shift(DOWN*0.2)
        # ear_vec_line_2_c = Line(nap_space.number_to_point(0), nap_space.number_to_point(0.7), color='#ADD8E6', fill_opacity=0.9)
        # ear_vec_line_2_c.z_index = 5
        # self.add(ear_vec_line_2_c)

        nap_dot = Dot(nap_space.number_to_point(2), radius=0.01).shift(UP*0.2)
        conn_2 = Line(mid_dot, nap_dot)
        self.remove(weight_2) #else will leave behind
        self.play(Transform(nose_unit_1_copy, nose_unit_2_b), Transform(nose_group_1_copy, nose_group_2_b), GrowFromPoint(conn_2, nose_group_2))
        
        self.wait(2)
        weight_line_nose = Line(nose_dot, nap_dot)
        both_conns_nose = VGroup(conn_1, conn_2)
        self.remove(mid_dot)
        self.play(Transform(both_conns_nose, weight_line_nose))

        self.wait(2)

        ################
        '''And since studies on cat people suggest that nose tip and ear length can independently build on top of each other to predict nap enjoyment, we can add them together:'''

        eqn_3a = MathTex(r"2 \ \frac{Nap}{Nose} * (1 \ Nose) + 0.75 \ \frac{Nap}{Nose} * (1 \ Ear)", font_size=45, tex_to_color_map={
            "(1 \ Nose)": RED,
            "(1 \ Ear)": BLUE
        }).shift(UP*0.9+RIGHT*4).scale(0.7)
        eqn_3b = Tex("= ? Nap", font_size=45).shift(UP*0.1+RIGHT*3.8).scale(0.7)
        self.play(Transform(eqn_1, eqn_3a), Transform(eqn_2, eqn_3a), Transform(napName, eqn_3b))

        self.wait(2)

        ###        
        op_lv = 0.4
        face_outline_op = Circle(radius=1.75, color=WHITE, fill_color=BLACK, fill_opacity=1, stroke_width=2, stroke_opacity = op_lv).move_to([0, 0, 0])

        nose_line_1 = Line([-0.5, 0, 0], [0.5, 0, 0], stroke_opacity = op_lv)
        nose_line_2 = Line([-0.5, 0, 0], [0, nose_tip, 0], stroke_opacity = op_lv)
        nose_line_3 = Line([0, nose_tip, 0], [0.5, 0, 0], stroke_opacity = op_lv)
        nose_op = VGroup(nose_line_1, nose_line_2, nose_line_3)

        ear_length = 0.5
        left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0], stroke_opacity = op_lv)
        left_ear_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0], stroke_opacity = op_lv)
        left_ear_op = VGroup(left_ear_1, left_ear_2)
        
        right_ear_1 = Line([1.5, 0, 0], [1, ear_length+1.5, 0], stroke_opacity = op_lv)
        right_ear_2 = Line([1, ear_length+1.5, 0], [0, 0, 0], stroke_opacity = op_lv)
        right_ear_op = VGroup(right_ear_1, right_ear_2)

        for nl in nose_op:
            nl.z_index=5
            nl.stroke_width=2  #default is 4
        face_outline_op.z_index=3
        left_ear_op.z_index=1
        right_ear_op.z_index=1

        ################

        Tom_pt = Dot(nap_space.number_to_point(0), radius=0.1, color='#CBC3E3', fill_opacity=1)
        Tom_pt.z_index = 4
        self.play(FadeIn(Tom_pt))

        targ_dot = Dot(nap_space.number_to_point(2.75)).shift(UP*0.2)
        # ear_group_1_copy.generate_target()
        # ear_group_1_copy.target.move_to(targ_dot.get_center())

        nose_group_11 = VGroup(face_outline_op.copy(), nose_op.copy(), box.copy()).scale(0.2).move_to(nap_space.number_to_point(2)).shift(UP*0.2)

        Tom_pt.generate_target()
        Tom_pt.target.move_to(nap_space.number_to_point(2))

        self.wait(2)
        self.play(MoveToTarget(Tom_pt), Transform(nose_group_1_copy, nose_group_11), run_time=2)

        ####
        ear_group_11 = VGroup(face_outline_op.copy(), left_ear_op.copy(), right_ear_op.copy(), box.copy()).scale(0.2).move_to(targ_dot.get_center())
      
        ear_vec_line_add = Line(nap_space.number_to_point(2) ,nap_space.number_to_point(2.7), color='#ADD8E6', fill_opacity=0.9)
        ear_vec_line_add.z_index = 4
        ear_vec_tip_add = Triangle(fill_color='#ADD8E6', fill_opacity=0.9, color='#ADD8E6').scale(0.07).rotate(-90*DEGREES).move_to(nap_space.number_to_point(2.7))
        ear_vec_tip_add.z_index = 4
        ear_vec_add = VGroup(ear_vec_line_add, ear_vec_tip_add)
        
        weight_line_ear_add = Line(ear_dot, targ_dot)
        
        self.wait(2)
        # self.play(MoveToTarget(ear_group_1_copy), Transform(ear_unit_1_copy, ear_vec_add), Transform(both_conns_ear, weight_line_ear_add))
        self.play(Transform(ear_group_1_copy, ear_group_11), Transform(ear_unit_1_copy, ear_vec_add), Transform(both_conns_ear, weight_line_ear_add), run_time=2)
             
        self.wait(2)

        ################
        nose_group_1_copy.generate_target()
        nose_group_1_copy.target.move_to(targ_dot.get_center())
        Tom_pt.generate_target()
        Tom_pt.target.move_to(nap_space.number_to_point(2.75))
              
        weight_line_nose_add = Line(nose_dot, targ_dot)

        nose_group_11_nofade = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.2).move_to(targ_dot.get_center())
        ear_group_11_nofade = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.2).move_to(targ_dot.get_center())

        self.play(MoveToTarget(nose_group_1_copy), Transform(both_conns_nose, weight_line_nose_add), MoveToTarget(Tom_pt))

        self.play(Transform(nose_group_1_copy, nose_group_11_nofade), Transform(ear_group_1_copy, ear_group_11_nofade), FadeOut(Tom_pt))

        self.wait(2)

        purp_vec_line = Line(nap_space.number_to_point(0), nap_space.number_to_point(2.7), color='#CF9FFF', fill_opacity=1)
        purp_vec_line.z_index = 5
        purp_vec_tip = Triangle(fill_color='#CF9FFF', fill_opacity=1, color='#CF9FFF').scale(0.07).rotate(-90*DEGREES).move_to(nap_space.number_to_point(2.7))
        purp_vec_tip.z_index = 5
        purp_vec = VGroup(purp_vec_line, purp_vec_tip)

        eqn_3c = Tex("= 2.75 Nap", font_size=45).shift(UP*0.1+RIGHT*4.3).scale(0.7)

        self.play(Transform(nose_unit_1_copy, purp_vec), Transform(napName, eqn_3c))
        self.remove(ear_vec_add)
                     
        self.wait(2)