from manim import *
import pdb

class scene_6_2(Scene):
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

        ear_space = NumberLine(
            x_range=[0, 5, 1],
            include_numbers=True,
            label_direction=UP,
        ).scale(1.2).shift(UP*2.5+LEFT*1.6)

        nap_space = NumberLine(
            x_range=[0, 5, 1],
            include_numbers=True,
            label_direction=DOWN,
        ).scale(1.2).shift(LEFT*1.6)
        
        ear_group_1 = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.2).move_to(ear_space.number_to_point(1)).shift(UP*0.2)   

        ear_vec_line = Line(ear_space.number_to_point(0), ear_space.number_to_point(0.95), color=BLUE, fill_opacity=0.9)
        ear_vec_line.z_index = 4
        ear_vec_tip = Triangle(fill_color=BLUE, fill_opacity=0.9, color=BLUE).scale(0.07).rotate(-90*DEGREES).move_to(ear_space.number_to_point(0.95))
        ear_vec_tip.z_index = 4
        ear_unit_1 = VGroup(ear_vec_line, ear_vec_tip)
        
        # self.add(ear_space, nap_space, ear_group_1, ear_unit_1)

        ####################
        numberplane = NumberPlane()

        Tom_pt = Dot([0,0,0], radius=0.1, color=PURPLE)
        Tom_pt.z_index = 4

        nose_vec_line = Line([0,0,0],[0.8, 0, 0], color=RED)
        nose_vec_line.z_index = Tom_pt.z_index + 1
        nose_vec_tip = Triangle(fill_color=RED, fill_opacity=1, color=RED).scale(0.1).rotate(-90*DEGREES).move_to([0.8,0,0])
        nose_vec_tip.z_index = Tom_pt.z_index + 1
        nose_vec = VGroup(nose_vec_line, nose_vec_tip)

        ear_group = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.2).move_to([0,1,0])

        ear_vec_line = Line([0,0,0],[0, 0.8, 0], color=BLUE)
        ear_vec_line.z_index = Tom_pt.z_index + 1
        ear_vec_tip = Triangle(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.1).rotate(360*DEGREES).move_to([0, 0.8, 0])
        ear_vec_tip.z_index = Tom_pt.z_index + 1
        ear_vec = VGroup(ear_vec_line, ear_vec_tip)

        ###

        nap_space_IS = VGroup(Line([0,0,0], [5, 0, 0], color=WHITE, stroke_width=1))
        for x in range(6):
            nap_space_IS.add(Line([x, 0.1,0], [x, -0.1, 0], color=WHITE, stroke_width=1))
            nap_space_IS.add(Tex(str(x), color=WHITE, stroke_width=1, font_size=38).move_to([x,0,0]).shift(DOWN*0.38))
        nap_space_IS.move_to(np.array([3.7, 2.5, 0]))
        # nap_space_IS.shift(2.5*LEFT)

        NS_bg = Rectangle(color=WHITE, height=1.4, width=6.5, fill_color=BLACK, fill_opacity=1, stroke_width=2).move_to(np.array([3.7, 2.5, 0]))
        # NS_bg.z_index = 2
        # for item in nap_space_IS:
        #     item.z_index = NS_bg.z_index + 1
        # NS_bg = BackgroundRectangle(nap_space_IS, color=BLACK, fill_opacity=1)

        nap_space_IS.scale(1.2)
        nap_space_2 = NumberLine(
            x_range=[0, 5, 1],
            include_numbers=True,
            label_direction=DOWN,
        ).scale(1.2).shift(2.5*RIGHT).move_to(np.array([3.7, 2.5, 0]))

        ear_group_nap = ear_group_1.copy().move_to(nap_space_2.number_to_point(0.75)).shift(UP*0.2)
        
        ear_vec_line_nap = Line(nap_space_2.number_to_point(0), nap_space_2.number_to_point(0.7), color='#ADD8E6', fill_opacity=0.9)
        ear_vec_line_nap.z_index = 5
        ear_vec_tip_nap = Triangle(fill_color='#ADD8E6', fill_opacity=0.9, color='#ADD8E6').scale(0.07).rotate(-90*DEGREES).move_to(nap_space_2.number_to_point(0.7))
        ear_vec_tip_nap.z_index = 5
        ear_unit_nap = VGroup(ear_vec_line_nap, ear_vec_tip_nap).shift(UP*0.1)

        # use dots b/c shifts down/up, not exactly on pt
        # mid_dot = Dot(ear_space.number_to_point(0.75), radius=0.01).shift(DOWN*1) 
        nap_dot = Dot(nap_space_2.number_to_point(0.75), radius=0.01).shift(UP*0.2)
        conn_ear = Line([0,1,0], nap_dot)

        self.add(nap_space)
        self.play(Transform(nap_space, nap_space_2), run_time=2)
        self.play(FadeIn(numberplane, ear_group, ear_vec, NS_bg, nap_space_IS))

        self.play(GrowFromPoint(ear_group_nap, ear_group_nap.get_center()), FadeIn(ear_unit_nap), GrowFromPoint(conn_ear, [0,1,0]), run_time=2)
        
        self.wait(2)