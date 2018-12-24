import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
#from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import Qt, QTimer
 
class myApp(QWidget):
 
    def __init__(self):
 
        QWidget.__init__(self)
 
        self.init_ui() # вызов метода в котором задается интерфейс и начальные параметры
 
    def init_ui(self):
        self.speed = 5   # каждые 5 мс будет обновляться таймер
        self.timer = QTimer(self)  # создаем таймер
        btn_left = QPushButton("Влево", self) # создаем кнопку "влево"
        btn_right = QPushButton("Вправо", self)  # создаем кнопку "вправо"
        btn_stop = QPushButton("Стоямба", self) # создаем кнопку "стоп"
        btn_left.move(10, 10)         #  абсолютное позиционирование:
        btn_right.move(350, 10)       #  задаем расположение кнопок
        btn_stop.move(180, 10)        #  надписей путем указания координат x, y
        self.x = 200                  #  начальные координаты
        self.y = 150                  #  бегущей строки
        self.setWindowTitle("Thomas the Tankengine")      # задаем заголовок окна
        self.label = QLabel("Thomas", self)  # создаем метку которая
                                                     # содержит текст "бегущая строка"
        self.label.move(self.x, self.y)              # устанавливаем бегущую строку
                                                     # в координаты
        self.setGeometry(300, 300, 450, 300)         # задаем размеры окна и его координаты                
 
 
        btn_right.clicked.connect(self.buttonClicked)   # подключаем сигнал кнопок 
        btn_left.clicked.connect(self.buttonClicked)    # clicked к методу
        btn_stop.clicked.connect(self.buttonClicked)    # buttonClicked

 
 
 
 
        self.show() # отображает виджет
 
 
    def buttonClicked(self):    # метод обработки нажатых кнопок
        sender = self.sender()  # создаем экземпляр sender
        if sender.text() == "Вправо":   # вызываем метод text() который возвратит надпись на 
                                        # кнопке
            if self.timer.isActive():   # проверяем включен ли таймер
                self.timer.stop()       # если включен - останавливаем
                self.timer.timeout.disconnect()  # отсоединяем таймер от сигнала timeout
                self.timer.start(self.speed)     # запускаем таймер со значением self.speed
                self.timer.timeout.connect(self.move_thomas_right)  # подключаем событие
                                                                   # timeout к методу
                                                                   # self.move_label_right
            else:
                self.timer.start(self.speed)
                self.timer.timeout.connect(self.move_thomas_right)
 
 
# ниже всё аналогично верхнему блоку кода
 
        elif sender.text() == "Влево":
            if self.timer.isActive():
                self.timer.stop()
                self.timer.timeout.disconnect()
                self.timer.start(self.speed)
                self.timer.timeout.connect(self.move_thomas_left)
            else:
                self.timer.start(self.speed)
                self.timer.timeout.connect(self.move_thomas_left)
        elif sender.text() == "Стоямба":                             # если нажата кнопка стоп
            self.stop_move()                                      # вызываем метод      
                                                                  # self.stop_move()
 
    def move_thomas_left(self): 
        if self.x == -100:       # проверяем не вышла ли бегущая строка далеко влево за 
                                 # пределы окна
            self.x = 500         # если вышла за пределы то устанавливаем исходную координату 
                                 # self.x
            self.x = self.x - 0.5    # отнимаем от текущего значения координаты х    0.5
            self.label.move(self.x, self.y)   # передвигаем  бегущую строку
 
        else:
            self.x = self.x - 0.5                     
            self.label.move(self.x, self.y)
 
 
 
 
    def move_thomas_right(self):
 
        if self.x == 500:
            self.x = -100
            self.x = self.x + 0.5
            self.label.move(self.x, self.y)
 
        else:
            self.x = self.x + 0.5
            self.label.move(self.x, self.y)
 
    def stop_move(self):
        if self.timer.isActive():
            self.timer.stop()
            self.timer.timeout.disconnect()
 
 
 
 
if __name__ == '__main__':
 
    app = QApplication(sys.argv)
    ex = myApp()
    sys.exit(app.exec_())
