from manim import *
import pdb

class scene_8_0(Scene):
    def construct(self):  
        inNode_1 = Circle(radius=0.5, fill_color=WHITE, fill_opacity=1,  color=WHITE, stroke_width=1).move_to([-1.5, -1, 0])
        inNode_2 = Circle(radius=0.5, fill_color=WHITE, fill_opacity=1,  color=WHITE, stroke_width=1).move_to([-1.5, -3, 0])

        midNode_1 = Circle(radius=0.5, fill_color=WHITE, fill_opacity=1,  color=WHITE, stroke_width=1).move_to([1.5, -1, 0])
        midNode_2 = Circle(radius=0.5, fill_color=WHITE, fill_opacity=1,  color=WHITE, stroke_width=1).move_to([1.5, -3, 0])

        conn_1 = Line(inNode_1.get_center(), midNode_1.get_center(), color=WHITE)
        conn_2 = Line(inNode_2.get_center(), midNode_1.get_center(), color=WHITE)
        conn_3 = Line(inNode_1.get_center(), midNode_2.get_center(), color=WHITE)
        conn_4 = Line(inNode_2.get_center(), midNode_2.get_center(), color=WHITE)

        self.add(inNode_1, midNode_1, conn_1, conn_2, inNode_2)

        ####
        m1 = Matrix([["w_{11}", "w_{12}"], ["w_{21}", "w_{22}"]]).set_row_colors(WHITE, BLACK).move_to([-2.5,2,0])
        x = Matrix([["x_{1}"], ["x_{2}"]]).move_to([0,2,0])
        A = Matrix([["a_{1}"], ["a_{2}"]]).set_row_colors(WHITE, BLACK).move_to([3,2,0])
        equal_sign = Text('=').scale(0.65)
        equal_sign.move_to(np.array([1.15, 2, 0]))

        self.add(m1, x, equal_sign, A)

        A2 = Matrix([["a_{1}"], ["a_{2}"]]).move_to([3,2,0])
        self.play(TransformMatchingShapes(A, A2), FadeIn(midNode_2))
        self.wait(2)

        m2 = Matrix([["w_{11}", "w_{12}"], ["w_{21}", "w_{22}"]]).move_to([-2.5,2,0])
        self.play(TransformMatchingShapes(m1, m2), FadeIn(conn_3, conn_4))
        self.wait(2)

        ############################
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
                
        ########################################
        ear_space = NumberLine(
            x_range=[0, 4, 1],
            include_numbers=True,
            label_direction=UP,
        ).scale(1.2).shift(UP*2+LEFT*3)
        
        nose_space = NumberLine(
            x_range=[0, 4, 1],
            include_numbers=True,
            label_direction=DOWN,
        ).scale(1.2).shift(DOWN*2+LEFT*3)
        
        earName = Text("Ear").shift(UP*3+LEFT*6).scale(0.75)
        noseName = Text("Nose").shift(DOWN*3+LEFT*6).scale(0.75)

        nap_space = NumberLine(
            x_range=[0, 4, 1],
            include_numbers=True,
            label_direction=UP,
        ).scale(1.2).shift(UP*2+RIGHT*3)
        
        luck_space = NumberLine(
            x_range=[0, 4, 1],
            include_numbers=True,
            label_direction=DOWN,
        ).scale(1.2).shift(DOWN*2+RIGHT*3)
        
        napName = Text("Nap").shift(UP*3+RIGHT*6).scale(0.75)
        luckName = Text("?").shift(DOWN*3+RIGHT*6).scale(0.75)

        ############################

        # fade away eqns, shift and scale NN, add spaces and DMs

        NN = VGroup(inNode_1, midNode_1, conn_1, conn_2, inNode_2, midNode_2, conn_3, conn_4)
        NN_2 = VGroup(inNode_1.copy(), midNode_1.copy(), conn_1.copy(), conn_2.copy(), inNode_2.copy(), midNode_2.copy(), conn_3.copy(), conn_4.copy()).scale(0.6).shift(LEFT*4.5+UP*2)  

        self.play(FadeOut(m1, x, A, m2, A2, equal_sign), Transform(NN, NN_2))

        self.wait(2)

        self.play(FadeIn(ear_space, nose_space, earName, noseName, nap_space, napName))

        self.wait(2)

        #############
        ## add DMs, vectors, and conns

        ear_DM = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.2).move_to(ear_space.number_to_point(1)).shift(UP*0.2)   

        nose_DM = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.2).move_to(nose_space.number_to_point(1)).shift(UP*0.2)  

        nap_DM = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), box.copy()).scale(0.2).move_to(nap_space.number_to_point(2.2)).shift(UP*0.2)

        luck_DM = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), box.copy()).scale(0.2).move_to(luck_space.number_to_point(3.7)).shift(UP*0.2)

        ear_vec = Arrow(ear_space.number_to_point(0), ear_space.number_to_point(1), color=BLUE, buff=0)
        nose_vec = Arrow(nose_space.number_to_point(0), nose_space.number_to_point(1), color=RED, buff=0)
        nap_vec = Arrow(nap_space.number_to_point(0), nap_space.number_to_point(1), color=ORANGE, buff=0)
        luck_vec = Arrow(luck_space.number_to_point(0), luck_space.number_to_point(1), color=GREEN, buff=0)

        self.play(GrowFromCenter(ear_DM), GrowFromCenter(nose_DM), GrowFromCenter(nap_DM), FadeIn(ear_vec, nose_vec, nap_vec))

        self.wait(2)
        
        #############
        # transform NN to conns

        # NN = VGroup(inNode_1, midNode_1, conn_1, conn_2, inNode_2, midNode_2, conn_3, conn_4)

        conn_en = Line(ear_DM.get_center(), nap_DM.get_center(), stroke_width = 2, color=BLUE)
        conn_nn = Line(nose_DM.get_center(), nap_DM.get_center(), stroke_width = 2, color=RED)
        conn_el = Line(ear_DM.get_center(), luck_DM.get_center(), stroke_width = 2, color=BLUE)
        conn_nl = Line(nose_DM.get_center(), luck_DM.get_center(), stroke_width = 2, color=RED)

        in_cop = inNode_1.copy()
        in_cop_2 = inNode_2.copy()
        self.play(Transform(conn_1, conn_en), Transform(conn_2, conn_nn), Transform(in_cop, ear_DM[0]), Transform(in_cop_2, nose_DM[0]), Transform(midNode_1, nap_DM[0]), run_time=2)
        
        #####

        self.play(FadeIn(luck_space, luckName))
        self.play(GrowFromCenter(luck_DM), FadeIn(ear_vec, nose_vec, nap_vec, luck_vec))
        
        self.wait(2)

        self.play(Transform(conn_3, conn_el), Transform(conn_4, conn_nl), Transform(inNode_1, ear_DM[0]), Transform(inNode_2, nose_DM[0]), Transform(midNode_2, luck_DM[0]), run_time=2)

        self.wait(2)

        luckName_2 = Text("Luck").shift(DOWN*3+RIGHT*6).scale(0.75)
        self.play(Transform(luckName, luckName_2))

        #############
        # fade away conns, and rotate

        ear_space_vert = NumberLine(
            x_range=[0, 4, 1],
            rotation=90 * DEGREES,
            label_direction=UP,
        ).scale(1.2).shift(UP*0.4+LEFT*5.4)

        ear_DM_vert = ear_DM.copy().move_to(ear_space_vert.number_to_point(1))
        ear_vec_vert = Arrow(ear_space_vert.number_to_point(0), ear_space_vert.number_to_point(1), color=BLUE, buff=0)
        
        luck_space_vert = NumberLine(
            x_range=[0, 4, 1],
            rotation=90 * DEGREES,
            label_direction=UP,
        ).scale(1.2).shift(UP*0.4+RIGHT*0.6)

        luck_DM_vert = luck_DM.copy().move_to(luck_space_vert.number_to_point(3.7))
        luck_vec_vert = Arrow(luck_space_vert.number_to_point(0), luck_space_vert.number_to_point(1), color=GREEN, buff=0)
        
        nap_space_2 = NumberLine(
            x_range=[0, 4, 1],
            include_numbers=True,
            label_direction=DOWN,
        ).scale(1.2).shift(DOWN*2+RIGHT*3)
        nap_DM_2 = nap_DM.copy().move_to(nap_space_2.number_to_point(2.2))
        nap_vec_2 = Arrow(nap_space_2.number_to_point(0), nap_space_2.number_to_point(1), color=ORANGE, buff=0)

        self.wait(2)

        self.remove(in_cop, in_cop_2)
        self.play(FadeOut(NN, earName, noseName, napName, luckName))

        self.play(Transform(ear_space, ear_space_vert), Transform(luck_space, luck_space_vert), Transform(ear_DM, ear_DM_vert), Transform(luck_DM, luck_DM_vert), Transform(ear_vec, ear_vec_vert), Transform(luck_vec, luck_vec_vert), Transform(nap_space, nap_space_2), Transform(nap_DM, nap_DM_2), Transform(nap_vec, nap_vec_2), run_time=2)

        self.wait(2)
        
        self.play(FadeOut(ear_space, ear_DM, ear_vec, nose_space, nose_DM, nose_vec, shift=LEFT), FadeOut(nap_space, nap_DM, nap_vec, luck_space, luck_DM, luck_vec, shift=RIGHT))

        self.wait(2)
        