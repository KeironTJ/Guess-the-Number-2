import pygame
import button
import game
import math
import csv

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

#---------------------------------------------------------------------#
#Screen Size + Display Setup
SW = 600
SH = 400

screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption('Guess the Number 2')

# Font
HEADERFONT = pygame.font.SysFont('Arial', 24)
buttonfont = pygame.font.SysFont('Arial', 18)
buttonnumberfont = pygame.font.SysFont('Arial', 36)
INGAMEFONT = pygame.font.SysFont('Arial', 18)

# Function for displaying text
def draw_text (text, FONT, text_col,x,y):
    img = FONT.render(text, True, text_col)
    screen.blit(img,(x,y))


clock = pygame.time.Clock()


### Create button instances

## Main Menu Buttons
play_game_button = button.ButtonStd((0,205,255),235,75,130,50,"Play Game")
mainmenu_button1 = button.ButtonStd((0,205,255),235,150,130,50,"Game History")
mainmenu_button2 = button.ButtonStd((0,205,255),235,225,130,50,"Options")
quit_game_button = button.ButtonStd((0,205,255),235,300,130,50,"Quit Game")

## Play Game Buttons
one_button = button.ButtonStd((0,205,255),75,75,50,50,"1")
two_button = button.ButtonStd((0,205,255),135,75,50,50,"2")
three_button = button.ButtonStd((0,205,255),195,75,50,50,"3")

four_button = button.ButtonStd((0,205,255),75,135,50,50,"4")
five_button = button.ButtonStd((0,205,255),135,135,50,50,"5")
six_button = button.ButtonStd((0,205,255),195,135,50,50,"6")

seven_button = button.ButtonStd((0,205,255),75,195,50,50,"7")
eight_button = button.ButtonStd((0,205,255),135,195,50,50,"8")
nine_button = button.ButtonStd((0,205,255),195,195,50,50,"9")

backspace_button = button.ButtonStd((0,205,255),135,255,110,50,"BackSpace")
zero_button = button.ButtonStd((0,205,255),75,255,50,50,"0")

submit_button = button.ButtonStd((0,205,255),75,315,170,50,"Submit")

pg_back_button = button.ButtonStd((0,205,255),450,325,125,50,"End Game")

# Game History Buttons
gh_back_button = button.ButtonStd((0,205,255),450,325,125,50,"Back")
gh_resetall_button = button.ButtonStd((0,205,255),300,325,125,50,"Reset [All]")
gh_resetlast_button = button.ButtonStd((0,205,255),150,325,125,50,"Reset [Last]")

# Option Buttons
set_minr_button = button.ButtonStd((0,205,255),300,135,275,25,"Set Min Range: (Min: 0)")
set_maxr_button = button.ButtonStd((0,205,255),300,195,275,25,"Set Max Range: (Max: 99999)")
set_attempts_button = button.ButtonStd((0,205,255),300,255,275,25,"Set # of Attempts: ")
o_back_button = button.ButtonStd((0,205,255),450,325,125,50,"Main Menu")
default_button = button.ButtonStd((0,205,255),300,325,125,50,"Reset Values")

# Win Screen Buttons
ws_menu_button = button.ButtonStd((0,205,255),150,325,125,50,"Main Menu")
ws_options_button = button.ButtonStd((0,205,255),300,325,125,50,"Options")
ws_play_again_button = button.ButtonStd((0,205,255),450,325,125,50,"Play Again")


# Lose Screen Buttons
ls_menu_button = button.ButtonStd((0,205,255),150,325,125,50,"Main Menu")
ls_options_button = button.ButtonStd((0,205,255),300,325,125,50,"Options")
ls_play_again_button = button.ButtonStd((0,205,255),450,325,125,50,"Play Again")
#+--------------------------------------------------------------------#

### Game History Functions
def totalgames():
    with open('history.csv','r',newline = '') as readhistory:
        rows = list(csv.reader(readhistory, delimiter = ','))
        wins = sum([1 for row in rows[1:]])
        readhistory.close()
        return str(wins)

