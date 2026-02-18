import random
import turtle as trtl

#------------------Setup------------------#

#Screen setup
wn = trtl.Screen()
wn.setup(width = 800, height = 544)
wn.bgpic("pig background.gif")

#Adding photos
pvp_b = ("PVP button.gif")
wn.addshape(pvp_b)
pvc_b = ("PVC button.gif")
wn.addshape(pvc_b)
d_1 = ("dice 1.gif")
wn.addshape(d_1)
d_2 = ("dice 2.gif")
wn.addshape(d_2)
d_3 = ("dice 3.gif")
wn.addshape(d_3)
d_4 = ("dice 4.gif")
wn.addshape(d_4)
d_5 = ("dice 5.gif")
wn.addshape(d_5)
d_6 = ("dice 6.gif")
wn.addshape(d_6)
roll = ("roll.gif")
wn.addshape(roll)
hold = ("hold.gif")
wn.addshape(hold)
rstart = ("restart.gif")
wn.addshape(rstart)

#creating a list of dice
global dice
dice = [d_1, d_2, d_3, d_4, d_5, d_6]

#Dice turtle
die = trtl.Turtle()
die.shape(d_1)
die.hideturtle()
die.penup()
die.teleport(225, 100)

#Turtle that writes menu screen
writer = trtl.Turtle()
writer.speed(0)
writer.hideturtle()
writer.penup()
writer.teleport(0, 100)

#Arrow that points to who's turn it is
turn = trtl.Turtle()
turn.pencolor("white")
turn.penup()
turn.hideturtle()

#Turtle that colors in bar
bar = trtl.Turtle()
bar.speed(0)
bar.pensize(2)
bar.hideturtle()
bar.penup()

#Turtle that colors in progress during turn
p_bar = trtl.Turtle()
p_bar.speed(0)
p_bar.color("aqua")
p_bar.pensize(2)
p_bar.hideturtle()
p_bar.penup()

#Turtle that writes score
score_t = trtl.Turtle()
score_t.penup()
score_t.hideturtle()
score_t.speed(0)
score_t.teleport(225, -50)

#Player 1
global p1_turn
p1_turn = True
p1_score = 0

#Player 2
global p2_turn
p2_turn = False
p2_score = 0

#------------------Function Definition------------------#

#Function that enables gamemode
def pvp_enable(x, y):
    global play
    global score
    wn.bgpic("table.gif") #Switches the background
    pvp.hideturtle()
    pvc.hideturtle()
    r.showturtle()
    h.showturtle()
    turn.showturtle()
    die.showturtle()
    play = 1 #sets the gamemode
    bar.teleport(-340, -212) #Draws the player bars
    for i in range(2):
        bar.pendown()
        bar.forward(200)
        bar.left(90)
        bar.forward(20)
        bar.left(90)
    bar.teleport(-340, -182)
    for i in range(2):
        bar.pendown()
        bar.forward(200)
        bar.left(90)
        bar.forward(20)
        bar.left(90)
    writer.penup()
    writer.teleport(-65, -187) #states the players scores
    writer.write(f"\nPlayer 1: {p1_score}", align = "center", font = ("Times New Roman", 20, "normal"))
    writer.teleport(-65, -217)
    writer.write(f"\nPlayer 2: {p2_score}", align = "center", font = ("Times New Roman", 20, "normal"))
    score_t.write(f"Turn Total: 0", align = "center", font = ("Times New Roman", 20, "normal"))
    start()

#Function that enables gamemode
def pvc_enable(x, y): #THE WORKEST OF WORK IN PROGRESSES
    global play
    wn.bgpic("table.gif")
    pvp.hideturtle()
    pvc.hideturtle()
    r.showturtle()
    h.showturtle()
    turn.showturtle()
    play = 2
    start()

#Function that colors bars in
def draw_bar():
    global p1_score
    global p2_score
    global p1_turn
    global p2_turn
    if p1_turn == True: #checks for who's turn
        bar.teleport(-340, -182)
        for i in range(2): #fills in the bar of the player to corresponding score
            bar.begin_fill()
            bar.pendown()
            bar.forward(p1_score * 10)
            bar.left(90)
            bar.forward(20)
            bar.left(90)
            bar.end_fill()
    elif p2_turn == True:
        bar.teleport(-340, -212)
        for i in range(2):
            bar.begin_fill()
            bar.pendown()
            bar.forward(p2_score * 10)
            bar.left(90)
            bar.forward(20)
            bar.left(90)
            bar.end_fill()

