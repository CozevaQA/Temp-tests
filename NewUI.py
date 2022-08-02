import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello App")
        self.setWindowIcon(QIcon('assets/icon.ico'))
        self.resize(500, 350)

        layout = QVBoxLayout()
        self.setLayout(layout)

        #widgets
        self.inputField = QLineEdit()
        button = QPushButton("&SayHello", clicked=self.sayHello)
        self.output = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)

    def sayHello(self):
        inputText = self.inputField.text()
        self.output.setText("hello {0}".format(inputText))



app = QApplication(sys.argv)
app.setStyleSheet('''
    QWidget {
        fint-size: 25px;
    }
    
    QPushButton {
        font-size: 20px;
        background-color: #4caf50!important;
        position: relative;
        cursor: pointer;
        display: inline-block;
        overflow: hidden;
        user-select: none;
        -webkit-tap-highlight-color: transparent;
        vertical-align: middle;
        z-index: 1;
        text-decoration: none;
        color: #fff;
        text-align: center;
        letter-spacing: .5px;
        font-size: 14px;
        outline: 0;
        border: none;
        border-radius: 2px;
        height: 36px;
        line-height: 36px;
        padding: 0 16px;
        text-transform: uppercase;
        box-shadow: 0 2px 2px 0 rgb(0 0 0 / 14%), 0 3px 1px -2px rgb(0 0 0 / 12%), 0 1px 5px 0 rgb(0 0 0 / 20%);
        -webkit-appearance: button;
        margin-right: 1em;
        font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif;
        box-sizing: inherit;
        writing-mode: horizontal-tb !important;
        font-style: ;
        font-variant-ligatures: ;
        font-variant-caps: ;
        font-variant-numeric: ;
        font-variant-east-asian: ;
        font-weight: ;
        font-stretch: ;
        text-rendering: auto;
        word-spacing: normal;
        text-indent: 0px;
        text-shadow: none;
        align-items: flex-start;
        
        
        
    }
''')

window = MyApp()
window.show()

sys.exit(app.exec())





