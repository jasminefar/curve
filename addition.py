#updating this (adding)

# imports (turtle is the main i have import used)
import turtle
import random
import math

class TwistedSpiral:
    def __init__(self, steps, step_length, angle):
        self.steps = steps
        self.step_length = step_length
        self.angle = angle
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.setup(width=800, height=800)
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(0, 0)
        self.turtle.pendown()
        self.color_mode = 'gradient'
        self.angle_variation = False
        self.custom_colors = [(0, 0, 0)]

    def set_color_mode(self, mode):
        """Set the color mode for the spiral ('gradient', 'random', 'custom')."""
        if mode in ['gradient', 'random', 'custom']:
            self.color_mode = mode
        else:
            raise ValueError("Invalid color mode. Choose 'gradient', 'random', or 'custom'.")

    def set_custom_colors(self, colors):
        """Set custom colors for the spiral if 'custom' mode is selected."""
        if isinstance(colors, list) and all(isinstance(c, tuple) and len(c) == 3 for c in colors):
            self.custom_colors = colors
        else:
            raise ValueError("Colors must be a list of RGB tuples.")

    def enable_angle_variation(self, enable):
        """Enable or disable random angle variation."""
        self.angle_variation = enable

    def draw(self):
        length = self.step_length
        direction = 1  # forward direction

        for step in range(self.steps):
            self.turtle.forward(length)
            length += self.step_length / 2  # Increase length gradually

            #direction nd angle
            if step % 2 == 0:
                if self.angle_variation:
                    self.turtle.right(self.angle + random.randint(-10, 10))
                else:
                    self.turtle.right(self.angle)
            else:
                if self.angle_variation:
                    self.turtle.left(self.angle + random.randint(-10, 10))
                else:
                    self.turtle.left(self.angle)

            # setting color
            self.turtle.pencolor(self._get_color(step))

        self.screen.mainloop()

    def _get_color(self, step):
        if self.color_mode == 'gradient':
            return self._get_gradient_color(step)
        elif self.color_mode == 'random':
            return self._get_random_color()
        elif self.color_mode == 'custom':
            return self._get_custom_color(step)

    def _get_gradient_color(self, step):
        # color using step numbeers
        r = (step % 256) / 255.0
        g = ((step * 2) % 256) / 255.0
        b = ((step * 3) % 256) / 255.0
        return (r, g, b)

    def _get_random_color(self):
        # random color
        r = random.random()
        g = random.random()
        b = random.random()
        return (r, g, b)

    def _get_custom_color(self, step):
        # custom colors
        return self.custom_colors[step % len(self.custom_colors)]

if __name__ == "__main__":
    steps = 200  # steps in the spiral
    step_length = 5  # len(each step)
    angle = 89  # rotation after each step

    spiral = TwistedSpiral(steps, step_length, angle)
    
    # custom spiral
    spiral.set_color_mode('custom')  # 'gradient', 'random', 'custom'
    spiral.set_custom_colors([(1, 0, 0), (0, 1, 0), (0, 0, 1)])  # Red, Green, Blue
    spiral.enable_angle_variation(True)

    spiral.draw()