def totalwins():
    with open('history.csv','r',newline = '') as readhistory:
        rows = list(csv.reader(readhistory, delimiter = ','))
    wins = sum([1 for row in rows[1:] if row[1] == "True"])
    readhistory.close()
    return str(wins)

def totalattempts():
    with open('history.csv','r',newline = '') as readhistory:
        rows = list(csv.reader(readhistory, delimiter = ','))
    attempts = sum([int(row[2]) for row in rows[1:]])
    readhistory.close()
    return str(attempts)

def maxattempts():
    with open('history.csv','r',newline = '') as readhistory:
        rows = list(csv.reader(readhistory, delimiter = ','))
    attempts = sum([int(row[3]) for row in rows[1:]])
    readhistory.close()
    return str(attempts) 

def winrate():
    if int(totalgames()) == 0:
        return "0.00"
    else: 
        return str("%.2f"%( int(totalwins()) / int(totalgames())*100))

def deleteallentry():
    with open("history.csv","w", newline = "") as historyfile:
        writer = csv.writer(historyfile)
        writer.writerow(["Game Number"," Win Status"," Attempts"," Max Attempts"])

def deletelastentry():
    with open("history.csv","r+") as readhistoryfile:
        listrows = list(csv.reader(readhistoryfile))[0:-1]
    if len(listrows) < 1:
        pass
    else:
        with open("history.csv", "w+") as updatehistoryfile:
            writer = csv.writer(updatehistoryfile)
            writer.writerows(listrows)

#---------------------------------------------------------------------#
# outside Loop variables etc.  
playernumber = ""
storednumber = ""
MAINLOOP = True
gamemenu = "Main Menu"


#---------------------------------------------------------------------#
### Menu Functions: 


def keypad():
    global playernumber, storednumber
    
    if one_button.draw(screen, buttonnumberfont, True):
        playernumber += "1"
    if two_button.draw(screen, buttonnumberfont, True):
        playernumber += "2"
    if three_button.draw(screen, buttonnumberfont, True):
        playernumber += "3"
    if four_button.draw(screen, buttonnumberfont, True):
        playernumber += "4"
    if five_button.draw(screen, buttonnumberfont, True):
        playernumber += "5"
    if six_button.draw(screen, buttonnumberfont, True):
        playernumber += "6"
    if seven_button.draw(screen, buttonnumberfont, True):
        playernumber += "7"
    if eight_button.draw(screen, buttonnumberfont, True):
        playernumber += "8"
    if nine_button.draw(screen, buttonnumberfont, True):
        playernumber += "9"
    if zero_button.draw(screen, buttonnumberfont, True):
        playernumber += "0"
    if backspace_button.draw(screen, buttonfont, True):
        playernumber  = playernumber[:-1]
    #if submit_button.draw(screen, buttonnumberfont, True):
    #  storednumber = playernumber
    #  if storednumber == "":
    #    return False
    #  playernumber = ""
    #  return True
    return False

def mainmenu():
    global gamemenu, MAINLOOP, playernumber, storednumber
    
    draw_text("Main Menu",HEADERFONT,(0,0,0),235,25)
    playernumber = ""
    storednumber = ""
    if play_game_button.draw(screen,buttonfont,True):
        gamemenu = "New Game"
    if mainmenu_button1.draw(screen,buttonfont,True):
        gamemenu = "Game History"
    if mainmenu_button2.draw(screen,buttonfont,True):
        gamemenu = "Options"
    if quit_game_button.draw(screen,buttonfont, True):
        MAINLOOP = False 

