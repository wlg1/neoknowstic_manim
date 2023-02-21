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
        nose_new = Vector(np.array([2, -1, 0]), color='#FF8BA0', stroke_width=6, max_tip_length_to_length_ratio=0.15)
        ear_orig = Vector(np.array([0, 1, 0]), color=BLUE)
        ear_orig_copy = ear_orig.copy()
        ear_new = Vector(np.array([1, 2, 0]), color='#ADD8E6')

        # columns of inverse go to basis
        nap_orig = Vector(np.array([0.4, 0.2, 0]), color=YELLOW, max_stroke_width_to_length_ratio =10)
        nap_new = Vector(np.array([1, 0, 0]), color=ORANGE)
        
        luck_orig = Vector(np.array([-0.2, 0.4, 0]), color=GRAY, max_stroke_width_to_length_ratio =10)
        luck_new = Vector(np.array([0, 1, 0]), color=GREEN)

        # matrix = [[2, 1], [-1, 2]]
        # self.apply_matrix(matrix)
        
        ##############################
        numberplane = NumberPlane()
        self.add(numberplane)
       
        # self.play(GrowArrow(nose_orig), GrowArrow(ear_orig))
        # self.play(GrowArrow(nap_orig), GrowArrow(luck_orig))
        
        self.add(ear_group_1_0, nose_group_1_0, nap_1_0, luck_1_0)
        # self.wait(1)
        # self.add(GrowFromCenter(ear_group_1_0), GrowFromCenter(nose_group_1_0), GrowFromCenter(nap_1_0), GrowFromCenter(luck_1_0))

        self.add(nose_orig, ear_orig)
        # , nap_orig, luck_orig, nose_new, ear_new)

        # self.wait(1)
        self.play(Transform(ear_group_1_0, ear_group_1_copy), Transform(nose_group_1_0, nose_group_1_copy), Transform(nap_1_0, nap_1_copy), Transform(luck_1_0, luck_1_copy), Transform(nose_orig, nap_new), Transform(ear_orig, luck_new))

        self.wait(1)

        self.play(Transform(nose_orig, nose_orig_copy), Transform(ear_orig, ear_orig_copy))

        self.wait(1)