#Function that draws in bar during turn
def progress_bar():
    global turnscore
    global p1_score
    global p2_score
    global p1_turn
    global p2_turn
    if p1_turn == True: #checks for who's turn
        turn.teleport(-350,-172)
        p_bar.teleport(-340 + (p1_score * 10), -182) #moves the turtle to the new starting position
        for i in range(2): #fills in bar as player rolls
            p_bar.begin_fill()
            p_bar.forward(turnscore * 10)
            p_bar.left(90)
            p_bar.forward(20)
            p_bar.left(90)
            p_bar.end_fill()
    elif p2_turn == True:
        turn.teleport(-350,-202)
        p_bar.teleport(-340 + (p2_score * 10), -212)
        for i in range(2):
            p_bar.begin_fill()
            p_bar.forward(turnscore * 10)
            p_bar.left(90)
            p_bar.forward(20)
            p_bar.left(90)
            p_bar.end_fill()

#Function that handles turns
def take_turn():
    global player
    global turnscore
    global stillgoing
    global p1_turn
    global p2_turn
    global win
    writer.teleport(-65, -187) #states the players scores
    writer.clear()
    writer.write(f"\nPlayer 1: {p1_score}", align = "center", font = ("Times New Roman", 20, "normal"))
    writer.teleport(-65, -217)
    writer.write(f"\nPlayer 2: {p2_score}", align = "center", font = ("Times New Roman", 20, "normal"))
    if p1_turn == True: #checks for who's turn 
        turn.teleport(-350,-172) #sets arrow to player to show who goes
        turnscore = 0
        stillgoing = True
        while stillgoing == True: #keeps the buttons running until player rolls a 1 or holds
            r.onclick(roll_score)
            if full_bar(p1_score) == True:
                win = True
                break
            h.onclick(hold_score)
        turnscore = 0
        writer.clear()
        writer.penup()
        writer.teleport(-65, -187) #states the players scores
        writer.clear()
        writer.write(f"\nPlayer 1: {p1_score}", align = "center", font = ("Times New Roman", 20, "normal"))
        writer.teleport(-65, -217)
        writer.write(f"\nPlayer 2: {p2_score}", align = "center", font = ("Times New Roman", 20, "normal"))
        score_t.write(f"Turn Total: 0", align = "center", font = ("Times New Roman", 20, "normal"))
        p1_turn = False #sets it to other players turn
        p2_turn = True
    elif p2_turn == True: #checks for who's turn
        turn.teleport(-350,-202) #sets arrow to player to show who goes
        turnscore = 0
        stillgoing = True
        while stillgoing == True: #keeps the buttons running until player rolls a 1 or holds
            r.onclick(roll_score)
            if full_bar(p2_score) == True:
                win = True
                break
            h.onclick(hold_score)
        turnscore = 0
        writer.clear()
        writer.penup()
        writer.teleport(-65, -187) #states the players scores
        writer.clear()
        writer.write(f"\nPlayer 1: {p1_score}", align = "center", font = ("Times New Roman", 20, "normal"))
        writer.teleport(-65, -217)
        writer.write(f"\nPlayer 2: {p2_score}", align = "center", font = ("Times New Roman", 20, "normal"))
        score_t.write(f"Turn Total: 0", align = "center", font = ("Times New Roman", 20, "normal"))
        p1_turn = True #sets it to other players turn
        p2_turn = False

#Deals with the roll
def roll_score(x, y):
    global turnscore
    global testscore
    global stillgoing
    global roll1
    global player
    global p1_turn
    global p2_turn
    global win
    testscore = 0
    roll1 = False
    temp_num = 4#random.randint(1, 6) #gives a random dice roll
    die.shape(dice[temp_num - 1]) #shows the die face corresponding to the roll
    if temp_num == 1: #checks for if player rolled a 1
        roll1 = True
        stillgoing = False
        turnscore = 0 #resets the running turn score
        score_t.clear()
        score_t.write(f"Turn Total: {turnscore}", align = "center", font = ("Times New Roman", 20, "normal"))
        p_bar.clear()
        if p2_turn == True: #switches it to other players turn
            p1_turn = True
            p2_turn = False
        elif p1_turn == True:
            p1_turn = False
            p2_turn = True
    else:
        turnscore = turnscore + temp_num #adds a running total until player holds or rolls a 1
        score_t.clear() #writes the updated turn score for every roll
        score_t.write(f"Turn Total: {turnscore}", align = "center", font = ("Times New Roman", 20, "normal"))
        progress_bar()
        if p1_turn == True:
            if turnscore + p1_score >= 20:
                testscore = turnscore + p1_score
            print(f"score 1: {p1_score}")
            if full_bar(testscore) == True:
                win = True
        elif p2_turn == True:
            if turnscore + p2_score >= 20:
                testscore = turnscore + p2_score
            print(f"score 2: {p2_score}")
            if full_bar(testscore) == True:
                win = True

