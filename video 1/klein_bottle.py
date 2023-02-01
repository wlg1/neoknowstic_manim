from manim import *

class KleinBottleTransformation(Scene):
    def construct(self):
        # Create the Klein bottle object
        klein_bottle = Surface(
            lambda u, v: np.array([
                3 * np.cos(u) * (1 + np.sin(u)) + (2 * (1 - np.cos(u) / 2)) * np.cos(u) * np.cos(v),
                3 * np.sin(u) * (1 + np.sin(u)) + (2 * (1 - np.cos(u) / 2)) * np.sin(u) * np.cos(v),
                -2 * (1 - np.cos(u) / 2) * np.sin(v)
            ]), u_range = [ -np.pi, np.pi], v_range = [-np.pi, np.pi], checkerboard_colors=[YELLOW_E, BLUE],
            resolution=(15, 32)).scale(0.5)
            # ]), u_min=-np.pi, u_max=np.pi, v_min=-np.pi, v_max=np.pi, checkerboard_colors=[YELLOW_E, BLUE],
            # resolution=(15, 32)).scale(0.5)
        
        klein_bottle.move_to(ORIGIN)

        # Add the Klein bottle to the scene
        self.add(klein_bottle)
        
        # Create a transformation for the Klein bottle
        transform = Rotate(klein_bottle, about_point=ORIGIN, axis=UP, angle=2*PI, rate_func=linear)
        
        # Show the transformation animation
        self.play(transform, run_time=5)



# https://www.reddit.com/r/manim/comments/p0042w/klein_bottle/
# from manim import *

# from numpy import *

# class Topology(ThreeDScene):
#     def construct(self):

#         self.set_camera_orientation(phi=55 * DEGREES, theta=-45 * DEGREES)

#         klein_bottle = Surface(

#         lambda u, v : np.array([

#         (-2/15)*cos(u)*( 3*cos(v) - 30*sin(u) + 90*(cos(u)**4)*sin(u) - 60*(cos(u)**6)*sin(u) + 5*cos(u)*cos(v)*sin(u) ),

#         (-1/15)*sin(u)*( 3*cos(v) - 3*(cos(u)**2)*cos(v) - 48*(cos(u)**4)*cos(v) + 48*(cos(u)**6)*cos(v) - 60*sin(u) + 5*cos(u)*cos(v)*sin(u)

#         - 5*(cos(u)**3)*cos(v)*sin(u) - 80*(cos(u)**5)*cos(v)*sin(u) + 80*(cos(u)**7)*cos(v)*sin(u) ),

#         (2/15)*( 3 + 5*cos(u)*sin(u) )*sin(v)

#         ]),

#         u_min = 0,

#         u_max = np.pi,

#         v_min = 0,

#         v_max = 2*np.pi,

#         resolution=55,

#         stroke_color=[BLUE_B],

#         stroke_width=0.50,

#         surface_piece_config={},

#         fill_color=GREY_B,

#         #fill_opacity=0.2,

#         checkerboard_colors=[GREY_B],

#         should_make_jagged=True,

#         make_smooth_after_applying_functions=True,

#         )

#         # klein_bottle.set_style(fill_opacity=1)

#         # klein_bottle.set_style(stroke_color=[BLUE, GREEN, YELLOW])

#         klein_bottle.set_fill_by_checkerboard(GREY_B, GREY_B, opacity=0.2)

#         klein_bottle.move_to(ORIGIN)

#         klein_bottle.scale(2)

#         self.add(klein_bottle)

#         self.begin_ambient_camera_rotation(rate=0.2)

#         self.wait(10)