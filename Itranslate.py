import speech_recognition as sr
from googletrans import Translator
import sys
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit
from PyQt5.QtCore import pyqtSignal, QObject

class SpeechRecognitionThread(QObject):
    textDetected = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.recognizer = sr.Recognizer()
        self.is_running = True
        self.translator = Translator()

    def run(self):
        """
        Continuously listens to microphone input, recognizes speech,
        translates it, and emits a signal with the original and translated text.
        """
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while self.is_running:
                try:
                    # Listen for audio input
                    audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=5)
                    
                    # Recognize speech using Google Speech Recognition
                    text = self.recognizer.recognize_google(audio)
                    
                    # Translate recognized text
                    translated = self.translator.translate(text)
                    
                    # Emit signal with original and translated text
                    self.textDetected.emit(f"Original ({self.translator.detect(text).lang}): {text}\nTranslated ({translated.dest}): {translated.text}")
                except sr.WaitTimeoutError:
                    pass
                except sr.UnknownValueError:
                    pass
                except Exception as e:
                    print(f"An error occurred: {e}")

    def stop(self):
        """Stop the speech recognition thread."""
        self.is_running = False

class VoiceTranslator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.speech_thread = SpeechRecognitionThread()
        self.thread = threading.Thread(target=self.speech_thread.run)
        self.speech_thread.textDetected.connect(self.updateText)

    def initUI(self):
        """Initialize the user interface."""
        self.setWindowTitle('Real-time Voice Translator')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.startButton = QPushButton('Start Translation', self)
        self.startButton.clicked.connect(self.toggleTranslation)
        layout.addWidget(self.startButton)

        self.textEdit = QTextEdit(self)
        self.textEdit.setPlaceholderText("Translated text will appear here...")
        layout.addWidget(self.textEdit)

        self.setLayout(layout)

        self.is_translating = False

    def toggleTranslation(self):
        """Toggle the start and stop of translation."""
        if not self.is_translating:
            self.startButton.setText('Stop Translation')
            self.is_translating = True
            self.thread.start()
        else:
            self.startButton.setText('Start Translation')
            self.is_translating = False
            self.speech_thread.stop()
            self.thread.join()
            self.thread = threading.Thread(target=self.speech_thread.run)
            self.speech_thread = SpeechRecognitionThread()
            self.speech_thread.textDetected.connect(self.updateText)

    def updateText(self, text):
        """Update the text in the QTextEdit widget."""
        self.textEdit.append(text)
        self.textEdit.append("------------------------")

    def closeEvent(self, event):
        """Stop the speech recognition thread on application close."""
        self.speech_thread.stop()
        if self.thread.is_alive():
            self.thread.join()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    translator = VoiceTranslator()
    translator.show()
    sys.exit(app.exec_())
