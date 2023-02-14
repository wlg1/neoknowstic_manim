from manim import *
import pdb

class scene_7_3(Scene):
    def construct(self):  
        '''This Activation Space, commonly referred to as a Hidden or Latent Space, is where analogies such as King - Man + Woman = Queen can be made by adding its vectors. '''

        numberplane = NumberPlane()

        king = ImageMobject("crown2.png").scale(0.35).move_to([1, 2, 0])
        queen = ImageMobject("tiara white.png").scale(0.1).move_to([3, 2, 0])

        gender = Text("Gender").move_to([1, 0, 0]).scale(0.5).shift(DOWN*0.5+RIGHT*0.5)
        royalty = Text("Royalty").move_to([0, 1, 0]).scale(0.5).shift(UP*0.5+LEFT*0.75)
        
        M = Text("M", color=RED).move_to([1, 0, 0]).scale(0.5).shift(UP*0.5)
        Mdot = Dot([1, 0, 0], color = RED)
        W = Text("W", color=BLUE).move_to([3, 0, 0]).scale(0.5).shift(UP*0.5)
        Wdot = Dot([3, 0, 0], color = BLUE)

        gender_line = Line([0,0,0],[1, 0, 0], color=RED)
        gender_tip = Triangle(fill_color=RED, fill_opacity=1, color=RED).scale(0.1).rotate(-90*DEGREES).move_to([1, 0, 0])
        gender_vec = VGroup(gender_line, gender_tip)

        royal_line = Line([0,0,0],[0, 1, 0], color=BLUE)
        royal_tip = Triangle(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.1).rotate(360*DEGREES).move_to([0, 1, 0])
        royal_vec = VGroup(royal_line, royal_tip)

        self.add(numberplane, king, queen, gender, royalty, gender_vec, M, W, Mdot, Wdot)
        
        space_words = Text("Activation Space").scale(0.8).move_to([4, 3.5, 0])
        self.play(Write(space_words))

        self.wait(2)

        space_words_2 = Text("Latent Space").scale(0.8).move_to([4, 3.5, 0])
        self.play(Transform(space_words, space_words_2))

        self.wait(2)

        vector_king = Vector([1, 2, 0], color = ORANGE)
        self.play(GrowArrow(vector_king))

        self.wait(2)

        gender_line = Line([0,0,0],[-1, 0, 0], color=RED)
        gender_tip = Triangle(fill_color=RED, fill_opacity=1, color=RED).scale(0.1).rotate(90*DEGREES).move_to([-1, 0, 0])
        gender_vec_2 = VGroup(gender_line, gender_tip)

        M2 = Text("-M", color=RED).move_to([-1, 0, 0]).scale(0.5).shift(UP*0.5)

        self.play(Transform(gender_vec, gender_vec_2), FadeIn(M2))
        
        self.wait(2)

        gender_line = Line([1,2,0],[0, 2, 0], color=RED)
        gender_tip = Triangle(fill_color=RED, fill_opacity=1, color=RED).scale(0.1).rotate(90*DEGREES).move_to([0, 2, 0])
        gender_vec_3 = VGroup(gender_line, gender_tip)

        M3 = Text("-M", color=RED).move_to([0.5, 2, 0]).scale(0.5).shift(UP*0.5)

        self.play(Transform(gender_vec, gender_vec_3), Transform(M2, M3))
        
        self.wait(2)

        woman_line = Line([0,0,0],[3, 0, 0], color=BLUE)
        woman_tip = Triangle(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.1).rotate(-90*DEGREES).move_to([3, 0, 0])
        woman_vec = VGroup(woman_line, woman_tip)

        self.play(GrowFromPoint(woman_vec, [0, 0, 0]))
        
        self.wait(2)
        
        woman_line = Line([0,2,0],[3, 2, 0], color=BLUE)
        woman_tip = Triangle(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.1).rotate(-90*DEGREES).move_to([3, 2, 0])
        woman_vec_2 = VGroup(woman_line, woman_tip).shift(UP*0.1)
        
        W2 = Text("+W", color=BLUE).move_to([2.5, 2, 0]).scale(0.5).shift(UP*0.5)

        self.play(Transform(woman_vec, woman_vec_2), FadeIn(W2))
        
        self.wait(2)