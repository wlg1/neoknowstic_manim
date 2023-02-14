from manim import *

from manim import *

# class FloatingSphereWithShadowAndLight(ThreeDScene):
#     def construct(self):
#         # Define the sphere
#         sphere = Sphere(radius=1, fill_color=BLUE, fill_opacity=0.5)
        
#         # Add the sphere to the scene
#         self.add(sphere)
#         self.set_camera_orientation(phi=70 * DEGREES)
        
#         # Animate the sphere to float
#         self.play(
#             sphere.animate.shift([0, 0, 2]),
#             run_time=3
#         )
        
#         # Define the plane to receive the shadow
#         plane = NumberPlane(stroke_width=1, stroke_color=WHITE)
#         plane.rotate(TAU/4, RIGHT)
#         plane.rotate(TAU/4, UP)
#         plane.shift(2 * UP + 2 * LEFT)
        
#         # Add the plane to the scene
#         self.add(plane)
        
#         # Define the shadow
#         shadow = Circle(radius=1, fill_color=GRAY, fill_opacity=0.5)
        
#         # Project the shadow onto the plane
#         shadow_on_plane = shadow.copy().move_to(plane)
        
#         # Add the shadow to the scene
#         self.add(shadow_on_plane)
        
#         # Define the light source
#         light = self.camera.light_source
#         light.move_to(3 * UP + 3 * LEFT)
        
#         # Add the light source to the scene
#         self.add(light)
        
#         # Apply the light source to the sphere
#         sphere_with_light = sphere.copy().add_shade(light)
#         sphere_with_light.move_to(sphere)
        
#         # Animate the sphere with the light source
#         self.play(
#             ReplacementTransform(sphere, sphere_with_light),
#             run_time=2
#         )
        
#         # Animate the sphere to show its 3D nature
#         self.begin_ambient_camera_rotation(rate=0.1)
#         self.wait(2)


# class FloatingSphereWithShadowSurface(ThreeDScene):
#     def construct(self):
#         # Define the sphere
#         sphere = Sphere(radius=1, fill_color=BLUE, fill_opacity=0.5)
#         sphere.shift([0, 0, 2])
        
#         # Add the sphere to the scene
#         self.add(sphere)
#         # self.set_camera_orientation(phi=70 * DEGREES)
        
#         # Animate the sphere to float
#         # self.play(
#         #     sphere.animate.shift([0, 0, 2]),
#         #     run_time=3
#         # )

        
#         # Define the plane to receive the shadow
#         plane = NumberPlane(stroke_width=1, stroke_color=WHITE)
#         plane.rotate(TAU/2, RIGHT)
#         plane.rotate(TAU/2, UP)
#         # plane.shift(2 * UP + 2 * LEFT)
        
#         # Add the plane to the scene
#         self.add(plane)
        
#         # Define the shadow
#         shadow = Circle(radius=1, fill_color=GRAY, fill_opacity=0.5)
        
#         # Project the shadow onto the plane
#         shadow_on_plane = shadow.copy().move_to(plane)
        
#         # Add the shadow to the scene
#         self.add(shadow_on_plane)
        
#         # Animate the sphere to show its 3D nature
#         # self.begin_ambient_camera_rotation(rate=0.1)
#         # self.wait(2)


class FloatingSphereWithShadow(ThreeDScene):
    def construct(self):
        # Define the sphere
        sphere = Sphere(radius=1, fill_color=BLUE, fill_opacity=0.5)
        
        # Add the sphere to the scene
        self.add(sphere)
        self.set_camera_orientation(phi=70 * DEGREES)
        
        # Animate the sphere to float
        self.play(
            sphere.animate.shift([0, 0, 2]),
            run_time=3
        )
        
        # Define the shadow
        shadow = Circle(radius=1, fill_color=GRAY, color = RED, fill_opacity=1)
        shadow.move_to([-2, -2, 0])

        shadow_2 = Circle(radius=1, fill_color=GRAY, color = BLUE, fill_opacity=1)
        shadow_2.move_to([2, -2, 0])

        shadow_3 = Circle(radius=1, fill_color=GRAY, color = PURPLE, fill_opacity=1)
        shadow_3.move_to([0, 0, 0])

        conn_1 = Line(shadow.get_center(), shadow_3.get_center())
        conn_2 = Line(shadow_2.get_center(), shadow_3.get_center())
        conn_1.z_index = -1
        conn_2.z_index = -1
        
        # Add the shadow to the scene
        self.add(shadow, shadow_2, shadow_3, conn_1, conn_2)
        
        # Animate the sphere to show its 3D nature
        self.begin_ambient_camera_rotation(rate=0.1)

        sphere_copy = sphere.copy()
        self.play(Transform(sphere_copy, shadow))

        self.wait(4)


# from manim import *

# class SphereWithShadow(ThreeDScene):
#     def construct(self):
#         # Define the sphere
#         sphere = Sphere(radius=1, fill_color=BLUE, fill_opacity=0.5)
        
#         # Add the sphere to the scene
#         self.add(sphere)
        
#         # Define the shadow
#         shadow = Circle(radius=1, fill_color=GRAY, fill_opacity=0.5)
#         shadow.move_to([1, -1, 0])
        
#         # Add the shadow to the scene
#         self.add(shadow)
        
#         # Animate the sphere to show its 3D nature
#         self.begin_ambient_camera_rotation(rate=0.1)
#         self.wait(2)
