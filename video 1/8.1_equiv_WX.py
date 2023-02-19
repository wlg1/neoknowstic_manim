from manim import *
import pdb, re

class scene_8_1_equiv_WX(Scene):
    def construct(self):  
        #error- whenever within matrix, cannot do tex_to_color_map
        ''', tex_to_color_map={
            "x_{1}": RED,
            "x_{2}": BLUE,
            "w_{11}": '#FFD580',
            "w_{12}": '8B4000',
            "w_{21}": '#90EE90',
            "w_{22}": '#023020'
        }'''

        '''(Pdb) asdf = [x for x in dir(row1[0][3]) if 'text' in x or 'str' in x]
        (Pdb) asdf
        ['__abstractmethods__', '__str__', 'background_stroke_color', 'background_stroke_opacity', 'background_stroke_rgbas', 'background_stroke_width', 'get_stroke_color', 'get_stroke_colors', 'get_stroke_opacities', 'get_stroke_opacity', 'get_stroke_rgbas', 'get_stroke_width', 'set_background_stroke', 'set_stroke', 'stretch', 'stretch_about_point', 'strerow1_pure_string="\begin{bmatrix} w_{11} \ \ w_{12} \\\\ w_{21} \ \ w_{22} \end{bmatrix} \ \begin{bmatrix} x_{1} \\\\ x_{2} \end{bmatrix} = \begin{bmatrix} w_{11} * x_{1} + w_{12} * x_{2} \\\\ w_{21} * x_{1} + w_{22} * x_{2} \end{bmatrix}"tch_to_fit_depth', 'stretch_to_fit_height', 'stretch_to_fit_width', 'stroke_color', 'stroke_opacity', 'stroke_rgbas', 'stroke_width']
        
        
        row1_pure_string=".w11w12..w21w22..x1..x2.=.w11*x1+w12*x2..w21*x1+w22*x2."

        #f = [x for x,i in enumerate(row1_pure_string) if i=='=']
        # row1[0][24].set_color(RED) 
        for i,x in enumerate(row1[0]):
            if row1_pure_string[i-1] == '1':
                row1[0][i].set_color('#FFD580')
                
        '''

        # row1 = MathTex(r"\begin{bmatrix} w_{11} \ \ w_{12} \\\\ w_{21} \ \ w_{22} \end{bmatrix} \ \begin{bmatrix} x_{1} \\\\ x_{2} \end{bmatrix} = \begin{bmatrix} w_{11} * x_{1} + w_{12} * x_{2} \\\\ w_{21} * x_{1} + w_{22} * x_{2} \end{bmatrix}").shift(UP*2.5)
        
        # self.add(row1)

        # row2 = MathTex(r"= \begin{bmatrix} w_{11} * x_{1} + w_{12} * x_{2} \\\\ 0 \end{bmatrix} + \begin{bmatrix} 0 \\\\ w_{21} * x_{1} + w_{22} * x_{2} \end{bmatrix}")
        
        # self.add(row2)

        #####################
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

        # take frame w/ only first row, then paint over 2nd rows as black in gimp. fade in in video editor the second rows

        m1 = get_colored_mat([["w_{11}", "w_{12}"], ["w_{21}", "w_{22}"]])
        x = get_colored_mat([["x_{1}"], ["x_{2}"]])

        dot_prod_row1 = get_colored_mat([["w_{11} * x_{1} + w_{12} * x_{2}"], ["w_{21} * x_{1} + w_{22} * x_{2}"]])

        row1_left = Group(m1, x).arrange(buff=0.2)

        equals = MathTex("=")

        row1 = Group(row1_left, equals, dot_prod_row1).arrange(buff=0.6).shift(UP*2.5)

        self.add(row1)

        #####################
        equals_row_2 = MathTex("=")
        plus_row2 = MathTex("+")

        dot_prod_row2_left = get_colored_mat([["w_{11} * x_{1} + w_{12} * x_{2}"], ["0"]])
        dot_prod_row2_right = get_colored_mat([["0"], ["w_{21} * x_{1} + w_{22} * x_{2}"]])

        row2 = Group(equals_row_2, dot_prod_row2_left, plus_row2, dot_prod_row2_right).arrange(buff=0.6)

        self.wait(2)
        self.play(FadeIn(row2, shift=DOWN))

        self.wait(2)
        
        rec_1 = SurroundingRectangle(dot_prod_row2_left)
        self.play(FadeIn(rec_1))

        self.wait(2)

        rec_1 = SurroundingRectangle(dot_prod_row2_right)
        self.play(FadeIn(rec_1))
        
        self.wait(2)