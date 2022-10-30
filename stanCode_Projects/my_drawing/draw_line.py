"""
File: draw_line.py
Name: Joanna
-------------------------
User can draw a line by clicking the mouse. There is a circle if the number of the mouse click is odd.
As the user clicks again, the circle disappears and a line appears.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10   # radius of the ball.
# Global Variable
window = GWindow()  # creating a window to draw the line.
circle = GOval(2*SIZE, 2*SIZE)  # creating a circle.
click = 0   # number of mouse clicks.


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)   # starting to draw a line when user clicks the mouse.


def draw_line(event):
    global click    # to change the value of the global variable.
    click += 1  # when the user clicks the mouse, the number of the mouse click adds one.
    if click % 2 != 0:  # drawing a circle if the number of the mouse click is odd.
        window.add(circle, x=event.x-circle.width/2, y=event.y-circle.height/2)
    else:
        # False. Remove the circle and draw a line in the window.
        # The start point of the line is the center of the circle,
        # and the end point of the line is the position which user clicks.
        window.remove(circle)
        line = GLine(circle.x, circle.y, event.x, event.y)
        window.add(line)


if __name__ == "__main__":
    main()
