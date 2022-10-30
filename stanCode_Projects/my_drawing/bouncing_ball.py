"""
File: bouncing_ball.py
Name: Joanna
-------------------------
When user clicks the mouse, there is a window showing an animation of bouncing ball at (START_X, START_Y).
During falling the ball, the x velocity remains constant and the y velocity increases
with the gravitational acceleration.
When the ball collides the floor, each bounce reduces y velocity to REDUCE of itself.
If the ball is out of the window more than three times,
the animation will stop and the ball appear in the initial position.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3  # x component of the velocity.
DELAY = 10  # animation duration.
GRAVITY = 1  # gravitational acceleration, each while loop increases y velocity.
SIZE = 20   # diameter of the ball.
REDUCE = 0.9    # the reduced ratio of the vertical velocity for each bounce.
START_X = 30    # initial x coordinate of the ball.
START_Y = 40    # initial y coordinate of the ball.
# global Variable
window = GWindow(800, 500, title='bouncing_ball.py')    # creating a window for animation of bouncing ball.
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)  # creating a ball according to the SIZE and the initial position.
click = False   # controlling only one bouncing ball in the window.
num = 0     # counting the number of times when ball is out of the window.


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True  # filling color in the ball.
    window.add(ball)    # adding a ball in the window.
    onmouseclicked(bounce)  # when user clicks the mouse, the window starts to show bouncing ball.


def bounce(_):
    # using 'global + variable' to change the value of the global variable.
    global num
    global click
    global ball
    if not click:   # checking whether only one bouncing ball in the window.
        if num < 3:     # user only has three times to bounce the ball.
            num += 1    # counting the number of the times to animate bouncing ball.
            vy = 0     # initial y velocity is zero.
            click = True    # when click == True, user can not add another ball in the window.
            while True:
                if ball.x + ball.width < window.width:  # the ball is inside the window
                    ball.move(VX, vy)   # moving the ball.
                    pause(DELAY)    # animation duration
                    vy += GRAVITY   # each while loop increases y velocity with gravity acceleration.
                    if ball.y + ball.height >= window.height:   # the ball collides the floor.
                        vy *= -REDUCE   # y velocity is reduced to 'REDUCE' constant of itself.
                        while True:
                            if vy <= 0:   # y velocity is negative
                                ball.move(VX, vy)   # moving the ball.
                                pause(DELAY)    # animation duration
                                vy += GRAVITY   # each while loop increases y velocity with gravity acceleration.
                            else:   # False. y velocity is positive, the ball is going to fall down
                                break
                else:
                    window.remove(ball)     # False. The ball is out of the window.
                    click = False   # when click == False, user can click the mouse to start a bouncing ball.
                    window.add(ball, x=START_X, y=START_Y)  # adding a ball in the window.
                    break


if __name__ == "__main__":
    main()
