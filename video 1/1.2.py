from manim import *
import pdb

class scene_1_2(Scene):
    def construct(self):
        # word_1 = Text("Eigendecomposition?", color = BLACK).shift(LEFT+UP)
        # word_2 = Text("Manifold?", color = BLACK).shift(RIGHT+DOWN)
        word_1 = Text("Eigendecomposition?").shift(LEFT+UP)
        word_2 = Text("Manifold?").shift(RIGHT+DOWN)
        
        self.play(Write(word_1))
        self.play(Write(word_2))
        
        self.play(FadeOut(word_1, word_2))