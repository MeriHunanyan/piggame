
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QProgressBar, QSpacerItem, QHBoxLayout, QVBoxLayout, QGridLayout

import piggame
import playerindicator


class PigGameWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.indicatorPlayer = playerindicator.PlayerIndicator()
        self.indicatorComputer = playerindicator.PlayerIndicator()

        label1 = QLabel("Your Score:")
        label2 = QLabel("Comp Score:")

        progress1 = QProgressBar()
        progress2 = QProgressBar()

        scoreLabel1 = QLabel("0")
        scoreLabel2 = QLabel("0")

        turnTotal = QLabel("Turn Total:")
        self.turnTotalScore = QLabel("0")

        self.rollButton = QPushButton("Roll")
        self.holdButton = QPushButton("Bank!")
        restartButton = QPushButton("Restart")

        gridLayout = QGridLayout()
        gridLayout.addWidget(self.indicatorPlayer, 0, 0);
        gridLayout.addWidget(self.indicatorComputer, 1, 0);

        gridLayout.addWidget(label1, 0, 1);
        gridLayout.addWidget(label2, 1, 1);

        gridLayout.addWidget(progress1, 0, 2);
        gridLayout.addWidget(progress2, 1, 2);

        gridLayout.addWidget(scoreLabel1, 0, 3);
        gridLayout.addWidget(scoreLabel2, 1, 3);
        gridLayout.setSpacing(10)

        btnLayout = QHBoxLayout()
        btnLayout.addWidget(turnTotal)
        btnLayout.addWidget(self.turnTotalScore)
        btnLayout.addItem(QSpacerItem(100, 10, QSizePolicy.Expanding, QSizePolicy.Fixed))
        btnLayout.addWidget(restartButton)
        btnLayout.addItem(QSpacerItem(50, 10, QSizePolicy.Fixed, QSizePolicy.Fixed))
        btnLayout.addWidget(self.rollButton)
        btnLayout.addWidget(self.holdButton)
        btnLayout.setSpacing(10)

        vBox = QVBoxLayout()
        vBox.addItem(gridLayout)
        vBox.addItem(QSpacerItem(10, 250, QSizePolicy.Fixed, QSizePolicy.Expanding))
        vBox.addItem(btnLayout);

        self.setLayout(vBox)

        # Connections
        self.rollButton.clicked.connect(self.onRollPressed)
        self.holdButton.clicked.connect(self.onHoldPressed)
        restartButton.clicked.connect(self.onRestartPressed)

        self.game = piggame.PigGame()
        self.game.roundScoreChanged.connect(self.onRoundScoreChanged)
        self.game.playerChangedSignal.connect(self.onPlayerChanged)

        self.onPlayerChanged(self.game.nowPlaying)

    def onRollPressed(self):
        self.game.roll()

    def onHoldPressed(self):
        pass

    def onRestartPressed(self):
        pass

    def onRoundScoreChanged(self, newScore):
        self.turnTotalScore.setText(str(newScore))

    def onPlayerChanged(self, val):
        if val == piggame.Player.COMPUTER:
            self.rollButton.setDisabled(True)
            self.holdButton.setDisabled(True)
            self.indicatorComputer.setState(1)
            self.indicatorPlayer.setState(0)
        else:
            self.indicatorComputer.setState(0)
            self.indicatorPlayer.setState(1)


class PigGameMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Piggy")

        self.setCentralWidget(PigGameWidget())

