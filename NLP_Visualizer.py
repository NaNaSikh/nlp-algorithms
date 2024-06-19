import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QWidget, QVBoxLayout, QLabel, QLineEdit, \
    QComboBox, QScrollArea
from stemming import stemmingPoterAlgorithm, stemmingSnowballAlgorithm
from lemmatization import wordnet_lemmatization_function , spacy_lemmatization_function
from tokenization_algorithms import  whitespaceTokenizationAlgorithm, punctuationTokenizationAlgorithm

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

        # toolbar = QToolBar()
        # toolbar.setOrientation(Qt.Vertical)
        # toolbar.setFont(self.font)
        # self.addToolBar(Qt.LeftToolBarArea, toolbar)

        # Create a central widget and layout
        # central_widget = QWidget()
        # self.layout = QVBoxLayout(central_widget)
        # self.setCentralWidget(central_widget)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Create a scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)

        layout.addWidget(self.scroll_area)


        self.dropdown = QComboBox()
        self.dropdown.addItems(["Potter Stemmer", "Stemming Snowball Algorithm", "Lemmatization WordNet", "Lemmatization Spacy"])
        self.dropdown.currentIndexChanged.connect(self.choose_algorithm)
        layout.addWidget(self.dropdown)

        self.dropdownTokens = QComboBox()
        self.dropdownTokens.addItems(
            ["Whitespace Tokenization", "Punctuation Tokenization"])
        self.dropdownTokens.currentIndexChanged.connect(self.choose_algorithm_tokens)
        layout.addWidget(self.dropdownTokens)

        # Create a menubar
        menubar = self.menuBar()
        menubar.setFont(self.font)

        # Create actions for the menu
        exitAction = QAction('&Exit', self)
        exitAction.setFont(self.font)
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        aboutAction = QAction('&About', self)
        aboutAction.setFont(self.font)
        aboutAction.setStatusTip('About this application')
        aboutAction.triggered.connect(self.about)

        # Add actions to the menubar
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(aboutAction)

        # Create the input field and add it to the layout
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText('Enter some text')
        layout.addWidget(self.input_field)
        self.input_field.setFont(self.font)

        # Label to display the result
        self.result_label = QLabel("Hi")
        self.result_label.setFont(self.font)
        self.scroll_layout.addWidget(self.result_label)

        # toolbar.addAction(stemmingActionPoter)
        # toolbar.addAction(stemmingActionSnowball)
        # toolbar.addAction(lemmatizationAction)

    tokenizedText = ""
    def choose_algorithm(self ):
        text = self.tokenizedText
        selected_algorithm = self.dropdown.currentText()

        if selected_algorithm == "Potter Stemmer":
            result = self.getLabelDataPoter(text)
        elif selected_algorithm == "Stemming Snowball Algorithm":
            result = self.getLabelDataSnowball(text)
        elif selected_algorithm == "Lemmatization WordNet":
            result = self.getLabelDataWordnet(text)
        elif selected_algorithm == "Lemmatization Spacy":
            result = self.getLabelDataSpacy(text)
        else:
            result = "Unknown algorithm"

        self.result_label.setText(result)

    def choose_algorithm_tokens(self):
        text = self.input_field.text()
        selected_algorithm = self.dropdownTokens.currentText()

        if selected_algorithm == "Whitespace Tokenization":
            result = whitespaceTokenizationAlgorithm(text)
        elif selected_algorithm == "Punctuation Tokenization":
            result = punctuationTokenizationAlgorithm(text)
        else:
            result = "Unknown algorithm"

        self.tokenizedText = ' '.join(result)
        print(self.tokenizedText)
        # self.result_label.setText(self.tokenizedText)

    def about(self):
        # Pop up a simple about message box
        aboutText = "This is a simple PyQt5 application."
        aboutTitle = "About"
        QMessageBox.about(self, aboutTitle, aboutText)

    def getLabelDataPoter(self, text):
        stemmed_words = stemmingPoterAlgorithm(text)
        stemmed_text = ", ".join(stemmed_words)
        return f"Potter Stemmer: {stemmed_text}"

    def getLabelDataSnowball(self, text):
        stemmed_words = stemmingSnowballAlgorithm(text)
        stemmed_text = ", ".join(stemmed_words)
        return f"Snowball Stemmer: {stemmed_text}"

    def getLabelDataWordnet(self, text):
        stemmed_words = wordnet_lemmatization_function(text)
        stemmed_text = ", ".join(stemmed_words)
        return f"WordNet: {stemmed_text}"

    def getLabelDataSpacy(self, text):
        stemmed_words = spacy_lemmatization_function(text)
        stemmed_text = ", ".join(stemmed_words)
        return f"SpiCy: {stemmed_text}"

if __name__ == '__main__':
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MyWindow()
    window.show()

    # Start the event loop
    sys.exit(app.exec_())
