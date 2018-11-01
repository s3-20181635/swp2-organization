import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit,QGridLayout)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'

        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        grid = QGridLayout()
        Name = QLabel('Name:',self)
        self.Name_edit = QLineEdit()
        Age = QLabel('Age:',self)
        self.Age_edit = QLineEdit()
        Score = QLabel('Score:',self)
        self.Score_edit = QLineEdit()
        hinf = QHBoxLayout()
        hinf.addWidget(Name)
        hinf.addWidget(self.Name_edit)
        hinf.addWidget(Age)
        hinf.addWidget(self.Age_edit)
        hinf.addWidget(Score)
        hinf.addWidget(self.Score_edit)

        hinf1 = QHBoxLayout()
        Amount = QLabel('Amount:',self)
        self.Amount_edit = QLineEdit()
        Key = QLabel('Key:',self)
        self.QC = QComboBox()
        self.QC.addItem('Age')
        self.QC.addItem('Score')
        hinf1.addWidget(Amount)
        hinf1.addWidget(self.Amount_edit)
        hinf1.addWidget(Key)
        hinf1.addWidget(self.QC)

        button1 = QPushButton('Add')
        button2= QPushButton('Del')
        button3 = QPushButton('Find')
        button4 = QPushButton('Inc')
        button5 = QPushButton('Show')

        button1.clicked.connect(self.buttonClicked_1)
        button2.clicked.connect(self.buttonClicked_2)
        button3.clicked.connect(self.buttonClicked_3)
        button4.clicked.connect(self.buttonClicked_4)
        button5.clicked.connect(self.buttonClicked_5)

        hinf2 = QHBoxLayout()
        hinf2.addWidget(button1)
        hinf2.addWidget(button2)
        hinf2.addWidget(button3)
        hinf2.addWidget(button4)
        hinf2.addWidget(button5)

        Result = QLabel('Result:')
        self.Result_edit = QTextEdit(self)
        grid.addLayout(hinf,1,0)
        grid.addLayout(hinf1,2,0)
        grid.addLayout(hinf2,3,0)
        grid.addWidget(Result,4,0)
        grid.setColumnStretch(3,0)
        grid.setRowStretch(5,1)
        grid.addWidget(self.Result_edit,5,0,8,0)


        self.setLayout(grid)
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        fH = open(self.dbfilename, 'rb')
        self.scoredb =  pickle.load(fH)
        print(self.scoredb)



    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        for p in (self.scoredb):
            for attr in p:
                self.Result_edit.setText(self.Result_edit.toPlainText()+ ' ' + attr + "=" + str(p[attr]))
            self.Result_edit.setText(self.Result_edit.toPlainText() + "\n")
    def buttonClicked_1(self):
        print("Success")
        record = {'Name':self.Name_edit.text(), 'Age':int(self.Age_edit.text()), 'Score':int(self.Score_edit.text())}
        self.scoredb += [record]
        self.Result_edit.setText(None)
        for p in self.scoredb:
            for attr in p:
                self.Result_edit.setText(self.Result_edit.toPlainText() + ' ' + attr + "=" + str(p[attr]))
            self.Result_edit.setText(self.Result_edit.toPlainText() + "\n")





    def buttonClicked_2(self):
        print("Success")
        for p in self.scoredb:
           if p['Name'] == self.Name_edit.text():
                 self.scoredb.remove(p)
        self.Result_edit.setText(None)
        for p in self.scoredb:
            for attr in p:
                self.Result_edit.setText(self.Result_edit.toPlainText() + ' ' + attr + "=" + str(p[attr]))
            self.Result_edit.setText(self.Result_edit.toPlainText() + "\n")

    def buttonClicked_3(self):
        self.Result_edit.setText(None)
        for p in self.scoredb:
            if p['Name'] == self.Name_edit.text():
                for attr in p:
                    self.Result_edit.setText(self.Result_edit.toPlainText() + ' ' + attr + "=" + str(p[attr]))
                self.Result_edit.setText(self.Result_edit.toPlainText() + "\n")

    def buttonClicked_4(self):
        self.Result_edit.setText(None)
        for p in self.scoredb:
            if p['Name'] == self.Name_edit.text():
               p['Score'] = int(p['Score'])
               p['Score'] += int(self.Amount_edit.text())
               p['Score'] = str(p['Score'])
            for attr in p:
                self.Result_edit.setText(self.Result_edit.toPlainText() + ' ' + attr + "=" + str(p[attr]))
            self.Result_edit.setText(self.Result_edit.toPlainText() + "\n")

    def buttonClicked_5(self):
        self.Result_edit.setText(None)
        list = []
        print(self.scoredb)
        if self.QC.currentText() == "Age":
            for i in sorted(self.scoredb, key=lambda age: int(age["Age"])):
                for attr in i:
                    self.Result_edit.setText(self.Result_edit.toPlainText() + ' ' + attr + "=" + str(i[attr]))
                self.Result_edit.setText(self.Result_edit.toPlainText() + "\n")

        elif self.QC.currentText() == "Score":
            for i in sorted(self.scoredb, key=lambda age: int(age["Score"])):
                for attr in i:
                    self.Result_edit.setText(self.Result_edit.toPlainText() + ' ' + attr + "=" + str(i[attr]))
                self.Result_edit.setText(self.Result_edit.toPlainText() + "\n")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
    ''''''

