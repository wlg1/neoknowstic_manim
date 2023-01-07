from manim import *
from random import randint, random


class VectorArrow(VectorScene, Scene):
    def setup(self):
        Scene.setup(self)
        VectorScene.setup(self)
        
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        
        faceText = Text('Face \nLength', 
            font_size=16).next_to([1,0,0], DOWN*2)
        arrow_c = self.add_vector([1, 0, 0], buff=0, color='#FA8072',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #light red
        self.play(FadeIn(faceText))
        
        bodyText = Text('Body \nSize', 
            font_size=16).next_to([0,1,0], LEFT*2)
        arrow_d = self.add_vector([0, 1, 0], buff=0, color='#ADD8E6',
            stroke_width=4, max_tip_length_to_length_ratio=0.15, 
            max_stroke_width_to_length_ratio=5)
        self.play(FadeIn(bodyText))
        
        ###########################
        # face = ImageMobject("face 1.png")
        # face.scale(0.5)
        # face.move_to(np.array([1, 0, 0]))
        # # self.play(GrowFromPoint(face, [1, 0, 0]))
        # self.add(face)
        
        # body = ImageMobject("body 1.png")
        # body.scale(0.5)
        # body.move_to(np.array([0, 1, 0]))
        # # self.play(GrowFromPoint(body, [0, 1, 0]))
        # self.add(body)
        ##################################
        
        face_1 = Rectangle(color=WHITE, height=0.15, width=0.3, stroke_width=1)
        face_1.move_to(np.array([1, 0, 0])).shift(UP*0.1 + LEFT*0.25)
        face_box = Rectangle(color=WHITE, height=0.8, width=1, stroke_width=1)
        face_box.move_to(np.array([1, 0, 0]))
        
        add_face = GrowFromPoint(face_1, [1, 0, 0])
        add_faceBox = GrowFromPoint(face_box, [1, 0, 0])
        self.play(add_face, add_faceBox)
        
        face_1_text = Text("1")
        face_1_text.scale(0.8 * face_1.get_height() / face_1_text.get_height()).move_to(face_1.get_center())
        self.play(FadeIn(face_1_text))
        
        body_1 = Ellipse(color=WHITE, stroke_width=1).scale(0.2)
        body_1.move_to(np.array([0, 1, 0])).shift(DOWN*0.1 + RIGHT*0.1)
        body_box = Rectangle(color=WHITE, height=0.8, width=1, stroke_width=1)
        body_box.move_to(np.array([0, 1, 0]))
        
        add_body = GrowFromPoint(body_1, [0, 1, 0])
        add_bodyBox = GrowFromPoint(body_box, [0, 1, 0])
        self.play(add_body, add_bodyBox)
        
        body_1_text = Text("1")
        body_1_text.scale(0.7 * body_1.get_height() / body_1_text.get_height()).move_to(body_1.get_center())
        self.play(FadeIn(body_1_text))
        
        self.wait(2)
                
        ################ Move to (1, 1)
        
        # will leave a copy behind if this isn't done
        # self.remove(face_1, body_1, face_box, body_box)
        
        self.play(FadeOut(face_1_text), FadeOut(body_1_text))
        
        face_2 = Rectangle(color=WHITE, height=0.15, width=0.3, stroke_width=1)
        face_2.move_to(np.array([1, 1, 0])).shift(UP*0.1 + LEFT*0.25)
        face_box_2 = Rectangle(color=WHITE, height=0.8, width=1, stroke_width=1)
        face_box_2.move_to(np.array([1, 1, 0]))
        
        body_2 = Ellipse(color=WHITE, stroke_width=1).scale(0.2)
        body_2.move_to(np.array([1, 1, 0])).shift(DOWN*0.1 + RIGHT*0.1)
        body_box_2 = Rectangle(color=WHITE, height=0.8, width=1, stroke_width=1)
        body_box_2.move_to(np.array([1, 1, 0]))
        
        # face_1_text_2 = Text("1")
        # face_1_text.scale(0.8 * face_1.get_height() / face_1_text_2.get_height()).move_to(face_2.get_center())
        # body_1_text_2 = Text("1")
        # body_1_text.scale(0.7 * body_1.get_height() / body_1_text_2.get_height()).move_to(body_2.get_center())
        
        self.play(Transform(face_1, face_2), Transform(face_box, face_box_2), Transform(body_1, body_2), Transform(body_box, body_box_2))
        # Transform(face_1_text, face_1_text_2), Transform(body_1_text, body_1_text_2))
       
        self.wait(2)
        
        self.remove(face_1, body_1, face_box, body_box)
        
        ######### Recreate basis data samples
        
        face_1 = Rectangle(color=WHITE, height=0.15, width=0.3, stroke_width=1)
        face_1.move_to(np.array([1, 0, 0])).shift(UP*0.1 + LEFT*0.25)
        face_box = Rectangle(color=WHITE, height=0.8, width=1, stroke_width=1)
        face_box.move_to(np.array([1, 0, 0]))
        
        add_face = GrowFromPoint(face_1, [1, 0, 0])
        add_faceBox = GrowFromPoint(face_box, [1, 0, 0])
        self.play(add_face, add_faceBox)
                
        body_1 = Ellipse(color=WHITE, stroke_width=1).scale(0.2)
        body_1.move_to(np.array([0, 1, 0])).shift(DOWN*0.1 + RIGHT*0.1)
        body_box = Rectangle(color=WHITE, height=0.8, width=1, stroke_width=1)
        body_box.move_to(np.array([0, 1, 0]))
        
        add_body = GrowFromPoint(body_1, [0, 1, 0])
        add_bodyBox = GrowFromPoint(body_box, [0, 1, 0])
        self.play(add_body, add_bodyBox)
                
        ######### Scale and move to (0.5, 0), (0, 2)
                
        # generate_target() doesn't seem to be able to use in a group animation since it plays directly
        face_2 = Rectangle(color=WHITE, height=0.15, width=0.15, stroke_width=1)
        face_2.move_to(np.array([0.5, 0, 0])).shift(UP*0.1 + LEFT*0.25)
        face_box_2 = Rectangle(color=WHITE, height=0.8, width=1, stroke_width=1)
        face_box_2.move_to(np.array([0.5, 0, 0]))
        self.play(Transform(face_1, face_2), Transform(face_box, face_box_2))
        
        body_2 = Ellipse(color=WHITE, stroke_width=1).scale(0.4)
        body_2.move_to(np.array([0, 2, 0])).shift(DOWN*0.1 + RIGHT*0.1)
        body_box_2 = Rectangle(color=WHITE, height=0.8, width=1, stroke_width=1)
        body_box_2.move_to(np.array([0, 2, 0]))
        self.play(Transform(body_1, body_2), Transform(body_box, body_box_2))
       
        self.wait(1)
        
        ######### Move to (0.5, 2)
        
        # will leave a copy behind if this isn't done
        self.remove(face_1, body_1, face_box, body_box)
        
        face_3 = Rectangle(color=WHITE, height=0.15, width=0.15, stroke_width=1)
        face_3.move_to(np.array([0.5, 2, 0])).shift(UP*0.1 + LEFT*0.25)
        face_box_3 = Rectangle(color=WHITE, height=0.8, width=1, stroke_width=1)
        face_box_3.move_to(np.array([0.5, 2, 0]))
        
        body_3 = Ellipse(color=WHITE, stroke_width=1).scale(0.4)
        body_3.move_to(np.array([0.5, 2, 0])).shift(DOWN*0.1 + RIGHT*0.1)
        body_box_3 = Rectangle(color=WHITE, height=0.8, width=1, stroke_width=1)
        body_box_3.move_to(np.array([0.5, 2, 0]))
        
        self.play(Transform(face_2, face_3), Transform(face_box_2, face_box_3), Transform(body_2, body_3), Transform(body_box_2, body_box_3))
       
        self.wait(2)
        
        ################################################
        # face.generate_target()
        # face.target.move_to(np.array([1, 1, 0]))
        # face_move_1 = MoveToTarget(face)
                
        # body.generate_target()
        # body.target.move_to(np.array([1, 1, 0]))
        # body_move_1 = MoveToTarget(body)
        
        # FBgroup = AnimationGroup(face_move_1, body_move_1)
        # self.play(FBgroup)
        
        ########
        # oneone = ImageMobject("1 1.png")
        # oneone.scale(0.5)
        # oneone.move_to(np.array([1, 1, 0]))
        # self.play(FadeIn(oneone))
                
        #########################################
        # faceText = Text('Face \nLength', 
            # font_size=16).next_to([1,0,0], DOWN*0.5)
        # arrow_c = Arrow(ORIGIN, [1, 0, 0], buff=0, color='#FA8072',
            # stroke_width=4, max_tip_length_to_length_ratio=0.15, 
            # max_stroke_width_to_length_ratio=5) #light red
        # self.add(faceText, arrow_c)
            
        # bodyText = Text('Body \nSize', 
            # font_size=16).next_to([0,1,0], LEFT)
        # arrow_d = Arrow(ORIGIN, [0, 1, 0], buff=0, color='#ADD8E6',
            # stroke_width=4, max_tip_length_to_length_ratio=0.15, 
            # max_stroke_width_to_length_ratio=5)
        # self.add(bodyText, arrow_d)
        
        # dot3 = Dot([0.5,2,0], radius=0.07, color = '#CBC3E3')
        # dot3_text = Text('(0.5, 2)', font_size=16, color = '#CBC3E3').next_to(dot3, UP*0.5)
        # self.add(dot3_text, dot3)
        
        # dot2 = Dot([1,1,0], radius=0.07, color='gold')
        # dot2_text = Text('(1, 1)', font_size=16, color='gold').next_to(dot2, RIGHT*0.5+UP*0.5)
        # self.add(dot2_text, dot2)
        
        # dot1 = Dot([1,0,0], radius=0.07, color='#FA8072')
        # dot1_text = Text('(1, 0)', font_size=16, color='#FA8072').next_to(dot1, RIGHT*0.5+UP*0.5)
        # self.add(dot1_text, dot1)

        
        
        
        