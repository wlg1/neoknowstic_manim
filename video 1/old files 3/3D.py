from manim import *

class LinearTransformation3D(ThreeDScene):
    def construct(self):
        # Define the 3D coordinate system
        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)

        # Define the transformation matrix
        matrix = np.array([
            [1, 0],
            [0, 1],
            [0, 0]
        ])

        # Define the initial and final points
        point1 = np.array([1, 0])
        point2 = np.array([0, 1])
        point3 = np.array([0, 0, 1])
        point4 = np.dot(matrix, point1)
        point5 = np.dot(matrix, point2)
        point6 = np.dot(matrix, point3)
        
        # Create the initial and final points as spheres
        sphere1 = Sphere(color=RED, radius=0.2)
        sphere2 = Sphere(color=GREEN, radius=0.2)
        sphere3 = Sphere(color=BLUE, radius=0.2)
        sphere4 = Sphere(color=RED, radius=0.2)
        sphere5 = Sphere(color=GREEN, radius=0.2)
        sphere6 = Sphere(color=BLUE, radius=0.2)

        # Add the initial points to the scene
        self.add(sphere1)
        self.add(sphere2)
        self.add(sphere3)
        
        # Transform the initial points to the final points
        self.play(Transform(sphere1, sphere4, matrix=matrix))
        self.play(Transform(sphere2, sphere5, matrix=matrix))
        self.play(Transform(sphere3, sphere6, matrix=matrix))