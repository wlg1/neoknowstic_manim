from manim import *
import random
import numpy as np
import pdb

class scene_9_5(Scene):
    def construct(self):        
        ####################
        ear_length = 1.5  
        nose_tip = 1.5  

        left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0], color=WHITE)
        left_ear_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0], color=WHITE)
        left_ear = VGroup(left_ear_1, left_ear_2)
        
        right_ear_1 = Line([1.5, 0, 0], [1, ear_length+1.5, 0], color=WHITE)
        right_ear_2 = Line([1, ear_length+1.5, 0], [0, 0, 0], color=WHITE)
        right_ear = VGroup(right_ear_1, right_ear_2)
                
        face_outline = Circle(radius=1.75, color=WHITE, fill_color=BLACK, fill_opacity=1, stroke_width=2).move_to([0, 0, 0])
                    
        nose_line_1 = Line([-0.5, 0, 0], [0.5, 0, 0], color=WHITE)
        nose_line_2 = Line([-0.5, 0, 0], [0, nose_tip, 0], color=WHITE)
        nose_line_3 = Line([0, nose_tip, 0], [0.5, 0, 0], color=WHITE)
        nose = VGroup(nose_line_1, nose_line_2, nose_line_3)
        
        left_ear.z_index=1
        right_ear.z_index=1                
        face_outline.z_index=3
        for er in left_ear:
            er.stroke_width=2
        for er in right_ear:
            er.stroke_width=2
        for nl in nose:
            nl.z_index=5
            nl.stroke_width=2  #default is 4

        # box = Rectangle(color=BLACK, height=5.7, width=6, stroke_width=0.01, fill_color=BLACK).shift(UP*0.33)
        # box.z_index = -2

        def cat_person(nose_tip, ear_length, in_mouth, in_color):
            # ear_length = 1.5  #lowest is 0.5. each +1 is 0.5; largest is 1.5
            # nose_tip = 1.5  # each unit of 1 is 0.25. 3 is 0.75, etc
            
            left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0], color=in_color)
            left_ear_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0], color=in_color)
            left_ear = VGroup(left_ear_1, left_ear_2)
            
            right_ear_1 = Line([1.5, 0, 0], [1, ear_length+1.5, 0], color=in_color)
            right_ear_2 = Line([1, ear_length+1.5, 0], [0, 0, 0], color=in_color)
            right_ear = VGroup(right_ear_1, right_ear_2)
                    
            face_outline = Circle(radius=1.75, color=in_color, fill_color=BLACK, fill_opacity=1, stroke_width=2).move_to([0, 0, 0])
            
            # left_eye = Circle(radius = 0.1, color=in_color).move_to([-1, 0.5, 0]).scale(in_eye)
            # right_eye = Circle(radius = 0.1, color=in_color).move_to([1, 0.5, 0]).scale(in_eye)
            left_eye = Dot(color=in_color).move_to([-1, 0.5, 0])
            right_eye = Dot(color=in_color).move_to([1, 0.5, 0])
            left_eye.z_index=3
            right_eye.z_index=3
            
            left_eye_zzz = ArcBetweenPoints([-0.3, -0.75,0], [0.3, -0.75,0], stroke_width=2).rotate(180*DEGREES).move_to([-1, 0.5, 0])
            right_eye_zzz = ArcBetweenPoints([-0.3, -0.75,0], [0.3, -0.75,0], stroke_width=2).rotate(180*DEGREES).move_to([1, 0.5, 0])
            left_eye_zzz.z_index=3
            right_eye_zzz.z_index=3
            
            nose_line_1 = Line([-0.5, 0, 0], [0.5, 0, 0], color=in_color)
            nose_line_2 = Line([-0.5, 0, 0], [0, nose_tip, 0], color=in_color)
            nose_line_3 = Line([0, nose_tip, 0], [0.5, 0, 0], color=in_color)
            nose = VGroup(nose_line_1, nose_line_2, nose_line_3)
            
            whisker_1 = Line([-1, -0.3, 0], [-2.3, -0.5, 0], color=in_color) # left down
            whisker_2 = Line([-1, -0.3, 0], [-2.3, 0.5, 0], color=in_color) # left up
            whisker_3 = Line([-1, -0.3, 0], [-2.3, 0, 0], color=in_color) # left middle
            whisker_4 = Line([1, -0.3, 0], [2.3, -0.5, 0], color=in_color) # right down
            whisker_5 = Line([1, -0.3, 0], [2.3, 0.5, 0], color=in_color)  # right up
            whisker_6 = Line([1, -0.3, 0], [2.3, 0, 0], color=in_color) # r mid                 
            whiskers = VGroup(whisker_1, whisker_2, whisker_3, whisker_4, whisker_5, whisker_6)
            # .scale(in_whisk)          
            
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
                    
            mouth_smile = ArcBetweenPoints([-0.5, -0.75,0], [0.5, -0.75,0], stroke_width=2, color=in_color)
            mouth_smile.scale(in_mouth)
            mouth_smile.z_index=3
                    
            zzz = Text("...zZz...", font_size = 35, color=WHITE).move_to([2.2, 1.8,0])
            zzz.z_index=3
            
            box = Rectangle(color=BLACK, height=5.7, width=6, stroke_width=0.01, fill_color=BLACK).shift(UP*0.33)
            box.z_index = -2

            return VGroup(face_outline, nose, left_eye, right_eye, left_ear, right_ear, mouth_smile, whiskers, box)
        
        def get_new_coords(prev_cat_list): 
            w11 = 2
            w12 = 1
            w21 = -w12
            w22 = w11
            # W = [[w11, w12],
            #     [w21, w22]]
            W = [[w11, w21],
                [w12, w22]]  #within lists are cols

            new_cat_list = VGroup()
            for prev_cat in prev_cat_list:
                old_x = prev_cat.get_center()[0]
                old_y = prev_cat.get_center()[1]                
                inVec = [[old_x, old_y]]
                
                out_vec = np.matmul(inVec, W)
                new_cat = prev_cat.copy().move_to([out_vec[0][0], out_vec[0][1], 0])

                new_cat_list.add(new_cat)
            return new_cat_list

        def get_inv_coords(prev_cat_list): 
            w11 = 2
            w12 = 1
            w21 = -w12
            w22 = w11
            W = [[w11, w21],
                [w12, w22]]  #within lists are cols
            
            Winv = np.linalg.inv(W)

            new_cat_list = VGroup()
            for prev_cat in prev_cat_list:
                old_x = prev_cat.get_center()[0]
                old_y = prev_cat.get_center()[1]                
                inVec = [[old_x, old_y]]
                
                out_vec = np.matmul(inVec, Winv)
                new_cat = prev_cat.copy().move_to([out_vec[0][0], out_vec[0][1], 0])

                new_cat_list.add(new_cat)
            return new_cat_list

        ###########################################
        numberplane = NumberPlane()
        self.add(numberplane)

        cat_list = VGroup()

        nap_DM_1 = cat_person( 1.5 /2, 1.5 /4, 1, WHITE).scale(0.11).move_to(([0.4, 0.2, 0]))
        cat_list.add(nap_DM_1)

        nap_DM_neg = cat_person( -1.5 /2, -1.5 /4, 1, WHITE).scale(0.11).move_to(([-0.4, -0.2, 0]))
        cat_list.add(nap_DM_neg)

        nap_DM_dub = cat_person( 4.5 /2, 4.5 /4, 1, WHITE).scale(0.11).move_to(([1.2, 0.6, 0]))
        cat_list.add(nap_DM_dub)

        luck_DM = cat_person(-1.5 /4, 1.5 /2, 1, WHITE).scale(0.11).move_to(([-0.2, 0.4, 0]))
        cat_list.add(luck_DM)

        nose_vec = Vector(np.array([1, 0, 0]), color=RED)
        nap_vec = Vector(np.array([0.4, 0.2, 0]), color=ORANGE, max_stroke_width_to_length_ratio = 10)
        luck_vec = Vector(np.array([-0.2, 0.4, 0]), color=GREEN, max_stroke_width_to_length_ratio = 10)

        ###
        '''Notice that when we performed matrix multiplication, we were bringing the data measurements along the line matching the orange vector onto the red basis vector.'''

        self.add(cat_list, nose_vec, nap_vec, luck_vec)

        new_cat_list = get_new_coords(cat_list)
        self.play(Transform(cat_list, new_cat_list))
        self.wait(2)

        # transform back
        new_cat_list_2 = get_inv_coords(new_cat_list)
        self.play(Transform(cat_list, new_cat_list_2))
        self.wait(2)

        ####
        '''This entire line is just scaled versions of the orange vector. What all of these scaled orange vectors share is a common ratio of nose to ear.'''

        nap_vec_neg = Vector(np.array([-0.4, -0.2, 0]), color=ORANGE, max_stroke_width_to_length_ratio = 10)
        nap_vec_scale = Vector(np.array([1.2, 0.6, 0]), color=ORANGE, max_stroke_width_to_length_ratio = 10)
        self.play(FadeIn(nap_vec_neg, nap_vec_scale))
        self.wait(2)

        ###
        eqn_background = Rectangle(color=WHITE, height=2, width=3, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background.move_to(np.array([2, -1.5, 0]))
                
        nose_group_eqn = VGroup(face_outline.copy(), nose.copy()).scale(0.11).move_to(np.array([2, -2, 0]))
                        
        ears_eqn = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy()).scale(0.11).move_to(np.array([2, -1, 0]))

        nap_eqn = nap_DM_1.copy().move_to(np.array([3, -1.5, 0]))

        conn_1 = Line(nose_group_eqn.get_center() + np.array([0.15, 0.15, 0]), nap_eqn.get_center(), color=WHITE)
        conn_2 = Line(ears_eqn.get_center() + np.array([0.15, -0.15, 0]), nap_eqn.get_center(), color=WHITE)

        nose_val = Text('0.4', font_size=25).move_to(np.array([1.2, -2, 0]))
        ears_val = Text('0.2', font_size=25).move_to(np.array([1.2, -1, 0]))

        self.play(FadeIn(eqn_background, nose_group_eqn, ears_eqn, nose_val, ears_val))
        self.wait(2)
        
        ###
        ''' You might have seen this before as the slope of a line.'''

        nap_x = 0.4
        nap_y = 0.2
        nap_line = Line([-20 * nap_x, -20 * nap_y, 0], [20 * nap_x, 20 * nap_y, 0], color=ORANGE)
        
        ratio_line = Line([0.8, -1.5, 0], [1.5, -1.5, 0], color=WHITE)

        self.play(FadeIn(nap_line), FadeIn(ratio_line))
        self.wait(2)

        ###
        '''If we look at the neural network corresponding to this coordinate space representation, given that these vector dimensions each correspond to a neuron, this family of orange vectors corresponds to certain combinations nose and ear activations.'''

        nose_val_1 = Text('0.4 *', font_size=25).move_to(np.array([1.2, -2, 0]))
        ears_val_1 = Text('0.2 *', font_size=25).move_to(np.array([1.2, -1, 0]))

        self.play(FadeIn(nap_eqn, conn_1, conn_2), Transform(nose_val, nose_val_1), Transform(ears_val, ears_val_1))
        
        self.wait(2)

        nose_val_2 = Text('-0.4 *', font_size=25).move_to(np.array([1.2, -2, 0]))
        ears_val_2 = Text('-0.2 *', font_size=25).move_to(np.array([1.2, -1, 0]))
        self.play(Transform(nose_val, nose_val_2), Transform(ears_val, ears_val_2))
        self.wait(2)

        nose_val_3 = Text('1.2 *', font_size=25).move_to(np.array([1.2, -2, 0]))
        ears_val_3 = Text('0.6 *', font_size=25).move_to(np.array([1.2, -1, 0]))
        self.play(Transform(nose_val, nose_val_3), Transform(ears_val, ears_val_3))
        self.wait(2)

        ###
        '''Let's turn the neurons and weights into variables. '''

        # first turn DMs into vars and fade out scalars into them

        x_var = MathTex('x', font_size=42).move_to(nose_group_eqn.get_center())
        y_var = MathTex('y', font_size=42).move_to(ears_eqn.get_center())
        n_var = MathTex('n', font_size=42).move_to(nap_eqn.get_center())

        self.play(FadeOut(ratio_line), FadeOut(nose_val, ears_val, shift=RIGHT), Transform(nose_group_eqn, x_var), Transform(ears_eqn, y_var), Transform(nap_eqn, n_var))
        self.wait(1)
        
        wx_0 = MathTex('2 *', font_size=42).move_to(np.array([1.2, -2, 0]))
        wy_0 = MathTex('1 *', font_size=42).move_to(np.array([1.2, -1, 0]))
        self.play(Transform(conn_1, wx_0), Transform(conn_2, wy_0))
        self.wait(2)

        ###########
        '''These combinations of nose and ear neurons make up their own dimension. '''

        eqn_background_2 = Rectangle(color=WHITE, height=1, width=4, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background_2.move_to(np.array([4, -1, 0]))
                
        NN = VGroup(conn_1, nose_group_eqn, conn_2, ears_eqn, nap_eqn)

        eqngrp = MathTex("2 *", "x", "+", "1 *", "y" "=", "n", font_size=42).move_to(np.array([4, -1, 0]))
        
        self.play(TransformMatchingShapes(NN, eqngrp), Transform(eqn_background, eqn_background_2))
        self.wait(2)

        ###
        '''When we look at reality from this dimension, defining it by placing a basis vector on it, we are looking at a region alongside these data measurements- in this case, it's a line.'''

        napName = Text("Nap Dimension").scale(0.6).move_to([4, 0.6, 0])
        
        new_cat_list = get_new_coords(cat_list)
        self.play(Transform(cat_list, new_cat_list))
        self.play(FadeIn(napName))
        self.wait(2)

        # transform back
        new_cat_list_2 = get_inv_coords(new_cat_list)
        self.play(Transform(cat_list, new_cat_list_2))
        self.wait(2)

        ##
        '''If we take our nap equation and plug in any value of ear, such as 1 or 3, we can always get any nap value by solving for nose. These two points map to the same nap value.'''

        eqngrp_2 = MathTex("y", "=", "-2 *", "x", "+", "n", font_size=42).move_to(np.array([4, -1, 0]))
        
        self.play(TransformMatchingShapes(eqngrp, eqngrp_2))
        self.wait(2)

        ### fix nap as 1
        eqngrp_3 = MathTex("y", "=", "-2 *", "x", "+", "1", font_size=42).move_to(np.array([4, -1, 0]))
        self.play(TransformMatchingShapes(eqngrp_2, eqngrp_3))
        self.wait(2)

        to_nap_1_line = Line([-20, 41, 0], [20, -39, 0], color=YELLOW)
        self.play(GrowFromPoint(to_nap_1_line, [0.4, 0.2, 0]))
        self.wait(2)
        
        # # plug in vars and show dots
        eqngrp_4 = MathTex("y", "=", "-2 *", "0", "+", "1", font_size=42).move_to(np.array([4, -1, 0]))
        self.play(TransformMatchingShapes(eqngrp_3, eqngrp_4))
        self.wait(1)
        eqngrp_4b = MathTex("y", "=", "1", font_size=42).move_to(np.array([3, -1, 0]))
        dot1 = Dot([0, 1, 0], color=PURPLE, radius = 0.2)
        self.play(TransformMatchingShapes(eqngrp_4, eqngrp_4b), GrowFromCenter(dot1))

        self.wait(2)

        eqngrp_5 = MathTex("y", "=", "-2 *", "1", "+", "1", font_size=42).move_to(np.array([4, -1, 0]))
        self.play(TransformMatchingShapes(eqngrp_4b, eqngrp_5))
        self.wait(1)
        eqngrp_5b = MathTex("y", "=", "-1", font_size=42).move_to(np.array([3, -1, 0]))
        dot2 = Dot([1, -1, 0], color='#00FFFF', radius = 0.2)
        self.play(TransformMatchingShapes(eqngrp_5, eqngrp_5b), GrowFromCenter(dot2))

        self.wait(2)
        
        # move to 1
        dot1c = Dot([0.4, 0.2, 0], color=PURPLE, radius = 0.2, fill_opacity=0.5)
        dot2c = Dot([0.4, 0.2, 0], color='#00FFFF', radius = 0.2, fill_opacity=0.5)
        dotT = Dot([0.4, 0.2, 0], color=YELLOW, radius = 0.2, fill_opacity=0.5)
        self.play(Transform(dot1, dot1c), Transform(dot2, dot2c), Transform(to_nap_1_line, dotT))

        self.wait(2)
       
        ### transform all
        to_nap_1_line_rep = Line([-20, 41, 0], [20, -39, 0], color=YELLOW)
        to_nap_1_line_tr = Line([1, 20, 0], [1, -20, 0], color=YELLOW)
        dot1b = Dot([1, 2, 0], color=PURPLE, radius = 0.2)
        dot2b = Dot([1, -3, 0], color='#00FFFF', radius = 0.2)
        eqngrp_6 = MathTex("y", "=", "-2 *", "x", "+", "n", font_size=42).move_to(np.array([4, -1, 0]))

        self.play(TransformMatchingShapes(eqngrp_5b, eqngrp_6), ShrinkToCenter(dot1), ShrinkToCenter(dot2), ShrinkToCenter(to_nap_1_line), GrowFromPoint(to_nap_1_line_rep, [0.4, 0.2, 0]))
        self.play(Transform(cat_list, new_cat_list), Transform(to_nap_1_line_rep, to_nap_1_line_tr), run_time = 2)
        self.play(GrowFromCenter(dot1b), GrowFromCenter(dot2b))
        self.wait(2)
    
        # transform back
        # to_nap_1_line_rep = Line([-20, 41, 0], [20, -39, 0], color=YELLOW)
        # new_cat_list_2 = get_inv_coords(new_cat_list)
        # self.play(Transform(cat_list, new_cat_list_2), Transform(to_nap_1_line, to_nap_1_line_rep), ShrinkToCenter(dot1b), ShrinkToCenter(dot2b))
        # self.wait(2)

        # to_nap_1_line_tr_rep = Line([1, 20, 0], [1, -20, 0], color=YELLOW)
        # new_cat_list = get_new_coords(cat_list)
        # self.play(Transform(cat_list, new_cat_list), Transform(to_nap_1_line, to_nap_1_line_tr_rep), run_time = 2.5)
        # self.wait(2)
       