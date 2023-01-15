from manim import *
import cat_human
import pdb

class ManimScene(Scene):
    def construct(self):
        pdb.set_trace()
        human = cat_human.cat_human.human
        self.add(human)