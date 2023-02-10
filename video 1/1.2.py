from manim import *
import pdb

class scene_1_2(Scene):
    def construct(self):
        word_1 = Text("Manifold?", color = WHITE, font_size=100).shift(LEFT+UP)
        word_2 = Text("Isometry?", color = WHITE, font_size=100).shift(RIGHT+DOWN)
        
        self.play(Write(word_1))
        self.play(Write(word_2))

        self.wait(2)
        
        # self.play(FadeOut(word_1, word_2))