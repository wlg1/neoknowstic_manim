from manim import *
# from DottedLine import *

class DottedLine(Line):

    """A dotted :class:`Line`.
    Parameters
    ----------
    args : Any
        Arguments to be passed to :class:`Line`
    dot_spacing : Optional[:class:`float`]
        Minimal spacing of the dots. The spacing is scaled up to fit the start and end of the line.
    dot_kwargs : Any
        Arguments to be passed to ::class::`Dot`
    kwargs : Any
        Additional arguments to be passed to :class:`Line`
    Examples
    --------
    .. manim:: DottedLineExample
        :save_last_frame:
        class DottedLineExample(Scene):
            def construct(self):
                # default dotted line
                dotted_1 = DottedLine(LEFT, RIGHT))
                # reduced spacing
                dotted_2 = DottedLine(LEFT, RIGHT, dot_spacing=.3).shift(.5*DOWN))
                # smaller and colored dots
                dotted_3 = DottedLine(LEFT, RIGHT, dot_kwargs=dict(radius=.04, color=YELLOW)).shift(DOWN))
        
                self.add(dotted_1, dotted_2, dotted_3)

    """

    def __init__(
        self,
        *args,
        dot_spacing=0.4,
        dot_kwargs={},
        **kwargs
    ):
        Line.__init__(self, *args, **kwargs)
        n_dots = int(self.get_length() / dot_spacing) + 1
        dot_spacing = self.get_length() / (n_dots - 1)
        unit_vector = self.get_unit_vector()
        start = self.start

        self.dot_points = [start + unit_vector * dot_spacing * x for x in range(n_dots)]
        self.dots = [Dot(point, **dot_kwargs) for point in self.dot_points]

        self.clear_points()

        self.add(*self.dots)

        self.get_start = lambda: self.dot_points[0]
        self.get_end = lambda: self.dot_points[-1]

    def get_first_handle(self):
        return self.dot_points[-1]

    def get_last_handle(self):
        return self.dot_points[-2]
        
class VectorArrow(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        
        face = ImageMobject("face1_nonum.png")
        face.scale(0.4)
        face.move_to(np.array([-2, 2.5, 0]))
        self.add(face)
        
        body = ImageMobject("body1_nonum.png")
        body.scale(0.4)
        body.move_to(np.array([2.5, -2, 0]))
        self.add(body)
        
        arrow_c = Arrow(ORIGIN, [-2, 2.5, 0], buff=0, color='#E74C3C',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker red
        text_c = Tex('$\\vec{face} = $', font_size=30).next_to(arrow_c.get_end(), 
            LEFT*4.3+UP*1.1)
        m_c = Matrix([[-2], [2.5]]).scale_to_fit_height(0.75).next_to(arrow_c.get_end(), 
            LEFT+UP*1.1)
        arrow_d = Arrow(ORIGIN, [2.5, -2, 0], buff=0, color='#3498DB',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) #darker blue
        text_d = Tex('$\\vec{body} = $', font_size=30).next_to(arrow_d.get_end(), 
            RIGHT*0.5+UP*1.1)
        m_d = Matrix([[2.5], [-2]]).scale_to_fit_height(0.75).next_to(arrow_d.get_end(), 
            RIGHT*5.3+UP*1.1)
        self.add(arrow_c, text_c, m_c, arrow_d, text_d, m_d)
        
        x = Tex('x', font_size=40).move_to(np.array([1.2, -0.2, 0]))
        y = Tex('y', font_size=40).move_to(np.array([0.2, 1.2, 0]))
        self.add(x, y)
        
        #to create dashed line w/ arrow, first place arrow. 
        #then place black dashed line on top of it, adjusting so doesn't overlap w/ grid

        # arrow_face_x = DottedLine([0, -0.1, 0], [-0.5, -0.1, 0], color='#E74C3C').add_tip()         
        arrow_face_x = Arrow([0, -0.1, 0], [-2, -0.1, 0], buff=0, color='#E74C3C',
            stroke_width=4, max_tip_length_to_length_ratio=0.2, 
            max_stroke_width_to_length_ratio=3) 
        dashed_face_x = DashedLine([-0.01, -0.1, 0], [-1.65, -0.1, 0], color='black')
        text_1 = Tex('$\\vec{face}_x = $', font_size=30).next_to(arrow_face_x.get_end(), 
            LEFT*4.3+UP*1.1)
        m_x = Matrix([[-2], [0]]).scale_to_fit_height(0.75).next_to(arrow_face_x.get_end(), 
            LEFT+UP*1.1)
        arrow_body_x = Arrow([0, 0.1, 0], [2.5, 0.1, 0], buff=0, color='#3498DB',
            stroke_width=4, max_tip_length_to_length_ratio=0.1, 
            max_stroke_width_to_length_ratio=3) 
        dashed_body_x = DashedLine([0.01, 0.1, 0], [2.15, 0.1, 0], color='black')
        text_2 = Tex('$\\vec{body}_x = $', font_size=30).next_to(arrow_body_x.get_end(), 
            RIGHT*0.5+UP*1.1)
        m_y = Matrix([[2.5], [0]]).scale_to_fit_height(0.75).next_to(arrow_body_x.get_end(), 
            RIGHT*5.3+UP*1.1)
        self.add(arrow_face_x, dashed_face_x, text_1, m_x,
                arrow_body_x, dashed_body_x, text_2, m_y)
        