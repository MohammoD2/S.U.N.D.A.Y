import os
import sys
import random
import time
import threading
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QMovie, QPalette
from PyQt6.QtCore import Qt

# Update the system path to include the "FUNCTION" directory
sys.path.append(os.path.abspath(os.path.dirname("FUNCTION")))

# Import necessary modules
from FUNCTION.Zaki_listan.listan import listen
from FUNCTION.zaki_speak.speak import speak
from BRAIN.brain import brain_cmd
from AUTOMATION.INTEGRATION_ANIMATION.integretion_animation import Automation
from FUNCTION.INTEGRETION_FUNCTION.integration_funtion import Function_cmd
from DATA.zaki_dlg_dataset.DLG import *

class SundayAI(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set window properties
        self.setWindowTitle("Sunday AI")
        self.setFixedSize(1000, 550)
        # Set black background
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.black)
        self.setPalette(palette)
        # Set up layout
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        # Create initial GIF (hello.gif)
        self._createGIF("E:/Work files/Ai/Z.A.K.I/Desktop_app/hello.gif")

    def _createGIF(self, gif_name):
        """Function to load and display a GIF."""
        self.gifLabel = QLabel(self)
        self.movie = QMovie(gif_name)
        self.gifLabel.setMovie(self.movie)
        # Align GIF to center and add to the layout
        self.gifLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.generalLayout.addWidget(self.gifLabel)
        self.movie.start()  # Start the GIF initially
        self.movie.finished.connect(self.handleGIFEnd)

    def handleGIFEnd(self):
        """Handle the end of each GIF animation."""
        if self.movie.fileName() == "E:/Work files/Ai/Z.A.K.I/Desktop_app/hello.gif":
            self._createGIF("E:/Work files/Ai/Z.A.K.I/Desktop_app/hello3.gif")
        elif self.movie.fileName() == "E:/Work files/Ai/Z.A.K.I/Desktop_app/hello3.gif":
            self._createGIF("E:/Work files/Ai/Z.A.K.I/Desktop_app/hello4.gif")
            self.startListening()

    def startListening(self):
        """Start the command listening in a separate thread."""
        threading.Thread(target=self.listenForCommands).start()

    def listenForCommands(self):
        """Function to listen for voice commands."""
        while True:
            text = listen().lower()
            Automation(text)
            Function_cmd(text)
            if text in bye_key_word:
                x = random.choice(res_bye)
                speak(x)
                break
            elif "sunday" in text:
                response = brain_cmd(text)
                speak(response)
            self.movie.stop()  # Pause GIF when detecting input
            time.sleep(0.5)
            self.movie.start()  # Resume GIF when input stops

def comain():
    """Main command handling function after wake word is detected."""
    while True:
        text = listen().lower()
        Automation(text)
        Function_cmd(text)
        if text in bye_key_word:
            x = random.choice(res_bye)
            speak(x)
            break
        elif "sunday" in text:
            response = brain_cmd(text)
            speak(response)
        time.sleep(0.5)

def main():
    """Main loop to listen for the wake word and handle the wake-up sequence."""
    while True:
        wake_cmd = listen().lower()
        if wake_cmd in wake_key_word:
            window.handleGIFEnd()
            welcomedlg1 = random.choice(welcomedlg)
            speak(welcomedlg1)
            comain()
        time.sleep(0.5)

def startSunday():
    """Function to run the application and start the AI."""
    app = QApplication([])
    global window
    window = SundayAI()
    window.show()
    threading.Thread(target=main).start()
    sys.exit(app.exec())

if __name__ == "__main__":
    startSunday()
