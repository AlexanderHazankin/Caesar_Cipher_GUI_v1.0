import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout

import alphabet_list


def caesar(text, shift, alphabet):
    alphabets = {
        "English": alphabet_list.english_alphabet,
        "Russian": alphabet_list.russian_alphabet,
        "Hebrew": alphabet_list.hebrew_alphabet,
        "Arabic": alphabet_list.arabic_alphabet,
        "Greek": alphabet_list.greek_alphabet,
        "English alphabet in bits": alphabet_list.english_alphabet_bits,
        "International alphabet morse code": alphabet_list.international_alphabet_morse

    }
    alphabet = alphabets.get(alphabet, "Invalid alphabet")

    cipher_text = ""
    for char in text:
        if char in alphabet:

            # Shift the index of the character
            index_shift = (alphabet.index(char) + shift) % len(alphabet)
            cipher_char = alphabet[index_shift]

        # Add the character to the encoded text if it is not in the alphabet
        else:
            cipher_char = char

        # Append the encoded character to the encoded_text string
        cipher_text += cipher_char
    return cipher_text


def encode(text, shift, alphabet):

    # Encodes the given text using a Caesar cipher with the given shift.
    return caesar(text, shift, alphabet)


def decode(text, shift, alphabet):

    # Decodes the given text using a Caesar cipher with the given shift.
    return caesar(text, -shift, alphabet)


class CaesarCipherGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Define the alphabet
        self.alphabet = "English", "Russian", "Hebrew", "Arabic", "Greek", "English alphabet in bits",\
                        "International alphabet morse code"
        self.setMinimumSize(400, 300)

        # Create a label and line edit for the text
        self.text_label = QLabel('Text:')
        self.text_edit = QLineEdit()

        # Create a combo box for the direction
        self.direction_label = QLabel('Direction:')
        self.direction_combo = QComboBox()
        self.direction_combo.addItems(['encode', 'decode'])

        # Create a label and line edit for the shift
        self.shift_label = QLabel('Shift:')
        self.shift_edit = QLineEdit()

        # Create a label and line edit for the alphabet
        self.alphabet_label = QLabel('Alphabet:')
        self.alphabet_combo = QComboBox()
        self.alphabet_combo.addItems(['English', 'Russian', 'Hebrew', 'Arabic', 'Greek', 'English alphabet in bits',
                                      'International alphabet morse code'])
        self.alphabet_edit = QLineEdit()

        # Create a push button to run the encryption/decryption
        self.encrypt_button = QPushButton('Encrypt/Decrypt')
        self.encrypt_button.clicked.connect(self.encrypt_decrypt)

        # Create a label and line edit for the result
        self.result_label = QLabel('Result:')
        self.result_edit = QLineEdit()

        # Create a vertical layout to hold the widgets
        layout = QVBoxLayout()

        # Add the widgets to the layout
        layout.addWidget(self.text_label)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.direction_label)
        layout.addWidget(self.direction_combo)
        layout.addWidget(self.shift_label)
        layout.addWidget(self.shift_edit)
        layout.addWidget(self.alphabet_label)
        layout.addWidget(self.alphabet_combo)
        layout.addWidget(self.encrypt_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_edit)

        # Set the layout of the widget
        self.setLayout(layout)
        self.text_edit.clear()

    @pyqtSlot()
    def encrypt_decrypt(self):

        # Get the text from the text_edit field
        text = self.text_edit.text().lower()

        # Get the shift from the shift_edit field
        shift_text = self.shift_edit.text()

        # Get the alphabet from the alphabet_edit field
        alphabet = self.alphabet_combo.currentText()

        # Check if the shift is a valid integer
        if shift_text.isdigit():

            # Convert the shift to an integer
            shift = int(self.shift_edit.text())

            # Get the direction from the direction_combo field
            direction = self.direction_combo.currentText()

            # Initialize the result variable
            result = ""
            try:

                # Call the appropriate function based on the direction
                if direction == "encode":
                    result = encode(text, shift, alphabet)
                elif direction == "decode":
                    result = decode(text, shift, alphabet)
            except ValueError:

                # Display an error message if the alphabet is invalid
                result = "Error: Invalid alphabet"

            # Display the result in the result_edit field
            self.result_edit.setText(result)
        else:

            # Display an error message if the shift is not a valid integer
            self.result_edit.setText("Error: Shift must be a valid digit")

        self.shift_edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = CaesarCipherGUI()
    gui.show()
    sys.exit(app.exec_())
