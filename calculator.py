import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_equation_solution = QFormLayout()
        layout_all = QGridLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_equation = QLabel("Calculator: ")
        self.equation = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addRow(label_equation, self.equation)
  
				# 계산기 첫 번째 줄 버튼 생성
        button_remainder = QPushButton("%")
        button_clear_entry = QPushButton("CE")
        button_clear = QPushButton("C")
        button_backspace = QPushButton("BackSpace")

        layout_all.addWidget(button_remainder, 0, 0)
        layout_all.addWidget(button_clear_entry, 0, 1)
        layout_all.addWidget(button_clear, 0, 2)
        layout_all.addWidget(button_backspace, 0, 3)

        # 첫 번째 줄의 버튼을 Layout_all 레이아웃에 추가
        layout_all.addWidget(button_remainder)
        layout_all.addWidget(button_clear_entry)
        layout_all.addWidget(button_clear)
        layout_all.addWidget(button_backspace)

        # 계산기 두 번째 줄 버튼 생성
        button_reciprocal = QPushButton("1/x")
        button_square = QPushButton("x^2")
        button_square_root = QPushButton("sqrt")
        button_divide = QPushButton("/")

        layout_all.addWidget(button_reciprocal, 1, 0)
        layout_all.addWidget(button_square, 1, 1)
        layout_all.addWidget(button_square_root, 1, 2)
        layout_all.addWidget(button_divide, 1, 3)

        # 두 번째 줄의 버튼을 Layout_all 레이아웃에 추가
        layout_all.addWidget(button_reciprocal)
        layout_all.addWidget(button_square)
        layout_all.addWidget(button_square_root)
        layout_all.addWidget(button_divide)

        # 계산기 세 번째 줄 버튼 생성
        button_7 = QPushButton("7")
        button_8 = QPushButton("8")
        button_9 = QPushButton("9")
        button_mul = QPushButton("*")

        layout_all.addWidget(button_7, 2, 0)
        layout_all.addWidget(button_8, 2, 1)
        layout_all.addWidget(button_9, 2, 2)
        layout_all.addWidget(button_mul, 2, 3)

        # 세 번째 줄의 버튼을 Layout_all 레이아웃에 추가
        layout_all.addWidget(button_7)
        layout_all.addWidget(button_8)
        layout_all.addWidget(button_9)
        layout_all.addWidget(button_mul)

        # 계산기 네 번째 줄 버튼 생성
        button_4 = QPushButton("4")
        button_5 = QPushButton("5")
        button_6 = QPushButton("6")
        button_sub = QPushButton("-")

        layout_all.addWidget(button_4, 3, 0)
        layout_all.addWidget(button_5, 3, 1)
        layout_all.addWidget(button_6, 3, 2)
        layout_all.addWidget(button_sub, 3, 3)

        # 네 번째 줄의 버튼을 Layout_all 레이아웃에 추가
        layout_all.addWidget(button_4)
        layout_all.addWidget(button_5)
        layout_all.addWidget(button_6)
        layout_all.addWidget(button_sub)

        # 계산기 다섯 번째 줄 버튼 생성
        button_1 = QPushButton("1")
        button_2 = QPushButton("2")
        button_3 = QPushButton("3")
        button_add = QPushButton("+")

        layout_all.addWidget(button_1, 4, 0)
        layout_all.addWidget(button_2, 4, 1)
        layout_all.addWidget(button_3, 4, 2)
        layout_all.addWidget(button_add, 4, 3)

        # 다섯 번째 줄의 버튼을 Layout_all 레이아웃에 추가
        layout_all.addWidget(button_1)
        layout_all.addWidget(button_2)
        layout_all.addWidget(button_3)
        layout_all.addWidget(button_add)

        # 계산기 여섯 번째 줄 버튼 생성
        button_double_zero = QPushButton("00")
        button_0 = QPushButton("0")
        button_dot = QPushButton(".")
        button_equal = QPushButton("=")

        layout_all.addWidget(button_double_zero, 5, 0)
        layout_all.addWidget(button_0, 5, 1)
        layout_all.addWidget(button_dot, 5, 2)
        layout_all.addWidget(button_equal, 5, 3)

        # 여섯 번째 줄의 버튼을 Layout_all 레이아웃에 추가
        layout_all.addWidget(button_double_zero)
        layout_all.addWidget(button_0)
        layout_all.addWidget(button_dot)
        layout_all.addWidget(button_equal)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_all)

        self.setLayout(main_layout)
        self.show()