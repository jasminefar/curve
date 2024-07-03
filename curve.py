import turtle

class HilbertCurveDrawer:
    def __init__(self, order=5, size=10, speed=1):
        """
        Initialize the HilbertCurveDrawer with initial parameters.
        
        order: The order of the Hilbert curve (the higher the order, the more complex the curve).
        size: The size of each segment.
        speed: The drawing speed of the turtle.
        """
        self.order = order
        self.size = size
        self.speed = speed
        self.t = turtle.Turtle()
        self.t.speed(speed)
    
    def hilbert_curve(self, order, angle):
        """
        Recursively draw the Hilbert curve.
        
        order: The order of the curve.
        angle: The turning angle.
        """
        if order == 0:
            return
        self.t.right(angle)
        self.hilbert_curve(order - 1, -angle)
        self.t.forward(self.size)
        self.t.left(angle)
        self.hilbert_curve(order - 1, angle)
        self.t.forward(self.size)
        self.hilbert_curve(order - 1, angle)
        self.t.left(angle)
        self.t.forward(self.size)
        self.hilbert_curve(order - 1, -angle)
        self.t.right(angle)

    def start_drawing(self):
        """Start the drawing process."""
        turtle.bgcolor("black")
        self.t.color("white")
        self.t.penup()
        self.t.goto(-200, 200)  # Position the turtle at the starting point
        self.t.pendown()
        self.hilbert_curve(self.order, 90)
        turtle.done()

    def set_colors(self, background_color="black", curve_color="white"):
        """
        Set the colors for the background and the curve.
        
        background_color: The color of the background.
        curve_color: The color of the curve.
        """
        turtle.bgcolor(background_color)
        self.t.color(curve_color)

    def start_drawing_with_colors(self, background_color="black", curve_color="white"):
        """Start the drawing process with custom colors."""
        self.set_colors(background_color, curve_color)
        self.t.penup()
        self.t.goto(-200, 200)  # Position the turtle at the starting point
        self.t.pendown()
        self.hilbert_curve(self.order, 90)
        turtle.done()

# Create an instance of HilbertCurveDrawer with parameters to extend drawing time and start drawing
hilbert = HilbertCurveDrawer(order=6, size=10, speed=1)
hilbert.start_drawing_with_colors(background_color="darkblue", curve_color="cyan")