#Deals with the hold
def hold_score(x, y):
    global stillgoing
    global turnscore
    global p1_score
    global p2_score
    global p1_turn
    global p2_turn
    global player
    global win
    stillgoing = False #sets it to other players turn
    score_t.clear() #resets the running turn score
    score_t.write(f"Turn Total: 0", align = "center", font = ("Times New Roman", 20, "normal"))
    if p1_turn == True: #checks for who's turn 
        bar.teleport(-340, -182) #moves turtle to the players bar to fill in
        p1_score =  p1_score + turnscore #adds the turn score to players score
        if full_bar(p1_score) == True:
                win = True
        draw_bar()
    elif p2_turn == True: #checks for who's turn
        bar.teleport(-340, -212) #moves turtle to the players bar to fill in
        p2_score = p2_score + turnscore #adds the turn score to the players score
        draw_bar()
        if full_bar(p2_score) == True:
                win = True

#Function that checks for a win
def full_bar(score): #work in progress
    global player
    global turnscore
    global testscore
    global stillgoing
    global p1_turn
    global p2_turn
    global p1_score
    global p2_score
    global win
    win = False
    if p1_turn == True:
        if score >= 20:
            score = 20
            score = p1_score
            p_bar.clear()
            draw_bar()
            win = True
            r.hideturtle()
            h.hideturtle()
            p_bar.clear()
            bar.clear()
            die.hideturtle()
            turn.hideturtle()
            writer.clear()
            score_t.clear()
            replay.showturtle()
            wn.bgpic("game over.gif")
            replay.onclick(restart)
            writer.penup()
            writer.teleport(0, 100)
            writer.write(f"Player 1 Wins!", align = "center", font = ("Times New Roman", 20, "normal"))
            return True
    elif p2_turn ==  True:
        if score >= 20:
            score = 20
            score = p2_score
            p_bar.clear()
            draw_bar()
            win = True
            r.hideturtle()
            h.hideturtle()
            p_bar.clear()
            bar.clear()
            die.hideturtle()
            turn.hideturtle()
            writer.clear()
            score_t.clear()
            replay.showturtle()
            wn.bgpic("game over.gif")
            replay.onclick(restart)
            writer.penup()
            writer.teleport(0, 100)
            writer.write(f"Player 2 Wins!", align = "center", font = ("Times New Roman", 20, "normal"))
            return True
    else:
        if p1_turn == True:
            p1_turn = False
            p2_turn = True
        elif p2_turn == True:
            p1_turn = True
            p2_turn = False
        return False

#Function that restarts game
def restart(x, y):
    global play
    global score
    global p1_score
    global p2_score
    p1_score = 0
    p2_score = 0
    wn.bgpic("table.gif") #Switches the background
    pvp.hideturtle()
    pvc.hideturtle()
    r.showturtle()
    h.showturtle()
    turn.showturtle()
    die.showturtle()
    replay.hideturtle()
    writer.clear()
    play = 1 #sets the gamemode
    bar.teleport(-340, -212) #Draws the player bars
    for i in range(2):
        bar.pendown()
        bar.forward(200)
        bar.left(90)
        bar.forward(20)
        bar.left(90)
    bar.teleport(-340, -182)
    for i in range(2):
        bar.pendown()
        bar.forward(200)
        bar.left(90)
        bar.forward(20)
        bar.left(90)
    start()

#Function that starts game
def start():
    global play
    global win
    global player
    global p1_turn
    global p2_turn
    win = False
    player = random.randint(1,2) #sets it to a random player to start first
    if player == 1: #checks for who's turn
        p1_turn = True
        p2_turn = False
    elif player == 2:
        p1_turn = False
        p2_turn = True
    if play == 1:
        while win == False: #Keeps running until someone wins
            take_turn()
        replay.showturtle()
    elif play == 2: #THE WORKEST OF WORK IN PROGRESSES
        player = random.randint(1,2)
        while win == False:
            take_turn()

#------------------Main Code------------------#

#pvp button
pvp = trtl.Turtle()
pvp.shape(pvp_b)
pvp.penup()
pvp.teleport(-223, -63)
pvp.onclick(pvp_enable)

#pvc button
pvc = trtl.Turtle()
pvc.shape(pvc_b)
pvc.penup()
pvc.teleport(220, -63)
pvc.onclick(pvc_enable)

#roll button
r = trtl.Turtle()
r.shape(roll)
r.penup()
r.teleport(110, -202)
r.hideturtle()
r.onclick(take_turn)

#hold button
h = trtl.Turtle()
h.shape(hold)
h.penup()
h.teleport(332, -202)
h.hideturtle()
h.onclick(take_turn)

#restart button
replay = trtl.Turtle()
replay.shape(rstart)
replay.penup()
replay.teleport(-5, -160)
replay.hideturtle()
replay.onclick(restart)

wn.mainloop()