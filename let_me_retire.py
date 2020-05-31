## ---------------------------------------------------------------------------------------
##        Name: Edweyza Rodriguez, Hyana Kang, Zephyr Wang
##    Filename: let_me_retire.py
##     Section: L04(Hyana), L01(Edweyza, Zephyr)
##        Date: 04/28/2019
##  References: See README.txt
## ---------------------------------------------------------------------------------------

import time, random, string
from tkinter import *
from tkinter import messagebox
import pygame


class Ending: # to show each ending considering user's past choices after calculating them
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def openEnding(self):
        self.result = self.first * self.second # calculate user's choice
        if self.result == 10: # with Jake
            playmusic("gunshot.wav")
            time.sleep(1)
            playmusic("ending1.wav")
            openfile("ending1.txt")
            print("\nENDING 1 : LIVE HAPPILY WITH JAKE FOREVER\n")
        elif self.result == 14: # with Ian
            playmusic("ending2.wav")
            openfile("ending2.txt")
            print("\nENDING 2 : MAKE A DEAL WITH IAN TO SAVE JAKE FROM HIM\n")
        elif self.result == 15: # divorce
            playmusic("gunshot.wav")
            time.sleep(1)
            playmusic("ending3.wav")
            openfile("ending3.txt")
            print("\nENDING 3 : KILL IAN BUT GET DIVORCED WITH JAKE\n")
        elif self.result == 21: # all die
            playmusic("gunshot.wav")
            time.sleep(0.5)
            playmusic("gunshot.wav")
            time.sleep(1)
            playmusic("ending4.wav")
            openfile("ending4.txt")
            print("\nENDING 4 : EVERYONE DIES EXCEPT YOU. YOU WILL BE ALONE FOREVER\n")


def openfile(filename): # function that opens the file with time break
    time.sleep(3)
    file = open(filename, "r+")
    print("-"*40, "Loading", "-"*40, "\n") # add it for user's convenience to read the file
    while True: # read each line in the file one-by-one
        reading = file.readline()
        reading = reading.replace("Y/N", username) # replace "Y/N" in the file to entered usrename
        print(reading)
        if not reading:
            break
        time.sleep(2.5) # add it for user's convenience to read the line with enough time 
    file.close()


def background(): # function that reads the background context of our story
    root = Tk() # tkinter main window
    root.withdraw() # kill the tkinter main window
    # messagebox uses tkinter modules that pops up the warning message
    messagebox.showwarning("WARNING", "***Genders/pronouns for this game are already decided***")
    time.sleep(1)
    print("\n"+"-"*40, "Loading", "-"*40)
    global username # so that openfile()can call the username
    username = input("\nWhat is your name?: ")
    time.sleep(2)
    # welcome messages
    print("\nHi", username + "!","Welcome to Let Me Retire: our first text-based RPG!")
    time.sleep(2)
    print("\nEvery decision you make will affect the ending of this game.\n")
    time.sleep(2)
    print("So please make careful decisions within the time limit. Enjoy!\n")
    openfile("background.txt")
    stopmusic("ring.wav", 2) # soundeffect
    openfile("start.txt")

    
def firstNode(): # first decision making moment
    time.sleep(2)
    print("{0}: {1} [{2}]".format("First Choice", "Do you want to tell the TRUTH or LIE to Jake?", "Time Limit: 10 secs"))                  
    max_time = 10 
    start_time = time.time() 
    time.sleep(2)
    playmusic("clock.wav") # soundeffect
    options = print("""
[A] Tell the truth that you were a secret agent who had killed a lot of people
[B] Hide the truth. Just pretend that it is the call from your ex""")
    option = input("\nYOUR CHOICE: ")
    pygame.mixer.music.stop() # stop soundeffect
    option = option.upper()
    if (time.time() - start_time) < max_time: # calculate the time for making the decision
        if option == "A":
            print("{0}. {1}".format("A","You choose to tell the truth to your husband"),"\n")
            playmusic("truth.wav")
            openfile("truth.txt")
            
        elif option == "B":
            print("{0}. {1}".format("B","You choose to lie to your husband"),"\n")
            playmusic("truth.wav")
            openfile("lie.txt")
            
        else: # if the input is neither A nor B
            print("Error! Please choose between A and B. The choice will be randomized.")
            ranoption = random.choice(["A", "B"]) # randomize the choice
            if ranoption == "A":
                print("{0}. {1}".format("A","You choose to tell the truth to your husband","\n"),"\n")
                playmusic("truth.wav")
                openfile("truth.txt")
                
            elif ranoption == "B":
                print("{0}. {1}".format("B","You choose to lie to your husband"),"\n")
                playmusic("truth.wav")
                openfile("lie.txt")              
            
    elif (time.time() - start_time) >= max_time: # if the user exceeds the time
        ranoption = random.choice(["A", "B"]) # randomize the choice
        print("\nYou exceed the time limit! The choice will be randomized.\n")
        if ranoption == "A":
            print("{0}. {1}".format("A","You choose to tell the truth to your husband","\n"),"\n")
            playmusic("truth.wav")     
            openfile("truth.txt")
            
        elif ranoption == "B":
            print("{0}. {1}".format("B","You choose to lie to your husband"),"\n")
            playmusic("truth.wav")
            openfile("lie.txt")
            

