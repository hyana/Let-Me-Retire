## ---------------------------------------------------------------------------------------
##        Name: Edweyza Rodriguez, Hyana Kang, Zephyr Wang
##    Filename: let_me_retire.py
##      Section: L04(Hyana), L01(Edweyza, Zephyr)
##          Date: 04/28/2019
##  References: See the last part of this file
## ---------------------------------------------------------------------------------------


## Files needed
1. One main py file: let_me_retire.py
2. Sixteen txt files : background.txt, start.txt, truth.txt, lie.txt, hide.txt, callIan.txt, hold.txt, jake.txt, ian.txt, wait.txt, force.txt, ending1.txt, ending2.txt, ending3.txt, ending4.txt, feedback.txt
3. Thirteen wav files: title.wav, background.wav, ring.wav, clock.wav, rain.wav, telephone.wav, truth.wav, battle.wav, gunshot.wav, ending1.wav, ending2.wav, ending3.wav, ending4.wav
4. One png file: titlebg.png


## Explanation of how to run our project
1. Extract the let_me_retire.zip file
2. Install pygame module to your python using pip and the terminal
   - Users of Window 10 and Python 3: go to cmd -> enter ‘pip install pygame’
   For more information about pip and pygame module:  
   (pip: https://phoenixnap.com/kb/install-pip-windows, https://docs.python.org/ko/3.6/installing/index.html#installing-index)
   (pygame: https://www.pygame.org/wiki/GettingStarted)
   - Users of Mac (with the most recent ios) and Python3: 
   install Homebrew: enter /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" -> pip3 install pygame
3. Go to the let_me_retire.py file and run it
4. Click the PLAY button under the title image
5. Press OK when the warning message pops up
6. Enter your name when it asks you to do so
7. Choose one of the options using “a/A” and  “b/B” letters on the keyboard within the time limit when it asks you to do so. If you exceed the time limit or choose the wrong option(e.g. “T” or “1”), your choice will be randomized
8. Enter some feedbacks for our game


## Description of the project, including the primary objective/purpose and intended audience.
Our project is a text-based RPG with multi-options and multi-endings. Users can choose either A and B when there is a decision to make. 
But for the ending, it cannot be chosen by the user, but it will be decided by the user’s past choices. 
We also add the title window, background music, sound effects, warning pop-up message, and time limit to choose options to add suspense in our game. 
For the player’s convenience, we make the script be printed line-by-line with some breaks.
In our story, the protagonist is a secret agent who retired a year ago and now is living a married happy life. 
However, the protagonist receives a threatening voicemail from an old secret agent enemy, Ian. 
The protagonist had an unrequited love with Ian. Now Ian is trying to ruin the protagonist happy married life and convince the protagonist to become an agent again. 
Throughout the game, the protagonist fights against Ian in order to keep Jake, the protagonist's husband, safe. 
The game has four endings. In the first ending, the protagonist kills Ian secretly and Jake never finds out so Jake and the protagonist have a happy ending. 
In the second ending Jake witnesses the protagonist killing Ian. Therefore, Jake becomes afraid of the protagonist and their relationship ends. 
In the third ending, the protagonist manages to convince Ian to not kill Jake by going on a date with Ian. 
Lastly, in the fourth ending, Ian kills Jake so the protagonist kills Ian as revenge.
A hypothetical person who will play our game would be a person who is lonely and bored with their own lives and seek a better life through virtual reality. 
This person would use technology a lot and enjoys playing video games. This person is probably in their teens or early 20s. 
This person might be motivated to use our role play game in order to escape reality and have fun or because they enjoy reading stories.


## Architecture of our code
We imported time, random, tkinter and pygame. 
Time was used in order to give time break between each line for better readability and give time limit when the user chooses the option
We used random to randomize the decision picked if the user exceeded the time limit. 
Tkinter was used in order to get the title image. 
Pygame was used in order to play the music while the program is running. 

We used one class and several def functions:
1. openfile() function which contains the methods that open the files with time break. It us
2. background() function which shows the background context of our story with sound effects 
3. firstNode() function which contains code for 1st decision making 
4. secondNode() function which contains code for 2nd decision making. It also contains a global variable called firstcause that would be used to decide the ending
5. subsecond() function decision-making function but only shows up depending on your previous decisions. Also has the global variable firstcause
6. thirdNode() function includes the last decision-making moment which contains another global variable called secondcause which is used to determine the ending
7. Ending class determines the user’s ending after multiplying firstcause and secondcause, the user’s past choices, and shows the ending. 
    This is why we give prime numbers for firstcause and secondcause have clear different endings for all decisions that the user made and make them as global variables 
    so that we can call class Ending referring them
8. title() function which shows the title image using tkinter module and calls the main function
9. playmusic() which plays music using pygame module
10. stopmusic() function which plays music for a certain amount of time
11. bye() function which ends the game with thank you message 
12. feedback() function which appends the user’s feedback to the txt file 
13. main() function which calls the other functions according to our game’s storyline 

All functions related to decision making moments have several if-elif-else statements. 
One of the if-elif-else statements is for detecting whether the user exceeds the time or not, and the other ones in the if-elif statements are to detect the option that is inputted by the user.

For more specific information, please refer to the inline comments in the let_me_retire.py file.


## One Major Challenge:
One major challenge that we faced was to play music at the same time while other functions are working. 
After looking up the python webpage, we tried several kinds of modules like playsound, winsound, web browser to play music. 
However, these did not work because they include the music as part of the coding. 
Therefore, the program would wait until the music ends. Then we tried os.system but it asked for the terminal to open the file and close it. 
It popped up a new window and it took time to let the music play. 
At last, we imported the module called pygame which contains functions that can control music, keyboard, and mouse. 
And it works well; it enables us to play the music and run the program at the same time. Also, we can stop the music whenever we want. 
Since we didn’t learn any of these modules except webbrowser before, we took a long time to figure them out and try. 
Besides, we tried pygame at last and we realized that we could have used pygame to further visualize our game. 
However, we didn’t have enough time to accomplish that. 


## References for soundeffects and and the script
<Background musics and soundeffects>
Soundbible http://soundbible.com/suggest.php?q=noise&x=0&y=0 
Detective Spy Music (Copyright Free) Detective Theme Music - Background Music.  https://www.youtube.com/watch?v=RHeSXODgWWQ 
Fesliyan Studios - Royalty Free Music And Sound Effects https://www.fesliyanstudios.com/royalty-free-music  
Mr. Vs Mrs. Smith(2005) - Encounter Of Two Agents AKA Wife Vs Husband https://www.youtube.com/watch?v=6oGW8K1dYzc
Married life by Michael Giacchino https://www.youtube.com/watch?v=LaLegF2hAxI
Shutterstock https://www.shutterstock.com/music/?language=zh

<Script>
Battle scene: http://www.awesomefilm.com/script/mr_and_mrs_smith.pdf (page 79)
