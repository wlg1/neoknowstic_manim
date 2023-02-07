from manim import *
import pdb

class scene_3_2(Scene):
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
                        
        ####################        
        eqn_1 = Tex("2 * (1 Nose) = 2 Nap", font_size=53)

        self.play(FadeIn(eqn_1))
        
        self.wait(1)

        eqn_1b = Tex("0.5 Nose = 0.5 * (1 Nap)", font_size=53)

        self.play(Transform(eqn_1, eqn_1b))
        
        self.wait(1)

        ####################

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
        
        eqn_1.generate_target()
        eqn_1.target.shift(RIGHT*2.5)      
        weight_2 = Tex("0.5 * ", font_size=53).move_to(nose_space.number_to_point(1)).shift(DOWN*1.5)
        
        eqn_1_copy = eqn_1.copy()
        self.play(MoveToTarget(eqn_1), GrowFromPoint(nose_space, eqn_1), GrowFromPoint(nap_space, eqn_1), Transform(eqn_1_copy, weight_2), FadeIn(noseName, napName))
        
        ##################
        # convert nap to nose
        
        nose_group_1 = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.3) 
        
        nose_unit_1 = Line(nap_space.number_to_point(0), nap_space.number_to_point(1), stroke_width=10, color='#FF8BA0')
        nose_group_1.move_to(nap_space.number_to_point(1))  
        
        self.play(GrowFromPoint(nose_unit_1, nap_space.number_to_point(0)), FadeIn(nose_group_1))
        
        ## move and connect from nap space to middle
                
        # copy on orig nose space
        nose_unit_1_copy = nose_unit_1.copy()
        nose_group_1_copy = nose_group_1.copy()
        
        # in middle
        nose_unit_2 = Line(nose_space.number_to_point(0), nose_space.number_to_point(0.5), stroke_width=10, color='#FF8BA0').shift(DOWN*1.5)
        nose_group_2 = nose_group_1.copy().move_to(nose_space.number_to_point(0.5)).shift(DOWN*1.5)
        
        #conns down
        nose_dot = Dot(nap_space.number_to_point(1), radius=0.01)
        mid_dot = Dot(nose_space.number_to_point(0.5), radius=0.01).shift(DOWN*1.5) 
        conn_1 = Line(nose_dot, mid_dot.get_center())
        
        self.play(Transform(nose_unit_1_copy, nose_unit_2), Transform(nose_group_1_copy, nose_group_2), Transform(eqn_1_copy, nose_unit_2), GrowFromPoint(conn_1, nap_space.number_to_point(1)))
        self.add(mid_dot)
        
        self.wait(1)
                
        # move and connect from middle to nose space        
        nose_group_2_b = nose_group_1.copy().move_to(nose_space.number_to_point(0.5))
        nose_unit_2_b = Line(nose_space.number_to_point(0), nose_space.number_to_point(0.5), stroke_width=10, color=RED)
        nap_dot = Dot(nose_space.number_to_point(0.5), radius=0.01)
        conn_2 = Line(mid_dot, nap_dot)
        self.remove(weight_2, eqn_1_copy) #else will leave behind
        self.play(Transform(nose_unit_1_copy, nose_unit_2_b), Transform(nose_group_1_copy, nose_group_2_b), GrowFromPoint(conn_2, nose_group_2))
        
        self.wait(1)
        weight_line = Line(nose_dot, nap_dot)
        both_conns = VGroup(conn_1, conn_2)
        self.remove(mid_dot)
        self.play(Transform(both_conns, weight_line))
        
        ##################################                
        self.wait(2)
        
        #fade nap features in
        # cat_person_zzz = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), zzz.copy(), box.copy(), mouth_smile.copy()).scale(0.3).move_to(nose_group_2_b.get_center())
        # self.play(FadeIn(cat_person_zzz))
        
        
        
        
        
        