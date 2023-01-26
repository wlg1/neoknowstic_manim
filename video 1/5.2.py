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
            include_numbers=True, label_direction=DOWN, color=BLUE)
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
        self.wait(2)  
        self.play(FadeIn(ear_space, earText, backgroundRectangle2), GrowFromPoint(ear_group, ear_group.get_center()))
        self.wait(2)  
                
        ear_group_unit = VGroup(ear_space, ear_group, earText, backgroundRectangle2)
        ear_group_unit_vert = VGroup(ear_space_vert, ear_group_vert, earText_vert, backgroundRectangle2_vert)
        self.play(Transform(ear_group_unit, ear_group_unit_vert))
        # self.play(Rotate(ear_space, angle=PI/2))
        
        self.wait(2)
        
        nose_space_2 = NumberLine(
            x_range=[-7, 7, 1],
            include_numbers=True, label_direction=DOWN, color=BLUE, tick_size = 10)
        ear_space_vert_3 = NumberLine(
            x_range=[-7, 7, 1],
            rotation=90 * DEGREES, color=BLUE, tick_size = 10,
            include_numbers=True,
            label_direction=LEFT)
        numberplane = NumberPlane()
        nose_space_2.z_index = 1   
        ear_space_vert_3.z_index = 1
        numberplane.z_index = 0
        self.play(Transform(nose_space, nose_space_2), Transform(ear_space, ear_space_vert_3), FadeIn(numberplane))
        
        self.wait(2)
        
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
        
        nose_vec_line = Line([0,0,0],[0.8, 0, 0], color=RED)
        nose_vec_line.z_index = Tom_pt.z_index + 1
        nose_vec_tip = Triangle(fill_color=RED, fill_opacity=1, color=RED).scale(0.1).rotate(-90*DEGREES).move_to([0.8,0,0])
        nose_vec_tip.z_index = Tom_pt.z_index + 1
        nose_vec = VGroup(nose_vec_line, nose_vec_tip)
        
        # self.play(MoveToTarget(Tom_pt), GrowArrow(nose_vec))
        self.play(MoveToTarget(Tom_pt), GrowFromPoint(nose_vec, [0,0,0]))
        
        self.wait(2)
        
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
        
        self.wait(2)
        self.play(FadeOut(Tom_pt))
        
        self.wait(2)
        
        ####################        
        '''These arrows that formed a path of step-by-step instructions are called Vectors, which are defined by a length, and a direction. You can place them between two coordinate points, from a tail point to a head point. '''
        
        self.play(ShrinkToCenter(nose_group), ShrinkToCenter(ear_group), ShrinkToCenter(nose_group_11), ShrinkToCenter(ear_group_11), FadeOut(nose_vec, ear_vec))
        
        vector_1 = Vector([1,0,0], color=PURPLE)
        self.play(GrowArrow(vector_1))
        
        self.wait(2)
        vector_2 = Vector([2,0,0], color=PURPLE)
        self.play(Transform(vector_1, vector_2))
        
        self.wait(2)
        vector_3 = Vector([2,2,0], color=PURPLE)
        self.play(Transform(vector_1, vector_3))
        
        tail = Dot([0,0,0], radius=0.1, color=GOLD)
        tail.generate_target()
        tail.target.move_to([2,2,0])
        
        self.wait(2)
        self.play(FadeIn(tail))
        self.wait(2)
        self.play(MoveToTarget(tail))
        self.wait(2)
        
        ####################        
        '''Unlike the coordinate points, which are permanently fixed where they are, the vectors can be moved anywhere in coordinate space. '''
        
        dot1 = Dot([0,0,0], radius=0.1, color=GOLD)
        dot1_text = Text('(0, 0)', font_size=16).next_to([0,0,0], 0.3*LEFT+DOWN)
        dot2 = Dot([2,2,0], radius=0.1, color=GOLD)
        dot2_text = Text('(2, 2)', font_size=16).next_to([2,2,0], 0.3*LEFT+UP)
        self.play(FadeIn(dot1, dot1_text, dot2, dot2_text))
        self.remove(tail)
        
        vector_4 = Arrow([2,0,0],[4,2,0], color=PURPLE, buff=0)
        self.play(Transform(vector_1, vector_4))
        
        self.wait(2)
        
        '''This right-facing vector of length 1 is the SAME one that's been moved here. But it is not the same as this vector, or this one.'''
        
        vector_5 = Arrow([3,1,0],[5,3,0], color=PURPLE, buff=0)
        self.play(Transform(vector_1, vector_5))        
        self.wait(2)
        
        vector_6 = Arrow([3,1,0],[5.5,3.5,0], color=PURPLE, buff=0)
        self.play(Transform(vector_1, vector_6))        
        self.wait(2)
        
        vector_7 = Arrow([3,1,0],[5.828,1,0], color=PURPLE, buff=0)
        self.play(Transform(vector_1, vector_7))        
        self.wait(2)
        
        ####################
        '''Since the vectors can be moved, it seems like there's no fixed association between a vector and a Data Measurement. But for the ease of demonstration, we'll informally say there is to help us get a high-level understanding of how vectors add features together.'''
        
        self.play(FadeOut(dot1, dot1_text, dot2, dot2_text))
        
        self.wait(2)
        
        #remake b/c shrunk
        nose_group = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.2).move_to([1,0,0])
        ear_group = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.2).move_to([0,1,0])
        self.play(GrowFromPoint(nose_group, [1,0,0]), GrowFromPoint(ear_group, [0,1,0]))
        
        self.wait(2)
        
        ########## Show equations for imgs 
        
        '''Looking back at our example with Tom'''
               
        eqn_background = Rectangle(color=WHITE, height=1.4, width=4, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background.move_to(np.array([3.7, 1, 0]))
        
        equal_sign = Text('=', font_size=32)
        equal_sign.move_to(np.array([2, 1, 0]))
        
        nose_group_eqn = VGroup(face_outline.copy(), nose.copy(), box.copy()).scale(0.2).move_to(np.array([3, 1, 0]))
        
        plus_sign = Text('+', font_size=32)
        plus_sign.move_to(np.array([4, 1, 0]))
                
        ears_eqn = VGroup(face_outline.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.2).move_to(np.array([5, 1, 0]))
        
        self.remove(vector_1)
        self.play(FadeIn(eqn_background, nose_group_eqn, ears_eqn))
        
        self.wait(2)
        
        ######### Show vector equations for [1,1]
        
        ''', we'll represent our vectors using matrix brackets, whose values describe the head of a vector, with its tail on the origin.'''
        
        eqn_background_2 = Rectangle(color=WHITE, height=1.4, width=4, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        eqn_background_2.move_to(np.array([3.7, -1, 0]))
        
        equal_sign_2 = Text('=', font_size=32)
        equal_sign_2.move_to(np.array([2, -1, 0]))
        
        mat_1 = MathTex(r"\begin{bmatrix} 1 \\ 0 \end{bmatrix}")
        mat_1.move_to(np.array([3, -1, 0])).scale(0.85)
        
        plus_sign_2 = Text('+', font_size=32)
        plus_sign_2.move_to(np.array([4, -1, 0]))
        
        mat_2 = MathTex(r"\begin{bmatrix} 0 \\ 1 \end{bmatrix}")
        mat_2.move_to(np.array([5, -1, 0])).scale(0.85)
        
        ear_vec_line = Line([0,0,0],[0, 0.8, 0], color=BLUE)
        ear_vec_line.z_index = Tom_pt.z_index + 1
        ear_vec_tip = Triangle(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.1).rotate(360*DEGREES).move_to([0, 0.8, 0])
        ear_vec_tip.z_index = Tom_pt.z_index + 1
        ear_vec = VGroup(ear_vec_line, ear_vec_tip)
                
        self.play(FadeOut(backgroundRectangle1, backgroundRectangle2_vert, noseText, earText, earText_vert), GrowFromPoint(nose_vec, [0,0,0]), GrowFromPoint(ear_vec, [0,0,0]), FadeIn(eqn_background_2, equal_sign_2, mat_1, mat_2, shift=DOWN))
        
        self.wait(2)
                
        ###############
        
        '''We'll show that adding these two features together is the same as adding the two vectors pointing to these features'''
                
        Tom_pt = Dot([0,0,0], radius=0.1, color=PURPLE)
        Tom_pt.z_index = 4
        self.play(FadeIn(Tom_pt))

        '''When a vector's tail is on the origin, this vector points to the same Data Measurement as point (1,0). So far, we have this Data Measurement as a partial Data Measurement.'''
                
        Tom_pt.generate_target()
        Tom_pt.target.move_to([1,0,0])
        
        nose_vec_line = Line([0,0,0],[1, 0, 0], color=RED)
        nose_vec_line.z_index = Tom_pt.z_index + 1
        nose_vec_tip = Triangle(fill_color=RED, fill_opacity=1, color=RED).scale(0.1).rotate(-90*DEGREES).move_to([0.9,0,0])
        nose_vec_tip.z_index = Tom_pt.z_index + 1
        nose_vec = VGroup(nose_vec_line, nose_vec_tip)
        
        self.play(MoveToTarget(Tom_pt))
        
        self.wait(2)
        
        '''When you add it to the vector going up to (0, 1),'''
        
        ear_vec_line_2 = Line([1,0,0],[1, 0.8, 0], color=BLUE)
        ear_vec_line_2.z_index = Tom_pt.z_index + 1
        ear_vec_tip_2 = Triangle(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.1).rotate(360*DEGREES).move_to([1, 0.8, 0])
        ear_vec_tip_2.z_index = Tom_pt.z_index + 1
        ear_vec_2 = VGroup(ear_vec_line_2, ear_vec_tip_2)
        
        self.play(Transform(ear_vec, ear_vec_2), FadeIn(plus_sign, plus_sign_2))
        
        self.wait(2)

        ######### Sum up vectors to get [1,1]
        
        '''it's as if you're given an instruction to add the partial Data Measurement on [1, 0] with the Data Measurement on [0, 1].'''
        
        dot3_text = Text('(1, 1)', font_size=16).next_to([1, 1, 0], 0.3*LEFT+DOWN*2.5)
                             
        mat_3 = MathTex(r"\begin{bmatrix} 1 \\ 1 \end{bmatrix}")
        mat_3.move_to(np.array([3, -1, 0])).scale(0.85)
        
        #########
        
        Tom_pt_11 = Tom_pt.copy().move_to([1,1,0])        
        nose_group_11 = nose_group.copy()
        ear_group_11 = ear_group.copy()
        nose_group_11.remove(nose_group_11[-1])
        ear_group_11.remove(ear_group_11[-1])
        self.add(nose_group_11, ear_group_11)
        nose_group_11.generate_target()
        nose_group_11.target.move_to([1,0.975,0])
        ear_group_11.generate_target()
        ear_group_11.target.move_to([1,1,0])
                        
        self.remove(mat_1, mat_2)
        self.play(FadeOut(plus_sign_2, mat_2, shift=LEFT*2), Transform(mat_1, mat_3), Transform(Tom_pt, Tom_pt_11), MoveToTarget(nose_group_11), MoveToTarget(ear_group_11), FadeIn(equal_sign))
        
        self.wait(2)
        self.play(FadeOut(Tom_pt))
        
        self.wait(2)
        
        '''Therefore, Tom is on vector [1,1]. You can get to Tom either by the path of these two added vectors, or by the vector pointing to [1,1].'''
        
        # Tom_vec = Vector([1,1,0], color= PURPLE)        
        tom_vec_line = Line([0,0,0],[0.8, 0.8, 0], color=PURPLE)
        tom_vec_line.z_index = Tom_pt.z_index + 1
        tom_tip = Triangle(fill_color=PURPLE, fill_opacity=1, color=PURPLE).scale(0.1).rotate(-45*DEGREES).move_to([0.8, 0.8, 0])
        tom_tip.z_index = Tom_pt.z_index + 1
        Tom_vec = VGroup(tom_vec_line, tom_tip)
        
        self.play(GrowFromPoint(Tom_vec, [0,0,0]))
        
        self.wait(2)
        
        '''Because this combination of nose tip and ear length describes our cat people input, we call this 2D coordinate space our Input Space.'''
        
        # self.play([FadeOut(mob)for mob in self.mobjects if mob != numberplane])
        
        # input_space_text = Text("Input Space").shift(UP+LEFT)
        # self.play(Write(input_space_text))
        
        # self.wait(2)