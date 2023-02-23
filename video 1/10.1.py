from manim import *

class Scene_10_1(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        
        """
        2 -1
        1 1
        
        inv:
        0.33333333333333333333	0.33333333333333333334
	    -0.33333333333333333333	0.66666666666666666666
        
        """
        
        poison= ImageMobject("poison.jpg").scale(0.4).move_to(np.array([-1, 2, 0]))
        
        gift= ImageMobject("gift.jpg").scale(0.5).move_to(np.array([0.3333, 1.6667, 0]))
        
        arrow_light_pur = Arrow(ORIGIN, [-1, 2, 0], buff=0, color='#ffc0cb',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #light purple    
        arrow_light_pur.z_index=10    
        text_1 = Tex('gift').next_to(arrow_light_pur.get_end(), LEFT*0.7+UP*1.1)
        
        arrow_red = Arrow(ORIGIN, [1, 0, 0], buff=0, color=RED,
            stroke_width=5, max_tip_length_to_length_ratio=0.2, 
            max_stroke_width_to_length_ratio=4) #light red
        arrow_blue = Arrow(ORIGIN, [0, 1, 0], buff=0, color=BLUE,
            stroke_width=5, max_tip_length_to_length_ratio=0.2, 
            max_stroke_width_to_length_ratio=4) #light blue

        self.add(arrow_red, arrow_blue, arrow_light_pur)

        self.wait(1)
        self.play(FadeIn(poison))
        self.wait(1)
        self.play(FadeIn(gift))
        self.wait(1)
        self.play(FadeIn(text_1))
        self.wait(1)

        Ger = Text("Ger").scale(0.6).move_to([0, 1, 0])
        Man = Text("Man").scale(0.6).move_to([1, 0, 0])
        # German = Text("German").scale(0.8).move_to([4, 1, 0])
        self.play(FadeIn(Ger, Man))
        self.wait(1)

        ############################
        '''Since there is a misunderstanding, the English speaker needs to know what ‘gift’ is actually referring to; or in other words, to know the right English word to use for . So they need to translate from the language above, which resembles German, to English as follows'''

        poison_eng = ImageMobject("poison.jpg").scale(0.4).move_to(np.array([-4, 1, 0]))
        
        gift_eng = ImageMobject("gift.jpg").scale(0.5).move_to(np.array([-1, 2, 0]))

        ger_2 = Text("Ger", opacity=0.3, fill_opacity=0.3).scale(0.4).move_to([-1, 1, 0])
        man_2 = Text("Man", opacity=0.3, fill_opacity=0.3).scale(0.4).move_to([2, 1, 0])

        eng = Text("Eng").scale(0.6).move_to([0, 1, 0])
        lish = Text("Lish").scale(0.6).move_to([1, 0, 0])

        self.play(Transform(poison, poison_eng), Transform(gift, gift_eng), Transform(Ger, ger_2), Transform(Man, man_2))
        self.play(FadeIn(eng, lish))
        self.wait(1)

        arrow_purp = Arrow(ORIGIN, [-4, 1, 0], buff=0, color=PURPLE,
            stroke_width=4, max_tip_length_to_length_ratio=0.07, 
            max_stroke_width_to_length_ratio=3) 
        arrow_purp.z_index=10
        text_2 = Tex('poison').next_to(arrow_purp.get_end(), UP*1.5)

        self.play(FadeIn(arrow_purp), FadeIn(text_2))
        self.wait(1)

        ############################
        '''Now if the English speaker tells the German speaker that they’re giving them a ‘gift’, the German speaker must translate this to a German word or expression that makes them understand that it’s . The German word for  is ‘geschenk’. Going the other way around, the English word for  is ‘poison’.'''
        # inverse
        
        poison_ger = ImageMobject("poison.jpg").scale(0.4).move_to(np.array([-1, 2, 0]))
        
        gift_ger = ImageMobject("gift.jpg").scale(0.5).move_to(np.array([0.3333, 1.6667, 0]))
        
        ger_ger = Text("Ger").scale(0.6).move_to([0, 1, 0])
        man_ger = Text("Man").scale(0.6).move_to([1, 0, 0])
        
        eng_ger = Text("Eng", opacity=0.3, fill_opacity=0.3).scale(0.4).move_to([0.33333333333333333334, 0.66666666666666666666, 0])
        lish_ger = Text("Lish", opacity=0.3, fill_opacity=0.3).scale(0.4).move_to([0.33333333333333333333	, -0.33333333333333333333, 0])
    
        self.play(Transform(poison, poison_ger), Transform(gift, gift_ger), Transform(Ger, ger_ger), Transform(Man, man_ger), Transform(eng, eng_ger), Transform(lish, lish_ger))
        self.wait(1)