def choosenumber():
    global gamemenu, MAINLOOP, playernumber, storednumber
  
    draw_text("Guess the number between "+str(game.Options.lowernum)+ " and "+str(game.Options.highernum),HEADERFONT,(0,0,0),50,25)
   
    if one_button.draw(screen, buttonnumberfont, True):
        playernumber += "1"
    if two_button.draw(screen, buttonnumberfont, True):
        playernumber += "2"
    if three_button.draw(screen, buttonnumberfont, True):
        playernumber += "3"
    if four_button.draw(screen, buttonnumberfont, True):
        playernumber += "4"
    if five_button.draw(screen, buttonnumberfont, True):
        playernumber += "5"
    if six_button.draw(screen, buttonnumberfont, True):
        playernumber += "6"
    if seven_button.draw(screen, buttonnumberfont, True):
        playernumber += "7"
    if eight_button.draw(screen, buttonnumberfont, True):
        playernumber += "8"
    if nine_button.draw(screen, buttonnumberfont, True):
        playernumber += "9"
    if zero_button.draw(screen, buttonnumberfont, True):
        playernumber += "0"
    if backspace_button.draw(screen, buttonfont, True):
        playernumber  = playernumber[:-1]
    if submit_button.draw(screen, buttonnumberfont, True):
        if playernumber == "":
            return False
        if int(playernumber) > game.Options.highernum or int(playernumber) < game.Options.lowernum:
            game.my_games[len(game.my_games)].gamestatus = "Out of Range. Try Again"
            storednumber = ""
            playernumber = ""
            return False
        else: storednumber = playernumber
        if storednumber == "":
            return False
        playernumber = ""
        return True

    draw_text("Your Number: ",INGAMEFONT,(0,0,0),300,75)
    draw_text(playernumber,INGAMEFONT,(0,0,255),300,105)
    
    draw_text("Result: ",INGAMEFONT,(0,0,0),300,135)
    draw_text(game.my_games[len(game.my_games)].gamestatus,INGAMEFONT,(0,0,255),300,165)
    draw_text("Attempts Remaining: ",INGAMEFONT,(0,0,0),300,195)
    draw_text(str(game.my_games[len(game.my_games)].attemptsleft()),INGAMEFONT,(0,0,255),300,225)
    draw_text("Last 3 guesses:",INGAMEFONT,(0,0,0),300,255)
    draw_text(', '.join(map(str,(game.my_games[len(game.my_games)].guesses[:3]))),INGAMEFONT,(0,0,255),300,285)
    
    if pg_back_button.draw(screen,buttonfont, True):
        playernumber = ""
        storednumber = ""
        game.my_games[len(game.my_games)].gameover = True
        with open("history.csv","a", newline = "") as historyfile:
          writer = csv.writer(historyfile)
          writer.writerow([game.Guessthenumber.gamenumber,game.my_games[len(game.my_games)].winstatus,game.my_games[len(game.my_games)].attempts,game.my_games[len(game.my_games)].maxattempts])
        gamemenu = "Lose Screen"
        
        return False

def gamehistory():
    global gamemenu
    global MAINLOOP
    
    draw_text("Game History",HEADERFONT,(0,0,0),200,25)
    
    draw_text("Total Games: "+str(totalgames()),INGAMEFONT,(0,0,0),200,75)
    draw_text("Total Wins: "+totalwins(),INGAMEFONT,(0,0,0),200,125)
    draw_text("Total Attempts: "+str(totalattempts()),INGAMEFONT,(0,0,0),200,175)
    draw_text("Possible Attempts: "+maxattempts(),INGAMEFONT,(0,0,0),200,225)
    draw_text("Win Rate: "+winrate()+"%",INGAMEFONT,(0,0,0),200,275)
    
    if gh_resetall_button.draw(screen,buttonfont,True):
        deleteallentry()
    if gh_resetlast_button.draw(screen,buttonfont,True):
        deletelastentry()
    
    
    if gh_back_button.draw(screen,buttonfont, True):
        gamemenu = "Main Menu"
    