def secondNode(): # second decision making moment
    time.sleep(2)
    global firstcause
    # a variable that will be used as a reference to decide the ending.
    # We will give prime numbers to it so that we can have clear result for all decisions 
    openfile("callIan.txt")
    print("{0}: {1} [{2}]".format("Second Choice", "Do you want to HOLD a gun or HIDE the gun out?", "Time Limit: 10 secs"))                  
    max_time = 10
    time.sleep(2)
    start_time = time.time()
    playmusic("clock.wav")
    options = print("""
[A] Hold the gun in your right hand
[B] Hide the gun in your waist pack""")
    option = input("\nYOUR CHOICE: ")
    pygame.mixer.music.stop()
    option = option.upper()
    if (time.time() - start_time) < max_time:
        if option == "A":
            print("{0}. {1}".format("A","You choose to hold the gun in your hand"),"\n")
            playmusic("rain.wav")
            openfile("hold.txt")
            subsecond()
        elif option == "B":
            print("{0}. {1}".format("B","You choose to hide the gun because you don't want to upset Ian"),"\n")
            playmusic("rain.wav")
            openfile("hide.txt")
            playmusic("battle.wav")
            openfile("force.txt")
            firstcause = 3 # hide the gun is 3 because it is considered as the friendly action to Ian
        else:
            print("\nError! Please choose between A and B. The choice will be randomized.\n")
            ranoption = random.choice(["A", "B"])
            if ranoption == "A":
                print("{0}. {1}".format("A","You choose to hold the gun in your hand"),"\n")
                playmusic("rain.wav")
                openfile("hold.txt")
                subsecond()
            elif ranoption == "B":
                print("{0}. {1}".format("B","You choose to hide the gun because you don't want to upset Ian"),"\n")
                playmusic("rain.wav")
                openfile("hide.txt")
                playmusic("battle.wav")
                openfile("force.txt")
                firstcause = 3

    elif (time.time() - start_time) >= max_time:
        ranoption = random.choice(["A", "B"])
        print("\nYou exceed the time limit! The choice will be randomized.\n")
        if ranoption == "A":
            print("{0}. {1}".format("A","You choose to hold the gun in your hand"),"\n")
            playmusic("rain.wav")
            openfile("hold.txt")
            subsecond()
        elif ranoption == "B":
            print("{0}. {1}".format("B","You choose to hide the gun because you don't want to upset Ian"),"\n")
            playmusic("rain.wav")
            openfile("hide.txt")
            playmusic("battle.wav")
            openfile("force.txt")
            firstcause = 3

            
def subsecond(): # decision making moment but only happens when you chose to hold the gun before meeting Ian
    global firstcause
    time.sleep(2)
    print("{0}: {1} [{2}]".format("Third Choice", "Do you want to call JAKE and try to make up or call IAN and invite him to your house in order to settle things?", "Time Limit: 10 secs"))                  
    max_time = 10
    time.sleep(2)
    start_time = time.time()
    playmusic("clock.wav")
    options = print("""
[A] Call Jake.
[B] Call Ian""")
    option = input("\nYOUR CHOICE: ")
    pygame.mixer.music.stop()
    option = option.upper()
    if (time.time() - start_time) < max_time:
        if option == "A":
            firstcause = 2
            print("\n{0}. {1}".format("A","You choose to call Jake and tell him not to come back house for now."),"\n")
            playmusic("telephone.wav")
            openfile("jake.txt")
            playmusic("battle.wav")
            openfile("wait.txt")
        elif option == "B":
            firstcause = 3
            print("\n{0}. {1}".format("B","You choose to call Ian and attract him to your house to save Jake"),"\n")
            openfile("ian.txt")
            playmusic("battle.wav")
            openfile("wait.txt")
        else:
            print("\nError! Please choose between A and B. The choice will be randomized.\n")
            ranoption = random.choice(["A", "B"])
            if ranoption == "A":
                firstcause = 2
                print("{0}.{1}".format("A","You choose to call Jake and tell him not to come back house for now"),"\n")
                playmusic("telephone.wav")
                openfile("jake.txt")
                playmusic("battle.wav")
                openfile("wait.txt")
            elif ranoption == "B":
                firstcause = 3
                print("{0}.{1}".format("B","You choose to call Ian and attract him to your house to save Jake"),"\n")
                openfile("ian.txt")
                playmusic("battle.wav")
                openfile("wait.txt")
                
    elif (time.time() - start_time) >= max_time:
        ranoption = random.choice(["A", "B"])
        print("\nYou exceed the time limit! The choice will be randomized.\n")
        if ranoption == "A":
            firstcause = 2
            print("{0}.{1}".format("A","You choose to call Jake and tell him not to come back house for now"),"\n")
            playmusic("telephone.wav")
            openfile("jake.txt")
            playmusic("battle.wav")
            openfile("wait.txt")
        elif ranoption == "B":
            firstcause = 3
            print("{0}.{1}".format("B","You choose to call Ian and attract him to your house to save Jake"),"\n")
            openfile("ian.txt")
            playmusic("battle.wav")
            openfile("wait.txt")


