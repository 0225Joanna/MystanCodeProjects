"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Player needs to destroy all the bricks using a ball. When the player clicks the mouse, the ball start to fall down.
Control the left and right movement of the paddle to bounce the ball without letting the ball fall below the paddle.
Player has three lives at the start of a game. If the ball falls below the paddle, the player loses a life each time.
The goal is to break out all the bricks!!
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 4        # Number of rows of bricks
BRICK_COLS = 4        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self._paddle = GRect(paddle_width, paddle_height)
        self._paddle.filled = True
        self._paddle.fill_color = 'gold'
        self.window.add(self._paddle, x=(self.window.width-self._paddle.width)/2,
                        y=self.window.height-PADDLE_OFFSET-self._paddle.height)
        self._pfs = paddle_offset
        self._pw = paddle_width

        # Center a filled ball in the graphical window
        self.ball = GOval(2*BALL_RADIUS, 2*BALL_RADIUS)
        self.ball.filled = True
        self.ball.fill_color = 'gold'
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)
        self.ball_r = ball_radius

        # Default initial velocity for the ball
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randrange(1, MAX_X_SPEED)
        if random.random() > 0.5:   # determine the vector of the x velocity.
            self.__dx = -self.__dx

        # Initialize our mouse listeners
        self.click = 0
        onmouseclicked(self.start_game)     # when the player clicks the mouse, the game starts.
        onmousemoved(self.change_position)  # by moving the mouse to control the movement of the paddle.

        # Draw bricks
        y_position = BRICK_OFFSET
        self.brick_row = brick_rows
        self.brick_col = brick_cols
        self.brick_num = self.brick_col * self.brick_row    # the number of the bricks.
        for i in range(self.brick_row):     # construct the bricks
            x_position = 0
            for j in range(self.brick_col):
                self._bricks = GRect(brick_width, brick_height)
                self._bricks.filled = True
                if j % 2 == 0:  # determine the color of the bricks
                    self._bricks.fill_color = 'salmon'
                else:
                    self._bricks.fill_color = 'skyblue'
                self.window.add(self._bricks, x=x_position, y=y_position)
                x_position = x_position + self._bricks.width + BRICK_SPACING
            y_position = y_position + self._bricks.height + BRICK_SPACING

    def start_game(self, event):    # when the player click the mouse, the game starts
        if self.click == 0:     # controlling the animation of the ball.
            self.click = 1

    def x_velocity(self):   # return private variable of x velocity.
        return self.__dx

    def y_velocity(self):   # return private variable of y velocity.
        return self.__dy

    def change_position(self, event):   # controlling the movement of the paddle when player moves the mouse.
        if event.x + self._pw/2 >= self.window.width:
            self._paddle.x = self.window.width - self._paddle.width
            self._paddle.y = self.window.height - self._pfs
        elif event.x - self._pw/2 <= 0:
            self._paddle.x = 0
            self._paddle.y = self.window.height - self._pfs
        else:
            self._paddle.x = event.x - self._pw/2
            self._paddle.y = self.window.height - self._pfs

    def collision_checker(self):
        # loop over the corner of the square (ball).
        for i in range(0, 2):
            for j in range(0, 2):
                ball_x = self.ball.x + i*2*self.ball_r
                ball_y = self.ball.y + j*2*self.ball_r
                maybe_boj = self.window.get_object_at(ball_x, ball_y)
                if maybe_boj is not None:
                    if maybe_boj is self._paddle:   # the ball collides the paddle
                        return 0
                    else:
                        self.window.remove(maybe_boj)   # the ball collides the brick
                        self.brick_num -= 1     # counting the number of the remaining bricks.
                        return 1

    def reset_ball(self):   # putting a ball to its initial position.
        self.window.remove(self.ball)
        self.ball = GOval(2 * BALL_RADIUS, 2 * BALL_RADIUS)
        self.ball.filled = True
        self.ball.fill_color = 'gold'
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)