def options():
  global gamemenu, MAINLOOP, playernumber, storednumber

  draw_text("Enter Value",INGAMEFONT,(0,0,0),300,75)
  draw_text(playernumber,INGAMEFONT,(0,0,255),300,105)
    
  if set_minr_button.draw(screen,buttonfont,True):
    if playernumber == "":
      return False
    if int(playernumber) >= int(game.Options.highernum):
      game.Options.lowernum = int(game.Options.highernum) - 1
    else: 
      game.Options.lowernum = int(playernumber)
    game.Options.maxattempts = round(math.log((game.Options.highernum - game.Options.lowernum) +1,2))
    playernumber = ""
    
  if set_maxr_button.draw(screen,buttonfont,True): 
    if playernumber == "":
      return False

    if int(playernumber) <= int(game.Options.lowernum):
      game.Options.highernum = int(game.Options.lowernum) + 1  
    elif int(playernumber) > 99999:
      game.Options.highernum = 99999
    else: 
      game.Options.highernum = int(playernumber)
    game.Options.maxattempts = round(math.log((game.Options.highernum - game.Options.lowernum) +1,2))
    playernumber = ""
  
  if set_attempts_button.draw(screen,buttonfont,True): 
    if playernumber == "":
      game.Options.maxattempts = round(math.log((game.Options.highernum - game.Options.lowernum) +1,2))
      return False
    if int(playernumber) > (game.Options.highernum - game.Options.lowernum):
      game.Options.maxattempts = game.Options.highernum - game.Options.lowernum
    else: game.Options.maxattempts = int(playernumber)
    playernumber = ""

  if default_button.draw(screen,buttonfont,True):
    game.Options.lowernum = 1
    game.Options.highernum = 100
    game.Options.maxattempts = round(math.log((game.Options.highernum - game.Options.lowernum) +1,2))

  draw_text(str(game.Options.lowernum),INGAMEFONT,(0,0,0),300,165)
  draw_text(str(game.Options.highernum),INGAMEFONT,(0,0,0),300,225)
  draw_text(str(game.Options.maxattempts),INGAMEFONT,(0,0,0),300,290)
  
  draw_text("Options",HEADERFONT,(0,0,0),235,25)
  
  if o_back_button.draw(screen,buttonfont, True):
    playernumber = ""
    storednumber = ""
    gamemenu = "Main Menu"  

def winscreen():
    global gamemenu
    global MAINLOOP
    
    draw_text("You Won!",HEADERFONT,(0,0,0),235,25)
    
    draw_text("The correct number was:",INGAMEFONT,(0,0,0),150,105)
    draw_text(str(game.my_games[len(game.my_games)].ainumber()),INGAMEFONT,(0,0,255),150,135)
    
    draw_text(str("You made "+ str(game.my_games[len(game.my_games)].attempts)+ " guesses." ),INGAMEFONT,(0,0,0),150,165)
    draw_text(str(game.my_games[len(game.my_games)].guesses[0:6])[1:-1],INGAMEFONT,(0,0,255),150,195)
    draw_text(str(game.my_games[len(game.my_games)].guesses[6:12])[1:-1],INGAMEFONT,(0,0,255),150,225)
    draw_text(str(game.my_games[len(game.my_games)].guesses[12:18])[1:-1],INGAMEFONT,(0,0,255),150,255)
    draw_text(str(game.my_games[len(game.my_games)].guesses[18:24])[1:-1],INGAMEFONT,(0,0,255),150,285)
    
    if ws_play_again_button.draw(screen,buttonfont, True):
        gamemenu = "New Game"
    if ws_menu_button.draw(screen,buttonfont, True):
        gamemenu = "Main Menu"
    if ws_options_button.draw(screen,buttonfont, True):
        gamemenu = "Options"

def losescreen():
    global gamemenu
    global MAINLOOP
    
    draw_text("You Lost!",HEADERFONT,(0,0,0),235,25)
    
    draw_text("The correct number was:",INGAMEFONT,(0,0,0),150,105)
    draw_text(str(game.my_games[len(game.my_games)].ainumber()),INGAMEFONT,(0,0,255),150,135)
    
    draw_text(str("You made "+ str(game.my_games[len(game.my_games)].attempts)+ " guesses." ),INGAMEFONT,(0,0,0),150,165)
    draw_text(str(game.my_games[len(game.my_games)].guesses[0:6])[1:-1],INGAMEFONT,(0,0,255),150,195)
    draw_text(str(game.my_games[len(game.my_games)].guesses[6:12])[1:-1],INGAMEFONT,(0,0,255),150,225)
    draw_text(str(game.my_games[len(game.my_games)].guesses[12:18])[1:-1],INGAMEFONT,(0,0,255),150,255)
    draw_text(str(game.my_games[len(game.my_games)].guesses[18:24])[1:-1],INGAMEFONT,(0,0,255),150,285)
    
    
    if ls_play_again_button.draw(screen,buttonfont, True):
        gamemenu = "New Game" 
    if ls_menu_button.draw(screen,buttonfont, True):
        gamemenu = "Main Menu"
    if ls_options_button.draw(screen,buttonfont, True):
        gamemenu = "Options"
    
