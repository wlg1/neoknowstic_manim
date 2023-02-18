from manim import *
import pdb

class cat_human(Scene):
    def construct(self):
        # inNode_1 = Circle(radius=0.5, color=WHITE, fill_color=WHITE, fill_opacity=1, stroke_width=1).move_to([-1, 1.5, 0])
        # inNode_2 = Circle(radius=0.5, color=WHITE, fill_color=WHITE, fill_opacity=1, stroke_width=1).move_to([-1, -1.5, 0])
        # outNode = Circle(radius=0.5, color=WHITE, fill_color=WHITE, fill_opacity=1, stroke_width=1).move_to([3, 0, 0])
        
        # conn_1 = Line([-1, 1.5, 0], [3, 0, 0])
        # conn_2 = Line([-1, -1.5, 0], [3, 0, 0])
        
        # self.add(inNode_1, inNode_2, outNode, conn_1, conn_2)

        inNode_1 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([-3, 2, 0])
        # inNode_2 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([-3, 0, 0])
        inNode_3 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([-3, -2, 0])

        midNode_1 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([0, 1, 0])
        midNode_2 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([0, -1, 0])

        # outNode_1 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([3, 2, 0])
        outNode_2 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([3, 0, 0])
        # outNode_3 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([3, -2, 0])
        
        conn_1 = Line(inNode_1.get_center(), midNode_1.get_center(), color=GRAY)
        # conn_2 = Line(inNode_2.get_center(), midNode_1.get_center(), color=GRAY)
        conn_3 = Line(inNode_3.get_center(), midNode_1.get_center(), color=GRAY)
        conn_4 = Line(inNode_1.get_center(), midNode_2.get_center(), color=GRAY)
        # conn_5 = Line(inNode_2.get_center(), midNode_2.get_center(), color=GRAY)
        conn_6 = Line(inNode_3.get_center(), midNode_2.get_center(), color=GRAY)
        # conn_7 = Line(midNode_1.get_center(), outNode_1.get_center(), color=GRAY)
        conn_8 = Line(midNode_1.get_center(), outNode_2.get_center(), color=GRAY)
        # conn_9 = Line(midNode_1.get_center(), outNode_3.get_center(), color=GRAY)
        # conn_10 = Line(midNode_2.get_center(), outNode_1.get_center(), color=GRAY)
        conn_11 = Line(midNode_2.get_center(), outNode_2.get_center(), color=GRAY)
        # conn_12 = Line(midNode_2.get_center(), outNode_3.get_center(), color=GRAY)
                
        # bigNN = VGroup(conn_1, conn_2, conn_3, conn_4, conn_5, conn_6, conn_7, conn_8, conn_9, conn_10, conn_11, conn_12, inNode_1, inNode_2, inNode_3, midNode_1, midNode_2, outNode_1, outNode_2, outNode_3).scale(0.75).shift(DOWN*1.3)

        bigNN = VGroup(conn_1, conn_3, conn_4, conn_6, conn_8, conn_11, inNode_1, inNode_3, midNode_1, midNode_2, outNode_2)
        # .scale(0.75).shift(DOWN*1.3)
        
        self.add(bigNN)
        
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
        
        left_eye = Dot(color=WHITE).move_to([-1, 0.5, 0])
        right_eye = Dot(color=WHITE).move_to([1, 0.5, 0])
        
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
        left_eye.z_index=3
        right_eye.z_index=3
                
        for nl in nose:
            nl.z_index=3
        
        for whisk in whiskers:
            whisk.z_index=3
            
        face_group = VGroup(face_outline.copy(), left_eye.copy(), right_eye.copy(), left_ear.copy(), right_ear.copy(), nose.copy(), whiskers.copy()).scale(0.3).move_to(np.array([-3, 1, 0]))   
                        
        ##################################################    
        # humanFace = Circle(radius=1, color=WHITE, fill_color=BLACK, fill_opacity=1).move_to([0, 2.5, 0])
        # neck = Line([0, 1, 0], [0, 1.5, 0])

        # top_line = Line([-1, 1, 0], [1, 1, 0])
        # left_line = Line([-1, 1, 0], [0, -1.75, 0])
        # right_line = Line([1, 1, 0], [0, -1.75, 0])
        # body = VGroup(top_line, left_line, right_line)
        
        # left_arm = Line([-1, 1, 0], [-1.25, -1.25, 0])  #shoulder to hand
        # right_arm = Line([1, 1, 0], [1.25, -1.25, 0])
        
        # left_leg = Line([0, -1.75, 0], [-0.7, -4, 0])  #waist to foot
        # right_leg = Line([0, -1.75, 0], [0.7, -4, 0])
        
        # human = VGroup(humanFace, neck, body, left_arm, right_arm, left_leg, right_leg).scale(0.3).move_to(np.array([-3, -1, 0]))    
        
        # self.add(human)
        
        ##################################################
        human_face = face_group[0].copy()  
        human_face.z_index= 2
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
        human = VGroup(human_face, neck, body, left_arm, right_arm, left_leg, right_leg)
        
        ##################################################
        cat_human = VGroup(face_group.copy(), human.copy(), tail)
                
        cat_face = face_group.copy().move_to([-5, 2, 0])
        self.add(cat_face) 
        
        pure_human = human.copy().move_to(np.array([-5, -2, 0])).scale(0.5)
        self.add(pure_human)

        cat_human.move_to([5, 0, 0]).scale(0.75)
        
        self.add(cat_human)

        word_1 = Text("Cat").move_to([0, 2, 0]).scale(0.8)
        word_2 = Text("Face").move_to([0, -2, 0]).scale(0.8)

        self.add(word_1, word_2)

        self.wait(2)

        unk_1 = Text("?").move_to([0, 2, 0])
        unk_2 = Text("?").move_to([0, -2, 0])

        self.play(Transform(word_1, unk_1))
        
        self.wait(2)

        self.play(Transform(word_2, unk_2))

        self.wait(2)