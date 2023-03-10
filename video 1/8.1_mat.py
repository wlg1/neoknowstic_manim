from manim import *
import pdb

# isntead of replacing w_11 with 2, which throws off the functions applied on the indices, just replace w w/ 2 and turn the _11 black. this makes it an analogous form so the same funcs can be applied
# for -3: use ctrl + h for '21' to '22', then for the '3', turn it yellow

class scene_8_mat(Scene):
    def construct(self):
        # m1 = Matrix([["w_{11}", "w_{12}"], ["w_{21}", "w_{22}"]]).scale(2)
        # m2 = Matrix([["w_{11}", "w_{12}"], ["w_{21}", "w_{22}"]]).scale(2)
        # ent = m2.get_entries()
        # ent[0].set_color(YELLOW)
        # rec_1 = SurroundingRectangle(ent[0])
        # self.play(Transform(m1, m2), FadeIn(rec_1))

        # m0 = MathTex(r"\begin{bmatrix} w_{11} \frac{Nap}{Nose} \ \ w_{12} \frac{Nap}{Ear} \\\\ w_{21} \frac{Luck}{Nose} \ \ w_{22} \frac{Luck}{Ear} \end{bmatrix}").scale(2)
        m0 = MathTex(r"\begin{bmatrix} 2_{11} \frac{Nap}{Nose} \ \ 3_{12} \frac{Nap}{Ear} \\\\ -3_{21} \frac{Luck}{Nose} \ \ 2_{22} \frac{Luck}{Ear} \end{bmatrix}").scale(2)
        m0[0][3].set_color(BLACK) #1
        m0[0][4].set_color(BLACK) #1
        m0[0][5:8].set_color(ORANGE) # Nap
        m0[0][9:13].set_color(RED)  # Nose
        m0[0][14].set_color(BLACK) #1
        m0[0][15].set_color(BLACK) #2
        m0[0][16:19].set_color(ORANGE) # Nap
        m0[0][20:23].set_color(BLUE)  # Ear

        m0[0][3+22].set_color(BLACK) #2
        m0[0][4+22].set_color(BLACK) #1
        m0[0][5+22:9+22].set_color(GREEN) # Luck
        m0[0][10+22:14+22].set_color(RED)  # Nose
        m0[0][15+22].set_color(BLACK) #2
        m0[0][16+22].set_color(BLACK) #2
        m0[0][17+22:21+22].set_color(GREEN) # Luck
        m0[0][22+22:25+22].set_color(BLUE)  # Ear

        mat = m0.copy()            
        self.add(mat)

        #####
        # highlight w11
        
        m_yel = m0.copy()
        m_yel[0][2].set_color(YELLOW) 
        # m_yel[0][3].set_color(YELLOW) #1
        # m_yel[0][4].set_color(YELLOW) #1
        m_yel[0][5:8].set_color(YELLOW) # Nap
        m_yel[0][9:13].set_color(YELLOW)  # Nose
        
        rec_1 = SurroundingRectangle(m_yel[0][2:13])
        self.play(Transform(mat, m_yel), FadeIn(rec_1))
        
        self.wait(2)
        
        #####
        # Revert
        
        orig_mat = m0.copy()
        self.play(Transform(mat, orig_mat), FadeOut(rec_1))
        
        self.wait(2)
        
        #####        
        # highlight w12

        m_yel = m0.copy()
        m_yel[0][13].set_color(YELLOW) 
        # m_yel[0][14].set_color(YELLOW) #1
        # m_yel[0][15].set_color(YELLOW) #2
        m_yel[0][16:19].set_color(YELLOW) # Nap
        m_yel[0][20:23].set_color(YELLOW)  # Ear
        
        rec_1 = SurroundingRectangle(m_yel[0][13:23])
        self.play(Transform(mat, m_yel), FadeIn(rec_1))
        
        self.wait(2)

        #####
        # Revert
        
        orig_mat = m0.copy()
        self.play(Transform(mat, orig_mat), FadeOut(rec_1))
        
        self.wait(2)
        
        #####        
        # highlight w21

        m_yel = m0.copy()
        m_yel[0][23].set_color(YELLOW) #-
        m_yel[0][24].set_color(YELLOW) #3
        # m_yel[0][3+22].set_color(YELLOW) #2
        # m_yel[0][4+22].set_color(YELLOW) #1
        m_yel[0][5+22:9+22].set_color(YELLOW) # Luck
        m_yel[0][10+22:14+22].set_color(YELLOW)  # Nose
        
        rec_1 = SurroundingRectangle(m_yel[0][23:14+22])
        self.play(Transform(mat, m_yel), FadeIn(rec_1))
        
        self.wait(2)

        #####
        # Revert
        
        orig_mat = m0.copy()
        self.play(Transform(mat, orig_mat), FadeOut(rec_1))
        
        self.wait(2)
        
        #####        self.wait(2)
        # highlight w22

        m_yel = m0.copy()
        m_yel[0][14+22].set_color(YELLOW) #w
        # m_yel[0][15+22].set_color(YELLOW) #2
        # m_yel[0][16+22].set_color(YELLOW) #2
        m_yel[0][17+22:21+22].set_color(YELLOW) # Luck
        m_yel[0][22+22:25+22].set_color(YELLOW)  # Ear
        
        rec_1 = SurroundingRectangle(m_yel[0][14+22:25+22])
        self.play(Transform(mat, m_yel), FadeIn(rec_1))
        
        self.wait(2)

        #####
        # Revert
        
        orig_mat = m0.copy()
        self.play(Transform(mat, orig_mat), FadeOut(rec_1))
        
        self.wait(2)
        