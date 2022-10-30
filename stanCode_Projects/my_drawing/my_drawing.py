"""
File: my_drawing.py
Name: Joanna
----------------------
This file creates a pattern that is going to compete for the best my drawing.
"""

from campy.graphics.gobjects import GOval, GRect, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Winnie the Pooh
    I love Winnie the Pooh!!!
    """
    window = GWindow(width=500, height=500)     # creating a window to draw a pattern
    # create a background and fill color
    background = GRect(500, 500)
    background.filled = True
    background.fill_color = 'lightblue'
    window.add(background)
    # create the ears and fill color
    l_ear = GOval(80, 100, x=100, y=60)
    l_ear.color = 'gold'
    l_ear.filled = True
    l_ear.fill_color = 'gold'
    window.add(l_ear)
    r_ear = GOval(80, 100, x=320, y=60)
    r_ear.color = 'gold'
    r_ear.filled = True
    r_ear.fill_color = 'gold'
    window.add(r_ear)
    # create the hands and fill color
    l_hand = GOval(100, 70, x=90, y=300)
    l_hand.color = 'gold'
    l_hand.filled = True
    l_hand.fill_color = 'gold'
    window.add(l_hand)
    r_hand = GOval(100, 70, x=310, y=300)
    r_hand.color = 'gold'
    r_hand.filled = True
    r_hand.fill_color = 'gold'
    window.add(r_hand)
    # create a body and fill color
    body = GOval(240, 280)
    body.color = 'gold'
    body.filled = True
    body.fill_color = 'gold'
    window.add(body, x=130, y=260)
    # create a cloth and fill color
    cloth = GArc(240, 600, 0, 180)
    cloth.color = 'red'
    cloth.filled = True
    cloth.fill_color = 'red'
    window.add(cloth, x=130, y=250)
    # create a head and fill color
    head = GOval(280, 240, x=110, y=100)
    head.color = 'gold'
    head.filled = True
    head.fill_color = 'gold'
    window.add(head)
    # create the eyes and fill color
    l_eye = GOval(25, 25, x=170, y=230)
    l_eye.color = 'saddlebrown'
    l_eye.filled = True
    l_eye.fill_color = 'saddlebrown'
    window.add(l_eye)
    r_eye = GOval(25, 25, x=300, y=230)
    r_eye.color = 'saddlebrown'
    r_eye.filled = True
    r_eye.fill_color = 'saddlebrown'
    window.add(r_eye)
    # create the eyebrows and fill color
    l_eyebrow = GArc(80, 80, 30, 90)
    l_eyebrow.color = 'saddlebrown'
    window.add(l_eyebrow, x=150, y=190)
    l_eyebrow = GArc(80, 80, 30, 90)
    l_eyebrow.color = 'saddlebrown'
    window.add(l_eyebrow, x=150, y=191)
    l_eyebrow = GArc(80, 80, 30, 90)
    l_eyebrow.color = 'saddlebrown'
    window.add(l_eyebrow, x=150, y=192)

    r_eyebrow = GArc(80, 80, 30, 90)
    r_eyebrow.color = 'saddlebrown'
    window.add(r_eyebrow, x=280, y=190)
    r_eyebrow = GArc(80, 80, 30, 90)
    r_eyebrow.color = 'saddlebrown'
    window.add(r_eyebrow, x=280, y=191)
    r_eyebrow = GArc(80, 80, 30, 90)
    r_eyebrow.color = 'saddlebrown'
    window.add(r_eyebrow, x=280, y=192)
    # create a nose and fill color
    nose = GOval(40, 30)
    nose.color = 'saddlebrown'
    nose.filled = True
    nose.fill_color = 'saddlebrown'
    window.add(nose, x=230, y=260)


if __name__ == '__main__':
    main()
