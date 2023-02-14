from manim import *

class CatFace_shadow(ThreeDScene):
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
            nl.z_index=3
            nl.stroke_width=2  #default is 4
        
        for whisk in whiskers:
            whisk.z_index=3
            whisk.stroke_width=2
                   
        mouth_smile = ArcBetweenPoints([-0.5, -0.75,0], [0.5, -0.75,0], stroke_width=2)
        mouth_smile.z_index=3

        box = Rectangle(color=BLACK, height=5.7, width=6, stroke_width=0.01, fill_color=BLACK).shift(UP*0.33)
        box.z_index = -1

        ###########
        neck = Line([-3, 0, 0], [-3, 0.4, 0])
        
        top_line = Line([-3.75, 0, 0], [-2.25, 0, 0])
        left_line = Line([-3.75, 0, 0], [-3, -1.75, 0])
        right_line = Line([-2.25, 0, 0], [-3, -1.75, 0])
        body = VGroup(top_line, left_line, right_line)
        
        left_arm = Line([-3.75, 0, 0], [-4, -1.5, 0])  #shoulder to hand
        right_arm = Line([-2.25, 0, 0], [-2, -1.5, 0])
        
        left_leg = Line([-3, -1.75, 0], [-3.5, -3.25, 0])  #waist to foot
        right_leg = Line([-3, -1.75, 0], [-2.5, -3.25, 0])
        
        #############
        self.set_camera_orientation(phi=70 * DEGREES)

        cat_face = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy())
        # , box.copy())

        self.play(
            cat_face.animate.shift([0, 0, 2]),
            run_time=2
        )

        #######
        shadow_node = Circle(radius=1.75, color=RED, fill_color=BLACK, fill_opacity=1, stroke_width=2).move_to([0, 0, 0])
        shadow_node.z_index=3

        temp_catface = VGroup(shadow_node.copy(), left_eye.copy(), right_eye.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy()).scale(0.3).move_to(np.array([-3, 1, 0]))   

        shadow = VGroup(temp_catface.copy(), neck.copy(), body.copy(), left_arm.copy(), right_arm.copy(), left_leg.copy(), right_leg.copy()).scale(1.2).move_to([-2, -2, 0])  

        shadow_noFace = VGroup(shadow[0][0].copy(), shadow[1].copy(), shadow[2].copy(), shadow[3].copy(), shadow[4].copy(), shadow[5].copy(), shadow[6].copy())
        
        self.add(shadow_noFace)

        cat_face_copy = cat_face.copy()
        self.play(Transform(cat_face_copy, shadow[0]), run_time=2)
        self.add(shadow)

        self.wait(1)

        #######
        # shadow_node_2 = Circle(radius=1.75, color=BLUE, fill_color=BLACK, fill_opacity=1, stroke_width=2)
        # shadow_node_2.z_index=3
        # temp_catface = VGroup(shadow_node.copy(), left_eye.copy(), right_eye.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy()).scale(0.3).move_to(np.array([-3, 1, 0]))   
        # shadow = VGroup(temp_catface[0].copy(), neck.copy(), body.copy(), left_arm.copy(), right_arm.copy(), left_leg.copy(), right_leg.copy()).scale(1.2).move_to([-2, -2, 0]) 
        #    
        # shadow_2 = VGroup(shadow_node_2.copy(), left_ear.copy(), right_ear.copy(), box.copy()).scale(0.65).move_to([2, -2, 0])        


        #######
        # shadow_node_3 = Circle(radius=1.75, color=PURPLE, fill_color=BLACK, fill_opacity=1, stroke_width=2)        
        # shadow_node_3.z_index=3
        # shadow_3 = VGroup(shadow_node_3.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), mouth_smile.copy(), box.copy()).scale(0.65).move_to([0, -4, 0])   

        # conn_1 = Line(shadow.get_center(), shadow_3.get_center())
        # conn_2 = Line(shadow_2.get_center(), shadow_3.get_center())
        # conn_1.z_index = -1
        # conn_2.z_index = -1
        
        # self.play(FadeIn(shadow, shadow_2[0], shadow_3[0]))
        # self.play(GrowFromPoint(conn_1, shadow.get_center()), GrowFromPoint(conn_2, shadow_2.get_center()))
        
        # # Animate the cat_face rotating
        # self.begin_ambient_camera_rotation(rate=0.03)

        # cat_face_copy = cat_face.copy()
        # self.play(Transform(cat_face_copy, shadow[0]), run_time=2)
        # self.add(shadow)  #scene 1 w/o, s8 w/

        # cat_face_copy_2 = cat_face.copy()
        # self.play(Transform(cat_face_copy_2, shadow_2[0]), run_time=2)
        # self.add(shadow_2) #scene 1 w/o, s8 w/

        # self.play(GrowFromCenter(shadow_3.copy())) #scene 1 w/o, s8 w/

        # self.wait(4)