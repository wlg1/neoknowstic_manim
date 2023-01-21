from manim import *
import pdb

class scene_5_2(Scene):
    def construct(self): 
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
            nl.z_index=5
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
        
        ####################    
        '''How can we represent a Data Measurement of a cat person in terms of both nose tip and ear length? We'll use a 2-dimensional coordinate space.

        If we rotate our ear length number line by 90 degrees and put it next to our nose tip number line, we get a coordinate plane where we can represent each cat person using both nose tip and ear length as axes.'''
        
        nose_space = NumberLine(
            x_range=[-7, 7, 1],
            include_numbers=True, label_direction=UP, color=BLUE)
        noseText = Text('Nose \nTip', 
            font_size=16).move_to([1, -1, 0])
        backgroundRectangle1 = BackgroundRectangle(noseText, color=BLACK, fill_opacity=1)
        noseText.z_index = 2
        # backgroundRectangle1.z_index = 1
        
        ear_space = NumberLine(x_range=[-7, 7, 1], 
            include_numbers=True, label_direction=UP, color=BLUE).shift(DOWN*2)
        earText = Text('Ear \nLength', 
            font_size=16).next_to(ear_space, DOWN)
        backgroundRectangle2 = BackgroundRectangle(earText, color=BLACK, fill_opacity=1)
        earText.z_index = 2
        
        # nose_group = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.2).move_to(nose_space.number_to_point(1))
        nose_group = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.2).move_to([1,0,0])
        ear_group = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.2).move_to(ear_space.number_to_point(1))
        
        ear_space_vert = NumberLine(
            x_range=[-7, 7, 1],
            rotation=90 * DEGREES, color=BLUE,
            include_numbers=True,
            label_direction=LEFT)
        ear_group_vert = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.2).move_to([0,1,0])
        earText_vert = Text('Ear \nLength', 
            font_size=16).move_to([-1,1,0])
        backgroundRectangle2_vert = BackgroundRectangle(earText_vert, color=BLACK, fill_opacity=1)  
        earText_vert.z_index = 2
        # backgroundRectangle2_vert.z_index = 1
                      
        self.play(FadeIn(nose_space, noseText, backgroundRectangle1), GrowFromPoint(nose_group, nose_group.get_center()))
        self.wait(1)  
        self.play(FadeIn(ear_space, earText, backgroundRectangle2), GrowFromPoint(ear_group, ear_group.get_center()))
        self.wait(1)  
                
        ear_group_unit = VGroup(ear_space, ear_group, earText, backgroundRectangle2)
        ear_group_unit_vert = VGroup(ear_space_vert, ear_group_vert, earText_vert, backgroundRectangle2_vert)
        self.play(Transform(ear_group_unit, ear_group_unit_vert))
        # self.play(Rotate(ear_space, angle=PI/2))
        
        self.wait(1)
        
        nose_space_2 = NumberLine(
            x_range=[-7, 7, 1],
            include_numbers=True, label_direction=UP, color=BLUE, tick_size = 10)
        ear_space_vert_3 = NumberLine(
            x_range=[-7, 7, 1],
            rotation=90 * DEGREES, color=BLUE, tick_size = 10,
            include_numbers=True,
            label_direction=LEFT)
        numberplane = NumberPlane()
        nose_space_2.z_index = 0   
        ear_space_vert_3.z_index = 0
        numberplane.z_index = 0
        self.play(Transform(nose_space, nose_space_2), Transform(ear_space, ear_space_vert_3), FadeIn(numberplane))
        
        self.wait(1)
        
        ####################
        '''Now, how can we add together the Nose Tip and Ear Length Data Measurements to describe a Cat Person? '''
        self.add(noseText, earText_vert)
                
        '''Let's say we're taking measurements of a cat person named Tom. To describe him, we start at the origin point.'''
        Tom_pt = Dot([0,0,0], radius=0.1, color=PURPLE)
        Tom_pt.z_index = 4
        self.play(FadeIn(Tom_pt))

        '''We find that his nose tip is 1 unit, so we move from the origin to (1,0).'''
        
        # don't use vector or arrow b/c always falls behind all other objs except coord space, even in vectorscene
        # nose_vec = Vector([1, 0, 0], color=RED)
            # stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            # max_stroke_width_to_length_ratio=3)
        # nose_vec.z_index = Tom_pt.z_index + 1
        
        Tom_pt.generate_target()
        Tom_pt.target.move_to([1,0,0])
        
        nose_vec_line = Line([0,0,0],[1, 0, 0], color=RED)
        nose_vec_line.z_index = Tom_pt.z_index + 1
        nose_vec_tip = Triangle(fill_color=RED, fill_opacity=1, color=RED).scale(0.1).rotate(-90*DEGREES).move_to([0.9,0,0])
        nose_vec_tip.z_index = Tom_pt.z_index + 1
        nose_vec = VGroup(nose_vec_line, nose_vec_tip)
        
        # self.play(MoveToTarget(Tom_pt), GrowArrow(nose_vec))
        self.play(MoveToTarget(Tom_pt), GrowFromPoint(nose_vec, [0,0,0]))
        
        self.wait(1)
        
        '''Then we find his ears are 1 unit long, so we move up from (1,0) to (1,1).'''
        
        Tom_pt_11 = Tom_pt.copy().move_to([1,1,0])        
        nose_group_11 = nose_group.copy()
        ear_group_11 = ear_group.copy()
        nose_group_11.remove(nose_group_11[-1])
        ear_group_11.remove(ear_group_11[-1])
        # nose_group_11.z_index = ear_group_11.z_index+1
        self.add(nose_group_11, ear_group_11)
        nose_group_11.generate_target()
        nose_group_11.target.move_to([1,0.975,0])
        ear_group_11.generate_target()
        ear_group_11.target.move_to([1,1,0])
        
        ear_vec_line = Line([1,0,0],[1, 0.8, 0], color=BLUE)
        ear_vec_line.z_index = Tom_pt.z_index + 1
        ear_vec_tip = Triangle(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.1).rotate(360*DEGREES).move_to([1, 0.8, 0])
        ear_vec_tip.z_index = Tom_pt.z_index + 1
        ear_vec = VGroup(ear_vec_line, ear_vec_tip)
        
        self.play(Transform(Tom_pt, Tom_pt_11), MoveToTarget(nose_group_11), MoveToTarget(ear_group_11), GrowFromPoint(ear_vec, [1,0,0]))
        
        self.wait(1)
        self.play(FadeOut(Tom_pt))
        
        self.wait(1)
        
        ####################
        
        '''These arrows that formed a path of step-by-step instructions are called Vectors, which are defined by a length, and a direction. You can place them between two coordinate points, from a tail point to a head point. '''
        
        # self.play(FadeOut(nose_group, ear_group, nose_group_11, ear_group_11))
        