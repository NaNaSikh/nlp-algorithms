import sys
import pandas as pd
import seaborn as sns

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QMessageBox, QWidget,
    QVBoxLayout, QLabel, QLineEdit, QComboBox, QScrollArea,
    QPushButton, QStackedWidget
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from stemming import stemmingPoterAlgorithm, stemmingSnowballAlgorithm
from lemmatization import wordnet_lemmatization_function, spacy_lemmatization_function
from tokenization_algorithms import whitespaceTokenizationAlgorithm, punctuationTokenizationAlgorithm, NER_Algorithm
from testAlgorithmResultsLemmas import getLemmasPlots
from testAlgorithmsResults import  getStemmersPlots

class PlotCanvas(FigureCanvas):
    def __init__(self, df, df2, parent=None):
        self.fig, self.axs = plt.subplots(2, 2, figsize=(12, 8), dpi=100)
        super(PlotCanvas, self).__init__(self.fig)
        self.setParent(parent)
        self.plot(df ,  df2)

    def plot(self, df ,  df2):
        # Clear the axes
        for ax_row in self.axs:
            for ax in ax_row:
                ax.clear()

        # Plotting time taken by different lemmatization algorithms
        sns.barplot(x='Lemma', y='Time', data=df, ax=self.axs[0][0])
        self.axs[0][0].set_title('Time Taken by Different Lemmatization Algorithms')
        self.axs[0][0].set_ylabel('Time (seconds)')

        # Plotting number of unique lemmas
        sns.barplot(x='Lemma', y='Unique Lemmas', data=df, ax=self.axs[0][1])
        self.axs[0][1].set_title('Number of Unique Lemmas Produced by Different Lemmatization Algorithms')
        self.axs[0][1].set_ylabel('Unique Lemmas')

        # Optionally, plot more data in the other subplots as needed
        sns.barplot(x='Stemmer', y='Time', data=df2, ax=self.axs[1][0])
        self.axs[1][0].set_title('Time Taken by Different Stemmization Algorithms')
        self.axs[1][0].set_ylabel('Time (seconds)')

        sns.barplot(x='Stemmer', y='Unique Stems', data=df2, ax=self.axs[1][1])
        self.axs[1][1].set_title('Number of Unique Stemms  Produced by Different Stemmization  Algorithms')
        self.axs[1][1].set_ylabel('Unique Lemmas')

        # Redraw the canvas
        self.draw()




class MyWindow(QMainWindow):
    def __init__(self, df ,  df2):
        super().__init__()

        self.setWindowTitle('NLP Algorithms Visualizer')
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget
        central_widget = QWidget()
        self.layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Create a stacked widget
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)

        # Create different pages
        self.create_home_page()
        self.create_plot_page(df ,df2)
        self.create_model_page()

        # Create a menubar
        menubar = self.menuBar()

        # Create actions for the menu
        home_action = QAction('&Home', self)
        home_action.triggered.connect(self.show_home_page)
        plot_action = QAction('&Plot', self)
        plot_action.triggered.connect(self.show_plot_page)
        model_action = QAction('&Model' , self)
        model_action.triggered.connect(self.show_model_page)

        exit_action = QAction('&Exit', self)
        exit_action.triggered.connect(self.close)

        # Add actions to the menubar
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exit_action)

        view_menu = menubar.addMenu('&View')
        view_menu.addAction(home_action)
        view_menu.addAction(plot_action)
        view_menu.addAction(model_action)


    def create_model_page(self):
        home_widget = QWidget()
        home_layout = QVBoxLayout(home_widget)

        label = QLabel('Home Page', self)
        home_layout.addWidget(label)

        self.stacked_widget.addWidget(home_widget)
    def create_home_page(self):
        home_widget = QWidget()
        home_layout = QVBoxLayout(home_widget)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)  # Corrected from home_layout to scroll_layout
        scroll_area.setWidget(scroll_content)

        home_layout.addWidget(scroll_area)  # Add scroll_area to home_layout

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText('Enter some text')
        scroll_layout.addWidget(self.input_field)  # Corrected from home_layout to scroll_layout

        self.dropdown = QComboBox()
        self.dropdown.addItems(
            ["Potter Stemmer", "Stemming Snowball Algorithm", "Lemmatization WordNet", "Lemmatization Spacy"]
        )
        scroll_layout.addWidget(self.dropdown)  # Corrected from home_layout to scroll_layout

        self.dropdownTokens = QComboBox()
        self.dropdownTokens.addItems(["Whitespace Tokenization", "Punctuation Tokenization"])
        scroll_layout.addWidget(self.dropdownTokens)  # Corrected from home_layout to scroll_layout

        button = QPushButton('NER Algorithm', self)
        button.setToolTip('This is an example button')
        scroll_layout.addWidget(button)  # Corrected from home_layout to scroll_layout

        buttonCalc = QPushButton('Generate', self)
        buttonCalc.setToolTip('This is an example button')
        scroll_layout.addWidget(buttonCalc)  # Corrected from home_layout to scroll_layout

        self.stacked_widget.addWidget(home_widget)

    def create_plot_page(self, df ,  df2):
        plot_widget = QWidget()
        plot_layout = QVBoxLayout(plot_widget)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)  # Corrected from plot_layout to scroll_layout
        scroll_area.setWidget(scroll_content)

        plot_layout.addWidget(scroll_area)  # Add scroll_area to plot_layout

        # Example plot canvas
        self.plot_canvas = PlotCanvas(df, df2,  self)
        scroll_layout.addWidget(self.plot_canvas)  # Corrected from plot_layout to scroll_layout

        self.stacked_widget.addWidget(plot_widget)

    def show_home_page(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_plot_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_model_page(self):
        self.stacked_widget.setCurrentIndex(2)

    def choose_algorithm(self):
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

    @pyqtSlot()
    def check_ner(self):
        try:
            print('PyQt5 button click')
            text = self.input_field.text()
            entities = NER_Algorithm(text)
            ans = ""
            for ent in entities:
                ans += f'{ent.text} - {ent.label_}\n'
            self.result_label.setText(ans)
        except Exception as e:
            print(f'Error: {e}')
            self.result_label.setText('Error processing text')

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

def main(df , df2):
    app = QApplication(sys.argv)
    main_window = MyWindow(df , df2)
    main_window.show()
    sys.exit(app.exec_())


df = getLemmasPlots()
df2 = getStemmersPlots()

if __name__ == '__main__':
    main(df, df2)
