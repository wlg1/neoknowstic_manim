
        ###################################################################
        ###################################################################
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
