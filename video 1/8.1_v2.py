from manim import *
import pdb

class scene_8_1(Scene):
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
            
        ear_group_1 = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.2).move_to([0,1,0])

        ear_vec_line = Line([0,0,0],[0, 0.8, 0], color=BLUE)
        ear_vec_line.z_index = 5
        ear_vec_tip = Triangle(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.07).rotate(360*DEGREES).move_to([0, 0.8, 0])
        ear_vec_tip.z_index = 5
        ear_unit_1 = VGroup(ear_vec_line, ear_vec_tip)

        ear_group_unit = VGroup(ear_space, ear_group_1, ear_unit_1)

        ###
        nose_space = NumberLine(
            x_range=[-7, 7, 1],
            include_numbers=True,
            label_direction=DOWN)

        nose_group_1 = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.2).move_to(nose_space.number_to_point(1)).shift(UP*0.2)     

        nose_vec_line = Line(nose_space.number_to_point(0), nose_space.number_to_point(0.95), color=RED, fill_opacity=0.9)
        nose_vec_line.z_index = 5
        nose_vec_tip = Triangle(fill_color=RED, fill_opacity=0.9, color=RED).scale(0.07).rotate(-90*DEGREES).move_to(nose_space.number_to_point(0.95))
        nose_vec_tip.z_index = 5
        nose_unit_1 = VGroup(nose_vec_line, nose_vec_tip)
        
        nose_group_unit = VGroup(nose_space, nose_group_1, nose_unit_1)

        ###
        numberplane = NumberPlane()
        self.add(numberplane, ear_group_unit, nose_group_unit)

        ########################
        # USER INPUTS

        new_x = 1
        new_y = 1

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
        # width= 5
        eqn_background_2 = Rectangle(color=WHITE, height=1.3, width=4.3, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background_2.move_to(np.array([-4.1, 0, 0]))
                
        equal_sign_2 = Text('=', font_size=32)
        equal_sign_2.move_to(np.array([-6.5, 0, 0]))
        
        scalar_x1 = MathTex(r"x_1" + " \ * \ ")
        scalar_x1.move_to(np.array([-5.7, 0, 0])).scale(0.7)

        scalar_1 = MathTex(str(new_x) + " \ * \ ")
        scalar_1.move_to(np.array([-5.7, 0, 0])).scale(0.7)
        
        mat_1 = MathTex(r"\begin{bmatrix} 1 \\ 0 \end{bmatrix}", color = RED)
        mat_1.move_to(np.array([-4.9, 0, 0])).scale(0.85)
        
        plus_sign_2 = Text('+', font_size=32)
        plus_sign_2.move_to(np.array([-4.2, 0, 0]))
        
        scalar_x2 = MathTex(r"x_2" + " \ * \ ")
        scalar_x2.move_to(np.array([-3.6, 0, 0])).scale(0.7)
        
        scalar_2 = MathTex(str(new_y) + " \ * \ ")
        scalar_2.move_to(np.array([-3.6, 0, 0])).scale(0.7)
        
        mat_2 = MathTex(r"\begin{bmatrix} 0 \\ 1 \end{bmatrix}", color = BLUE)
        mat_2.move_to(np.array([-2.8, 0, 0])).scale(0.85)

        eqn_grp = VGroup(eqn_background_2, scalar_x1, scalar_1, mat_1, scalar_x2, scalar_2, plus_sign_2, mat_2).shift(UP*3+RIGHT*6.8)
        # ( UP*3+RIGHT*8.5)
                
        self.play(FadeIn(eqn_background_2, scalar_x1, mat_1, scalar_x2, plus_sign_2, mat_2, shift=DOWN))
        
        self.wait(2)

        #################
        # move x vec copy to right out-bounds

        nose_group_unit = VGroup(nose_group_1, nose_unit_1) # stays
        x_vec_copy = nose_group_unit.copy().rotate(-90*DEGREES).move_to([10, -1, 0]) #moves to
        nose_group_unit_copy = nose_group_unit.copy()  #the one that moves
        self.play(Rotate(nose_group_unit_copy, angle = -90*DEGREES))
        self.play(Transform(nose_group_unit_copy, x_vec_copy), run_time=3)

        self.wait(2)

        ear_group_unit = VGroup(ear_group_1, ear_unit_1)
        y_vec_copy = ear_group_unit.copy().move_to([10, 1, 0])
        ear_group_unit_copy = ear_group_unit.copy()
        self.play(Transform(ear_group_unit_copy, y_vec_copy), run_time=3)

        self.wait(2)

        ################# 
        # scale nose in both IS and nap

        # must shift AFTER move_to, else it'd be erased by move_to
        nose_group_axis_2 = VGroup(face_outline.copy(), nose_scaled.copy(), box.copy()).scale(0.2).move_to([new_x,0,0]).shift(UP*0.2)

        if new_x < 0:
            tip_dir = 90
            incr_x = 0.05
        else:
            tip_dir = -90
            incr_x = -0.05
        nose_vec_line = Line([0,0,0],[new_x + incr_x, 0, 0], color=RED)
        nose_vec_line.z_index = 5
        nose_vec_tip = Triangle(fill_color=RED, fill_opacity=1, color=RED).scale(0.07).rotate(tip_dir*DEGREES).move_to([new_x + incr_x, 0, 0])
        nose_vec_tip.z_index = 5
        nose_vec_axis_2 = VGroup(nose_vec_line, nose_vec_tip)

        #################
        # scale ear in both IS and nap

        ear_group_vert_2 = VGroup(face_outline.copy(), left_ear_scaled.copy(), right_ear_scaled.copy(), box.copy()).scale(0.2).move_to([0,new_y,0])

        if new_y < 0:
            tip_dir_y = 180
            incr_y = 0.2
        else:
            tip_dir_y = 360
            incr_y = -0.2
        ear_vec_line = Line([0,0,0],[0, new_y + incr_y, 0], color=BLUE)
        ear_vec_line.z_index = 5
        ear_vec_tip = Triangle(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.07).rotate(tip_dir_y*DEGREES).move_to([0, new_y + incr_y, 0])
        ear_vec_tip.z_index = 5
        ear_vec_vert_2 = VGroup(ear_vec_line, ear_vec_tip)

        ####### Multiply scalars into vectors and imgs
        
        mat_1_2 = MathTex(r"\begin{bmatrix}" + str(new_x) + r" \\ 0 \end{bmatrix}", color = RED)
        mat_1_2.move_to(np.array([-4.9, 0, 0])).scale(0.85)
        
        mat_2_2 = MathTex(r"\begin{bmatrix} 0 \\ " + str(new_y) + r" \end{bmatrix}", color = BLUE)
        mat_2_2.move_to(np.array([-2.8, 0, 0])).scale(0.85)
        
        plus_sign_b = Text('+', font_size=32).move_to(np.array([-3.8, 0, 0]))

        eqn_grp_2 = VGroup(mat_1_2, mat_2_2, plus_sign_b).shift(UP*3+RIGHT*6.8)

        ##########
        # play scaling of imgs and eqns

        self.play(Transform(scalar_x1, scalar_1), Transform(scalar_x2, scalar_2))

        self.wait(2)  

        self.play(Transform(nose_group_1, nose_group_axis_2), Transform(nose_unit_1, nose_vec_axis_2),  FadeOut(scalar_x1,  shift=RIGHT), Transform(mat_1, mat_1_2))
        
        self.play(Transform(ear_group_1, ear_group_vert_2), Transform(ear_unit_1, ear_vec_vert_2),FadeOut(scalar_x2, shift=RIGHT), Transform(mat_2, mat_2_2), Transform(plus_sign_2, plus_sign_b))

        self.wait(2)  
        
        ######
        # dot appears in both spaces

        Tom_pt = Dot([0,0,0], radius=0.1, color=PURPLE)
        Tom_pt.z_index = 4

        self.play(FadeIn(Tom_pt))

        Tom_pt.generate_target()
        Tom_pt.target.move_to([new_x,0,0])
        
        nose_group_11 = VGroup(face_outline_op.copy(), nose_op.copy(), box.copy()).scale(0.2).move_to([new_x,0,0]).shift(UP*0.2)

        self.play(MoveToTarget(Tom_pt), Transform(nose_group_1, nose_group_11))
        
        self.wait(2)

        ### dot moves to ear in both spaces

        ear_group_11 = VGroup(face_outline_op.copy(), left_ear_op.copy(), right_ear_op.copy(), box.copy()).scale(0.2).move_to([new_x, new_y,0])

        ear_vec_line_2 = Line([new_x,0,0],[new_x, new_y-0.2, 0], color=BLUE)
        ear_vec_line_2.z_index = Tom_pt.z_index + 1
        ear_vec_tip_2 = Triangle(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.07).rotate(360*DEGREES).move_to([new_x, new_y-0.2, 0])
        ear_vec_tip_2.z_index = Tom_pt.z_index + 1
        ear_vec_2 = VGroup(ear_vec_line_2, ear_vec_tip_2)
        
        self.play(Transform(ear_unit_1, ear_vec_2), Transform(ear_group_1, ear_group_11))

        self.wait(2)

        ### move face DM to final pos in both spaces
        # Sum up vectors 

        Tom_pt_11 = Tom_pt.copy().move_to([new_x ,new_y,0])    

        nose_group_1.generate_target()
        nose_group_1.target.move_to([new_x ,new_y,0])

        mat_3 = MathTex(r"\begin{bmatrix}" +str(new_x) + r" \\ " + str(new_y) + r" \end{bmatrix}", color = PURPLE).move_to(np.array([-4.9, 0, 0])).scale(0.85)
        mat_3.shift(UP*3+RIGHT*6.8)
        
        # eqn_nap_5 = MathTex(r"[-0.5 \ Nap]", tex_to_color_map={
        #     "[-0.5 \ Nap]": '#CF9FFF'
        # }).move_to(np.array([4.5, 0, 0])).scale(0.85)
              
        ###   
        self.remove(mat_1, mat_2)
        self.play(Transform(Tom_pt, Tom_pt_11), MoveToTarget(nose_group_1), FadeOut(plus_sign_2, mat_2_2, shift=LEFT*2), Transform(mat_1_2, mat_3))
        # , Transform(eqn_nap, eqn_nap_5))

        self.wait(2)

        ### unfade and final vec. don't copy nose_group b/c now it's faded
        nose_group_11_nofade = VGroup(face_outline.copy(), nose_scaled.copy(), box.copy()).scale(0.2).move_to([new_x,new_y,0])
        ear_group_11_nofade = VGroup(face_outline.copy(), left_ear_scaled.copy(), right_ear_scaled.copy(), box.copy()).scale(0.2).move_to([new_x ,new_y,0])
        
        final_vec = Vector([new_x, new_y, 0], color=PURPLE)

        self.play(GrowFromPoint(final_vec, [0,0,0]), Transform(nose_group_1, nose_group_11_nofade), Transform(ear_group_1, ear_group_11_nofade))
        
        self.remove(Tom_pt)

        self.wait(2)
