from manim import *

class MoebiusToKlein(Scene):
    def construct(self):
        # Create two Moebius strips
        mobius1 = Surface(
            lambda u, v: np.array([
                np.cos(u) * (1 + 0.5 * np.cos(v)),
                np.sin(u) * (1 + 0.5 * np.cos(v)),
                0.5 * np.sin(v)
            ]), u_range = [ -np.pi, np.pi], v_range = [-np.pi, np.pi], checkerboard_colors=[RED, YELLOW],
            resolution=(15, 32)).scale(0.5)
        mobius2 = Surface(
            lambda u, v: np.array([
                np.cos(u) * (1 + 0.5 * np.cos(v)),
                np.sin(u) * (1 + 0.5 * np.cos(v)),
                -0.5 * np.sin(v)
            ]), u_range = [ -np.pi, np.pi], v_range = [-np.pi, np.pi], checkerboard_colors=[BLUE, GREEN],
            resolution=(15, 32)).scale(0.5)
        
        # Add the Moebius strips to the scene
        self.add(mobius1)
        self.add(mobius2)
        
        # Create a transformation for the Moebius strips
        transform1 = rotation(about_point=ORIGIN, axis=UP, radians=TAU/8)
        transform2 = rotation(about_point=ORIGIN, axis=RIGHT, radians=TAU/8)
        
        # Apply the transformations to the Moebius strips
        transformed_mobius1 = mobius1.copy().apply_matrix(transform1)
        transformed_mobius2 = mobius2.copy().apply_matrix(transform2)
        
        # Merge the two transformed Moebius strips
        merged_mobius = SurfaceUnion(transformed_mobius1, transformed_mobius2)
        
        # Add the merged Moebius strips to the scene
        self.add(merged_mobius)
        
        # Show the merge animation
        self.play(Transform(mobius1, transformed_mobius1), Transform(mobius2, transformed_mobius2))
        self.play(Transform(mobius1, merged_mobius), Transform(mobius2, merged_mobius))
