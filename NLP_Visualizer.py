import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QWidget, QVBoxLayout, QLabel, QToolBar
from stemming import stemmingPoterAlgorithm , stemmingSnowballAlgorithm
from lemmatization import lemmatiazation_function


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Set window title and size
        self.setWindowTitle("NPL")
        self.setGeometry(100, 100, 300, 200)
        self.setStyleSheet("background-color: #FFB36D;")

        self.font = QFont("Arial", 15 )
        # Create a vertical layout
        self.layout = QVBoxLayout()

        # Set the layout for the main window
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        toolbar = QToolBar()
        toolbar.setOrientation(Qt.Vertical)
        toolbar.setFont(self.font)

        menubar = self.menuBar()
        menubar.setFont(self.font)


        # # Create actions for the menu
        exitAction = QAction('&Exit', self)
        exitAction.setFont(self.font)
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        aboutAction = QAction('&About', self)
        aboutAction.setStatusTip('About this application')
        aboutAction.triggered.connect(self.about)

        stemmingActionPoter = QAction('&Stemming Poter', self)
        stemmingActionPoter.setStatusTip('Stemming algorithm')
        stemmingActionPoter.triggered.connect(self.getLabelDataPoter)

        stemmingActionSnowball = QAction('&Stemming Snowball', self)
        stemmingActionSnowball.setStatusTip('Stemming algorithm')
        stemmingActionSnowball.triggered.connect(self.getLabelDataSnowball)

        lemmatizationAction = QAction('&Lemmatization', self)
        lemmatizationAction.setStatusTip('Lemmatization algorithm')
        lemmatizationAction.triggered.connect(self.getLabelDataLem)



        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(aboutAction)


        toolbar.addAction(stemmingActionPoter)
        toolbar.addAction(stemmingActionSnowball)
        toolbar.addAction(lemmatizationAction)

        self.addToolBar(Qt.LeftToolBarArea, toolbar)



    def about(self):
        # Pop up a simple about message box
        aboutText = "This is a simple PyQt5 application."
        aboutTitle = "About"
        QMessageBox.about(self, aboutTitle, aboutText)
    def getLabelDataPoter(self):

        stemmed_words = stemmingPoterAlgorithm()
        stemmed_text = ",".join(stemmed_words)
        label = QLabel(stemmed_text)
        label.setFont(self.font)
        self.layout.addWidget(label)

    def getLabelDataSnowball(self):
        stemmed_words = stemmingSnowballAlgorithm()
        stemmed_text = ",".join(stemmed_words)
        label = QLabel(stemmed_text)
        label.setFont(self.font)
        self.layout.addWidget(label)

    def getLabelDataLem(self):
        stemmed_words = lemmatiazation_function()
        stemmed_text = "".join(stemmed_words)
        label = QLabel(stemmed_text)
        label.setFont(self.font)
        self.layout.addWidget(label)




if __name__ == '__main__':
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MyWindow()
    window.show()

    # Start the event loop
    sys.exit(app.exec_())
