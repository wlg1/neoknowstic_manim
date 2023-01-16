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
        
        box = Rectangle(color=BLACK, height=5.7, width=6, stroke_width=1, fill_color=BLACK).shift(UP*0.33)
        box.z_index = -1
                        
        #####################
        #'''We notice a pattern here that's somewhat like unit conversion. For instance, for every 1 meter, there are 3.28 feet.''' 
        #
        #text_1 = Text("1").shift(LEFT*2+UP*1.5)                
        #meter = Text("Meter").shift(LEFT*4+UP*1.5)
        #self.play(FadeIn(text_1, meter))
        #
        #into = Arrow([0,0,0],[1,0,0]).scale(4).shift(LEFT*0.5+UP*1.5)
        #self.play(FadeIn(into))
        #        
        #text_2 = Text("3.28").shift(RIGHT*2+UP*1.5)
        #feet = Text("Feet").shift(RIGHT*4+UP*1.5)
        #self.play(FadeIn(text_2, feet))
        #        
        #self.wait(1)
        #
        #'''So if an person is 2 meters tall, they're also 6.56 feet tall.'''
        #
        #text_3 = Text("2").shift(LEFT*2+DOWN*1.5)
        #text_4 = Text("6.56").shift(RIGHT*2+DOWN*1.5)
        #                          
        #meter_2 = Text("Meter").shift(LEFT*4+DOWN*1.5)
        #self.play(FadeIn(text_3, meter_2))
        #
        #into_2 = Arrow([0,0,0],[1,0,0]).scale(4).shift(LEFT*0.5+DOWN*1.5)
        #self.play(FadeIn(into_2))
        #
        #feet_2 = Text("Feet").shift(RIGHT*4+DOWN*1.5)
        #self.play(FadeIn(text_4, feet_2))
        #                
        #self.wait(2)
        #
        #####################
        '''So let's convert nose units into nap units. Turning this into an equation, we have 2 * (nose) = 2 nap.'''
        
        # self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        eqn_1 = Tex("2 * Nose = 2 Nap", font_size=53)
        self.play(FadeIn(eqn_1))
        self.add(eqn_1)
        
        # self.wait(2)
        
        ####################
        '''And visually speaking, this means that for every one unit of nose tip, there are two units of Nap Smile.'''
        
        nose_space = NumberLine(
            x_range=[0, 6, 1],
            include_numbers=True,
            label_direction=UP,
        ).scale(2).shift(UP*2)
        
        nap_space = NumberLine(
            x_range=[0, 6, 1],
            include_numbers=True,
            label_direction=DOWN,
        ).scale(2).shift(DOWN*2)
        
        self.add(nose_space, nap_space)
        
        eqn_1.generate_target()
        eqn_1.target.shift(RIGHT*2)
        
        self.play(MoveToTarget(eqn_1), GrowFromPoint(nose_space, eqn_1), GrowFromPoint(nap_space, eqn_1))
        
        #create it as a cat face zzz then remv features b/c if create separately, it won't overlap on top of nose group
        # cat_person_zzz = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), nose.copy(), whiskers.copy(), zzz.copy()).scale(0.3).move_to(nap_space.number_to_point(2))
        # nose_group_1 = VGroup(cat_person_zzz[0].copy(), cat_person_zzz[5].copy())
        
        # that didn't work. the ears and whiskers are throwing off the center of balance.
        
        # use box to get center of balance the same in both. to not display box, put it behind all and make it black
        nose_group_1 = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.3) 
        
        # nose_group_1 = VGroup(face_outline.copy(), nose.copy()).scale(0.3)  
        nose_group_1.move_to(nose_space.number_to_point(1))
        self.add(nose_group_1)
        
        weight_2 = Tex("2 * ", font_size=53).move_to(nose_space.number_to_point(1)).shift(DOWN*1.5)
        self.add(weight_2)
        nose_unit_1 = Line(nose_space.number_to_point(0), nose_space.number_to_point(1), stroke_width=10, color=RED)
        self.add(nose_unit_1)
        
        # move and connect from nose space to middle
                
        # copy on orig nose space
        nose_unit_1_copy = nose_unit_1.copy()
        nose_group_1_copy = nose_group_1.copy()
        
        # in middle
        nose_unit_2 = Line(nose_space.number_to_point(0), nose_space.number_to_point(2), stroke_width=10, color='#FF8BA0').shift(DOWN*1.5)
        nose_group_2 = nose_group_1.copy().move_to(nose_space.number_to_point(2)).shift(DOWN*1.5)
        
        #conns down
        nose_dot = Dot(nose_space.number_to_point(1), radius=0.01)
        mid_dot = Dot(nose_space.number_to_point(2), radius=0.01).shift(DOWN*1.5) #use this instead of nose_unit_2 b/c nose_unit_2's center not small enough
        conn_1 = Line(nose_dot, mid_dot.get_center())
        
        self.wait(1)
        self.play(Transform(nose_unit_1_copy, nose_unit_2), Transform(nose_group_1_copy, nose_group_2), Transform(weight_2, nose_unit_2), GrowFromPoint(conn_1, nose_space.number_to_point(1)))
        self.add(mid_dot)
        
        self.wait(1)
                
        # move and connect from middle to nap space        
        nose_group_2_b = nose_group_1.copy().move_to(nap_space.number_to_point(2))
        nose_unit_2_b = Line(nap_space.number_to_point(0), nap_space.number_to_point(2), stroke_width=10, color='#FF8BA0')
        nap_dot = Dot(nap_space.number_to_point(2), radius=0.01)
        conn_2 = Line(mid_dot, nap_dot)
        self.remove(weight_2) #else will leave behind
        self.play(Transform(nose_unit_1_copy, nose_unit_2_b), Transform(nose_group_1_copy, nose_group_2_b), GrowFromPoint(conn_2, nose_group_2))
        
        self.wait(1)
        weight_line = Line(nose_dot, nap_dot)
        both_conns = VGroup(conn_1, conn_2)
        self.remove(mid_dot)
        self.play(Transform(both_conns, weight_line))
        
        ##################################
        '''Notice the point 1 in the Nose number line and the point 2 in the Nose number line are labeling the same Nose Tip Measurement. This is because we're saying that every nose tip of 1 ALWAYS has a nap smile of 2. '''
        
        #fade nap features in
        
        # self.wait(5)
        
        cat_person_zzz = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy(), zzz.copy(), box.copy()).scale(0.3).move_to(nose_group_2_b.get_center())
        faceBlack = cat_person_zzz[0].copy()
        faceBlack.color=BLACK
        # self.add(faceBlack)
        self.play(FadeIn(cat_person_zzz))
        
        ##################################
        '''Our equation isn't mapping a number, such as 1, to another number, such as 2, but it is mapping a Data Measurement from 1 in the nose space to 2 in the nap space. This is a Change of Units.'''
        
        # CoU = Text("Change of Units", font_size = 30).shift(RIGHT*2)
        # self.play(Write(CoU))
        # self.wait(6)
        
        ##################################
        '''Our unit conversation factor of 2 can be represented, in general, as a variable W, which means how much we should weigh our nose value by to get our nap value. '''
        
        
        ##################################
        ''' Likewise, for every two units of nose tip, there are four units of Nap Smile.'''
        #self.wait(1)
        #
        #self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in [nap_space, nose_space]])  
        #
        #nose_unit_0 = Line(nose_space.number_to_point(0), nose_space.number_to_point(1), stroke_width=10, color=RED)
        #nose_group_0 = VGroup(face_outline.copy(), nose.copy()).scale(0.3).move_to(nose_space.number_to_point(1))
        #self.add(nose_unit_0, nose_group_0)    
        #
        #nose_unit_1 = Line(nose_space.number_to_point(0), nose_space.number_to_point(2), stroke_width=10, color=RED)
        #nose_group_1 = VGroup(face_outline.copy(), nose.copy()).scale(0.3)  
        #nose_group_1.move_to(nose_space.number_to_point(2))
        #self.play(Transform(nose_unit_0, nose_unit_1), Transform(nose_group_0, nose_group_1))
        #
        #weight_2 = Tex("2 * ", font_size=53).move_to(nose_space.number_to_point(2)).shift(DOWN*1.5)
        #self.add(weight_2)
        #
        ## move and connect from nose space to middle
        #        
        ## copy on orig nose space
        #nose_unit_1_copy = nose_unit_1.copy()
        #nose_group_1_copy = nose_group_1.copy()
        #
        ## in middle
        #nose_unit_2 = Line(nose_space.number_to_point(0), nose_space.number_to_point(4), stroke_width=10, color='#FF8BA0').shift(DOWN*1.5)
        #nose_group_2 = nose_group_1.copy().move_to(nose_space.number_to_point(4)).shift(DOWN*1.5)
        #
        ##conns down
        #nose_dot = Dot(nose_space.number_to_point(2), radius=0.01)
        #mid_dot = Dot(nose_space.number_to_point(4), radius=0.01).shift(DOWN*1.5)
        #conn_1 = Line(nose_dot, mid_dot.get_center())
        #
        #self.wait(1)
        #self.play(Transform(nose_unit_1_copy, nose_unit_2), Transform(nose_group_1_copy, nose_group_2), Transform(weight_2, nose_unit_2), GrowFromPoint(conn_1, nose_space.number_to_point(1)))
        #self.add(mid_dot)
        #
        #self.wait(1)
        #        
        ## move and connect from middle to nap space        
        #nose_group_2_b = nose_group_1.copy().move_to(nap_space.number_to_point(4))
        #nose_unit_2_b = Line(nap_space.number_to_point(0), nap_space.number_to_point(4), stroke_width=10, color='#FF8BA0')
        #nap_dot = Dot(nap_space.number_to_point(4), radius=0.01)
        #conn_2 = Line(mid_dot, nap_dot)
        #self.remove(weight_2) #else will leave behind
        #self.play(Transform(nose_unit_1_copy, nose_unit_2_b), Transform(nose_group_1_copy, nose_group_2_b), GrowFromPoint(conn_2, nose_group_2))
        #
        #self.wait(1)
        #weight_line = Line(nose_dot, nap_dot)
        #both_conns = VGroup(conn_1, conn_2)
        #self.remove(mid_dot)
        #self.play(Transform(both_conns, weight_line))
        
        ##################################
        '''We can change this weight, such as making it bigger to w=3, which means for every one unit of nose tip, there are 3 units of Nap Smile, and for every two unit of nose tip, there are 6 units of Nap Smile.'''
        
        ##################################
        '''For this equation, we can also always go from nap smile to nose tip by multiplying nap smile by one half. But this always doesn't work for every equation.'''
        
        
        
        
        