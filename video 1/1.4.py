from manim import *
import pdb

class scene_1_4(Scene):
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
                
        face_outline = Circle(radius=1.75, color='#ADD8E6', fill_color=BLACK, fill_opacity=1).move_to([0, 0, 0]) 
        
        left_eye = Dot(color='#ADD8E6').move_to([-1, 0.5, 0])
        right_eye = Dot(color='#ADD8E6').move_to([1, 0.5, 0])
        
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

        for nl in left_ear:
            nl.color = '#ADD8E6'

        for nl in right_ear:
            nl.color = '#ADD8E6'
                
        for nl in nose:
            nl.z_index=3
            nl.color = '#ADD8E6'
        
        for whisk in whiskers:
            whisk.z_index=3
            whisk.color = '#ADD8E6'
            
        cat_face = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy()).scale(0.3).move_to(np.array([-3, 1, 0]))   
        
        ##################################################
        human_face = cat_face[0].copy()  
        human_face.z_index= 2
        neck = Line([-3, 0, 0], [-3, 0.4, 0], color = '#ADD8E6')
        
        top_line = Line([-3.75, 0, 0], [-2.25, 0, 0])
        left_line = Line([-3.75, 0, 0], [-3, -1.75, 0])
        right_line = Line([-2.25, 0, 0], [-3, -1.75, 0])
        body = VGroup(top_line, left_line, right_line)
        body = Polygon(*[[-3.75, 0, 0], [-2.25, 0, 0], [-3, -1.75, 0]], color='#ADD8E6', fill_color='#00008B', fill_opacity = 1)
        
        left_arm = Line([-3.75, 0, 0], [-4, -1.5, 0], color = '#ADD8E6')  #shoulder to hand
        right_arm = Line([-2.25, 0, 0], [-2, -1.5, 0], color = '#ADD8E6')
        
        left_leg = Line([-3, -1.75, 0], [-3.5, -3.25, 0], color = '#ADD8E6')  #waist to foot
        right_leg = Line([-3, -1.75, 0], [-2.5, -3.25, 0], color = '#ADD8E6')
                
        human = VGroup(human_face.copy(), neck.copy(), body.copy(), left_arm.copy(), right_arm.copy(), left_leg.copy(), right_leg.copy()).move_to(np.array([-3, -1.5, 0])).scale(0.75)
        
        tail = ArcBetweenPoints([-3, -1.75, 0], [-1.2, -1.2,0], color='#ADD8E6')
        cat_human = VGroup(cat_face.copy(), neck.copy(), body.copy(), left_arm.copy(), right_arm.copy(), left_leg.copy(), right_leg.copy(), tail).move_to(np.array([-1, -1, 0])).scale(0.75)
                        
        ##################################################
                                
        floor = ImageMobject("skew_check_3.png").scale(2)
        floor.z_index = -1
        self.add(floor)

        cat = ImageMobject("cat sitting, v2, transp flip.png").scale(1)
        
        self.add(cat, human)

        front_line = Line([0, -3.5, 0], [6, 1, 0]).shift(RIGHT)
        back_line = Line([-4, -2, 0], [5, 2, 0]).shift(UP*0.9)
        back_line.z_index = -1
        # self.add(front_line, back_line)

        self.wait(1)

        self.play(FadeOut(cat, shift=LEFT), Transform(human,cat_human), GrowFromCenter(cat_human), run_time=2)

        self.wait(1)