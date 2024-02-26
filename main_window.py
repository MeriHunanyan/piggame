
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QProgressBar, QSpacerItem, QHBoxLayout, QVBoxLayout, QGridLayout

class PigGameWidget(QWidget):
    def __init__(self):
        super().__init__()

        label1 = QLabel("Your Score:")
        label2 = QLabel("Comp Score:")

        progress1 = QProgressBar()
        progress2 = QProgressBar()

        scoreLabel1 = QLabel("0")
        scoreLabel2 = QLabel("0")

        turnTotal = QLabel("Turn Total:")
        turnTotalScore = QLabel("0")

        rollButton = QPushButton("Roll")
        holdButton = QPushButton("Bank!")

        gridLayout = QGridLayout()
        gridLayout.addWidget(label1, 0, 0);
        gridLayout.addWidget(label2, 1, 0);

        gridLayout.addWidget(progress1, 0, 1);
        gridLayout.addWidget(progress2, 1, 1);

        gridLayout.addWidget(scoreLabel1, 0, 2);
        gridLayout.addWidget(scoreLabel2, 1, 2);
        gridLayout.setSpacing(10)

        btnLayout = QHBoxLayout()
        btnLayout.addWidget(turnTotal)
        btnLayout.addWidget(turnTotalScore)
        btnLayout.addItem(QSpacerItem(100, 10, QSizePolicy.Expanding, QSizePolicy.Fixed))
        btnLayout.addWidget(rollButton)
        btnLayout.addWidget(holdButton)
        btnLayout.setSpacing(10)

        vBox = QVBoxLayout()
        vBox.addItem(gridLayout)
        vBox.addItem(QSpacerItem(10, 250, QSizePolicy.Fixed, QSizePolicy.Expanding))
        vBox.addItem(btnLayout);

        self.setLayout(vBox)


class PigGameMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Piggy")

        self.setCentralWidget(PigGameWidget())

