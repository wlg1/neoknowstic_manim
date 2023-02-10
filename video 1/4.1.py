from manim import *
import pdb

class scene_4_1(Scene):
    def construct(self):
        ####################
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
        
        box = Rectangle(color=BLACK, height=5.7, width=6, stroke_width=0.01, fill_color=BLACK).shift(UP*0.33)
        box.z_index = -1
                        
        #######################################
        nose_space = NumberLine(
            x_range=[0, 4, 1],
            include_numbers=True,
            label_direction=UP,
        ).scale(2).shift(UP*2+LEFT)
        
        nap_space = NumberLine(
            x_range=[0, 4, 1],
            include_numbers=True,
            label_direction=DOWN,
        ).scale(2).shift(DOWN*2+LEFT)
        
        noseName = Text("Nose").shift(UP*2+RIGHT*5)
        napName = Text("Nap").shift(DOWN*2+RIGHT*5)
                
        ###################
        ## convert nose to nap
        
        nose_group_1 = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.3)         
        nose_unit_1 = Line(nose_space.number_to_point(0), nose_space.number_to_point(1), stroke_width=10, color=RED)
        nose_group_1.move_to(nose_space.number_to_point(1))  
        
        # copy on orig nose space
        nose_unit_1_copy = nose_unit_1.copy()
        nose_group_1_copy = nose_group_1.copy()
        
        # in middle
        nose_unit_2 = Line(nose_space.number_to_point(0), nose_space.number_to_point(2), stroke_width=10, color='#FF8BA0').shift(DOWN*1.5)
        nose_group_2 = nose_group_1.copy().move_to(nose_space.number_to_point(2)).shift(DOWN*1.5)
        
        #conns down
        nose_dot = Dot(nose_space.number_to_point(1), radius=0.01)
        mid_dot = Dot(nose_space.number_to_point(2), radius=0.01).shift(DOWN*1.5) 
        conn_1 = Line(nose_dot, mid_dot.get_center())
        
        # move and connect from middle to nap space        
        nose_group_2_b = nose_group_1.copy().move_to(nap_space.number_to_point(2))
        nose_unit_2_b = Line(nap_space.number_to_point(0), nap_space.number_to_point(2), stroke_width=10, color='#FF8BA0')
        nap_dot = Dot(nap_space.number_to_point(2), radius=0.01)
        conn_2 = Line(mid_dot, nap_dot)
        
        weight_line = Line(nose_dot, nap_dot)
        both_conns = VGroup(conn_1, conn_2)
                        
        #fade nap features in
        cat_person_zzz = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), zzz.copy(), box.copy(), mouth_smile.copy()).scale(0.3).move_to(nose_group_2_b.get_center())
        
        ####################################################################
        '''So, what does this visual we've just seen have to do with a neural network? The answer actually has been hidden in front of our eyes this entire time. '''
        
        # eqn_1 = Tex("w*(x Nose) = w*x Nap", font_size=40).shift(RIGHT*3+UP)
        # eqn_1 = Tex("(w)*(x Nose) = (w*x Nap)", font_size=40).shift(RIGHT*3+UP)
        eqn_1 = MathTex("w", "*", "(x \ Nose)", "=", "(w*x \ Nap)", font_size=40).shift(RIGHT*3+UP)
        
        self.add(nose_unit_1, nose_group_1, weight_line, nose_unit_2_b, nose_group_2_b)
        self.add(nose_space, nap_space, noseName, napName, eqn_1)
        self.add(cat_person_zzz)
        
        # self.wait(1)

        ###
        eqn_n = Tex(r"$\sigma(WX + b) = A$", font_size=40).shift(DOWN + RIGHT*3)
        self.play(FadeIn(eqn_n, shift=DOWN))
        self.wait(1)
        
        ##################################
        # Transform eqns
        '''Let's analogously map out multiplication into matrix multiplication by putting our terms in brackets. '''
        
        eqn_1b = Tex("(w)*(x Nose) = (w*x Nap)", font_size=40).shift(RIGHT*3+UP)
        
        # self.play(TransformMatchingShapes(eqn_1, eqn_1b))
        # self.wait(1)
        
        # eqn_nap = MathTex(r"\begin{bmatrix} 2 \ \frac{Nap}{Nose} \end{bmatrix} * [1 \ Nose]

        # eqn_2 = Tex("[w]*[x \ Nose] = [w*x \ Nap]", font_size=40).shift(RIGHT*3+UP)
        eqn_2 = MathTex("[w]", "*", "[x \ Nose]", "=", "[w*x \ Nap]", font_size=40).shift(RIGHT*3+UP)
        self.play(TransformMatchingShapes(eqn_1, eqn_2))
        
        self.wait(1)

        eqn_2b = MathTex("[w]", "*", "[x \ Nose]", " ", "=", "[w*x \ Nap]", font_size=40).shift(RIGHT*3+UP)
        self.play(TransformMatchingShapes(eqn_2, eqn_2b))
        
        self.wait(1)

        '''Then we'll add 0 to the left side, '''
        
        # eqn_3 = Tex("[w]*[x \ Nose]+[0] = [w*x \ Nap]", font_size=40).shift(RIGHT*3+UP)
        eqn_3 = MathTex("[w]", "*", "[x \ Nose]", "+[0]", "=", "[w*x \ Nap]", font_size=40).shift(RIGHT*3+UP)

        eqn_addZero = MathTex("[w]", "*", "[x \ Nose]", "+[0]", "=", "[w*x \ Nap]", font_size=40).shift(RIGHT*3+UP)
        
        # self.remove(eqn_2)
        # self.play(TransformMatchingShapes(eqn_2, eqn_3))

        self.play(
            TransformMatchingShapes(
                VGroup(eqn_2b[0:3], MathTex("+[0]", color=BLACK), eqn_2b[4:]),
                eqn_3,
            )
        )

        # self.play(
        #     TransformMatchingShapes(
        #         VGroup(eqn_2b[0:3], eqn_addZero[3], eqn_2b[4:]),
        #         eqn_3,
        #     )
        # )
        
        self.wait(1)
        
        '''and put both sides through t2he Identity function, which doesn't change anything'''
        # eqn_3b = Tex("I([w][x \ Nose]+[0]) = [w*x \ Nap]", font_size=40).shift(RIGHT*3+UP)
        # self.play(Transform(eqn_1, eqn_3b))

        eqn_id = MathTex("I(", "x", ")", "= x", font_size=40).shift(RIGHT*3)
        self.play(FadeIn(eqn_id, shift=DOWN))
        self.wait(1)

        eqn_3b = MathTex(" ", "[w]", "*", "[x \ Nose]", "+[0]", " ", "=", " ", "[w*x \ Nap]", " ", font_size=40).shift(RIGHT*3+UP)
        self.play(TransformMatchingShapes(eqn_3, eqn_3b))

        eqn_4 = MathTex("I(", "[w]", "*", "[x \ Nose]", "+[0]", ")", "=", "I(", "[w*x \ Nap]", ")", font_size=40).shift(RIGHT*3+UP)

        # self.play(
        #     TransformMatchingShapes(
        #         VGroup(MathTex("I(", color=BLACK), eqn_3b[1:5], MathTex(")", color=BLACK), eqn_3b[7], MathTex("I(", color=BLACK), eqn_3b[8], MathTex(")", color=BLACK)),
        #         eqn_4,
        #     )
        # )

        self.play(
            TransformMatchingShapes(
                VGroup(eqn_id[0].copy(), eqn_3b[1:5], eqn_id[2].copy(), eqn_3b[7], eqn_id[0].copy(), eqn_3b[8], eqn_id[2].copy()),
                eqn_4,
            )
        )

        self.wait(1)
        
        # '''Finally, we'll represent our output values using a variable.'''
        # eqn_4 = Tex("I([w][x \ Nose]+[0]) = [A Nap]", font_size=40).shift(RIGHT*3+UP)
        # self.play(Transform(eqn_1, eqn_3b))
        # self.wait(1)
        
        # '''This is the exact same equation as before, just written in a different form.'''
        # self.wait(1)
        
        # '''Let's compare it to a neuron equation, which is what a neural network uses to compute a neuron activation. All the variables are matrices. The sigma is an activation function, which in our case is just the identity, and b is the bias, which we have as 0. So our equation is just a very simple neuron. '''
        # eqn_n = Tex(r"$\sigma(WX + b) = A$", font_size=40).shift(RIGHT*3)
        # self.play(FadeIn(eqn_n, shift=DOWN))
        # self.wait(1)
        
        # '''Now, we see that our unit conversion visual has been hiding a neural network neuron all along.'''
        
        # self.remove(nose_group_2_b)
        # self.play(FadeOut(nose_unit_1, nose_space, nap_space, noseName, napName, eqn_1, nose_unit_2_b))
        
        # NN_1_dot = Dot(nap_space.number_to_point(0), radius=0.01)
        # nose_group_1_N1 = nose_group_1.copy().move_to(NN_1_dot)
        # weight_line_NN = Line(NN_1_dot, nap_dot)
        
        # self.play(Transform(nose_group_1, nose_group_1_N1), Transform(weight_line, weight_line_NN))
        
        # self.wait(1) 
        
        # N1 = nose_group_1[0].copy()
        # N1.fill_color=WHITE
        # N2 = cat_person_zzz[0].copy()
        # N2.fill_color=WHITE
        # self.play(Transform(nose_group_1, N1), Transform(cat_person_zzz, N2))
             
        # NN = VGroup(nose_group_1, weight_line, cat_person_zzz)
        
        # NN.generate_target()
        # NN.target.shift(RIGHT*3)
        # eqn_n.generate_target()
        # eqn_n.target.shift(LEFT*3)
        # self.play(MoveToTarget(NN), MoveToTarget(eqn_n))
        
        # self.wait(1)
        
        
        
        
        
        
        