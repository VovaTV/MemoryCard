#создай приложение для запоминания информации
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton, QHBoxLayout, QVBoxLayout, QGroupBox
app = RadioGroupBox= QGroupBox("Варианты ответов")
rbtn_1 = QRadionButton("Энцы")
rbtn_2 = QRadionButton("Чульмцы")
rbtn_3 = QRadionButton("Смурфы")
rbtn_4 = QRadionButton("Алеуты")
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
lb_Question = QLabel("Какой национальности не существует?")
btn_OK = QPushButton("Ответить")
layout_line1 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1)
layout_card.addWidget(RadioGroupBox)
layout_card.addLayout(layout_line3)

win.setLayout(layout_card)
win.show()
app.exec_()
'''
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)

my_app = QApplication([])

window = QWidget()
window.setWindowTitle('MemoCard')

Button_Answer = QPushButton('Ответить')
LB_Question = QLabel('Сколько было гусей в тракторе?')

RadioGroupBox = QGroupBox('вАРИАНТЫ оТВЕТОВ')
b1 = QRadioButton('5')
b2 = QRadioButton('10')
b3 = QRadioButton('10000')
b4 = QRadioButton('1,5')

RadioGroup = QButtonGroup()
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)

AnsBox = QGroupBox('Результат')
label1 = QLabel('Прав/Неправ?')
label2 = QLabel('+/-')

lay1 = QVBoxLayout()
lay1.addWidget(label1, alignment=(Qt.AlignLeft | Qt.AlignTop))
lay1.addWidget(label2, alignment=Qt.AlignHCenter, stretch=2)
RadioGroupBox.setLayout(lay1)

l = QHBoxLayout()
l1 = QVBoxLayout()
l2 = QVBoxLayout()
l1.addWidget(b1)
l1.addWidget(b2)
l2.addWidget(b3)
l2.addWidget(b4)
l.addLayout(l1)
l.addLayout(l2)

RadioGroupBox.setLayout(l)

l_1 = QHBoxLayout()
l_2 = QHBoxLayout()
l_3 = QHBoxLayout()

l_1.addWidget(LB_Question)
l_2.addWidget(RadioGroupBox)
l_3.addWidget(Button_Answer)

l_main = QVBoxLayout()
l_main.addLayout(l_1)
l_main.addLayout(l_2)
l_main.addLayout(l_3)

def show_result():
    RadioGroupBox.hide()
    AnsBox.show()
    Button_Answer.setText('Следующий вопрос')
    
def show_question():
    RadioGroupBox.show()
    AnsBox.hide()
    Button_Answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    b1.setChecked(False)
    b2.setChecked(False)
    b3.setChecked(False)
    b4.setChecked(False)
    RadioGroup.setExclusive(True)
def test():
    if(Button_Answer.text() == 'Ответить'):
        show_result()
    else:
        show_question()

window.setLayout(l_main)
Button_Answer.clicked.connect(test)
window.show()
my_app.exec_()





def next_question():
    window.total = window.total + 1
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(questions_list):
        window.cur_question = 0
        shuffle(questions_list)
    q = questions_list[window.cur_question]
    ask(q)

def click_ok():
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()

window.cur_question = -1
window
btn_OK.clicked.connect(click_ok)
next_question()
questions_list = []
questions_list.append(Question('ТРОЛОЛОЛООЛОЛООЛООЛОО?', 'Т', 'Р', 'О', 'Л'))
questions_list.append(Question('ЛООООООООООООООООЛ?', 'Л', 'О', 'Л', 'О'))
questions_list.append(Question('КЕЕЕЕЕЕЕЕЕЕЕЕЕЕК?', 'К', 'Е', 'К', 'Е'))
questions_list.append(Question('ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ?', 'Ч', 'Е', 'Ч', 'Е'))
questions_list.append(Question('БУУУУУУУУУУУУУУУ?', 'Б', 'У', 'Б', 'У'))
questions_list.append(Question('РЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ?', 'Р', 'Е', 'Р', 'Е'))
questions_list.append(Question('к?', 'К', 'К', 'К', 'К'))
window.resize(400,300)
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import randint, shuffle 
 
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
 
questions_list = [] 
questions_list.append(Question('Где находится родина деда мороза?', 'Великий Устюг', 'Москва', 'Кемерово', 'Самара'))
questions_list.append(Question('В каком году появился салат оливье?', '1860', '1918', '1956', '2008'))
questions_list.append(Question('Кто является Божественным отцом Снегурки у славян?', 'Снеговик', 'Снегурочка', 'Дед Мороз', 'Чарли Чаплин'))
questions_list.append(Question('Кто жил в ледяной избушке, у леса на опушке?', 'Зима', 'Осень', 'Весна', 'Лето' ))
questions_list.append(Question('Как переводится "snow"?', 'Снег', 'Снежинка', 'Снежки', 'Снегопад'))
 
app = QApplication([])
 
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!') 
 
RadioGroupBox = QGroupBox("Варианты ответов") 
 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup()

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1) 
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')

    RadioGroup.setExclusive(False)

    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)

    RadioGroup.setExclusive(True)
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q: Question):

    shuffle(answers)

    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

    lb_Question.setText(q.question) 
    lb_Correct.setText(q.right_answer)

    show_question() 
 
def show_correct(res):

    lb_Result.setText(res)
    show_result()
 
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.correct += 1
        print('Статистика. Всего вопросов: ', window.total, ' Правильных ответов: ', window.correct)
        print('Рейтинг: ', (window.correct/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.correct/window.total*100), '%')
    
 
def next_question():
    window.total += 1
    print('Статистика. Всего вопросов: ', window.total, ' Правильных ответов: ', window.correct)
    cur_question = randint(0, len(questions_list) - 1) 
    q = questions_list[cur_question] 
    ask(q) 
 
def click_OK():
        if btn_OK.text() == 'Ответить':
            check_answer() 
        else:
            next_question() 

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')

window.correct = 0
window.total = 0
btn_OK.clicked.connect(click_OK) 
next_question()
window.resize(400, 300)
window.show()
app.exec()