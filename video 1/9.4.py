from manim import *
import random
import numpy as np
import pdb

# class scene_9_4(ThreeDScene):
class scene_9_4(Scene):
    def construct(self):        
        ####################
        def cat_person(ear_length, nose_tip, in_mouth, in_color):
            # ear_length = 1.5  #lowest is 0.5. each +1 is 0.5; largest is 1.5
            # nose_tip = 1.5  # each unit of 1 is 0.25. 3 is 0.75, etc
            
            left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0], color=in_color)
            left_ear_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0], color=in_color)
            left_ear = VGroup(left_ear_1, left_ear_2)
            
            right_ear_1 = Line([1.5, 0, 0], [1, ear_length+1.5, 0], color=in_color)
            right_ear_2 = Line([1, ear_length+1.5, 0], [0, 0, 0], color=in_color)
            right_ear = VGroup(right_ear_1, right_ear_2)
                    
            face_outline = Circle(radius=1.75, color=in_color, fill_color=BLACK, fill_opacity=1, stroke_width=2).move_to([0, 0, 0])
            
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

            return VGroup(face_outline.copy(),  left_eye.copy(), right_eye.copy(), left_ear.copy(), right_ear.copy(), mouth_smile.copy(), whiskers.copy(), box.copy())
        
        def get_new_coords(prev_cat):
            old_x = prev_cat.get_center()[0]
            old_y = prev_cat.get_center()[1]

            inVec = [[old_x, old_y]]

            w11 = random.uniform(-3,3)
            w12 = random.uniform(-3,3)
            w21 = random.uniform(-3,3)
            w22 = random.uniform(-3,3)
            W = [[w11, w12],
                [w21, w22]]
            
            out_vec = np.matmul(inVec, W)
            new_cat = prev_cat.copy().move_to([out_vec[0][0], out_vec[0][1], 0])

            return new_cat

        ###########################################
        # use a fn here b/c no need to exclude certain features (though that could've been done within func or using abstraction)

        numberplane = NumberPlane()
        # self.add(numberplane)

        cat_1 = cat_person(1.5, 0.5, 0.1, BLUE).scale(0.2).move_to([0,1,0])
        cat_2 = cat_person(0.5, -2, 2, RED).scale(0.2).move_to([3,1,0])
        cat_3 = cat_person(0.5, -2, 3, PURPLE_E).scale(0.2).move_to([-2,2,0])

        cat_list = [cat_1, cat_2, cat_3]
        for cat in cat_list:
            self.add(cat)

        for cat in cat_list:
            new_cat_list = []
            new_cat_list.append(Transform(cat, get_new_coords(cat)))
            self.play(*new_cat_list)

        #########
        # self.begin_ambient_camera_rotation(rate=0.1)
        # self.wait(12)