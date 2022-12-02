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

				   # %, CE, C, backspace 버튼 클릭 시 시그널 설정
        button_remainder.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))
        button_clear_entry.clicked.connect(self.button_clear_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        # 역수, 제곱, 제곱근, 나눗셈 버튼 클릭 시 시그널 설정
        button_reciprocal.clicked.connect(self.button_reciprocal_clicked)
        button_square.clicked.connect(self.button_square_clicked)
        button_square_root.clicked.connect(self.button_square_root_clicked)
        button_divide.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

         # 7, 8, 9, 곱셈 버튼 클릭 시 시그널 설정
        button_7.clicked.connect(lambda state, num = "7": self.number_button_clicked(num))
        button_8.clicked.connect(lambda state, num = "8": self.number_button_clicked(num))
        button_9.clicked.connect(lambda state, num = "9": self.number_button_clicked(num))
        button_mul.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))

        # 4, 5, 6, 뺄셈 버튼 클릭 시 시그널 설정
        button_4.clicked.connect(lambda state, num = "4": self.number_button_clicked(num))
        button_5.clicked.connect(lambda state, num = "5": self.number_button_clicked(num))
        button_6.clicked.connect(lambda state, num = "6": self.number_button_clicked(num))
        button_sub.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
    
         # 1, 2, 3, 덧셈 버튼 클릭 시 시그널 설정
        button_1.clicked.connect(lambda state, num = "1": self.number_button_clicked(num))
        button_2.clicked.connect(lambda state, num = "2": self.number_button_clicked(num))
        button_3.clicked.connect(lambda state, num = "3": self.number_button_clicked(num))
        button_add.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))

         # 00, 0, 소수점, 등호 버튼 클릭 시 시그널 설정
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        button_0.clicked.connect(lambda state, num = "0": self.number_button_clicked(num))
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        button_equal.clicked.connect(self.button_equal_clicked)

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation.text()
        solution = eval(equation)
        self.equation.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.equation.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)
    
    def button_reciprocal_clicked(self):
        self = numpy.reciprocal()
        equation = self.equation.text()
        equation = self
        self.equaion.setText(equation)

    def button_square_clicked(self):
        equation = self.equation.text()
        equation = math.pow(equation,2)
        self.equation.setText(str(equation))

    def button_square_root_clicked(self,num):
        equation = self.equation.text()
        equation = math.sqrt(num)
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())