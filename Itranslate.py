import speech_recognition as sr
from googletrans import Translator
import sys
import threading
import logging
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit
from PyQt5.QtCore import pyqtSignal, QObject

# Set up logging
logging.basicConfig(level=logging.DEBUG)

class SpeechRecognitionThread(QObject):
    textDetected = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.recognizer = sr.Recognizer()
        self.is_running = True
        self.translator = Translator()

    def run(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            logging.debug("Microphone calibrated.")
            while self.is_running:
                try:
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=3)
                    logging.debug("Audio captured.")
                    text = self.recognizer.recognize_google(audio)
                    logging.debug(f"Recognized text: {text}")

                    # Detect language and translate to English
                    detected_lang = self.translator.detect(text).lang
                    logging.debug(f"Detected language: {detected_lang}")
                    translated = self.translator.translate(text, dest='en')

                    # Emit the translation result
                    self.textDetected.emit(
                        f"Original ({detected_lang}): {text}\n"
                        f"Translated (English): {translated.text}"
                    )
                except sr.WaitTimeoutError:
                    logging.debug("Timeout error, no speech detected.")
                except sr.UnknownValueError:
                    logging.debug("Google Speech Recognition could not understand the audio.")
                except Exception as e:
                    logging.error(f"An error occurred: {e}")

    def stop(self):
        self.is_running = False

class VoiceTranslator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.speech_thread = None
        self.thread = None

    def initUI(self):
        self.setWindowTitle('Real-time Voice Translator')
        self.setGeometry(100, 100, 500, 400)

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
        if not self.is_translating:
            self.startButton.setText('Stop Translation')
            self.is_translating = True
            self.speech_thread = SpeechRecognitionThread()
            self.speech_thread.textDetected.connect(self.updateText)
            self.thread = threading.Thread(target=self.speech_thread.run)
            self.thread.start()
        else:
            self.startButton.setText('Start Translation')
            self.is_translating = False
            if self.speech_thread:
                self.speech_thread.stop()
            if self.thread and self.thread.is_alive():
                self.thread.join()
            self.thread = None
            self.speech_thread = None

    def updateText(self, text):
        self.textEdit.append(text)
        self.textEdit.append("------------------------")

    def closeEvent(self, event):
        if self.speech_thread:
            self.speech_thread.stop()
        if self.thread and self.thread.is_alive():
            self.thread.join()
        event.accept()

# Test components separately
def test_speech_recognition():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        logging.info("Say something...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
        try:
            text = recognizer.recognize_google(audio)
            logging.info(f"You said: {text}")
        except sr.UnknownValueError:
            logging.error("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            logging.error(f"Could not request results; {e}")

def test_translation():
    translator = Translator()
    text = "Hello, how are you?"
    translated = translator.translate(text, dest='en')
    logging.info(f"Original: {text}")
    logging.info(f"Translated: {translated.text}")

if __name__ == '__main__':
    # Optionally test components
    # test_speech_recognition()
    # test_translation()
    
    app = QApplication(sys.argv)
    translator = VoiceTranslator()
    translator.show()
    sys.exit(app.exec_())
