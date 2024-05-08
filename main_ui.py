from ans import takeCommand
from translate import load_model,translate
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI_ui import Ui_Form


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        self.start.clicked.connect(self.run)

        self.display.clicked.connect(self.close)

    def run(self):
        
        text = takeCommand()
        self.asr_ans.setText(text)
        
        tokenizer,model = load_model()
        decoded = translate(text,tokenizer,model)
        self.translate_ans.setText(decoded)

        os.remove("temp_file.wav")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
    