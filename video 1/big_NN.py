from manim import *
import pdb

class bigNN(Scene):
    def construct(self):   
        inNode_1 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([-3, 2, 0])
        inNode_2 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([-3, 0, 0])
        inNode_3 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([-3, -2, 0])

        midNode_1 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([0, 1, 0])
        midNode_2 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([0, -1, 0])

        outNode_1 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([3, 2, 0])
        outNode_2 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([3, 0, 0])
        outNode_3 = Circle(radius=0.5, fill_color=GRAY, fill_opacity=1,  color=GRAY, stroke_width=1).move_to([3, -2, 0])
        
        conn_1 = Line(inNode_1.get_center(), midNode_1.get_center(), color=GRAY)
        conn_2 = Line(inNode_2.get_center(), midNode_1.get_center(), color=GRAY)
        conn_3 = Line(inNode_3.get_center(), midNode_1.get_center(), color=GRAY)
        conn_4 = Line(inNode_1.get_center(), midNode_2.get_center(), color=GRAY)
        conn_5 = Line(inNode_2.get_center(), midNode_2.get_center(), color=GRAY)
        conn_6 = Line(inNode_3.get_center(), midNode_2.get_center(), color=GRAY)
        conn_7 = Line(midNode_1.get_center(), outNode_1.get_center(), color=GRAY)
        conn_8 = Line(midNode_1.get_center(), outNode_2.get_center(), color=GRAY)
        conn_9 = Line(midNode_1.get_center(), outNode_3.get_center(), color=GRAY)
        conn_10 = Line(midNode_2.get_center(), outNode_1.get_center(), color=GRAY)
        conn_11 = Line(midNode_2.get_center(), outNode_2.get_center(), color=GRAY)
        conn_12 = Line(midNode_2.get_center(), outNode_3.get_center(), color=GRAY)
                
        bigNN = VGroup(conn_1, conn_2, conn_3, conn_4, conn_5, conn_6, conn_7, conn_8, conn_9, conn_10, conn_11, conn_12, inNode_1, inNode_2, inNode_3, midNode_1, midNode_2, outNode_1, outNode_2, outNode_3).scale(0.75).shift(DOWN*1.2)

        inNode_1.color= WHITE
        conn_1.color= WHITE
        
        self.add(bigNN)