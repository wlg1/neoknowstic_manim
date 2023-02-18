from manim import *

class scene_8_mat(Scene):
    def construct(self):

        m0 = MathTex(r"\begin{bmatrix} w_{11} \frac{Nap}{Nose} \ \ w_{12} \frac{Nap}{Ear} \\\\ w_{21} \frac{Luck}{Nose} \ \ w_{22} \frac{Luck}{Ear} \end{bmatrix}", tex_to_color_map={
            "aq": '#FF0000',
            "xx": '#0000FF'} ).scale(2)
        m0[0][3].set_color(ORANGE) #1
        m0[0][4].set_color(RED) #1
        m0[0][5:8].set_color(ORANGE) # Nap
        m0[0][9:13].set_color(RED)  # Nose
        m0[0][14].set_color(ORANGE) #1
        m0[0][15].set_color(BLUE) #2
        m0[0][16:19].set_color(ORANGE) # Nap
        m0[0][20:23].set_color(BLUE)  # Ear

        m0[0][3+21].set_color(GREEN) #2
        m0[0][4+21].set_color(RED) #1
        m0[0][5+21:9+21].set_color(GREEN) # Luck
        m0[0][10+21:14+21].set_color(RED)  # Nose
        m0[0][15+21].set_color(GREEN) #2
        m0[0][16+21].set_color(BLUE) #2
        m0[0][17+21:21+21].set_color(GREEN) # Luck
        m0[0][22+21:25+21].set_color(BLUE)  # Ear
            
        self.add(m0)