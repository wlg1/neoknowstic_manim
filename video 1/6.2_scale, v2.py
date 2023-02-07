from manim import *
import pdb

class scene_6_2_scaled(Scene):
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
        # objects: spaces, vectors, DMs, connections

        nap_space = NumberLine(
            x_range=[-3, 2, 1],
            include_numbers=False,
            label_direction=DOWN,
        ).scale(1.2).shift(LEFT*1.6)

        ear_group_nap = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.2).move_to(nap_space.number_to_point(0.75)).shift(UP*0.2)

        ear_vec_line_nap = Line(nap_space.number_to_point(0), nap_space.number_to_point(0.7), color='#ADD8E6', fill_opacity=0.9)
        ear_vec_line_nap.z_index = 5
        ear_vec_tip_nap = Triangle(fill_color='#ADD8E6', fill_opacity=0.9, color='#ADD8E6').scale(0.07).rotate(-90*DEGREES).move_to(nap_space.number_to_point(0.7))
        ear_vec_tip_nap.z_index = 5
        ear_unit_nap = VGroup(ear_vec_line_nap, ear_vec_tip_nap).shift(UP*0.1)

        nose_group_nap = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.2).move_to(nap_space.number_to_point(2)).shift(UP*0.2)     

        nose_vec_line_nap = Line(nap_space.number_to_point(0), nap_space.number_to_point(1.95), color='#FF8BA0', fill_opacity=0.9)
        nose_vec_line_nap.z_index = 4
        nose_vec_tip_nap = Triangle(fill_color='#FF8BA0', fill_opacity=0.9, color='#FF8BA0').scale(0.07).rotate(-90*DEGREES).move_to(nap_space.number_to_point(1.95))
        nose_vec_tip_nap.z_index = 4
        nose_unit_nap = VGroup(nose_vec_line_nap, nose_vec_tip_nap)

        ###
        ear_space = NumberLine(
            x_range=[-3, 2, 1],
            include_numbers=True,
            label_direction=UP,
        ).scale(1.2).shift(UP*2.75+LEFT*1.6)
        
        ear_group_1 = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.2).move_to(ear_space.number_to_point(1)).shift(UP*0.2)   

        ear_vec_line = Line(ear_space.number_to_point(0), ear_space.number_to_point(0.95), color=BLUE, fill_opacity=0.9)
        ear_vec_line.z_index = 4
        ear_vec_tip = Triangle(fill_color=BLUE, fill_opacity=0.9, color=BLUE).scale(0.07).rotate(-90*DEGREES).move_to(ear_space.number_to_point(0.95))
        ear_vec_tip.z_index = 4
        ear_unit_1 = VGroup(ear_vec_line, ear_vec_tip)

        nap_dot = Dot(nap_space.number_to_point(0.75), radius=0.01).shift(UP*0.2)
        conn_ear_0 = Line(ear_group_1.get_center(), nap_dot)

        ear_group_unit = VGroup(ear_space, ear_group_1, ear_unit_1, conn_ear_0)

        ###
        nose_space = NumberLine(
            x_range=[-3, 2, 1],
            include_numbers=True,
            label_direction=DOWN,
        ).scale(1.2).shift(DOWN*2.75+LEFT*1.6)

        nose_group_1 = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.2).move_to(nose_space.number_to_point(1)).shift(UP*0.2)     

        nose_vec_line = Line(nose_space.number_to_point(0), nose_space.number_to_point(0.95), color=RED, fill_opacity=0.9)
        nose_vec_line.z_index = 4
        nose_vec_tip = Triangle(fill_color=RED, fill_opacity=0.9, color=RED).scale(0.07).rotate(-90*DEGREES).move_to(nose_space.number_to_point(0.95))
        nose_vec_tip.z_index = 4
        nose_unit_1 = VGroup(nose_vec_line, nose_vec_tip)
        
        nap_dot_nose_0 = Dot(nap_space.number_to_point(2), radius=0.01).shift(UP*0.2)
        conn_nose_0 = Line(nose_group_1.get_center(), nap_dot_nose_0)

        nose_group_unit = VGroup(nose_space, nose_group_1, nose_unit_1, conn_nose_0)

        ###
        self.add(nap_space, ear_group_nap, ear_unit_nap, conn_ear_0, ear_space, ear_group_1, ear_unit_1, nose_group_nap, nose_unit_nap, conn_nose_0, nose_space, nose_group_1, nose_unit_1)

        ################################
        # set up objs for 'transf to 2D'
        numberplane = NumberPlane()

        ###
        ear_space_vert = NumberLine(
            x_range=[-7, 7, 1],
            rotation=90 * DEGREES,
            include_numbers=True,
            label_direction=LEFT)
            
        ear_group_vert = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.2).move_to([0,1,0])

        ear_vec_line = Line([0,0,0],[0, 0.8, 0], color=BLUE)
        ear_vec_line.z_index = 5
        ear_vec_tip = Triangle(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.07).rotate(360*DEGREES).move_to([0, 0.8, 0])
        ear_vec_tip.z_index = 5
        ear_vec_vert = VGroup(ear_vec_line, ear_vec_tip)

        conn_ear_1 = Line(ear_group_vert.get_center(), nap_dot)

        ear_group_unit_vert = VGroup(ear_space_vert, ear_group_vert, ear_vec_vert, conn_ear_1)

        ###
        nose_space_axis = NumberLine(
            x_range=[-7, 7, 1],
            include_numbers=True,
            label_direction=DOWN)

        nose_group_axis = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.2).move_to(nose_space_axis.number_to_point(1)).shift(UP*0.2)     

        nose_vec_line = Line(nose_space_axis.number_to_point(0), nose_space_axis.number_to_point(0.95), color=RED, fill_opacity=0.9)
        nose_vec_line.z_index = 5
        nose_vec_tip = Triangle(fill_color=RED, fill_opacity=0.9, color=RED).scale(0.07).rotate(-90*DEGREES).move_to(nose_space_axis.number_to_point(0.95))
        nose_vec_tip.z_index = 5
        nose_vec = VGroup(nose_vec_line, nose_vec_tip)
        
        ###
        nap_space_IS = VGroup(Line([-3,0,0], [2, 0, 0], color=WHITE, stroke_width=1))
        for x in range(-3, 3):
            nap_space_IS.add(Line([x, 0.1,0], [x, -0.1, 0], color=WHITE, stroke_width=1))
            nap_space_IS.add(Tex(str(x), color=WHITE, stroke_width=1, font_size=38).move_to([x,0,0]).shift(DOWN*0.38))
        nap_space_IS.move_to(np.array([3.6, 2.75, 0]))

        NS_bg = Rectangle(color=WHITE, height=1.6, width=6.8, fill_color=BLACK, fill_opacity=1, stroke_width=2).move_to(np.array([3.7, 3, 0]))

        nap_space_IS.scale(1.2)
        nap_space_2 = NumberLine(
            x_range=[-3, 2, 1],
            include_numbers=True,
            color=BLACK,
            stroke_color=BLACK,
            fill_color=BLACK,
            label_direction=DOWN,
        ).scale(1.2).move_to(np.array([3.5, 2.75, 0]))

        ###
        ear_group_nap_2 = ear_group_1.copy().move_to(nap_space_2.number_to_point(0.75)).shift(UP*0.2)
        
        ear_vec_line_nap_2 = Line(nap_space_2.number_to_point(0), nap_space_2.number_to_point(0.7), color='#ADD8E6', fill_opacity=0.9)
        ear_vec_line_nap_2.z_index = 5
        ear_vec_tip_nap_2 = Triangle(fill_color='#ADD8E6', fill_opacity=0.9, color='#ADD8E6').scale(0.07).rotate(-90*DEGREES).move_to(nap_space_2.number_to_point(0.7))
        ear_vec_tip_nap_2.z_index = 5
        ear_unit_nap_2 = VGroup(ear_vec_line_nap_2, ear_vec_tip_nap_2).shift(DOWN*0.1)

        # use dots b/c shifts down/up, not exactly on pt
        nap_dot_2 = Dot(nap_space_2.number_to_point(0.75), radius=0.01).shift(UP*0.2)
        conn_ear_2 = Line([0,1,0], nap_dot_2)

        ##        
        nose_group_nap_2 = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.2).move_to(nap_space_2.number_to_point(2)).shift(UP*0.2)   

        nose_vec_line_nap_2 = Line(nap_space_2.number_to_point(0), nap_space_2.number_to_point(1.95), color='#FF8BA0', fill_opacity=0.9)
        nose_vec_line_nap_2.z_index = 5
        nose_vec_tip_nap_2 = Triangle(fill_color='#FF8BA0', fill_opacity=0.9, color='#FF8BA0').scale(0.07).rotate(-90*DEGREES).move_to(nap_space_2.number_to_point(1.95))
        nose_vec_tip_nap_2.z_index = 5
        nose_unit_nap_2 = VGroup(nose_vec_line_nap_2, nose_vec_tip_nap_2)

        nap_dot_nose_1 = Dot(nap_space_2.number_to_point(2), radius=0.01).shift(UP*0.2)
        conn_nose_1 = Line(nose_group_axis.get_center(), nap_dot_nose_1)

        nose_group_unit_axis = VGroup(nose_space_axis, nose_group_axis, nose_vec, conn_nose_1)

        ###############
        # play anim for 'transf to 2D'

        # rotate ear space to vert
        self.play(Transform(ear_group_unit, ear_group_unit_vert), run_time=2)
        self.wait(2)
        
        # move nose space to axis and nap space to top right
        self.play(Transform(nose_group_unit, nose_group_unit_axis), Transform(nap_space, nap_space_2), Transform(conn_ear_0, conn_ear_2), Transform(ear_group_nap, ear_group_nap_2), Transform(ear_unit_nap, ear_unit_nap_2), Transform(nose_group_nap, nose_group_nap_2), Transform(conn_nose_0, conn_nose_1), Transform(nose_unit_nap, nose_unit_nap_2), run_time=2)
        self.wait(2)

        # fade in number plane
        self.play(FadeIn(numberplane, NS_bg, nap_space_IS, conn_ear_2, conn_nose_1), run_time=2)
        self.wait(2)

        ########################
        # USER INPUTS

        new_x = -1
        new_y = 2
        new_x_nap = new_x * 2
        new_y_nap = 0.75*new_y
        new_nap = new_x_nap + new_y_nap 

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

        ########################
        # nap eqn

        self.remove(conn_ear_2, conn_ear_0, conn_nose_1, conn_nose_0)

        self.wait(1) # cut off prev video here

        conn_nose_0 = Line(nose_group_axis.get_center(), nap_dot_nose_1)
        conn_ear_0 = Line([0,1,0], nap_dot_2)

        nap_eqn_bg = Rectangle(color=WHITE, height=1.7, width=4.5, fill_color=BLACK, 
        fill_opacity=1, stroke_width=2).move_to(np.array([4.5, 0, 0]))

        eqn_nap = MathTex(r"\begin{bmatrix} 2 \ \frac{Nap}{Nose} \end{bmatrix} * [1 \ Nose] + \\ \begin{bmatrix} 0.75 \ \frac{Nap}{Ear} \end{bmatrix} * [1 \ Ear]", tex_to_color_map={
            "[1 \ Nose]": RED,
            "[1 \ Ear]": BLUE
        }).move_to(np.array([4.5, 0, 0])).scale(0.85)

        eqn_nap.z_index = nap_eqn_bg.z_index + 1

        self.play(FadeIn(nap_eqn_bg, eqn_nap))

        self.wait(1)

        eqn_nap_1 = MathTex(r"[2 \ Nose] + \\ \begin{bmatrix} 0.75 \ \frac{Nap}{Ear} \end{bmatrix} * [1 \ Ear]", tex_to_color_map={
            "[2 \ Nose]": '#FF8BA0',
            "[1 \ Ear]": BLUE
        }).move_to(np.array([4.5, 0, 0])).scale(0.85)

        self.play(Transform(eqn_nap, eqn_nap_1), GrowFromPoint(conn_nose_0, nose_group_axis.get_center()))

        self.wait(1)
        
        eqn_nap_2 = MathTex(r"[2 \ Nose] + [0.75 \ Ear]", tex_to_color_map={
            "[2 \ Nose]": '#FF8BA0',
            "[0.75 \ Ear]": '#ADD8E6'
        }).move_to(np.array([4.5, 0, 0])).scale(0.85)
        
        self.play(Transform(eqn_nap, eqn_nap_2), GrowFromPoint(conn_ear_0, [0,1,0]))
                
        self.wait(2)

        ########## Show equations for imgs
              
        eqn_background = Rectangle(color=WHITE, height=1.3, width=5, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background.move_to(np.array([-4.1, 2, 0]))
        
        scalar_1_face = MathTex(r"-1 \ * \ ")
        scalar_1_face.move_to(np.array([-5.7, 2, 0])).scale(0.7)
        
        nose_group_eqn = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.175).move_to(np.array([-4.9, 2, 0]))
                        
        plus_sign = Text('+', font_size=32)
        plus_sign.move_to(np.array([-4.1, 2, 0]))
        
        scalar_2_body = MathTex(r"2 \ * \ ")
        scalar_2_body.move_to(np.array([-3.6, 2, 0])).scale(0.7)
        
        ears_eqn = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.175).move_to(np.array([-2.8, 2, 0]))
        
        equal_sign = Text('=', font_size=32)
        equal_sign.move_to(np.array([-2, 2, 0]))
        
        self.play(FadeIn(eqn_background, scalar_1_face, nose_group_eqn, plus_sign, scalar_2_body, ears_eqn))
        
        self.wait(1)

        ########## Show vector equations 
        
        eqn_background_2 = Rectangle(color=WHITE, height=1.3, width=5, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background_2.move_to(np.array([-4.1, 0, 0]))
                
        equal_sign_2 = Text('=', font_size=32)
        equal_sign_2.move_to(np.array([-6.5, 0, 0]))

        scalar_1 = MathTex(r"-1 \ * \ ")
        scalar_1.move_to(np.array([-5.7, 0, 0])).scale(0.7)
        
        mat_1 = MathTex(r"\begin{bmatrix} 1 \\ 0 \end{bmatrix}")
        mat_1.move_to(np.array([-4.9, 0, 0])).scale(0.85)
        
        plus_sign_2 = Text('+', font_size=32)
        plus_sign_2.move_to(np.array([-4.1, 0, 0]))
        
        scalar_2 = MathTex(r"2 \ * \ ")
        scalar_2.move_to(np.array([-3.6, 0, 0])).scale(0.7)
        
        mat_2 = MathTex(r"\begin{bmatrix} 0 \\ 1 \end{bmatrix}")
        mat_2.move_to(np.array([-2.8, 0, 0])).scale(0.85)

        ###
        eqn_nap_3 = MathTex(r"-1 * [2 \ Nose] + 2 * [0.75 \ Ear]", tex_to_color_map={
            "[2 \ Nose]": '#FF8BA0',
            "[0.75 \ Ear]": '#ADD8E6'
        }).move_to(np.array([4.5, 0, 0])).scale(0.85)
                
        self.play(FadeIn(eqn_background_2, scalar_1, mat_1, scalar_2, plus_sign_2, mat_2, shift=DOWN))
        
        self.wait(2)

        ################# 
        # scale nose in both IS and nap

        # must shift AFTER move_to, else it'd be erased by move_to
        nose_group_axis_2 = VGroup(face_outline.copy(), nose_scaled.copy(), box.copy()).scale(0.2).move_to([new_x,0,0]).shift(UP*0.2)

        nose_vec_line = Line([0,0,0],[new_x + 0.05, 0, 0], color=RED)
        nose_vec_line.z_index = 5
        nose_vec_tip = Triangle(fill_color=RED, fill_opacity=1, color=RED).scale(0.07).rotate(90*DEGREES).move_to([new_x + 0.05, 0, 0])
        nose_vec_tip.z_index = 5
        nose_vec_axis_2 = VGroup(nose_vec_line, nose_vec_tip)

        ##
        nose_group_nap_2 = VGroup(face_outline.copy(), nose_scaled.copy(), box.copy()).scale(0.2).move_to(nap_space_2.number_to_point(new_x_nap)).shift(UP*0.2)  

        nose_vec_line_nap_2 = Line(nap_space_2.number_to_point(0), nap_space_2.number_to_point(new_x_nap+0.05), color='#FF8BA0', fill_opacity=0.9)
        nose_vec_line_nap_2.z_index = 5
        nose_vec_tip_nap_2 = Triangle(fill_color='#FF8BA0', fill_opacity=0.9, color='#FF8BA0').scale(0.07).rotate(90*DEGREES).move_to(nap_space_2.number_to_point(new_x_nap+0.05))
        nose_vec_tip_nap_2.z_index = 5
        nose_unit_nap_2_2 = VGroup(nose_vec_line_nap_2, nose_vec_tip_nap_2)

        conn_nose_2_2 = Line(nose_group_axis_2.get_center(), nose_group_nap_2.get_center())

        #################
        # scale ear in both IS and nap

        ear_group_vert_2 = VGroup(face_outline.copy(), left_ear_scaled.copy(), right_ear_scaled.copy(), box.copy()).scale(0.2).move_to([0,new_y,0])

        ear_vec_line = Line([0,0,0],[0, new_y - 0.2, 0], color=BLUE)
        ear_vec_line.z_index = 5
        ear_vec_tip = Triangle(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.07).rotate(360*DEGREES).move_to([0, new_y - 0.2, 0])
        ear_vec_tip.z_index = 5
        ear_vec_vert_2 = VGroup(ear_vec_line, ear_vec_tip)

        ##
        ear_group_nap_2_2 = ear_group_vert_2.copy().move_to(nap_space_2.number_to_point(new_y_nap)).shift(UP*0.2)
        
        ear_vec_line_nap_2 = Line(nap_space_2.number_to_point(0), nap_space_2.number_to_point(new_y_nap-0.05), color='#ADD8E6', fill_opacity=0.9)
        ear_vec_line_nap_2.z_index = 5
        ear_vec_tip_nap_2 = Triangle(fill_color='#ADD8E6', fill_opacity=0.9, color='#ADD8E6').scale(0.07).rotate(-90*DEGREES).move_to(nap_space_2.number_to_point(new_y_nap-0.05))
        ear_vec_tip_nap_2.z_index = 5
        ear_unit_nap_2_2 = VGroup(ear_vec_line_nap_2, ear_vec_tip_nap_2).shift(DOWN*0.1)

        conn_ear_2_2 = Line(ear_group_vert_2.get_center(), ear_group_nap_2_2.get_center())


        ####### Multiply scalars into vectors and imgs
        
        nose_group_eqn_2 = nose_group_axis_2.copy().move_to(np.array([-4.9, 2, 0]))
        ears_eqn_2 = ear_group_vert_2.copy().move_to(np.array([-2.8, 2, 0]))
        
        mat_1_2 = MathTex(r"\begin{bmatrix} -1 \\ 0 \end{bmatrix}")
        mat_1_2.move_to(np.array([-4.9, 0, 0])).scale(0.85)
        
        mat_2_2 = MathTex(r"\begin{bmatrix} 0 \\ 2 \end{bmatrix}")
        mat_2_2.move_to(np.array([-2.8, 0, 0])).scale(0.85)
        
        plus_sign_a = Text('+', font_size=32).move_to(np.array([-3.8, 2, 0]))
        plus_sign_b = Text('+', font_size=32).move_to(np.array([-3.8, 0, 0]))

        ##########
        # play scaling of imgs and eqns

        self.remove(conn_nose_1)
        self.play(Transform(nose_group_1, nose_group_axis_2), Transform(nose_unit_1, nose_vec_axis_2), Transform(nose_group_nap, nose_group_nap_2), Transform(nose_unit_nap, nose_unit_nap_2_2), Transform(conn_nose_0, conn_nose_2_2), FadeOut(scalar_1, scalar_1_face, shift=RIGHT), Transform(mat_1, mat_1_2), Transform(nose_group_eqn, nose_group_eqn_2))
        self.play(FadeIn(conn_nose_2_2))
        
        self.remove(conn_ear_2)
        self.play(Transform(ear_group_1, ear_group_vert_2), Transform(ear_unit_1, ear_vec_vert_2), Transform(ear_group_nap, ear_group_nap_2_2), Transform(ear_unit_nap, ear_unit_nap_2_2), Transform(conn_ear_0, conn_ear_2_2), FadeOut(scalar_2, scalar_2_body, shift=RIGHT), Transform(mat_2, mat_2_2), Transform(ears_eqn, ears_eqn_2), Transform(plus_sign, plus_sign_a), Transform(plus_sign_2, plus_sign_b))
        self.play(FadeIn(conn_ear_2_2))

        self.wait(2)  
        
        ######
        # dot appears in both spaces

        Tom_pt = Dot([0,0,0], radius=0.1, color=PURPLE)
        Tom_pt.z_index = 4

        Tom_pt_nap = Dot([0,0,0], radius=0.1, color='#CBC3E3').move_to(nap_space_2.number_to_point(0))
        Tom_pt_nap.z_index = 4

        self.play(FadeIn(Tom_pt, Tom_pt_nap))

        self.wait(2)

        ### dot moves to nose in both spaces
        Tom_pt.generate_target()
        Tom_pt.target.move_to([new_x,0,0])
        
        nose_group_11 = VGroup(face_outline_op.copy(), nose_op.copy(), box.copy()).scale(0.2).move_to([new_x,0,0]).shift(UP*0.2)

        ##
        Tom_pt_nap.generate_target()
        Tom_pt_nap.target.move_to(nap_space.number_to_point(new_x_nap))

        nose_group_11_nap = VGroup(face_outline_op.copy(), nose_op.copy(), box.copy()).scale(0.2).move_to(nap_space.number_to_point(new_x_nap)).shift(UP*0.2)

        self.play(MoveToTarget(Tom_pt), Transform(nose_group_1, nose_group_11), MoveToTarget(Tom_pt_nap), Transform(nose_group_nap, nose_group_11_nap), run_time=2)
        
        self.wait(2)

        ### dot moves to ear in both spaces

        ear_group_11 = VGroup(face_outline_op.copy(), left_ear_op.copy(), right_ear_op.copy(), box.copy()).scale(0.2).move_to([new_x, new_y,0])

        ear_vec_line_2 = Line([new_x,0,0],[new_x, new_y-0.2, 0], color=BLUE)
        ear_vec_line_2.z_index = Tom_pt.z_index + 1
        ear_vec_tip_2 = Triangle(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.07).rotate(360*DEGREES).move_to([new_x, new_y-0.2, 0])
        ear_vec_tip_2.z_index = Tom_pt.z_index + 1
        ear_vec_2 = VGroup(ear_vec_line_2, ear_vec_tip_2)
        
        ##
        ear_group_11_nap = VGroup(face_outline_op.copy(), left_ear_op.copy(), right_ear_op.copy(), box.copy()).scale(0.2).move_to(nap_space.number_to_point(new_nap)).shift(UP*0.2)
      
        ear_vec_line_add = Line(nap_space.number_to_point(new_x_nap) ,nap_space.number_to_point(new_nap-0.05), color='#ADD8E6', fill_opacity=0.9)
        ear_vec_line_add.z_index = 4
        ear_vec_tip_add = Triangle(fill_color='#ADD8E6', fill_opacity=0.9, color='#ADD8E6').scale(0.07).rotate(-90*DEGREES).move_to(nap_space.number_to_point(new_nap-0.05))
        ear_vec_tip_add.z_index = 4
        ear_vec_add = VGroup(ear_vec_line_add, ear_vec_tip_add).shift(DOWN*0.1)
        
        weight_line_ear_add = Line([new_x,new_y,0], nap_space.number_to_point(new_nap))

        self.remove(conn_ear_2_2)
        self.play(Transform(ear_unit_1, ear_vec_2), Transform(ear_group_1, ear_group_11), Transform(ear_unit_nap, ear_vec_add), Transform(ear_group_nap, ear_group_11_nap), Transform(conn_ear_0, weight_line_ear_add), run_time=2)
        self.add(weight_line_ear_add)

        self.wait(2)

        ### move face DM to final pos in both spaces
        # Sum up vectors 

        Tom_pt_11 = Tom_pt.copy().move_to([new_x ,new_y,0])    

        nose_group_1.generate_target()
        nose_group_1.target.move_to([new_x ,new_y,0])

        Tom_pt_nap.generate_target()
        Tom_pt_nap.target.move_to(nap_space.number_to_point(new_nap))

        nose_group_nap.generate_target()
        nose_group_nap.target.move_to(nap_space.number_to_point(new_nap)).shift(UP*0.2)

        mat_3 = MathTex(r"\begin{bmatrix} -1 \\ 2 \end{bmatrix}").move_to(np.array([-4.9, 0, 0])).scale(0.85)
              
        ###   
        self.remove(conn_nose_2_2, mat_1, mat_2)
        self.play(Transform(Tom_pt, Tom_pt_11), MoveToTarget(nose_group_1), MoveToTarget(nose_group_nap), Transform(conn_nose_0, weight_line_ear_add), MoveToTarget(Tom_pt_nap), FadeOut(plus_sign_2, mat_2_2, shift=LEFT*2), Transform(mat_1_2, mat_3))

        self.wait(1)

        ### unfade. don't copy nose_group b/c now it's faded
        nose_group_11_nofade = VGroup(face_outline.copy(), nose_scaled.copy(), box.copy()).scale(0.2).move_to([new_x,new_y,0])
        ear_group_11_nofade = VGroup(face_outline.copy(), left_ear_scaled.copy(), right_ear_scaled.copy(), box.copy()).scale(0.2).move_to([new_x ,new_y,0])
        
        nose_group_11_nofade_nap = VGroup(face_outline.copy(), nose_scaled.copy(), box.copy()).scale(0.2).move_to(nap_space.number_to_point(new_nap)).shift(UP*0.2)
        ear_group_11_nofade_nap = VGroup(face_outline.copy(), left_ear_scaled.copy(), right_ear_scaled.copy(), box.copy()).scale(0.2).move_to(nap_space.number_to_point(new_nap)).shift(UP*0.2)

        self.play(Transform(nose_group_1, nose_group_11_nofade), Transform(ear_group_1, ear_group_11_nofade), Transform(nose_group_nap, nose_group_11_nofade_nap), Transform(ear_group_nap, ear_group_11_nofade_nap), FadeIn(equal_sign))
        
        # self.play(FadeOut(Tom_pt), FadeOut(Tom_pt_nap)) #causes ear on nap to temp fade
        # self.play(ShrinkToCenter(Tom_pt), ShrinkToCenter(Tom_pt_nap))  #causes ear on nap to temp fade        
        self.remove(Tom_pt, Tom_pt_nap)

        self.wait(2)

        ### purple vector appears in both spaces
        tom_vec_line = Line([0,0,0],[new_x+0.2, new_y-0.2, 0], color=PURPLE)
        tom_vec_line.z_index = Tom_pt.z_index + 1
        tom_tip = Triangle(fill_color=PURPLE, fill_opacity=1, color=PURPLE).scale(0.1).rotate(45*DEGREES).move_to([new_x+0.2, new_y-0.2, 0])
        tom_tip.z_index = Tom_pt.z_index + 1
        Tom_vec = VGroup(tom_vec_line, tom_tip)
        
        purp_vec_line = Line(nap_space.number_to_point(0), nap_space.number_to_point(new_nap+0.05), color='#CF9FFF', fill_opacity=1)
        purp_vec_line.z_index = 5
        purp_vec_tip = Triangle(fill_color='#CF9FFF', fill_opacity=1, color='#CF9FFF').scale(0.07).rotate(90*DEGREES).move_to(nap_space.number_to_point(new_nap+0.05))
        purp_vec_tip.z_index = 5
        purp_vec = VGroup(purp_vec_line, purp_vec_tip).shift(UP*0.1)

        self.play(GrowFromPoint(Tom_vec, [0,0,0]), GrowFromPoint(purp_vec, nap_space.number_to_point(0)))

        self.wait(2)

        ### fade napping cat into ONLY nap space ? don't do this b/c doesn't show mapping DMs back
        '''now, pay attention closely to the next part. notice the napping cat only appears in'''

        # mouth_smile_2 = mouth_smile.copy().scale(1.875)
        # cat_person_zzz = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), zzz.copy(), box.copy(), mouth_smile_2).scale(0.2).move_to(nose_group_11_nofade_nap.get_center())

        # self.play(FadeIn(cat_person_zzz))
        
        # self.wait(2)