from manim import *

class ColorfulMathTexMatrix(Scene):
    def construct(self):
        # Define the matrix entries and their colors
        entries = [
            ["\\color{red} 1", "\\color{blue} 2", "\\color{green} 3"],
            ["\\color{purple} 4", "\\color{orange} 5", "\\color{teal} 6"],
            ["\\color{magenta} 7", "\\color{brown} 8", "\\color{gray} 9"]
        ]
        
        # Create the MathTex matrix
        matrix = MathTex("\\begin{pmatrix}", *["&".join(row) + "\\\\" for row in entries], "\\end{pmatrix}")
        matrix.set_color_by_tex_to_color_map({
            "red": RED,
            "blue": BLUE,
            "green": GREEN,
            "purple": PURPLE,
            "orange": ORANGE,
            "teal": TEAL,
            "magenta": ORANGE,
            "brown": ORANGE,
            "gray": GRAY
        })
        matrix.scale(1.5)
        
        # Add the matrix to the scene
        self.add(matrix)
