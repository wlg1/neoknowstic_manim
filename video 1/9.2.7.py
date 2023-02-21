from manim import *
from random import randint, random

class scene_9_1(Scene):
    def construct(self):        
        ####################
        ear_length = 1.5  #lowest is 0.5. each +1 is 0.5; largest is 1.5
        nose_tip = 1.5  # each unit of 1 is 0.25. 3 is 0.75, etc
        
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
        
        ###########################################
        ear_group_1 = VGroup(face_outline.copy(),  left_eye.copy(), right_eye.copy(), left_ear.copy(), right_ear.copy(), whiskers.copy(), box.copy()).scale(0.11).move_to([0,1,0])

        nose_group_1 = VGroup(face_outline.copy(),  left_eye.copy(), right_eye.copy(), nose.copy(), whiskers.copy(), box.copy()).scale(0.11).move_to([1,0,0]).shift(UP*0.1)  

        # nose 1/2 size, ear 1/4 size    
        ###
        ear_length = 1.5 /4  #lowest is 0.5. each +1 is 0.5; largest is 1.5
        nose_tip = 1.5 /2 # each unit of 1 is 0.25. 3 is 0.75, etc
        
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
        nap_1 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear_nap_u1.copy(), right_ear_nap_u1.copy(), nose_nap_u1.copy(), whiskers.copy(), box.copy()).scale(0.11).move_to([0.4, 0.2, 0]).shift(UP*0.1)
 
        # nose -1/4 size, ear 1/2 size   
        ###
        ear_length = 1.5 /2  #lowest is 0.5. each +1 is 0.5; largest is 1.5
        nose_tip = -1.5 /4 # each unit of 1 is 0.25. 3 is 0.75, etc
        
        left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0])
        left_ear_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0])
        left_ear_luck_u1 = VGroup(left_ear_1, left_ear_2)
        
        right_ear_1 = Line([1.5, 0, 0], [1, ear_length+1.5, 0])
        right_ear_2 = Line([1, ear_length+1.5, 0], [0, 0, 0])
        right_ear_luck_u1 = VGroup(right_ear_1, right_ear_2)
                
        nose_line_1 = Line([-0.5, 0, 0], [0.5, 0, 0])
        nose_line_2 = Line([-0.5, 0, 0], [0, nose_tip, 0])
        nose_line_3 = Line([0, nose_tip, 0], [0.5, 0, 0])
        nose_luck_u1 = VGroup(nose_line_1, nose_line_2, nose_line_3)
                       
        for er in left_ear_luck_u1:
            er.stroke_width=2
        for er in right_ear_luck_u1:
            er.stroke_width=2
            
        for nl in nose_luck_u1:
            nl.z_index=3
            nl.stroke_width=2  #default is 4
        ###
        luck_1 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear_luck_u1.copy(), right_ear_luck_u1.copy(), nose_luck_u1.copy(), whiskers.copy(), box.copy()).scale(0.11).move_to([-0.2, 0.4, 0])
        
        ############
        ear_group_1_0 = ear_group_1.copy()
        nose_group_1_0 = nose_group_1.copy()
        nap_1_0 = nap_1.copy()
        luck_1_0 = luck_1.copy()

        ear_group_1_copy = ear_group_1.copy().move_to([1, 2, 0])
        nose_group_1_copy = nose_group_1.copy().move_to([2, -1, 0]).shift(UP*0.1)
        nap_1_copy = nap_1.copy().move_to([1, 0, 0]).shift(UP*0.1)
        luck_1_copy = luck_1.copy().move_to([0, 1, 0])

        ########################
        nose_orig = Vector(np.array([1, 0, 0]), color=RED)
        nose_orig_copy = nose_orig.copy()
        nose_new = Vector(np.array([2, -1, 0]), color='#FF8BA0')
        ear_orig = Vector(np.array([0, 1, 0]), color=BLUE)
        ear_orig_copy = ear_orig.copy()
        ear_new = Vector(np.array([1, 2, 0]), color='#ADD8E6')

        # columns of inverse go to basis
        nap_orig = Vector(np.array([0.4, 0.2, 0]), color=ORANGE, max_stroke_width_to_length_ratio = 10)
        nap_new = Vector(np.array([1, 0, 0]), color=ORANGE)
        
        luck_orig = Vector(np.array([-0.2, 0.4, 0]), color=GREEN, max_stroke_width_to_length_ratio = 10)
        luck_new = Vector(np.array([0, 1, 0]), color=GREEN)

        # matrix = [[2, 1], [-1, 2]]
        # self.apply_matrix(matrix)
        
        ##############################
        numberplane = NumberPlane()
        # self.add(numberplane)

        # # # self.add(nose_orig, ear_orig, nap_orig, luck_orig)
        # self.play(GrowArrow(nose_orig), GrowArrow(ear_orig))
        # # self.play(GrowArrow(nap_orig), GrowArrow(luck_orig))
        
        # # # self.add(ear_group_1_0, nose_group_1_0, nap_1_0, luck_1_0)
        # self.wait(1)
        # self.play(GrowFromCenter(ear_group_1_0), GrowFromCenter(nose_group_1_0))
        # , GrowFromCenter(nap_1_0), GrowFromCenter(luck_1_0))

        # self.wait(1)
        # # self.play(Transform(ear_group_1_0, ear_group_1_copy), Transform(nose_group_1_0, nose_group_1_copy), Transform(nap_1_0, nap_1_copy), Transform(luck_1_0, luck_1_copy), Transform(nose_orig, nose_new), Transform(ear_orig, ear_new), Transform(nap_orig, nap_new), Transform(luck_orig, luck_new), run_time=2.6)
        # self.play(Transform(ear_group_1_0, ear_group_1_copy), Transform(nose_group_1_0, nose_group_1_copy), Transform(nose_orig, nose_new), Transform(ear_orig, ear_new), run_time=2.6)

        # self.wait(1)

        ####
        '''But what does it mean to map one vector to another? We aren't saying that the red vector equals the light red vector, or that the blue vector equals the light blue vector.'''
        # self.play(GrowArrow(nose_orig_copy), GrowArrow(ear_orig_copy))

        red_coord = nose_orig_copy.coordinate_label(color=RED).scale(0.65)
        blue_coord = ear_orig_copy.coordinate_label(color=BLUE).scale(0.65).shift(LEFT)
        l_red_coord = nose_new.coordinate_label(color='#FF8BA0').scale(0.65)
        l_blue_coord = ear_new.coordinate_label(color='#ADD8E6').scale(0.65)
        # self.play(FadeIn(red_coord, blue_coord, l_red_coord, l_blue_coord))

        # self.wait(1)

        red_coord_2 = red_coord.copy()
        # MathTex(r"\begin{bmatrix} 1 \\ 0 \end{bmatrix}", color = RED)
        neq = MathTex(r"\neq")
        l_red_coord_2 = l_red_coord.copy()
        neq_grp_1 = Group(red_coord_2, neq, l_red_coord_2).arrange(buff=0.2).move_to([3.5,1,0])
        eqn_bg = Rectangle(color=WHITE, height=1, width=2.5, fill_color=BLACK, fill_opacity=0, stroke_width=4).move_to(np.array([3.5, 1, 0]))
        neq_grp_1.z_index = 6
        eqn_bg.z_index = 5
        # # self.add(eqn_bg, neq_grp_1)
        # self.play(FadeIn(eqn_bg, neq_grp_1))  # split and fade in video editor

        # self.wait(2)

        # self.play(FadeOut(neq_grp_1, red_coord, blue_coord, l_red_coord, l_blue_coord))

        # self.wait(1)

        ######
        # keep all in 1 file to preserve same zoom
        '''Let's think about this in a different way. Instead of mapping one vector to another vector, '''

        # self.play(ShrinkToCenter(ear_group_1_0), ShrinkToCenter(nose_group_1_0))

        ear_group_1_1 = ear_group_1.copy()
        nose_group_1_1 = nose_group_1.copy()
        ear_group_1_copy_1 = ear_group_1.copy().move_to([1, 2, 0])
        nose_group_1_copy_1 = nose_group_1.copy().move_to([2, -1, 0]).shift(UP*0.1)

        # self.play(GrowFromCenter(ear_group_1_1), GrowFromCenter(nose_group_1_1))

        m1 = Matrix([["w_{11}", "w_{12}"], ["w_{21}", "w_{22}"]])
        x = Matrix([["x_{1}"], ["x_{2}"]])
        WX = Group(m1, x).arrange(buff=0.2).move_to(np.array([3.5, 1, 0])).scale(0.3)
        WX.z_index = 6
        # self.play(FadeIn(WX))

        '''let's map a Data Measurement on one vector to another vector by multiplying it with our matrix.'''

        # self.play(Transform(ear_group_1_1, ear_group_1_copy_1), Transform(nose_group_1_1, nose_group_1_copy_1), run_time=2.6)

        # self.wait(1)

        ################
        '''Now we'll look at more vectors, and have them point to Data Measurements. When we pass these vectors through a matrix, we are performing a change of basis because the basis vectors that were pointing to the nose and ear unit 1 measurements are now pointing to the nap and luck unit 1 measurements.'''

        # self.play(ShrinkToCenter(ear_group_1_1), ShrinkToCenter(nose_group_1_1), FadeOut(WX, eqn_bg))

        ear_group_1_2 = ear_group_1.copy()
        nose_group_1_2 = nose_group_1.copy()
        ear_group_1_copy_2 = ear_group_1.copy().move_to([1, 2, 0])
        nose_group_1_copy_2 = nose_group_1.copy().move_to([2, -1, 0]).shift(UP*0.1)

        # self.play(GrowArrow(nap_orig), GrowArrow(luck_orig))

        # self.wait(1)

        # self.play(GrowFromCenter(ear_group_1_2), GrowFromCenter(nose_group_1_2), GrowFromCenter(nap_1_0), GrowFromCenter(luck_1_0))

        # self.wait(1)

        # self.play(Transform(ear_group_1_2, ear_group_1_copy_2), Transform(nose_group_1_2, nose_group_1_copy_2), Transform(nap_1_0, nap_1_copy), Transform(luck_1_0, luck_1_copy), run_time=2.6)

        # self.wait(1)

        ################
        '''Similarly, the data measurement previously measured by the white vector [2,1] is now measured by the silver vector'''
        ###
        ear_length = 1.5  #lowest is 0.5. each +1 is 0.5; largest is 1.5
        nose_tip = 1.5 # each unit of 1 is 0.25. 3 is 0.75, etc
        
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
        DM_11 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear_nap_u1.copy(), right_ear_nap_u1.copy(), nose_nap_u1.copy(), whiskers.copy(), box.copy()).scale(0.11).move_to([1, 1, 0])
        
        DM_11_2 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear_nap_u1.copy(), right_ear_nap_u1.copy(), nose_nap_u1.copy(), whiskers.copy(), box.copy()).scale(0.11).move_to([3, 1, 0])

        vec_11 = Vector([1, 1, 0]).set_color(WHITE)
        vec_41 = Vector([3, 1, 0]).set_color('#c0c0c0')

        #####        
        # self.play(ShrinkToCenter(ear_group_1_2), ShrinkToCenter(nose_group_1_2), ShrinkToCenter(nap_1_0), ShrinkToCenter(luck_1_0))

        ear_group_1_2 = ear_group_1.copy()
        nose_group_1_2 = nose_group_1.copy()
        ear_group_1_copy_2 = ear_group_1.copy().move_to([1, 2, 0])
        nose_group_1_copy_2 = nose_group_1.copy().move_to([2, -1, 0]).shift(UP*0.1)
        nap_1_0 = nap_1.copy()
        luck_1_0 = luck_1.copy()
        nap_1_copy = nap_1.copy().move_to([1, 0, 0]).shift(UP*0.1)
        luck_1_copy = luck_1.copy().move_to([0, 1, 0])

        # self.play(GrowArrow(vec_11), GrowArrow(vec_41))
        # self.play(GrowFromCenter(DM_11))

        # self.wait(1)
        
        # self.play(GrowFromCenter(ear_group_1_2), GrowFromCenter(nose_group_1_2), GrowFromCenter(nap_1_0), GrowFromCenter(luck_1_0))
        
        # self.play(Transform(ear_group_1_2, ear_group_1_copy_2), Transform(nose_group_1_2, nose_group_1_copy_2), Transform(nap_1_0, nap_1_copy), Transform(luck_1_0, luck_1_copy), Transform(DM_11, DM_11_2), run_time=2.6)
        
        # self.wait(1)

        ################
        whitevec = MathTex(r"\begin{bmatrix} 1 \\ 1 \end{bmatrix}", color = WHITE).scale(2)
        neq = MathTex(r"\neq").scale(2)
        DM_11 = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear_nap_u1.copy(), right_ear_nap_u1.copy(), nose_nap_u1.copy(), whiskers.copy(), box.copy()).scale(0.7)
        
        leftgrp = Group(whitevec, neq).arrange(buff=0.9)
        neq_grp_1 = Group(leftgrp, DM_11).arrange(buff=0.4).shift(RIGHT)
        self.add(neq_grp_1)