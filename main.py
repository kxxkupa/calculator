# ch 4.2.1 main.py
import sys # 시스템 제어 관련 모듈

from ui import View
from ctrl import Control
from PyQt5.QtWidgets import QApplication    

def main():
    calc = QApplication(sys.argv)
    app=QApplication(sys.argv)
    view=View()
    Control(view=view)
    sys.exit(app.exec_())

# 클래스를 정의했으니, 여기에서 실행하겠다. 라는 실행부
# if __name__ == "__main__" : 이 모듈이 직접 실행되는 경우
if __name__ == "__main__" :
    main()