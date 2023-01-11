# Caesar Cipher GUI v1.0
This is a PyQt5-based GUI application that allows users to encode or decode text using the Caesar cipher.
This is a simple implementation of the Caesar Cipher in PyQt5.
The program includes a variety of alphabets to choose from, including
English, Russian, Hebrew, Arabic, Greek, English alphabet in bits, and international alphabet morse code.
This is a GUI program that allows a user to encode or decode a message using the Caesar Cipher

## Usage
To run the program, use the following command:

python caesar_cipher_gui.py

Then, enter the text to be encoded or decoded,
select the direction (encode or decode),
enter the shift value, and select the alphabet from the dropdown menu.
Click the "Encrypt/Decrypt" button to see the result.

## Requirements
Requires Python 3.x to run.

PyQt5

## Credits
The code created by Alexander Hazankin.

The GUI Pytq5 implementation and modifications to the original code were done by ChatGPT.

## Contact
For any questions or comments, you can reach me at:

https://www.linkedin.com/in/hazankin

https://github.com/AlexanderHazankin

https://replit.com/@Hazankin

## License
This project is licensed under the [MIT License](LICENSE).

Copyright (c) 2022 Alexander Hazankin.


## NOTE:
This is a simple implementation of the Caesar Cipher in PyQt5, a Python library for creating graphical user interfaces (GUIs).
The Caesar Cipher is a simple method of encryption that involves shifting the letters of a message by a certain number of positions in the alphabet.

The CaesarCipherGUI class is a subclass of QWidget and represents the main window of the application.
It contains a number of widgets such as labels, line edits, and a combo box for the user to input text,
choose the direction (encode or decode), specify the shift value, and select the alphabet.
There is also a push button that, when clicked, will run the encryption or decryption process.
The result of the process will be displayed in a line edit widget.

The caesar() function takes a string of text, a shift value, and an alphabet and returns an encrypted or decrypted string based on the shift value.
If the shift value is positive, the text is encrypted; if it is negative, the text is decrypted.
The alphabet parameter is used to specify which alphabet to use for the encryption or decryption process.
The function first defines a dictionary of alphabet strings, where the keys are the names of the alphabets and
the values are the corresponding alphabet strings. The function then uses the get() method of the dictionary
to retrieve the alphabet string based on the given alphabet name. If the given alphabet name is not found in the dictionary,
the function returns an "Invalid alphabet" string.

The encode() and decode() functions are wrappers around the caesar() function that take a string of text,
a shift value, and an alphabet and return the encoded or decrypted string, respectively.

The encrypt_decrypt() method is a PyQt slot that is called when the user clicks the "Encrypt/Decrypt" button.
It reads the values of the text, direction, shift, and alphabet from the corresponding widgets,
and then calls the appropriate function (encode() or decode()) to encrypt or decrypt the text.
The result is then displayed in the result line edit widget.
