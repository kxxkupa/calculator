# ch 4.2.1 main.py
import sys # 시스템 제어 관련 모듈

# 위젯이란 : GUI 프로그램에서 구성요소를 뜻하는 용어
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout)
from PyQt5.QtGui import QIcon

# 나는 계산기 유형을 직접 정의한다. 이때, QWidget에 기반을 둔다.
class Calculator(QWidget) :
    def __init__(self) :
        super().__init__() # 뭔가에 기반을 둘 경우 써줘야 하는 코드
        self.initUI()

    def initUI(self) :
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.btn1 = QPushButton("Message", self)
        # 이벤트 핸들링 : 클릭했을 때, 뭐를 할거다! 라고 정하는 것
        self.btn1.clicked.connect(self.activateMessage)

        self.btn2 = QPushButton("Clear", self)
        self.btn2.clicked.connect(self.clearMessage)

        # 레이아웃 설정
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        # 레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addWidget(self.te1) # 텍스트 에디터
        # vbox.addWidget(self.btn1) # 버튼
        vbox.addLayout(hbox) # btn1 위치에 hbox를 배치
        vbox.addStretch(1) # 여백

        self.setLayout(vbox) # 설정 적용

        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(256, 256)
        self.show()

    def activateMessage(self) :
        # QMessageBox.information(self, "information", "Button clicked!")
        self.te1.appendPlainText("Button clicked!")

    def clearMessage(self) :
        self.te1.clear()


# 클래스를 정의했으니, 여기에서 실행하겠다. 라는 실행부
# if __name__ == "__main__" : 이 모듈이 직접 실행되는 경우
if __name__ == "__main__" :
    app = QApplication(sys.argv) # Qt 프로그램 실행코드
    view = Calculator() # 내가 만든 계산기 GUI 생성 코드
    sys.exit(app.exec_()) # 계산기 종료 시 시스템 종료 명령