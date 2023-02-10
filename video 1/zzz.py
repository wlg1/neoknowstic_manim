from manim import *

class zzz(Scene):
    def construct(self):  

        for i in range(10):
            zzz = Text("...zZz...", font_size=144)
            self.play(Write(zzz))
            self.wait(1)
            self.play(Unwrite(zzz))