#---------------------------------------------------------------------#

### Game Loop
while MAINLOOP:
  screen.fill((202, 228, 241))

  if gamemenu == "Main Menu":
    mainmenu()

  if gamemenu == "New Game":
    if game.Guessthenumber.newgame():
      gamemenu = "Choose Number"
  
  if gamemenu == "Choose Number":
    if choosenumber():
      game.my_games[len(game.my_games)].maingame(storednumber)
      if game.my_games[len(game.my_games)].gameover:
        with open("history.csv","a", newline = "") as historyfile:
          writer = csv.writer(historyfile)
          writer.writerow([game.Guessthenumber.gamenumber,game.my_games[len(game.my_games)].winstatus,game.my_games[len(game.my_games)].attempts,game.my_games[len(game.my_games)].maxattempts])
        if game.my_games[len(game.my_games)].gamestatus == "Win":
          gamemenu = "Win Screen"
        elif game.my_games[len(game.my_games)].gamestatus == "Max Attempts Reached":
          gamemenu = "Lose Screen"
        else: gamemenu = "Lose Screen"
      playernumber = ""
      storednumber = ""
      
  if gamemenu == "Game History":
    gamehistory()
  if gamemenu == "Options":
    options()
    keypad()
  if gamemenu == "Win Screen":
    winscreen()
  if gamemenu == "Lose Screen":
    losescreen()
  
  ### EVENT LIST and HANDLER
  eventlist =  pygame.event.get() 
  for event in eventlist:
  
    #quit game
    if event.type == pygame.QUIT:
        MAINLOOP = False
      
    ### Button Logic
    if gamemenu == "Main Menu":
        play_game_button.isclicked(event)
        mainmenu_button1.isclicked(event)
        mainmenu_button2.isclicked(event)
        quit_game_button.isclicked(event)

    if gamemenu == "Choose Number":
        pg_back_button.isclicked(event)
        one_button.isclicked(event)
        two_button.isclicked(event)
        three_button.isclicked(event)
        four_button.isclicked(event)
        five_button.isclicked(event)
        six_button.isclicked(event)
        seven_button.isclicked(event)
        eight_button.isclicked(event)
        nine_button.isclicked(event)
        zero_button.isclicked(event)
        submit_button.isclicked(event)
        backspace_button.isclicked(event)
      
    if gamemenu == "Game History":
        gh_back_button.isclicked(event)
        gh_resetall_button.isclicked(event)
        gh_resetlast_button.isclicked(event)
      
    if gamemenu == "Options":
        one_button.isclicked(event)
        two_button.isclicked(event)
        three_button.isclicked(event)
        four_button.isclicked(event)
        five_button.isclicked(event)
        six_button.isclicked(event)
        seven_button.isclicked(event)
        eight_button.isclicked(event)
        nine_button.isclicked(event)
        zero_button.isclicked(event)
        submit_button.isclicked(event)
        backspace_button.isclicked(event)
        o_back_button.isclicked(event)
        set_minr_button.isclicked(event)
        set_maxr_button.isclicked(event)
        set_attempts_button.isclicked(event)
        default_button.isclicked(event)
      
    if gamemenu == "Win Screen":
        ws_play_again_button.isclicked(event)
        ws_menu_button.isclicked(event)
        ws_options_button.isclicked(event)
      
    if gamemenu == "Lose Screen":
        ls_play_again_button.isclicked(event)
        ls_menu_button.isclicked(event)
        ls_options_button.isclicked(event)

  fpsClock.tick(fps)
  pygame.display.update()
#---------------------------------------------------------------------#
pygame.quit()
