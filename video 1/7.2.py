from manim import *
import pdb

class scene_7_2(Scene):
    def construct(self):  
        inNode_1 = Circle(radius=0.5, fill_color=WHITE, fill_opacity=1,  color=WHITE, stroke_width=1).move_to([-1.5, -1, 0])
        inNode_2 = Circle(radius=0.5, fill_color=WHITE, fill_opacity=1,  color=WHITE, stroke_width=1).move_to([-1.5, -3, 0])

        midNode_1 = Circle(radius=0.5, fill_color=WHITE, fill_opacity=1,  color=WHITE, stroke_width=1).move_to([1.5, -2, 0])

        conn_1 = Line(inNode_1.get_center(), midNode_1.get_center(), color=WHITE)
        conn_2 = Line(inNode_2.get_center(), midNode_1.get_center(), color=WHITE)

        self.add(inNode_1, midNode_1, conn_1)
        # self.wait(2)

        ####
        '''Recall how our equation with only nose to nap could also be represented as a matrix with 1 row and 1 column. Now, we go from a matrix of 1 row and 1 column, to a matrix with 1 row and 2 columns'''

        # m1 = Matrix([["w_{11}", "w_{12}"], ["w_{21}", "w_{22}"]])
        m1 = Matrix([["w_{11}"]])
        m1.move_to([-2.5,2,0])
                
        # x = Matrix([["x_{1}"], ["x_{2}"]])
        x = Matrix([["x_{1}"]])
        x.move_to([0,2,0])
        
        equal_sign = Text('=').scale(0.65)
        equal_sign.move_to(np.array([1.5, 2, 0]))
        
        # A = Matrix([["a_{11}", "a_{12}"], ["a_{21}", "a_{22}"]])
        A = Matrix([["a_{11}"]])
        A.move_to([3,2,0])
        
        eqn = VGroup(m1, x, equal_sign, A).scale(1.5)
        self.add(m1, x, equal_sign, A)

        self.wait(2)

        m2 = Matrix([["w_{11}", "w_{12}"]]).set_column_colors(WHITE, BLACK).move_to([-2.5,2,0])
        x2 = Matrix([["x_{1}"], ["x_{2}"]]).set_row_colors(WHITE, BLACK).move_to([0,2,0])
        # A2 = Matrix([["a_{11}", "a_{12}"]]).set_column_colors(WHITE, BLACK).move_to([3,2,0])
        # equal_sign_2 = Text('=').scale(0.65)
        # equal_sign_2.move_to(np.array([1.15, 2, 0]))
        # self.play(TransformMatchingShapes(m1, m2), TransformMatchingShapes(x, x2), TransformMatchingShapes(A, A2), Transform(equal_sign, equal_sign_2))
        self.play(TransformMatchingShapes(m1, m2), TransformMatchingShapes(x, x2))
        self.wait(2)

        x3 = Matrix([["x_{1}"], ["x_{2}"]]).move_to([0,2,0])
        self.play(TransformMatchingShapes(x2, x3), FadeIn(inNode_2))
        self.wait(2)

        m3 = Matrix([["w_{11}", "w_{12}"]]).move_to([-2.5,2,0])
        self.play(TransformMatchingShapes(m2, m3), FadeIn(conn_2))
        self.wait(2)

        # A3 = Matrix([["a_{11}", "a_{12}"]]).move_to([3,2,0])
        # self.play(TransformMatchingShapes(A2, A3))
        # self.wait(2)

        #####
        dot_prod = MathTex(r"\textbf{w} \cdot \textbf{x} \ = \ w_{11}*x_{1} + w_{12}*x_{2} \ = \ a_{11}").scale(1.1).move_to([0.2,0.3,0])
        self.play(Write(dot_prod))
        
        self.wait(2)
        
        #####
        CoU = Text("Change of \n Units").move_to([4.5, -2, 0])
        self.play(Write(CoU))
        self.wait(2)

        CoB = Text("Change of \n Basis").move_to([4.5, -2, 0])
        self.play(Transform(CoU, CoB))
        self.wait(2)

        #####
        '''So our Input Space and our Nap Space are measuring neuron activations. We call these spaces Activation Space.'''

        self.play(FadeOut(CoU, m3, x3, A, equal_sign, dot_prod))

        numberplane = NumberPlane()

        nap_space_IS = VGroup(Line([0,0,0], [5, 0, 0], color=WHITE, stroke_width=1))
        for x in range(6):
            nap_space_IS.add(Line([x, 0.1,0], [x, -0.1, 0], color=WHITE, stroke_width=1))
            nap_space_IS.add(Tex(str(x), color=WHITE, stroke_width=1, font_size=38).move_to([x,0,0]).shift(DOWN*0.38))
        nap_space_IS.move_to(np.array([3.7, 2.75, 0]))
        NS_bg = Rectangle(color=WHITE, height=1.6, width=6.5, fill_color=BLACK, fill_opacity=1, stroke_width=2).move_to(np.array([3.7, 3, 0]))

        nap_space_IS.scale(1.2)
        nap_space_2 = NumberLine(
            x_range=[0, 5, 1],
            include_numbers=True,
            label_direction=DOWN,
        ).scale(1.2).shift(2.75*RIGHT).move_to(np.array([3.7, 2.75, 0]))

        self.play(FadeIn(numberplane, NS_bg, nap_space_2))

        nose_vec_line = Line([0,0,0], [0.95,0,0], color=RED, fill_opacity=0.9)
        nose_vec_line.z_index = 5
        nose_vec_tip = Triangle(fill_color=RED, fill_opacity=0.9, color=RED).scale(0.07).rotate(-90*DEGREES).move_to([0.95,0,0])
        nose_vec_tip.z_index = 5
        nose_vec = VGroup(nose_vec_line, nose_vec_tip)

        ear_vec_line = Line([0,0,0],[0, 0.8, 0], color=BLUE)
        ear_vec_line.z_index = 5
        ear_vec_tip = Triangle(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.07).rotate(360*DEGREES).move_to([0, 0.8, 0])
        ear_vec_tip.z_index = 5
        ear_vec_vert = VGroup(ear_vec_line, ear_vec_tip)

        self.play(GrowFromPoint(nose_vec, [0,0,0]), GrowFromPoint(ear_vec_vert, [0,0,0]))

        self.wait(2)

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

        ########################
        # scaled objs

        op_lv = 1

        nose_tip = 0.3 
        nose_line_1 = Line([-0.5, 0, 0], [0.5, 0, 0], stroke_opacity = op_lv)
        nose_line_2 = Line([-0.5, 0, 0], [0, nose_tip, 0], stroke_opacity = op_lv)
        nose_line_3 = Line([0, nose_tip, 0], [0.5, 0, 0], stroke_opacity = op_lv)
        nose_scaled = VGroup(nose_line_1, nose_line_2, nose_line_3)

        ear_length = 0.5 
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

        ############
        nose_group_axis = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.2).move_to([1,0,0]).shift(UP*0.2)   

        ear_group_vert = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.2).move_to([0,1,0])

        cat_person_zzz = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear_scaled.copy(), right_ear_scaled.copy(), nose_scaled.copy(), whiskers.copy(), zzz.copy(), box.copy(), mouth_smile.copy()).scale(0.2).move_to(nap_space_2.number_to_point(2.75)).shift(UP*0.2)   

        conn_1b = Line(nose_group_axis.get_center(), cat_person_zzz.get_center(), color=WHITE)
        conn_2b = Line(ear_group_vert.get_center(), cat_person_zzz.get_center(), color=WHITE)

        self.play(Transform(inNode_2, nose_group_axis[0]), Transform(inNode_1, ear_group_vert[0]), Transform(midNode_1, cat_person_zzz[0]), Transform(conn_1, conn_2b), Transform(conn_2, conn_1b), run_time=2)
        self.add(nose_group_axis, ear_group_vert, cat_person_zzz, conn_1b, conn_2b)

        purp_vec_line = Line(nap_space_2.number_to_point(0), nap_space_2.number_to_point(2.7), color='#CF9FFF', fill_opacity=1)
        purp_vec_line.z_index = 5
        purp_vec_tip = Triangle(fill_color='#CF9FFF', fill_opacity=1, color='#CF9FFF').scale(0.07).rotate(-90*DEGREES).move_to(nap_space_2.number_to_point(2.7))
        purp_vec_tip.z_index = 5
        purp_vec = VGroup(purp_vec_line, purp_vec_tip).shift(UP*0.1)
        self.play(GrowFromPoint(purp_vec, nap_space_2.number_to_point(0)))

        self.wait(2)

        ###
        ear_length = 0.5 /2.75  #lowest is 0.5. each +1 is 0.5; largest is 1.5
        nose_tip = 0.3 /2.75 # each unit of 1 is 0.25. 3 is 0.75, etc
        
        left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0])
        left_ear_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0])
        left_ear_nap_u1 = VGroup(left_ear_1, left_ear_2)
        
        right_ear_1 = Line([1.5, 0, 0], [1, ear_length+1.5, 0])
        right_ear_2 = Line([1, ear_length+1.5, 0], [0, 0, 0])
        right_ear_nap_u1 = VGroup(right_ear_1, right_ear_2)
                
        nose_line_1 = Line([-0.5, 0, 0], [0.5, 0, 0])
        nose_line_2 = Line([-0.5, 0, 0], [0, nose_tip, 0])
        nose_line_3 = Line([0, nose_tip, 0], [0.5, 0, 0])
        nose_nap_u1 = VGroup(nose_line_1, nose_line_2, nose_line_3)
                       
        for er in left_ear_nap_u1:
            er.stroke_width=2
        for er in right_ear_nap_u1:
            er.stroke_width=2
            
        for nl in nose_nap_u1:
            nl.z_index=3
            nl.stroke_width=2  #default is 4
        ###
        mouth_smile_2 = mouth_smile.copy().scale(0.3)

        nap_1 = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear_nap_u1.copy(), right_ear_nap_u1.copy(), nose_nap_u1.copy(), whiskers.copy(), mouth_smile_2, zzz.copy(), box.copy()).scale(0.2).move_to(nap_space_2.number_to_point(1)).shift(UP*0.2)   

        nap_1_line = Line(nap_space_2.number_to_point(0), nap_space_2.number_to_point(0.95), color='#FFD700', fill_opacity=0.9)
        nap_1_line.z_index = 5
        nap_1_tip = Triangle(fill_color='#FFD700', fill_opacity=0.9, color='#FFD700').scale(0.07).rotate(-90*DEGREES).move_to(nap_space_2.number_to_point(0.95))
        nap_1_tip.z_index = 5
        nap_1_unit = VGroup(nap_1_line, nap_1_tip).shift(UP*0.2) 

        self.play(GrowFromCenter(nap_1), GrowFromPoint(nap_1_unit, nap_space_2.number_to_point(0)))
        self.wait(2)
        
        basis_words = Text("Neurons are Basis Vectors \n in an Activation Space").shift(DOWN*1.2)
        self.play(Write(basis_words))
        self.wait(2)

        