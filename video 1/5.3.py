from manim import *
import pdb

class scene_5_3(Scene):
    def construct(self):      
        '''Because this combination of nose tip and ear length describes our cat people input, we call this 2D coordinate space our Input Space.'''
    
        numberplane = NumberPlane()
        self.add(numberplane)
        
        self.wait(2)
        
        input_space_text = Text("Input Space").shift(UP)
        self.play(Write(input_space_text))
        
        self.wait(2)
        
        
        