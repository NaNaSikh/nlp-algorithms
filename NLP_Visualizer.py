import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QWidget, QVBoxLayout, QLabel, QToolBar, QLineEdit
from stemming import stemmingPoterAlgorithm, stemmingSnowballAlgorithm
from lemmatization import lemmatiazation_function

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window title and size
        self.setWindowTitle("NLP")
        self.setGeometry(200, 100, 800, 600)
        self.setStyleSheet("background-color: #FFB36D;")

        self.font = QFont("Arial", 15)

        # Create a central widget and layout
        central_widget = QWidget()
        self.layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Create a toolbar
        toolbar = QToolBar()
        toolbar.setOrientation(Qt.Vertical)
        toolbar.setFont(self.font)
        self.addToolBar(Qt.LeftToolBarArea, toolbar)

        # Create a menubar
        menubar = self.menuBar()
        menubar.setFont(self.font)

        # Create actions for the menu and toolbar
        exitAction = QAction('&Exit', self)
        exitAction.setFont(self.font)
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        aboutAction = QAction('&About', self)
        aboutAction.setFont(self.font)
        aboutAction.setStatusTip('About this application')
        aboutAction.triggered.connect(self.about)

        stemmingActionPoter = QAction('&Stemming Poter', self)
        stemmingActionPoter.setFont(self.font)
        stemmingActionPoter.setStatusTip('Stemming algorithm')
        stemmingActionPoter.triggered.connect(self.getLabelDataPoter)

        stemmingActionSnowball = QAction('&Stemming Snowball', self)
        stemmingActionSnowball.setFont(self.font)
        stemmingActionSnowball.setStatusTip('Stemming algorithm')
        stemmingActionSnowball.triggered.connect(self.getLabelDataSnowball)

        lemmatizationAction = QAction('&Lemmatization', self)
        lemmatizationAction.setFont(self.font)
        lemmatizationAction.setStatusTip('Lemmatization algorithm')
        lemmatizationAction.triggered.connect(self.getLabelDataLem)

        # Add actions to the menubar
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(aboutAction)

        # Add actions to the toolbar
        toolbar.addAction(stemmingActionPoter)
        toolbar.addAction(stemmingActionSnowball)
        toolbar.addAction(lemmatizationAction)

        # Create the input field and add it to the layout
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText('Enter some text')
        self.layout.addWidget(self.input_field)
        self.input_field.setFont(self.font)


    def about(self):
        # Pop up a simple about message box
        aboutText = "This is a simple PyQt5 application."
        aboutTitle = "About"
        QMessageBox.about(self, aboutTitle, aboutText)

    def getLabelDataPoter(self):
        text = self.input_field.text()
        stemmed_words = stemmingPoterAlgorithm(text)
        stemmed_text = ",".join(stemmed_words)
        label = QLabel(stemmed_text)
        label.setFont(self.font)
        self.layout.addWidget(label)

    def getLabelDataSnowball(self):
        text = self.input_field.text()
        stemmed_words = stemmingSnowballAlgorithm(text)
        stemmed_text = ",".join(stemmed_words)
        label = QLabel(stemmed_text)
        label.setFont(self.font)
        self.layout.addWidget(label)

    def getLabelDataLem(self):
        text = self.input_field.text()
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
