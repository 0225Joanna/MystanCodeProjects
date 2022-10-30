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

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()   # using breakoutgraphics.py to construct a ball, paddle and the bricks.
    vx = graphics.x_velocity()  # x velocity of the ball.
    vy = graphics.y_velocity()  # y velocity of the ball.
    life = NUM_LIVES    # lives of the player.
    # animation loop
    while True:
        if life > 0:
            if graphics.brick_num == 0:   # counting the number of the bricks which is destroyed by the player.
                graphics.reset_ball()   # if player breaks out all the bricks, the ball moves to initial position.
                break
            if graphics.click:  # when player clicking the mouse, the game starts.
                graphics.ball.move(vx, vy)  # animation of the ball.
                collision = graphics.collision_checker()    # when a collision occurs, we need to check the object.
                if collision == 0:  # the ball collides the paddle and starts to bounce.
                    if vy > 0:
                        vy = -vy
                    else:
                        vy = vy   # preventing the ball oscillates in the paddle.
                if collision == 1:  # the ball collides the brick and starts to bounce.
                    vy = -vy
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    vx = -vx    # the ball bounces when it is out of the window.
                if graphics.ball.y <= 0:
                    vy = -vy    # the ball bounces when it is out of the window.
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    life -= 1   # when the ball fall below the paddle, the player loses a life.
                    graphics.reset_ball()   # the ball moves to initial position.
                    graphics.click = False  # waiting for another run
                pause(FRAME_RATE)
            pause(FRAME_RATE)
        else:   # player loses the game.
            break


if __name__ == '__main__':
    main()
