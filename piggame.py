import random
import time
from enum import Enum

from PyQt5.QtCore import QObject, pyqtSignal

class Player(Enum):
    PERSON = 0
    COMPUTER = 1

class PigGame(QObject):
    playerChangedSignal = pyqtSignal(Player)
    roundScoreChanged = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.playerScore = 0
        self.compScore = 0
        self.roundScore = 0
        self.setNowPlaying(Player.PERSON)

    def setNowPlaying(self, val):
        self.nowPlaying = val
        self.playerChangedSignal.emit(val)

    def roll(self):
        dicePoints = random.randint(1, 6)
        if dicePoints == 1:
            self.roundLost()
            return
        self.addRoundScore(dicePoints)
    
    def addRoundScore(self, val):
        self.roundScore += val
        self.roundScoreChanged.emit(self.roundScore)

    def roundLost(self):
        self.setNowPlaying(Player.COMPUTER)



