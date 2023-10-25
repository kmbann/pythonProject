from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QTableWidget, QListWidget, QListWidgetItem,
       QLineEdit, QFormLayout,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QButtonGroup, QRadioButton,
       QPushButton, QLabel, QSpinBox)

card_win = QWidget()
#создання кнопок
btn_menu = QPushButton("меню.")
btn_sleep = QPushButton("відпочити.")
box_min = QSpinBox()
box_min.setValue(30)
lbl_min = QLabel("хвилин")

lbl_question = QLabel("")

RadioGroupBox = QGroupBox("Варіанті відповідей.")
RadioGroup = QButtonGroup()

rbtn1 = QRadioButton("")
rbtn2 = QRadioButton("")
rbtn3 = QRadioButton("")
rbtn4 = QRadioButton("")
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

AnsGoupBox = QGroupBox("Результат тесту")
lbl_result = QLabel("")
lbl_correct = QLabel("")
#создання ліний
line_rbtn1 = QHBoxLayout()
line_rbtn2 = QHBoxLayout()
line_main = QVBoxLayout()

line_rbtn1.addWidget(rbtn1)
line_rbtn1.addWidget(rbtn2)
line_rbtn2.addWidget(rbtn3)
line_rbtn2.addWidget(rbtn4)

line_main.addLayout(line_rbtn1)
line_main.addLayout(line_rbtn2)

RadioGroupBox.setLayout(line_main)
#создання віджетів
line_ans = QVBoxLayout()
line_ans.addWidget(lbl_result, alignment=(Qt.AlignLeft|Qt.AlignTop))
line_ans.addWidget(lbl_correct, alignment=Qt.AlignHCenter, stretch=2)
line_ans.addWidget(lbl_correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGoupBox.setLayout(line_ans)
AnsGoupBox.hide()

btn_ok = QPushButton("Відповітсти")
#лінії
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
card_layout = QVBoxLayout()
#відпочинок
line1.addWidget(btn_menu)
line1.addStretch(2)
line1.addWidget(btn_sleep)
line1.addWidget(box_min)
line1.addWidget(lbl_min)

line2.addWidget(lbl_question, alignment=(Qt.AlignHCenter|Qt.AlignVCenter))

line3.addWidget(RadioGroupBox)
line3.addWidget(AnsGoupBox)

line4.addStretch(1)
line4.addWidget(btn_ok, stretch=2)
line4.addStretch(1)

card_layout.addLayout(line1, stretch=1)
card_layout.addLayout(line2, stretch=2)
card_layout.addLayout(line3, stretch=8)
card_layout.addLayout(line4)