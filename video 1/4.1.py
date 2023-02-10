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
        
        eqn_0 = MathTex("w", "*", "(x \ Nose)", "=", "(w*x \ Nap)", font_size=42).shift(RIGHT*3+UP)
        
        self.add(nose_unit_1, nose_group_1, weight_line, nose_unit_2_b, nose_group_2_b)
        self.add(nose_space, nap_space, noseName, napName, eqn_0)
        self.add(cat_person_zzz)
        
        ###
        eqn_n = MathTex("\sigma(WX + b) = A", font_size=42, tex_to_color_map={
        "+ b": '#00FFFF', "\sigma(": ORANGE, ")": ORANGE}).shift(DOWN + RIGHT*3)
        self.play(FadeIn(eqn_n, shift=DOWN))
        self.wait(1)
        
        ##################################
        # Transform eqns
        '''First, we'll represent the output value as one variable, and not look at units.'''

        eqn_0b = MathTex("(w)", " ", "(x \ Nose)", "=", "(w*x \ Nap)", font_size=42).shift(RIGHT*3+UP)
        self.play(Transform(eqn_0, eqn_0b))

        self.wait(1)

        eqn_0c = MathTex("(w)", "(x \ Nose)", "=", "(a \ Nap)", font_size=42).shift(RIGHT*3+UP)
        self.play(Transform(eqn_0, eqn_0c))

        self.wait(1)

        eqn_1 = MathTex("(w)", "(x)", "=", "(a)", font_size=42).shift(RIGHT*3+UP)
        self.play(Transform(eqn_0, eqn_1))

        self.wait(1)

        '''Let's analogously map out multiplication into matrix multiplication by putting our terms in brackets. '''
        
        eqn_2 = MathTex("[w]", "[x]", "=", "[a]", font_size=42).shift(RIGHT*3+UP)
        self.remove(eqn_0, eqn_0b, eqn_0c)
        self.play(TransformMatchingShapes(eqn_1, eqn_2))
        
        eqn_2b = MathTex("[w]", "[x]", " ", "=", "[a]", font_size=42).shift(RIGHT*3+UP)
        self.play(TransformMatchingShapes(eqn_2, eqn_2b))
        
        self.wait(1)

        '''Then we'll add 0 to the left side, '''
        
        eqn_3 = MathTex("[w]", "[x]", " + [0]", "=", "[a]", font_size=42, tex_to_color_map={
            "+ [0]": '#00FFFF'}).shift(RIGHT*3+UP)

        self.play(
            TransformMatchingShapes(
                VGroup(eqn_2b[0:2], MathTex(" + [0]", color=BLACK), eqn_2b[3:]),
                eqn_3,
            )
        )

        self.wait(1)
        
        '''and put both sides through t2he Identity function, which doesn't change anything'''

        eqn_id = MathTex("I(", "x", ")", "= x", font_size=42, tex_to_color_map={
            "I(": ORANGE, ")":ORANGE}).shift(RIGHT*3)
        self.play(FadeIn(eqn_id, shift=DOWN))
        self.wait(1)

        eqn_3b = MathTex(" ", "[w]", "[x]", " + [0]", " ", "=", " ", "[a]", " ", font_size=42).shift(RIGHT*3+UP)
        self.play(TransformMatchingShapes(eqn_3, eqn_3b))

        eqn_4 = MathTex("I(", "[w]", "[x]", " + [0]", ")", "=", "I(", "[a]", ")", font_size=42, tex_to_color_map={
            "+ [0]": '#00FFFF', "I(": ORANGE, ")":ORANGE}).shift(RIGHT*3+UP)

        self.play(
            TransformMatchingShapes(
                VGroup(eqn_id[0].copy(), eqn_3b[1:4], eqn_id[2].copy(), eqn_3b[5], eqn_id[0].copy(), eqn_3b[7], eqn_id[2].copy()),
                eqn_4,
            )
        )

        self.wait(1)

        eqn_5 = MathTex("I(", "[w]", "[x]", " + [0]", ")", "=", "[a]", font_size=42, tex_to_color_map={
            "+ [0]": '#00FFFF', "I(": ORANGE, ")":ORANGE}).shift(RIGHT*3+UP)

        self.play(TransformMatchingShapes(eqn_4, eqn_5))
        self.wait(1)

        eqn_n2 = MathTex("\sigma(WX + b) = A", font_size=42, tex_to_color_map={
        "+ b": '#00FFFF', "\sigma(": ORANGE, ")": ORANGE}).shift(RIGHT*3)
        self.play(FadeOut(eqn_id, shift=UP), Transform(eqn_n, eqn_n2))
                        
        self.wait(1)

        '''Now, we see that our unit conversion visual has been hiding a neural network neuron all along.'''
        
        self.remove(nose_group_2_b)
        self.play(FadeOut(nose_unit_1, nose_space, nap_space, noseName, napName, nose_unit_2_b))
        
        NN_1_dot = Dot(nap_space.number_to_point(0), radius=0.01)
        nose_group_1_N1 = nose_group_1.copy().move_to(NN_1_dot)
        weight_line_NN = Line(NN_1_dot, nap_dot)
        
        self.play(Transform(nose_group_1, nose_group_1_N1), Transform(weight_line, weight_line_NN))
        
        self.wait(1) 
                     
        NN = VGroup(nose_group_1, weight_line, cat_person_zzz)
        
        NN.generate_target()
        NN.target.shift(RIGHT*3)
        eqn_5.generate_target()
        eqn_5.target.shift(LEFT*3)
        eqn_n.generate_target()
        eqn_n.target.shift(LEFT*3)
        self.play(MoveToTarget(NN), MoveToTarget(eqn_5), MoveToTarget(eqn_n))
        
        self.wait(1)
        
        # N1 = nose_group_1[0].copy()
        # N1.fill_color=WHITE
        # N2 = cat_person_zzz[0].copy()
        # N2.fill_color=WHITE
        # self.play(Transform(nose_group_1, N1), Transform(cat_person_zzz, N2))
        
        # self.wait(1)
        
        ############
        '''W contains weight connections that the X inputs are multiplied with, and A contains the neuron activations, which in our case, is the nap neuron. '''

        w_copy = MathTex("w").move_to(eqn_5[1].get_center())
        w_copy_2 = w_copy.copy().next_to(weight_line).shift(UP*0.4+LEFT*2.5)
        x_copy = MathTex("x").move_to(eqn_5[2].get_center())
        x_copy_2 = x_copy.copy().next_to(nose_group_1).shift(UP*0.6+LEFT*2.2)
        a_copy =  MathTex("a").move_to(eqn_5[-1].get_center())
        a_copy_2 = a_copy.copy().next_to(cat_person_zzz).shift(UP*0.6)
        
        self.play(Transform(w_copy, w_copy_2), Transform(x_copy, x_copy_2), Transform(a_copy, a_copy_2))
        
        self.wait(1)
        '''In this case, the matrix W actually just consists of a single weight variable lower case w, also called w one. Same for the X  and A matrices.'''

        eqn_6 = MathTex("I(", "[w_1]", "[x_1]", " + [0]", ")", "=", "[a_1]", font_size=42, tex_to_color_map={"+ [0]": '#00FFFF', "I(": ORANGE, ")":ORANGE}).shift(UP)

        w_copy_3 = MathTex("w_1").next_to(weight_line).shift(UP*0.4+LEFT*2.5)
        x_copy_3 = MathTex("x_1").next_to(nose_group_1).shift(UP*0.6+LEFT*2.2)
        a_copy_3 =  MathTex("a_1").next_to(cat_person_zzz).shift(UP*0.6)

        self.play(TransformMatchingShapes(eqn_5, eqn_6), Transform(w_copy, w_copy_3), Transform(x_copy, x_copy_3), Transform(a_copy, a_copy_3))       

        self.wait(1)
        '''Or with two neurons, if you think of the input as a nose neuron represented by the equation 1*x.'''

        noseNN_eqn = MathTex("I(", "[1]", "[x_1]", " + [0]", ")", "=", font_size=42, tex_to_color_map={"+ [0]": '#00FFFF', "I(": ORANGE, ")":ORANGE}).next_to(x_copy_3).shift(LEFT*4)

        x_copy_4 = MathTex("[x_1]").next_to(nose_group_1).shift(UP*0.6+LEFT*2.2)

        self.play(FadeIn(noseNN_eqn), Transform(x_copy, x_copy_4))

        self.wait(1)

        #####################
        '''So a neural network can be viewed as a function that's composed of many smaller functions....'''

        NN_2  = NN.copy().scale(0.6).shift(UP*2.8)
        eqn_6.generate_target()
        eqn_6.target.shift(UP*2)
        eqn_n.generate_target()
        eqn_n.target.shift(UP*2)
        self.play(FadeOut(x_copy, w_copy, a_copy, noseNN_eqn), Transform(NN, NN_2), MoveToTarget(eqn_6), MoveToTarget(eqn_n))
        
        self.wait(1)

        #####
        inNode_1 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([-3, 2, 0])
        inNode_2 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([-3, 0, 0])
        inNode_3 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([-3, -2, 0])

        midNode_1 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([0, 1, 0])
        midNode_2 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([0, -1, 0])

        outNode_1 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([3, 2, 0])
        outNode_2 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([3, 0, 0])
        outNode_3 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([3, -2, 0])
        
        conn_1 = Line(inNode_1.get_center(), midNode_1.get_center(), color=GRAY)
        conn_2 = Line(inNode_2.get_center(), midNode_1.get_center(), color=GRAY)
        conn_3 = Line(inNode_3.get_center(), midNode_1.get_center(), color=GRAY)
        conn_4 = Line(inNode_1.get_center(), midNode_2.get_center(), color=GRAY)
        conn_5 = Line(inNode_2.get_center(), midNode_2.get_center(), color=GRAY)
        conn_6 = Line(inNode_3.get_center(), midNode_2.get_center(), color=GRAY)
        conn_7 = Line(midNode_1.get_center(), outNode_1.get_center(), color=GRAY)
        conn_8 = Line(midNode_1.get_center(), outNode_2.get_center(), color=GRAY)
        conn_9 = Line(midNode_1.get_center(), outNode_3.get_center(), color=GRAY)
        conn_10 = Line(midNode_2.get_center(), outNode_1.get_center(), color=GRAY)
        conn_11 = Line(midNode_2.get_center(), outNode_2.get_center(), color=GRAY)
        conn_12 = Line(midNode_2.get_center(), outNode_3.get_center(), color=GRAY)
                
        bigNN = VGroup(conn_1, conn_2, conn_3, conn_4, conn_5, conn_6, conn_7, conn_8, conn_9, conn_10, conn_11, conn_12, inNode_1, inNode_2, inNode_3, midNode_1, midNode_2, outNode_1, outNode_2, outNode_3).scale(0.75).shift(DOWN*1.3)
        
        self.play(FadeIn(bigNN))

        self.wait(1)

        #####        
        N1 = nose_group_1[0].copy()
        N1.fill_color=WHITE
        N2 = cat_person_zzz[0].copy()
        N2.fill_color=WHITE
        self.play(Transform(nose_group_1, N1), Transform(cat_person_zzz, N2))
        
        self.wait(1)

        ####

        inNode_1_b = inNode_1.copy()
        inNode_1_b.color = WHITE
        conn_1_b = conn_1.copy()
        conn_1_b.color = WHITE
        midNode_1_b = midNode_1.copy()
        midNode_1_b.color = WHITE

        NN_embed = VGroup(inNode_1_b, conn_1_b, midNode_1_b)

        self.play(Transform(NN, NN_embed))
        
        self.wait(1)

        ######
        '''Of course, a neural network is more than just this equation, so rather than saying this equation is a neural network, we can say it's analogous to a neural network.'''

        eqn_7 = eqn_6.copy().shift(DOWN+LEFT*2)
        eqn_n3 = eqn_n2.copy.shift(RIGHT*2)

        self.play(Transform(eqn_6, eqn_7), Transform(eqn_n2, eqn_n3))
        
        self.wait(1)