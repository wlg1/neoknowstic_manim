from manim import *
import pdb

class scene_1_1(Scene):
    def construct(self):
        ##################################################
        ear_length = 1  #lowest is 0.5. each +1 is 0.5; largest is 1.5
        nose_tip = -0.5  # each unit of 1 is 0.25. 3 is 0.75, etc
        
        left_ear_1 = Line([-1.5, 0, 0], [-1, ear_length+1.5, 0])
        left_ear_2 = Line([-1, ear_length+1.5, 0], [0, 0, 0])
        left_ear = VGroup(left_ear_1, left_ear_2)
        
        right_ear_1 = Line([1.5, 0, 0], [1, ear_length+1.5, 0])
        right_ear_2 = Line([1, ear_length+1.5, 0], [0, 0, 0])
        right_ear = VGroup(right_ear_1, right_ear_2)
                
        face_outline = Circle(radius=1.75, color=WHITE, fill_color=BLACK, fill_opacity=1).move_to([0, 0, 0])
        
        # left_eye = Dot(color=WHITE).move_to([-1, 0.5, 0])
        # right_eye = Dot(color=WHITE).move_to([1, 0.5, 0])
        
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
        
        mouth = Ellipse(width=0.4, height=0.8, color=WHITE).move_to([0, -0.75, 0])
               
        left_ear.z_index=1
        right_ear.z_index=1
               
        face_outline.z_index=3
        # left_eye.z_index=3
        # right_eye.z_index=3
                
        for nl in nose:
            nl.z_index=3
        
        for whisk in whiskers:
            whisk.z_index=3
            
        # face_group = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy()).scale(0.3).move_to(np.array([-3, 1, 0]))   
        
        ##################################################       
        
        left_brow = ArcBetweenPoints([-0.3, -0.75,0], [0.3, -0.75,0]).rotate(180*DEGREES).move_to([-0.6, 0.2, 0])
        right_brow = ArcBetweenPoints([-0.3, -0.75,0], [0.3, -0.75,0]).rotate(180*DEGREES).move_to([0.6, 0.2, 0])
        left_brow.z_index=3
        left_brow.stroke_width = 2
        right_brow.z_index=3
        right_brow.stroke_width = 2

        left_eye_zzz = ArcBetweenPoints([-0.5, -0.9,0], [0.5, -0.9,0]).rotate(180*DEGREES).move_to([-0.7, -0.2, 0])
        right_eye_zzz = ArcBetweenPoints([-0.5, -0.9,0], [0.5, -0.9,0]).rotate(180*DEGREES).move_to([0.7, -0.2, 0])
        # left_eye = Line([-0.3, -0.75,0], [0.3, -0.75,0]).rotate(180*DEGREES).move_to([-0.6, -0.2, 0])
        # right_eye = Line([-0.3, -0.75,0], [0.3, -0.75,0]).rotate(180*DEGREES).move_to([0.6, -0.2, 0])
        left_eye_zzz.z_index=3
        right_eye_zzz.z_index=3
        left_eye_zzz.stroke_width = 2
        right_eye_zzz.stroke_width = 2

        left_eye = Dot(color=WHITE).move_to([-0.6, -0.2, 0]).scale(2)
        right_eye = Dot(color=WHITE).move_to([0.6, -0.2, 0]).scale(2)
        left_eye.z_index=3
        right_eye.z_index=3
        human_face = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_brow.copy(), right_brow.copy()).scale(0.3).move_to(np.array([-3, 1, 0]))   
        neck = Line([-3, 0, 0], [-3, 0.4, 0])
        
        top_line = Line([-3.75, 0, 0], [-2.25, 0, 0])
        left_line = Line([-3.75, 0, 0], [-3, -1.75, 0])
        right_line = Line([-2.25, 0, 0], [-3, -1.75, 0])
        body = VGroup(top_line, left_line, right_line)
        
        left_arm = Line([-3.75, 0, 0], [-4, -1.5, 0])  #shoulder to hand
        right_arm = Line([-2.25, 0, 0], [-2, -1.5, 0])
        
        left_leg = Line([-3, -1.75, 0], [-3.5, -3.25, 0])  #waist to foot
        right_leg = Line([-3, -1.75, 0], [-2.5, -3.25, 0])
        
        tail = ArcBetweenPoints([-3, -1.75, 0], [-1.2, -1.2,0])
        
        human_top = VGroup(human_face, neck.copy(), body.copy(), left_arm.copy(), right_arm.copy())

        ###
        human_face_2 = VGroup(face_outline.copy(), left_eye_zzz.copy(), right_eye_zzz.copy()).scale(0.3).move_to(np.array([-3, 1, 0]))   

        human_top_2 = VGroup(human_face_2, neck.copy(), body.copy(), left_arm.copy(), right_arm.copy()).scale(0.75).move_to([3, -1.5, 0]).shift(UP)

        ##################################################

        book_top_left = Line([-3, 2, 0], [0, 1, 0], color=BLUE)
        book_top_right = Line([3, 2, 0], [0, 1, 0], color=BLUE)
        book_left = Line([-3, 2, 0], [-3, -1, 0], color=BLUE)
        book_bot_left = Line([-3, -1, 0], [0, -3, 0], color=BLUE)
        book_bot_right = Line([3, -1, 0], [0, -3, 0], color=BLUE)
        book_right = Line([3, 2, 0], [3, -1, 0], color=BLUE)
        book_mid = Line([0, 1, 0], [0, -3, 0], color=BLUE)
        book = VGroup(book_top_left, book_top_right, book_left, book_bot_left, book_bot_right, book_right, book_mid)
        
        ##################################################
        # cat_face = face_group.copy().move_to([1, -1.5, 0]).scale(0.65)
        # self.add(cat_face) 
        
        human_top.scale(0.75).move_to([3, -1.5, 0]).shift(UP)
        book.scale(0.35).move_to([3, -1.5, 0]).shift(DOWN*0.5)
        self.add(human_top, book)

        self.wait(2)

        self.play(Transform(human_face[1], human_face_2[1]), Transform(human_face[2], human_face_2[2]), FadeOut(human_face[3], human_face[4]))

        self.wait(2)

        # zzz = Text("...zZz...", font_size = 40, color=WHITE).scale(0.75).move_to([3, -1.5, 0]).shift(UP)
        
        # self.play(Write(zzz))
        # self.wait(1)
        # self.play(Unwrite(zzz))