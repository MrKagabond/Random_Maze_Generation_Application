# Random_Maze_Generation_Application
An application that randomly generates a maze

README

Installation
  A simple way of running this Application is to enter the code below into the command line… 

    git clone https://github.com/MrKagabond/Random_Maze_Generation_Application.git
    cd Random_Maze_Generation_Application/
    python -m src.Main

  Note: The above method using the command line assumes that A) you have Python configured/installed and B) you have PyGame configured/installed. To easily install PyGame, type         this into the command line…
    
    py -m pip install -U pygame -- <<ENTER USER HERE>>

  Alternatively, you can clone the repo directly from the Git Website and proceed to download and run the code that way. 
 
Product Use
  To run this application, run the Main.py file. You should then be prompted to enter the number of tiles you would like in the Terminal. Enter a valid number of tiles to receive  the next prompt, which will ask you whether you would like the computer to display the shortest solution of the maze.  Type and enter either ‘Y’ or ‘N’ to launch the maze generator.
  
  The maze generator is on the SAME thread as the rest of the program (due to time constraints). This means that during the maze creation, THE PROGRAM WILL BE UNABLE TO HANDLE NEW EVENTS. For this reason, the MAXIMUM number of tiles has been capped to 50. Remove this at your own discretion…

  To EXIT the application, either A) wait for the maze to FINISH generating or B) ALT + TAB and proceed to terminate the program. Once the maze is done, the program will accept/handle new events. Thus, simply CLICK on the window (to “enter focus”) and press the ‘ESC’ or ‘Q’ key. After that, the program should close. 

Known Issues
1) ALT + TABBING into and away from the program while it’s generating the maze often leads to the program freezing and inevitably crashing. As a general rule, it’s best to “leave the program be” while it’s generating a maze.
