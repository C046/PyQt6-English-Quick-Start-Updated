# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:15:05 2023

@author: hadaw
"""
import random
import sys
from PyQt6 import QtCore, QtWidgets

# Create a widget  class
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # Establish a list of hello worlds in different languages.
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        # Create a button for the list.
        self.button = QtWidgets.QPushButton("Click me!")
        # In the latest version of [PyQt6-6.4.1, PyQt6-Qt6-6.4.2, PyQt6-sip-13.4.1]
        # We set the alignment from AlignmentFlag.
        self.text = QtWidgets.QLabel(
            "Hello World",
            alignment=QtCore.Qt.AlignmentFlag.AlignCenter
        )

        
        # Establish a layout for the gui
        self.layout = QtWidgets.QVBoxLayout(self)
        # Add the widgets to the gui.
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        
        # Set what the button does using our function below.
        self.button.clicked.connect(self.magic)
    
    # How you set Slots/ Signals
    @QtCore.pyqtSlot()
    # Define what the button does.
    def magic(self):
        # In this case we are using random to select a random string to display from a list.
        self.text.setText(random.choice(self.hello))
        
        
        
if __name__ == "__main__":
    # Establish an application
    app = QtWidgets.QApplication([])
    
    # Set widget var to MyWidget Class
    widget = MyWidget()
    # Resize the window
    widget.resize(800,600)
    # Display the window
    widget.show()
    
    # Exit Application upon exit.
    sys.exit(app.exec())