from manim import *
import pdb

class scene_8_2(Scene):
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
        ear_space = NumberLine(
            x_range=[-7, 7, 1],
            rotation=90 * DEGREES,
            include_numbers=True,
            label_direction=LEFT)
            
        nose_space = NumberLine(
            x_range=[-7, 7, 1],
            include_numbers=True,
            label_direction=DOWN)

        nap_basis = Vector([1,0,0], color=ORANGE)
        luck_basis = Vector([0,1,0], color=GREEN)

        numberplane = NumberPlane()
        self.add(numberplane, ear_space, nose_space, nap_basis, luck_basis)

        ########################
        # USER INPUTS

        w_11 = 2
        w_12 = 3
        w_21 = -3
        w_22 = 2

        new_x = 1
        new_y = 1
        
        ########################
        # create faded objects before scaling     
        op_lv = 0.4
        face_outline_op_0 = Circle(radius=1.75, color=WHITE, fill_color=BLACK, fill_opacity=1, stroke_width=2, stroke_opacity = op_lv/2).move_to([0, 0, 0])

        nose_line_1 = Line([-0.5, 0, 0], [0.5, 0, 0], stroke_opacity = op_lv)
        nose_line_2 = Line([-0.5, 0, 0], [0, nose_tip, 0], stroke_opacity = op_lv)
        nose_line_3 = Line([0, nose_tip, 0], [0.5, 0, 0], stroke_opacity = op_lv)
        nose_op_0 = VGroup(nose_line_1, nose_line_2, nose_line_3)

        left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0], stroke_opacity = op_lv)
        left_ear_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0], stroke_opacity = op_lv)
        left_ear_op_0 = VGroup(left_ear_1, left_ear_2)
        
        right_ear_1 = Line([1.5, 0, 0], [1, ear_length+1.5, 0], stroke_opacity = op_lv)
        right_ear_2 = Line([1, ear_length+1.5, 0], [0, 0, 0], stroke_opacity = op_lv)
        right_ear_op_0 = VGroup(right_ear_1, right_ear_2)

        for nl in nose_op_0:
            nl.z_index=5
            nl.stroke_width=2  #default is 4
        face_outline_op_0.z_index=3
        left_ear_op_0.z_index=1
        right_ear_op_0.z_index=1
        for er in left_ear_op_0:
            er.stroke_width=2
        for er in right_ear_op_0:
            er.stroke_width=2

        ########################
        # scaled objs

        op_lv = 1

        nose_tip = 0.3 * new_x
        nose_line_1 = Line([-0.5, 0, 0], [0.5, 0, 0], stroke_opacity = op_lv)
        nose_line_2 = Line([-0.5, 0, 0], [0, nose_tip, 0], stroke_opacity = op_lv)
        nose_line_3 = Line([0, nose_tip, 0], [0.5, 0, 0], stroke_opacity = op_lv)
        nose_scaled = VGroup(nose_line_1, nose_line_2, nose_line_3)

        ear_length = 0.5 * new_y
        left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0], stroke_opacity = op_lv)
        left_ear_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0], stroke_opacity = op_lv)
        left_ear_scaled = VGroup(left_ear_1, left_ear_2)
        
        right_ear_1 = Line([1.5, 0, 0], [1, ear_length+1.5, 0], stroke_opacity = op_lv)
        right_ear_2 = Line([1, ear_length+1.5, 0], [0, 0, 0], stroke_opacity = op_lv)
        right_ear_scaled = VGroup(right_ear_1, right_ear_2)

        for nl in nose_scaled:
            nl.z_index=5
            nl.stroke_width=2  #default is 4
        left_ear_scaled.z_index=1
        right_ear_scaled.z_index=1
        for er in left_ear_scaled:
            er.stroke_width=2
        for er in right_ear_scaled:
            er.stroke_width=2

        ########################
        # create faded objects         
        op_lv = 0.4
        face_outline_op = Circle(radius=1.75, color=WHITE, fill_color=BLACK, fill_opacity=1, stroke_width=2, stroke_opacity = op_lv/2).move_to([0, 0, 0])

        nose_line_1 = Line([-0.5, 0, 0], [0.5, 0, 0], stroke_opacity = op_lv)
        nose_line_2 = Line([-0.5, 0, 0], [0, nose_tip, 0], stroke_opacity = op_lv)
        nose_line_3 = Line([0, nose_tip, 0], [0.5, 0, 0], stroke_opacity = op_lv)
        nose_op = VGroup(nose_line_1, nose_line_2, nose_line_3)

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
        for er in left_ear_op:
            er.stroke_width=2
        for er in right_ear_op:
            er.stroke_width=2

        ########## Show vector equations         
        eqn_background_2 = Rectangle(color=WHITE, height=1.3, width=4.3, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background_2.move_to(np.array([-4.1, 0, 0]))
                
        equal_sign_2 = Text('=', font_size=32)
        equal_sign_2.move_to(np.array([-6.5, 0, 0]))

        scalar_1 = MathTex(str(new_x) + " \ * \ ")
        scalar_1.move_to(np.array([-5.7, 0, 0])).scale(0.7)
        
        mat_1 = MathTex(r"\begin{bmatrix} "+str(w_11)+r" \\ 0 \end{bmatrix}", color = '#FF8BA0')
        mat_1.move_to(np.array([-4.9, 0, 0])).scale(0.85)
        
        plus_sign_2 = Text('+', font_size=32)
        plus_sign_2.move_to(np.array([-4.1, 0, 0])).shift(RIGHT*0.2)
        
        scalar_2 = MathTex(str(new_y) + " \ * \ ")
        scalar_2.move_to(np.array([-3.6, 0, 0])).scale(0.7)
        
        mat_2 = MathTex(r"\begin{bmatrix} "+str(w_12)+r" \\ 0 \end{bmatrix}", color = '#ADD8E6')
        mat_2.move_to(np.array([-2.8, 0, 0])).scale(0.85)

        # eqn_grp = VGroup(eqn_background_2, scalar_1, mat_1, scalar_2, plus_sign_2, mat_2).shift(UP*3+RIGHT*6.8)
        eqn_grp = VGroup(eqn_background_2, mat_1).shift(UP*3+RIGHT*6.8)
                
        ########### LUCK SPACE ADDITION
        eqn_background_luck = Rectangle(color=WHITE, height=1.3, width=4.3, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background_luck.move_to(np.array([-4.1, 0, 0]))
                
        equal_sign_luck = Text('=', font_size=32)
        equal_sign_luck.move_to(np.array([-6.5, 0, 0]))

        scalar_1 = MathTex(str(new_x) + " \ * \ ")
        scalar_1.move_to(np.array([-5.7, 0, 0])).scale(0.7)
        
        mat_1_luck = MathTex(r"\begin{bmatrix} 0 \\ " +str(w_21)+ r" \end{bmatrix}", color = '#FF8BA0')        
        mat_1_luck.move_to(np.array([-4.9, 0, 0])).scale(0.85)
        0.1
        plus_sign_luck = Text('+', font_size=32)
        plus_sign_luck.move_to(np.array([-4.1, 0, 0]))
        
        scalar_2 = MathTex(str(new_y) + " \ * \ ")
        scalar_2.move_to(np.array([-3.6, 0, 0])).scale(0.7)
        
        mat_2_luck = MathTex(r"\begin{bmatrix} 0 \\ " +str(w_22)+ r" \end{bmatrix}", color = '#ADD8E6')      
        mat_2_luck.move_to(np.array([-2.8, 0, 0])).scale(0.85)

        # eqn_grp_luck = VGroup(eqn_background_luck, scalar_1, mat_1_luck, scalar_2, plus_sign_luck, mat_2_luck).shift(DOWN*3+RIGHT*6.8)
        eqn_grp_luck = VGroup(eqn_background_luck, mat_1_luck).shift(DOWN*3+RIGHT*6.8)
                        
        #################
        # move x vec copy from left out-bounds

        nap_nose_DM = VGroup(face_outline_op_0.copy(), nose_op_0.copy(), box.copy()).scale(0.2).move_to(nose_space.number_to_point(w_11)).shift(UP*0.2)   

        if w_11 < 0:
            tip_dir = 90
            incr_x = 0.05
        else:
            tip_dir = -90
            incr_x = -0.05
        nose_vec_line = Line(nose_space.number_to_point(0), nose_space.number_to_point(w_11 + incr_x), color='#FF8BA0', fill_opacity=0.9)
        nose_vec_line.z_index = 5
        nose_vec_tip = Triangle(fill_color='#FF8BA0', fill_opacity=0.9, color='#FF8BA0').scale(0.07).rotate(tip_dir*DEGREES).move_to(nose_space.number_to_point(w_11 + incr_x))
        nose_vec_tip.z_index = 5
        nap_nose_vec = VGroup(nose_vec_line, nose_vec_tip).shift(DOWN*0.1)
        
        nap_nose_DM_unit = VGroup(nap_nose_DM, nap_nose_vec)
        nap_nose_DM_unit_2 = VGroup(nap_nose_DM.copy(), nap_nose_vec.copy())
        nap_nose_DM_unit.move_to([-10, 3, 0])

        self.play(FadeIn(eqn_grp, shift=DOWN), Transform(nap_nose_DM_unit, nap_nose_DM_unit_2, run_time=3))

        self.wait(2)

        #################
        # move x vec copy from left out-bounds to luck space

        luck_nose_DM = VGroup(face_outline_op_0.copy(), nose_op_0.copy(), box.copy()).scale(0.2).move_to(ear_space.number_to_point(w_21))   

        if w_21 < 0:
            tip_dir = 180
            incr_x = 0.05
        else:
            tip_dir = 360
            incr_x = -0.05
        nose_vec_line = Line(ear_space.number_to_point(0), ear_space.number_to_point(w_21 + incr_x), color='#FF8BA0', fill_opacity=0.9)
        nose_vec_line.z_index = 5
        nose_vec_tip = Triangle(fill_color='#FF8BA0', fill_opacity=0.9, color='#FF8BA0').scale(0.07).rotate(tip_dir*DEGREES).move_to(ear_space.number_to_point(w_21 + incr_x))
        nose_vec_tip.z_index = 5
        luck_nose_vec = VGroup(nose_vec_line, nose_vec_tip).shift(RIGHT*0.1)
        
        luck_nose_DM_unit = VGroup(luck_nose_DM, luck_nose_vec)
        luck_nose_DM_unit_2 = VGroup(luck_nose_DM.copy(), luck_nose_vec.copy())
        luck_nose_DM_unit.move_to([-10, 3, 0])

        self.play(FadeIn(eqn_grp_luck, shift=DOWN), Transform(luck_nose_DM_unit, luck_nose_DM_unit_2, run_time=3))

        self.wait(2)

        # move x equations up
        mat_1_luck_copy = mat_1_luck.copy().move_to(np.array([-2.8, 0, 0])).shift(UP*3+RIGHT*6.8)

        plus_sign_2 = Text('+', font_size=32)
        plus_sign_2.move_to(np.array([-4.1, 0, 0])).shift(RIGHT*0.2).shift(UP*3+RIGHT*6.8)

        self.play(Transform(mat_1_luck, mat_1_luck_copy), FadeOut(eqn_background_luck))
        self.play(FadeIn(plus_sign_2))
        self.wait(2)

        #### move nose DMs and vectors into 2D space, add eqns
        luck_nose_DM.generate_target()
        luck_nose_DM.target.move_to([w_11*new_x, w_21*new_x, 0])
        nap_nose_DM.generate_target()
        nap_nose_DM.target.move_to([w_11*new_x, w_21*new_x, 0])

        nose_vec = Vector([w_11*new_x, w_21*new_x, 0], color='#FF8BA0')
        
        mat_nose = MathTex(r"\begin{bmatrix}" +str(w_11*new_x) + r" \\ " + str(w_21*new_x) + r" \end{bmatrix}", color = '#FF8BA0').move_to(np.array([-4.9, 0, 0])).scale(0.85)
        mat_nose.shift(UP*3+RIGHT*6.8)

        self.play(MoveToTarget(luck_nose_DM), MoveToTarget(nap_nose_DM), Transform(luck_nose_vec, nose_vec), Transform(nap_nose_vec, nose_vec), FadeOut(plus_sign_2, mat_1_luck, shift=LEFT*2), Transform(mat_1, mat_nose))

        self.wait(2)

        #############
        # move y vec copy from left out-bounds

        nap_ear_DM = VGroup(face_outline_op_0.copy(), left_ear_op_0.copy(), right_ear_op_0.copy(), box.copy()).scale(0.2).move_to(nose_space.number_to_point(w_12)).shift(UP*0.2)   
        
        if w_12 < 0:
            tip_dir = 90
            incr_x = 0.05
        else:
            tip_dir = -90
            incr_x = -0.05
        nose_vec_line = Line(nose_space.number_to_point(0), nose_space.number_to_point(w_12 + incr_x), color='#ADD8E6', fill_opacity=0.9)
        nose_vec_line.z_index = 5
        nose_vec_tip = Triangle(fill_color='#ADD8E6', fill_opacity=0.9, color='#ADD8E6').scale(0.07).rotate(tip_dir*DEGREES).move_to(nose_space.number_to_point(w_12 + incr_x))
        nose_vec_tip.z_index = 5
        nap_ear_vec = VGroup(nose_vec_line, nose_vec_tip).shift(UP*0.1)
        
        nap_ear_DM_unit = VGroup(nap_ear_DM, nap_ear_vec)
        nap_ear_DM_unit_2 = VGroup(nap_ear_DM.copy(), nap_ear_vec.copy())
        nap_ear_DM_unit.move_to([-10, 3, 0])

        mat_2.shift(UP*3+RIGHT*6.8)
        self.play(FadeIn(mat_2, shift=DOWN), Transform(nap_ear_DM_unit, nap_ear_DM_unit_2, run_time=3))

        self.wait(2)

        ####
        # move y vec copy from left out-bounds to luck

        luck_ear_DM = VGroup(face_outline_op_0.copy(), left_ear_op_0.copy(), right_ear_op_0.copy(), box.copy()).scale(0.2).move_to(ear_space.number_to_point(w_22))   
        
        if w_22 < 0:
            tip_dir = 180
            incr_x = 0.05
        else:
            tip_dir = 360
            incr_x = -0.05
        nose_vec_line = Line(ear_space.number_to_point(0), ear_space.number_to_point(w_22 + incr_x), color='#ADD8E6', fill_opacity=0.9)
        nose_vec_line.z_index = 5
        nose_vec_tip = Triangle(fill_color='#ADD8E6', fill_opacity=0.9, color='#ADD8E6').scale(0.07).rotate(tip_dir*DEGREES).move_to(ear_space.number_to_point(w_22 + incr_x))
        nose_vec_tip.z_index = 5
        luck_ear_vec = VGroup(nose_vec_line, nose_vec_tip).shift(LEFT*0.1)
        
        luck_ear_DM_unit = VGroup(luck_ear_DM, luck_ear_vec)
        luck_ear_DM_unit_2 = VGroup(luck_ear_DM.copy(), luck_ear_vec.copy())
        luck_ear_DM_unit.move_to([-10, 3, 0])

        eqn_background_luck = Rectangle(color=WHITE, height=1.3, width=2, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background_luck.move_to(np.array([-4.1, 0, 0])).shift(RIGHT)

        eqn_grp_luck = VGroup(eqn_background_luck, mat_2_luck).shift(DOWN*3+RIGHT*6.8)
        self.play(FadeIn(eqn_grp_luck, shift=DOWN), Transform(luck_ear_DM_unit, luck_ear_DM_unit_2, run_time=3))

        self.wait(2)

        #### move ear DMs and vectors into 2D space, move y equations up
        luck_ear_DM.generate_target()
        luck_ear_DM.target.move_to([w_12*new_y, w_22*new_y, 0])
        nap_ear_DM.generate_target()
        nap_ear_DM.target.move_to([w_12*new_y, w_22*new_y, 0])

        ear_vec = Vector([w_12*new_y, w_22*new_y, 0], color='#ADD8E6')

        mat_ear = MathTex(r"\begin{bmatrix}" +str(w_12*new_y) + r" \\ " + str(w_22*new_y) + r" \end{bmatrix}", color = '#ADD8E6').move_to(np.array([-2.8, 0, 0])).scale(0.85)
        mat_ear.shift(UP*3+RIGHT*6.8)

        self.play(Transform(mat_2_luck, mat_ear), Transform(mat_2, mat_ear), FadeOut(eqn_background_luck), MoveToTarget(luck_ear_DM), MoveToTarget(nap_ear_DM), Transform(luck_ear_vec, ear_vec), Transform(nap_ear_vec, ear_vec))
        self.wait(2)
        
        ### move ear vec to head of nose vec

        ear_vec_add = Arrow([w_11*new_x, w_21*new_x,0],[w_11*new_x + w_12*new_y, w_21*new_x + w_22*new_y,0], color='#ADD8E6', buff=0)

        ear_DM_add = VGroup(face_outline_op.copy(), left_ear_op.copy(), right_ear_op.copy(), box.copy()).scale(0.2).move_to([w_11*new_x + w_12*new_y, w_21*new_x + w_22*new_y,0])

        ear_grp = VGroup(nap_ear_vec, luck_ear_DM)
        ear_add_grp = VGroup(ear_vec_add, ear_DM_add)
        
        plus_sign_2 = Text('+', font_size=32)
        plus_sign_2.move_to(np.array([-4.1, 0, 0])).shift(RIGHT*0.2).shift(UP*3+RIGHT*6.8)

        self.remove(luck_ear_vec, nap_ear_DM)
        self.play(Transform(ear_grp, ear_add_grp))
        self.play(FadeIn(plus_sign_2))

        self.wait(2)

        ### move face DM to final pos 

        luck_nose_DM.generate_target()
        luck_nose_DM.target.move_to([w_11*new_x + w_12*new_y, w_21*new_x + w_22*new_y, 0])
        self.remove(nap_nose_DM)
        self.play(MoveToTarget(luck_nose_DM))

        ##########################################
        DM_nofade = VGroup(face_outline.copy(), left_ear_scaled.copy(), right_ear_scaled.copy(), nose_scaled.copy(), box.copy()).scale(0.2).move_to([w_11*new_x + w_12*new_y, w_21*new_x + w_22*new_y, 0])

        final_vec = Vector([w_11*new_x + w_12*new_y, w_21*new_x + w_22*new_y, 0], color='#C4A484')
        
        mat_fin = MathTex(r"\begin{bmatrix}" +str(w_11*new_x + w_12*new_y) + r" \\ " + str(w_21*new_x + w_22*new_y) + r" \end{bmatrix}", color = '#C4A484').move_to(np.array([-4.1, 0, 0])).scale(0.85)
        mat_fin.shift(UP*3+RIGHT*6.8)

        self.remove(mat_2)
        self.play(GrowArrow(final_vec), FadeOut(mat_2_luck, shift=LEFT*2), FadeOut(mat_1, shift=RIGHT*2), Transform(plus_sign_2, mat_fin), Transform(luck_nose_DM, DM_nofade))

        self.wait(2)