def thirdNode():# last decision making moment
    global secondcause
    # another variable that will be used as a reference to decide the ending.
    # We will give prime numbers to it so that we can have clear result for all decisions 
    time.sleep(2)
    print("{0}: {1} [{2}]".format("Last Choice", "Do you want to PULL the trigger or try to TALK with him?", "Time Limit: 10 secs"))                  
    max_time = 10
    time.sleep(2)
    start_time = time.time()
    playmusic("clock.wav")
    options = print("""
[A] Pull the trigger and kill Ian so that you and Jake can be safe from his threat
[B] Try to talk with Ian. You are now a civilian. You will be a murderer if you kill Ian""")
    option = input("\nYOUR CHOICE: ")
    pygame.mixer.music.stop()
    option = option.upper()
    if (time.time() - start_time) < max_time:
        if option == "A" :
            secondcause = 5
            print("{0}.{1}".format("A","You choose to kill Ian"),"\n")
            ending = Ending(firstcause, secondcause) # call the class Ending
            ending.openEnding() # call the function within the class
        elif option == "B":
            secondcause = 7 
            print("{0}.{1}".format("B","You choose to try to talk with Ian"),"\n")
            ending = Ending(firstcause, secondcause)
            ending.openEnding()
        else:
            print("\nError! Please choose between A and B. The choice will be randomized.\n")
            ranoption = random.choice(["A", "B"])
            if ranoption == "A":
                secondcause = 5
                print("{0}.{1}".format("A","You choose to kill Ian"),"\n")
                ending = Ending(firstcause, secondcause)
                ending.openEnding()
            elif ranoption == "B":
                secondcause = 7
                print("{0}. {1}".format("B", "You choose to try to talk with Ian"),"\n")
                ending = Ending(firstcause, secondcause)
                ending.openEnding()
    elif (time.time() - start_time) >= max_time:
        ranoption = random.choice(["A", "B"])
        print("\nYou exceed the time limit! The choice will be randomized.\n")
        if ranoption == "A":
            secondcause = 5 
            print("{0}. {1}".format("A", "You choose to kill Ian"),"\n")
            ending = Ending(firstcause, secondcause)
            ending.openEnding()
        elif ranoption == "B":
            secondcause = 7
            print("{0}. {1}".format("B", "You choose to try to talk with Ian"),"\n")
            ending = Ending(firstcause, secondcause)
            ending.openEnding()


def feedback(): # function that stores the feedback
    file = open("feedback.txt", 'a') # append the input to the txt file
    time.sleep(3)
    print("-"*40, "Loading", "-"*40, "\n")
    time.sleep(2)
    comments = input("Did you enjoy our game? Please give us some feedbacks!: ")
    file.write(comments + "\n")
    file.close


def title(): # function that pops up the title of our game
    playmusic("title.wav")
    window = Tk()
    window.title("Final Project: Let Me Retire")
    window.geometry('672x900')
    canvas = Canvas(window, bg = 'red', height = 800, width = 800)
    image_file = PhotoImage(file = 'titlebg.png')
    image = canvas.create_image(340, 0, anchor = 'n', image = image_file)
    canvas.pack()
            
    def play():
        time.sleep(0.2)
        window.destroy() # close the title
        main()
    # play button
    button = Button(window, text = 'PLAY', font = ('Stencil', 40), fg = 'white', bg = 'black', width= 800, height = 30, command = play)
    button.pack()
    window.mainloop()

    
def playmusic(name): # function that plays music
    pygame.init()
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()

def stopmusic(name, timer): # function that plays music only for a certain amount of time
    pygame.init()
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()
    time.sleep(timer)
    pygame.mixer.music.stop()

def bye(): # function that ends the game
    time.sleep(2)
    print("\nThank you for playing our game!")
    print("\n"+"-"*90)

def main(): # main function that calls the other functions according to our game's storyline
    background()
    firstNode()
    secondNode()
    thirdNode()
    feedback()
    bye()

title() # start the game with the title
