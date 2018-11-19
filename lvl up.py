# Simple Sanke game

import turtle
import time
import random

delay = 0.1

# --------------------     score    ----------

score = 0
high_score = 0


#               ----------set up screen-------------------

wn = turtle.Screen()
wn.title("Snake game")
wn.bgcolor("purple")
wn.setup(width=600, height=600)
wn.tracer(0)


#                  ----------------- Snake head------------------
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#                  ----------Snake Food ----------
food = turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("yellow")
food.penup()
food.goto(0,40)

segments = []


# ------------------            PEN -----------------

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


#                ---------------------Function------------

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"



def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#                        ----------keyboard binding-----------
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(level_hard, "h")
wn.onkeypress(level_easy, "e")
#                ------------------main game loop-------------

while True:
    wn.update()

# ==============================      check for a cllsion with bordr    =========
                                                # --------- eikhan thaika  -----------
    def level_hard():
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(.5)
            head.goto(0, 0)
            head.direction = "stop"
            wn.bgcolor("green")

    def level_easy():
        if head.xcor() > 290:
            head.goto(-290, y)

        if head.xcor() < -290:
            head.goto(290, y)

        if head.ycor() > 290:
            head.goto(x, -290)

        if head.ycor() < - 290:
            head.goto(x, 290)
        #wn.onkeypress(level_hard, "h")
        #wn.onkeypress(level_easy, "e")

                                                       # --------- ei porjonto ami korsi  -----------

 # =======================      hide the segment   ====================

        for segment in segments:
            segment.goto(1000, 1000)

# ==================     clear the segments   =======

        segments.clear()
#      ===========      RESET SCORE           =================
        score = 0

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        segments.clear()
# ===================== check cllsion with food   =========
    if head.distance(food) < 20:








            #++++++++++Move the food a random+++++++++


        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

            # +++++++++== ADD A SEGMENT +++++++++++

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("royal blue")
        new_segment.penup()
        segments.append(new_segment)


        # --------------------      Increase Score   ------------

        score += 10

        if score > high_score:
            high_score = score


        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


 # +++++++++++++++++++++++       Move the end segment 1st in reverse order    +++++++++++++


    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

#  +++++++++++           Move segmnt 0 to where head the head is      +++++++++++


    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()


    # ----------    check for head cllsn with the body sgmnt -----------

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.color("red")
            head.direction = "stop"

            # ==========    hide segment =============
            for segment in segments:
                segment.goto(1000, 1000)


            # ==========      clear the segment list   ===========

            segments.clear()







    time.sleep(delay)


wn.mainloop()
