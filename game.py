import random
import math
import csv

### Local Game Archive
my_games = {}


def gamenumber():
  with open('history.csv','r',newline = '') as readhistory:
    rows = csv.reader(readhistory, delimiter = ',')
    for i, row in enumerate(rows):
      pass
    return i


class Options:
  lowernum = 1
  highernum = 100
  maxattempts = round(math.log((highernum - lowernum) +1,2))


### Main class to allows game objects to be created from.
class Guessthenumber(Options):
  gamenumber = gamenumber()
  
  ### Constructor for new game objects.
  def __init__(self):
    Guessthenumber.gamenumber += 1
    self.gamenumber = Guessthenumber.gamenumber
    self.lowernum = int(Options.lowernum)
    self.highernum = int(Options.highernum)
    self.maxattempts = int(Options.maxattempts)
    self.attempts = 0
    self.winstatus = False
    self.gameover = False
    self.gamestatus = "Start"
    self.ainumberstore = random.randint(self.lowernum, self.highernum)
    self.guesses = []

  ### Stores AI Number
  def ainumber(self):
    ai_number = int(self.ainumberstore)
    return ai_number

  ### Stores Player Number
  def playernumber(self, playernumber):
    user_number = int(playernumber)
    return(user_number)
                                                     
  ### Method Runs the main game logic.
  def maingame(self, playernumbermaingame):
    a = self.ainumber()
    b = self.playernumber(playernumbermaingame)
    if b == "":
      return False

    self.attempts += 1
    self.guesses.insert(0,b)

    if b == a:
      self.gamestatus = "Win"
      self.winstatus = True
      self.gameover = True
      return self.gamestatus
    elif b > a:
      self.gamestatus = "Too High"
      self.gameover = False
    elif b < a:
      self.gamestatus = "Too Low"
      self.gameover = False
    if self.attempts == self.maxattempts:
      self.gamestatus = "Max Attempts Reached"
      self.gameover = True
      return self.gamestatus
      
    return self.gameover

      
  def newgame():
    game = len(my_games)
    game +=1
    my_games[game] = my_games.get(game,Guessthenumber())
    return True
    #return my_games[game].maingame(playernumbernewgame)

  def totalwins():
    return str(sum(my_games[i].winstatus for i in my_games))

  def attemptsleft(self):
    attemptsrem = self.maxattempts - self.attempts
    return attemptsrem

  #a = Guessthenumber.newgame(rangehigh=10)