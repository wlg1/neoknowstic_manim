from manim import *

class test2(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            include_foreground_plane=False,  #get rid of grid lines
            # include_background_plane=False,  #get rid of transforming grid lines
            show_basis_vectors=False,
        )
# class VectorArrow(Scene):
    def construct(self):
        # numberplane = NumberPlane()
        # self.add(numberplane)

        vec_n1 = Vector([1.5, 1, 0], buff=0, color='red',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        label_1 = vec_n1.coordinate_label().scale(0.6).next_to(vec_n1.get_end(), 
                            RIGHT+UP*1.1).set_color(RED)
        label_n1 = Tex('$\\vec{n_1} = [1.5, 1]$', font_size=40).scale(0.6).next_to(vec_n1.get_end(), 
                        LEFT + 0.6*UP).set_color(RED)
        
        vec_n2 = Vector([3, 0, 0], buff=0, color='blue',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        label_n2 = Tex('$\\vec{n_2}$', color='blue', font_size=40).scale(0.6).next_to(vec_n2.get_end(), 
                        LEFT*0.3 + UP)
        self.add(vec_n1, label_n1, vec_n2, label_n2)
        
        # arrow_C = Arrow([1.5, 0, 0], [1.5, 1, 0], buff=0, color='#A020F0',
        #     stroke_width=5, max_tip_length_to_length_ratio=0.2, 
        #     max_stroke_width_to_length_ratio=5) 
        arrow_C = Arrow([1.5, 0, 0], [2.1, 1, 0], buff=0, color='green',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        
        C = Tex('$\\vec{C}$', font_size=40, color = '#A020F0').scale(0.6).next_to(arrow_C.get_end(), 
                    RIGHT+DOWN*2)
        # C = Tex('$non-orthogonal$', font_size=50, color = '#A020F0').scale(0.6).next_to(arrow_C.get_end(), 
        #             RIGHT+DOWN*2)
        # self.add(arrow_C, C)
        self.add(arrow_C)
    
        # START = (3,-10,0)
        # END =   (3,10,0)
        # x_line = Line(START,END, color='green')
        # self.add(x_line)