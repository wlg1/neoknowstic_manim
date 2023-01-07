#https://machinelearningmastery.com/singular-value-decomposition-for-machine-learning/


# Reconstruct SVD
from numpy import array
from numpy import diag
from numpy import dot
from numpy import zeros
from scipy.linalg import svd, inv, eig
# define a matrix
# A = array([[1, 2], [3, 4], [5, 6]])
A = array([[1, -2], [3, 4]])
# print(A)

# Singular-value decomposition
# s is vector of eigenvals
U, s, VT = svd(A)
# create m x n Sigma matrix
Sigma = zeros((A.shape[0], A.shape[1]))
# populate Sigma with n x n diagonal matrix
Sigma[:A.shape[1], :A.shape[1]] = diag(s)

# reconstruct matrix
B = U.dot(Sigma.dot(VT))
# print(B)

print(VT)

inv_VT = inv(VT)
print(inv_VT)

# print(U)

#####
# w, eigvec = eig(A)
# print(eigvec)

# print(inv(eigvec))
#####

#V is a matrix of eigenvectors of A^T * A, not of A
# inv(A) != transpose(A)

#to make it equal V, should rearrange columns
w, eigvec = eig(A.transpose().dot(A))
print(eigvec)

AA = A.transpose().dot(A)
mult_eigen = AA.dot(VT)

from manim import *
from random import randint, random
        
class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        self.add(numberplane, dot)
        
        # face = ImageMobject("face1.png")
        # face.scale(0.55)
        # face.move_to(np.array([1, 0, 0]))
        # self.add(face)
        # 
        # body = ImageMobject("body1.png")
        # body.scale(0.55)
        # body.move_to(np.array([0, 1, 0]))
        # self.add(body)
        
        arrow_c = Arrow(ORIGIN, [1, 0, 0], buff=0, color='#FA8072',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #light red
        arrow_d = Arrow(ORIGIN, [0, 1, 0], buff=0, color='#CCCCFF',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #light blue
        self.add(arrow_c, arrow_d)

        arrow_c = Arrow(ORIGIN, [VT[0][0], VT[1][0], 0], buff=0, color='#FA8072',
             stroke_width=4, max_tip_length_to_length_ratio=0.1, 
             max_stroke_width_to_length_ratio=3) #light red
        arrow_d = Arrow(ORIGIN, [VT[0][1], VT[1][1], 0], buff=0, color='#CCCCFF',
             stroke_width=4, max_tip_length_to_length_ratio=0.1, 
             max_stroke_width_to_length_ratio=3) #light blue
        self.add(arrow_c, arrow_d)
        
        # arrow_c = Arrow(ORIGIN, [eigvec[0][0], eigvec[1][0], 0], buff=0, color='red',
        #      stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #      max_stroke_width_to_length_ratio=3) 
        # arrow_d = Arrow(ORIGIN, [eigvec[0][1], eigvec[1][1], 0], buff=0, color='blue',
        #      stroke_width=4, max_tip_length_to_length_ratio=0.1, 
        #      max_stroke_width_to_length_ratio=3)
        # self.add(arrow_c, arrow_d)
        
        arrow_c = Arrow(ORIGIN, [AA[0][0], AA[1][0], 0], buff=0, color='orange',
             stroke_width=4, max_tip_length_to_length_ratio=0.1, 
             max_stroke_width_to_length_ratio=3) 
        arrow_d = Arrow(ORIGIN, [AA[0][1], AA[1][1], 0], buff=0, color='green',
             stroke_width=4, max_tip_length_to_length_ratio=0.1, 
             max_stroke_width_to_length_ratio=3)
        self.add(arrow_c, arrow_d)
        
        arrow_c = Arrow(ORIGIN, [mult_eigen[0][0], mult_eigen[1][0], 0], buff=0, color='red',
             stroke_width=4, max_tip_length_to_length_ratio=0.1, 
             max_stroke_width_to_length_ratio=3) 
        arrow_d = Arrow(ORIGIN, [mult_eigen[0][1], mult_eigen[1][1], 0], buff=0, color='blue',
             stroke_width=4, max_tip_length_to_length_ratio=0.1, 
             max_stroke_width_to_length_ratio=3)
        self.add(arrow_c, arrow_d)
                
        