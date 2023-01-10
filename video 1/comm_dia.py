from manim import *

class ArrowAnimation(Scene):
    def construct(self):
        dot1 = Dot(radius=0.1, color=WHITE)
        dot1.move_to([0,1,0])
        self.add(dot1)
        
        topLine = Line([0,1,0], [1,1,0], color = '#00008B') #dark blue
        leftLine = Line([0,1,0], [0,0,0], color = 'blue') # light blue
        self.play(GrowFromPoint(topLine, [0,1,0]),
                    GrowFromPoint(leftLine, [0,1,0]))
        
        dot2 = Dot(radius=0.1, color=PURPLE)
        dot2.move_to([1,0,0])
                            
        rightLine = Line([1,1,0], [1,0,0], color = '#8b0000') # dark red
        bottomLine = Line([0,0,0], [1,0,0], color = 'red') #light red
        self.play(GrowFromPoint(rightLine, [1,1,0]),
                    GrowFromPoint(bottomLine, [0,0,0]),
                    FadeIn(dot2))
        
        Neoknowstic = Text("Neoknowstic", font_size='20').next_to(dot2).shift(LEFT+DOWN*0.2)
        # so below
        
        self.play(
           dot2.animate.scale(1.3),
           # FadeIn(Neoknowstic, shift=DOWN),
           rate_func=linear,
           run_time=0.3
        )
        self.play(
           dot2.animate.scale(0.77),
           rate_func=linear,
           run_time=0.3
        )
        
        self.wait(3)
        
        # rightArr = Arrow([1,1,0], [1,0,0], color = '#8b0000') # dark red
        # bottomArr = Arrow([0,0,0], [1,0,0], color = 'red') 
        # self.play(GrowArrow(rightArr),
                    # GrowArrow(bottomArr))
        
    
