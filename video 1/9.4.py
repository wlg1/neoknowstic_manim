from manim import *
import random
import numpy as np
import pdb

# class scene_9_4(ThreeDScene):
class scene_9_4(Scene):
    def construct(self):        
        ####################
        # def cat_person(ear_length, nose_tip, in_eye, in_whisk, in_mouth, in_color):
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
        
        def get_new_coords(prev_cat_list, tr_range):    
            # w11 = random.randint(-tr_range,tr_range)
            # w12 = random.randint(-tr_range,tr_range)
            # w21 = -w12
            # w22 = w11
            # w11 = random.uniform(0,tr_range)
            # w12 = random.uniform(-tr_range,tr_range)
            # w21 = random.uniform(0,tr_range)
            # w22 = random.uniform(0,tr_range)
            # w11 = 2
            # w12 = 1
            # w21 = -1
            # w22 = 2
            w11 = random.uniform(1,tr_range)
            w12 = random.uniform(1,tr_range)
            w21 = -w12
            w22 = w11
            W = [[w11, w12],
                [w21, w22]]

            new_cat_list = VGroup()
            for prev_cat in prev_cat_list:
                old_x = prev_cat.get_center()[0]
                old_y = prev_cat.get_center()[1]                
                inVec = [[old_x, old_y]]
                
                out_vec = np.matmul(inVec, W)
                # new_cat = prev_cat.copy().move_to([out_vec[0][0], out_vec[0][1], 0])
                new_cat = prev_cat.copy().move_to((numberplane.coords_to_point(out_vec[0][0], out_vec[0][1])))

                new_cat_list.add(new_cat)
            return new_cat_list

        ###########################################
        # use a fn here b/c no need to exclude certain features (though that could've been done within func or using abstraction)

        numberplane = NumberPlane(x_range=(-20, 20, 1), y_range=(-20, 20, 1)).scale(0.5)
        # numberplane = NumberPlane()
        # self.add(numberplane)

        # cat_1 = cat_person(1.5, 0.5, 0.1, BLUE).scale(0.2).move_to([0,1,0])
        # cat_2 = cat_person(0.5, -2, 2, RED).scale(0.2).move_to([3,1,0])
        # cat_3 = cat_person(0.5, -2, 3, PURPLE_E).scale(0.2).move_to([-2,2,0])
        # cat_list = VGroup(cat_1, cat_2, cat_3)
       
        cat_list = VGroup()
        for c in range(10):
            nose_tip = random.uniform(-0.75, 0.75)
            ear_length = random.uniform(0.5, 2)
            # eye_size = random.uniform(0.1, 2)
            # whisk_size = random.uniform(0.1, 2)
            mouth_size = random.uniform(0.1, 2)
            randColor = lambda: random.randint(0,255)
            cat_color = '#%02X%02X%02X' % (randColor(),randColor(),randColor())
            rand_x = random.uniform(-6,6)
            rand_y = random.uniform(-3,3)
            # cat_list.add(cat_person(nose_tip, ear_length, mouth_size, eye_size, whisk_size, cat_color).scale(0.2).move_to((numberplane.coords_to_point(rand_x, rand_y))))
            cat_list.add(cat_person(nose_tip, ear_length, mouth_size, cat_color).scale(0.2).move_to((numberplane.coords_to_point(rand_x, rand_y))))

        #####################
        # longer run times take longer to render, so no adv to just use more shorter anims

        # fade into this. narrates around 15 seconds, so repeat 6 times

        # get list of coords. then instead of transforming, use 'move to' in a path

        transf_list = [get_new_coords(cat_list, 2) for i in range(3)]
        # self.play(AnimationGroup(*[Transform(cat_list, new_cat_list) for new_cat_list in transf_list]))
        self.play(Succession(*[Transform(cat_list, new_cat_list) for new_cat_list in transf_list]), rate_func=linear)
        # for i in range(3):
        #     new_cat_list = get_new_coords(cat_list, 2)
        #     self.play(Transform(cat_list, new_cat_list))
        # , run_time=2.5

        # basis_pairs = [("Fast", "Playful"), ("Funny", "Scheming"), ("Ambitious", "Trusting")]
        # for z in range(3):
        #     curr_pair = basis_pairs[z]
        #     numberplane_copy = numberplane.copy()
        #     x_text = Text(curr_pair[0], color=RED).move_to([4, 0.5, 0])
        #     x_text.z_index=10
        #     x_vec = Arrow([0,0,0], [10,0,0], color=RED, buff=0)
        #     y_text = Text(curr_pair[1], color=BLUE).move_to([3, 3.5,0])
        #     y_text.z_index=10
        #     y_vec = Arrow([0,0,0], [0,10,0], color=BLUE, buff=0)
        #     self.play(FadeIn(numberplane_copy, x_text, x_vec, y_text, y_vec))
        #     # self.add_foreground_mobjects(x_text, y_text)

        #     self.wait(2)

        #     self.play(FadeOut(numberplane_copy, x_text, x_vec, y_text, y_vec))

        #     for i in range(2):
        #         new_cat_list = get_new_coords(cat_list, 2)
        #         self.play(Transform(cat_list, new_cat_list))

        # # afterwards, takes around 20 secs to narrate
        # for i in range(20):
        #     new_cat_list = get_new_coords(cat_list, 2)
        #     self.play(Transform(cat_list, new_cat_list))

        #########
        # self.begin_ambient_camera_rotation(rate=0.1)
        # self.wait(12)