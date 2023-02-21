from manim import *
import pdb, re

class scene_8_equiv_WX(Scene):
    def construct(self):  
        def get_colored_mat(strings_ASLIST):
            tex_to_color_map={
                "x1": RED,
                "x2": BLUE,
                "w11": YELLOW,
                "w12": ORANGE,
                "w21": GRAY,
                "w22": GREEN
            }            
            strings_ASMAT = Matrix(strings_ASLIST, 
            element_alignment_corner=ORIGIN)
            ent = strings_ASMAT.get_entries()
            strings_flatList = [item for sublist in strings_ASLIST for item in sublist]
            for ent_ind, pure_string in enumerate(strings_flatList):
                pure_string_cut = pure_string.replace('_', '').replace('{', '').replace('}', '').replace(' ', '')
                for qry, color in tex_to_color_map.items():
                    match_inds = [ i.start() for i in re.finditer(qry, pure_string_cut)]
                    for ind in match_inds:
                        ent[ent_ind][0][ind: ind +len(qry)].set_color(color)
            return strings_ASMAT

        # row1 = MathTex(r"\begin{bmatrix} w_{11} \ \ w_{12} \\\\ w_{21} \ \ w_{22} \end{bmatrix} \ \begin{bmatrix} x_{1} \\\\ x_{2} \end{bmatrix} = \begin{bmatrix} w_{11} * x_{1} + w_{12} * x_{2} \\\\ w_{21} * x_{1} + w_{22} * x_{2} \end{bmatrix}").shift(UP*2.5)

        m1 = get_colored_mat([["w_{11}", "w_{12}"], ["w_{21}", "w_{22}"]])
        x = get_colored_mat([["x_{1}"], ["x_{2}"]])
        dot_prod_row1 = get_colored_mat([["w_{11} * x_{1} + w_{12} * x_{2}"], ["w_{21} * x_{1} + w_{22} * x_{2}"]])
        row1_left = Group(m1.copy(), x.copy()).arrange(buff=0.2)
        equals = MathTex("=")
        row1 = Group(row1_left.copy(), equals.copy(), dot_prod_row1.copy()).arrange(buff=0.6).shift(UP*2.5)

        self.add(row1)

        self.wait(2)

        # row2 = MathTex(r"= \begin{bmatrix} w_{11} \ \ w_{12} \\\\ w_{21} \ \ w_{22} \end{bmatrix} \ \begin{bmatrix} x_{1} \\\\ 0 \end{bmatrix} + \begin{bmatrix} w_{11} \ \ w_{12} \\\\ w_{21} \ \ w_{22} \end{bmatrix} \ \begin{bmatrix} 0 \\\\ x_{2} \end{bmatrix}")
        
        x1 = get_colored_mat([["x_{1}"], ["0"]])
        x2 = get_colored_mat([["0"], ["x_{2}"]])
        w_x1 = Group(m1.copy(), x1.copy()).arrange(buff=0.2)
        w_x2 = Group(m1.copy(), x2.copy()).arrange(buff=0.2)
        plus = MathTex("+")
        row2 = Group(equals.copy(), w_x1.copy(), plus.copy(), w_x2.copy()).arrange(buff=0.6)
        
        self.play(FadeIn(row2, shift=DOWN))

        self.wait(2)

        # row3 = MathTex(r"= x_{1} * \begin{pmatrix} \begin{bmatrix} w_{11} \ \ w_{12} \\\\ w_{21} \ \ w_{22} \end{bmatrix} \ \begin{bmatrix} 1 \\\\ 0 \end{bmatrix} \end{pmatrix} + x_{2} * \begin{pmatrix} \begin{bmatrix} w_{11} \ \ w_{12} \\\\ w_{21} \ \ w_{22} \end{bmatrix} \ \begin{bmatrix} 0 \\\\ 1 \end{bmatrix} \end{pmatrix}").shift(DOWN*2.5)
                
        top1_mat = Matrix([["1"], ["0"]]).set_row_colors(RED, WHITE)
        bot1_mat = Matrix([["0"], ["1"]]).set_row_colors(WHITE, BLUE)
        w_top1 = Group(m1.copy(), top1_mat.copy()).arrange(buff=0.2)
        w_bot2 = Group(m1.copy(), bot1_mat.copy()).arrange(buff=0.2)
        row3 = Group(equals.copy(), MathTex("x_{1} \ *"), w_top1.copy(), plus.copy(), MathTex("x_{2} \ *"), w_bot2.copy()).arrange(buff=0.6).shift(DOWN*2.5)
        
        self.play(FadeIn(row3, shift=DOWN))

        self.wait(2)

        # row4 = MathTex(r"= x_{1} * \begin{pmatrix} \begin{bmatrix} w_{11} * 1 + w_{12} * 0 \\\\ w_{21} * 1 + w_{22} * 0 \end{bmatrix} \end{pmatrix} + x_{2} * \begin{pmatrix} \begin{bmatrix} w_{11} * 0 + w_{12} * 1 \\\\ w_{21} * 0 + w_{22} * 1 \end{bmatrix} \end{pmatrix}").shift(DOWN*2.5)

        dot_prod_row4_left = get_colored_mat([["w_{11} * 1 + w_{12} * 0"], ["w_{21} * 1 + w_{22} * 0"]])
        ent = dot_prod_row4_left.get_entries()
        ent[0][0][4].set_color(RED)
        ent[1][0][4].set_color(RED)
        dot_prod_row4_right = get_colored_mat([["w_{11} * 0 + w_{12} * 1"], ["w_{21} * 0 + w_{22} * 1"]])
        ent = dot_prod_row4_right.get_entries()
        ent[0][0][10].set_color(BLUE)
        ent[1][0][10].set_color(BLUE)
        row4 = Group(equals.copy(), MathTex("x_{1} \ *"), dot_prod_row4_left.copy(), plus.copy(), MathTex("x_{2} \ *"), dot_prod_row4_right.copy()).arrange(buff=0.6).shift(DOWN*2.5)
        
        row3_up = row3.copy().shift(UP*2.5)
        self.play(FadeOut(row2, shift=UP), Transform(row3, row3_up), FadeIn(row4, shift=DOWN))
        self.wait(2)
                
        # row5 = MathTex(r"= x_{1} * \begin{pmatrix} \begin{bmatrix} w_{11} \\\\ w_{21} \end{bmatrix} \end{pmatrix} + x_{2} * \begin{pmatrix} \begin{bmatrix} w_{12} \\\\ w_{22} \end{bmatrix} \end{pmatrix}").shift(DOWN*2.5)
        
        dot_prod_row5_left = get_colored_mat([["w_{11}"], ["w_{21}"]])
        dot_prod_row5_right = get_colored_mat([["w_{12}"], ["w_{22}"]])
        # row5 = Group(equals.copy(), MathTex("x_{1} \ *"), dot_prod_row5_left.copy(), plus.copy(), MathTex("x_{2} \ *"), dot_prod_row5_right.copy(), equals.copy(), dot_prod_row1.copy()).arrange(buff=0.4).shift(DOWN*2.5)
        row5 = Group(equals.copy(), MathTex("x_{1} \ *"), dot_prod_row5_left.copy(), plus.copy(), MathTex("x_{2} \ *"), dot_prod_row5_right.copy()).arrange(buff=0.6).shift(DOWN*2.5)
        
        row3_up_up = row3_up.copy().shift(UP*2.5)
        row4_up = row4.copy().shift(UP*2.5)
        self.play(FadeOut(row1, shift=UP), Transform(row3, row3_up_up), Transform(row4, row4_up), FadeIn(row5, shift=DOWN))
        self.wait(2)

        dot_prod_row5_left_2 = row5[2].copy().set_row_colors('#FF8BA0','#FF8BA0')
        dot_prod_row5_right_2 = row5[5].copy().set_row_colors('#ADD8E6','#ADD8E6')

        self.play(Transform(row5[2], dot_prod_row5_left_2), Transform(row5[5], dot_prod_row5_right_2))
        self.wait(2)

        dot_prod_row6_left = Matrix([["1"], ["0"]]).set_row_colors('#FF8BA0','#FF8BA0')
        dot_prod_row6_right = Matrix([["0"], ["1"]]).set_row_colors('#ADD8E6','#ADD8E6')

        row6 = Group(equals.copy(), MathTex("x_{1} \ *"), dot_prod_row6_left.copy(), plus.copy(), MathTex("x_{2} \ *"), dot_prod_row6_right.copy()).arrange(buff=0.6).shift(DOWN*2.5)

        self.play(Transform(row5, row6))
        self.wait(2)
        
        ## alt: create matrix, then get entries and fill in with mathtex that's used tex to color already before adding to matrix?